from flask import Flask
from flask_restx import Resource, Api, fields, reqparse
import pymysql
from secrets import token_urlsafe
from datetime import datetime 
from datetime import date
from datetime import timedelta
import json
from flask import jsonify

# Usefull ressources :
## https://flask-restplus.readthedocs.io/en/stable/index.html
## https://blog.invivoo.com/designer-des-apis-rest-avec-flask-restplus/
## https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP
## http://filldb.info/


# Config Flask App Definition
app = Flask(__name__)
api = Api(app=app, version="0.1", doc="/api", title="ZEUS", description="Station meteo en Flask ", default="station meteo", default_label='une première station meteo', validate=True)

# Generate db from http://filldb.info/
# db_host = "mydb"
db_host = "localhost"
try:
    db=pymysql.connect(
        host=db_host,
        user="root",
        passwd="toortoor",
        db="station_meteo")
    cursor=db.cursor()
        
except (pymysql.err.InternalError, pymysql.err.OperationalError) as e:
    print("La DB n'existe pas elle va etre cree")
    print(repr(e))
    db=pymysql.connect(
        host=db_host,
        user="root",
        passwd="toortoor",
        db="station_meteo")
    sql = ["CREATE DATABASE station_meteo;","use station_meteo;"]
    with db.cursor() as cursor:
        for query in sql:
            cursor.execute(query)

### Changement de format du DATETIME
def date_to_str(id):
    cursor.execute("SELECT added_at FROM mesure WHERE id=%s", id)
    date = cursor.fetchall()
    returndate = date[0][0].strftime("%Y-%m-%d %H:%M:%S")
    return returndate


### API
#### MESURES - READ 
##### Retourne une donnée en fonction de l'id en paramètres 
@api.route("/api/v1/mesure/<id>")
class ReturnDate(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Error')
    def get(self, id):
        """
        Return all values of one mesure 
        """
        cursor.execute("SELECT id, temperature, humidity, CAST(added_at AS CHAR) FROM mesure WHERE id=%s", id)
        date = cursor.fetchall()
        return date, 200


##### Retourne toutes les valeurs en base de données
@api.route("/api/v1/mesures")
class ReturnAll(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Error')
    def get(self):
        """
        Return all mesure data
        """
        try:
            cursor.execute("SELECT id, temperature, humidity, CAST(added_at AS CHAR) FROM mesure")
            data = cursor.fetchall()
            return data, 200
        except:
            return 400


##### Retourne le dernier insert
@api.route("/api/v1/mesure/last")
class ReturnLast(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Error')
    def get(self):
        """
        Return last row insert 
        """
        try:
            cursor.execute("SELECT id, temperature, humidity, CAST(added_at AS CHAR) FROM mesure ORDER BY id DESC LIMIT 1")
            last_id = cursor.fetchall()
            return last_id, 200
        except:
            return {'erreur'}, 400


##### Retourne toutes les valeurs des dernières 24h
@api.route("/api/v1/mesures/day")
class ReturnDayMesures(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Error')
    def get(self):
        """
        Return all values of the day
        """
        dateNow = datetime.today()
        datePastDay = dateNow - timedelta(days=1)

        data = []
        cursor.execute("SELECT id, temperature, humidity, CAST(added_at AS CHAR) FROM mesure WHERE added_at BETWEEN '%s' AND '%s'" %(datePastDay, dateNow))
        data = cursor.fetchall()
        return jsonify(data)   

##### Retourne toutes les valeurs des dernières 24hx7

##### Retourne toutes les valeurs des dernières 24hx30

#### MESURE - POST
#### Modèle de données
##### A quoi vont servir ces données ? => Récupérer les informations envoyées par la sonde
posts_mesures = reqparse.RequestParser()
posts_mesures.add_argument('temperature')
posts_mesures.add_argument('humidity')

mesure_post = api.model('Measure Post Informations', {
    'temperature': fields.Float(),
    'humidity': fields.Float()
})

##### Ajouter une donnée
@api.route("/api/v1/mesure/add")
class postMesure(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Error')
    @api.expect(mesure_post)
    def post(self):
        """
        Add a new value with ESP 
        """

        temperature = api.payload['temperature']
        humidity = api.payload['humidity']
        dateNow = datetime.today()
        values = {'temperature': temperature, 'humidity': humidity}
        try :
            cursor.execute("INSERT INTO mesure (id_sonde ,temperature, humidity, added_at) VALUES (1, "+str(temperature)+", "+str(humidity)+", '"+str(dateNow)+"');")
            db.commit()
            cursor.execute("SELECT id, temperature, humidity, CAST(added_at AS CHAR) FROM mesure ORDER BY id DESC LIMIT 1")
            values = cursor.fetchone()
            print(values)
            return jsonify(values)
        except:
            return 400

### SONDE 
#### Affichage des informations de la sonde dont l'ID est passé en paramètres
@api.route("/api/v1/sonde/<id>")
class Sonde(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Error')
    def get(self, id):
        """
        Return Sonde informations
        :param id:
        """
        cursor.execute("SELECT * FROM sonde WHERE id=%s", id)
        data = cursor.fetchall()
        return data


posts_sonde = reqparse.RequestParser()
posts_sonde.add_argument('name')
posts_sonde.add_argument('active')
posts_sonde.add_argument('pos_longitude')
posts_sonde.add_argument('pos_latitude')
sonde_post = api.model('Sonde Post Informations', {
    'name': fields.String,
    'pos_longitude': fields.Float(),
    'pos_latitude': fields.Float(),
    #'active' : fields.Integ

})
@api.route("/api/v1/sonde/add")
class SondeAdd(Resource):
    @api.expect(sonde_post)
    def post(self):
        """
        Create a new sonde
        """
        name = api.payload['name']
        pos_latitude = api.payload['pos_latitude']
        pos_longitude = api.payload['pos_longitude']

        cursor.execute("INSERT INTO sonde (sonde_name, pos_latitude, pos_longitude, active) VALUES ('%s', '%s', '%s', 0);" % (name, pos_latitude, pos_longitude))
        db.commit()
        cursor.execute("SELECT * FROM sonde ORDER BY id DESC LIMIT 1")
        values = cursor.fetchall()
        print(values)
        return jsonify(values)


@api.route("/api/v1/sondes/<id>")
class SondeUpdate(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Error')
    @api.expect(sonde_post)
    def put(self, id):
        """
        Update Sonde informations with his ID
        :param id:
        """
        active = api.payload['active']

        cursor.execute("SELECT id FROM sonde WHERE id=%s", id)
        cursor.execute("UPDATE sonde SET active = %s WHERE id=%s" % (active, id))
        db.commit()
        last_id = cursor.lastrowid
        return jsonify(last_id)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
