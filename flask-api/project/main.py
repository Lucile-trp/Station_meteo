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
api = Api(app=app, version="1.0", doc="/api", title="ZEUS", description="Projet CUBES : Conception et programmation d'une station météorologique en python. <br><br> Par : Mariam EL-ALLALI <br> Hugo DOURLEN <br> Gregory LEBLOND <br> Lucile TRIPIER", default="API", default_label='Descriptions des routes', validate=True)

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
        Return all values of one mesure with his ID in parameters
        """
        try:
            cursor.execute("SELECT id, temperature, humidity, CAST(added_at AS CHAR) FROM mesure WHERE id=%s", id)
            data = cursor.fetchall()
            return data, 200
        except:
            return 400


##### Retourne toutes les valeurs en base de données
@api.route("/api/v1/mesures")
class ReturnAll(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Error')
    def get(self):
        """
        Return all mesure data
        """

        cursor.execute("SELECT id, temperature, humidity, CAST(added_at AS CHAR) FROM mesure ORDER BY added_at DESC")
        data = cursor.fetchall()
        return data, 200



##### Retourne le dernier insert
@api.route("/api/v1/mesure/last")
class ReturnLast(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Error')
    def get(self):
        """
        Return the last row inserted
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
        dateNow = dateNow.strftime("%Y-%m-%d 00:00:00")

        data = []
        try:
            cursor.execute("SELECT id, temperature, humidity, CAST(added_at AS CHAR) FROM mesure WHERE added_at >= '%s' ORDER BY added_at DESC" % dateNow)
            data = cursor.fetchall()
            return jsonify(data)
        except:
            feedback = "La requête a echouée"
            return feedback, 400

### Retourne la moyenne des valeurs du jour entre 6h et 18h 
@api.route("/api/v1/mesures/day/moy")
class ReturnDayMesures(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Error')
    def get(self):
        """
        Return average of values of the day between 6pm and 6am.
        """
        dateNow = datetime.today()
        morning = dateNow.strftime("%Y-%m-%d 06:00:00")
        evening = dateNow.strftime("%Y-%m-%d 18:00:00")

        data = []
        try:
            cursor.execute("SELECT AVG(temperature), AVG(humidity) FROM mesure WHERE added_at BETWEEN '%s' and '%s' ;" % (morning, evening))
            data = cursor.fetchall()
            return jsonify(data)
        except:
            feedback = "La requête a echouée"
            return feedback, 400

##### Retourne toutes les valeurs des dernières 24hx7
@api.route("/api/v1/mesures/week")
class ReturnWeekMesures(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Error')
    def get(self):
        """
        Return all values of the week
        """
        dateNow = datetime.today()
        datePastDay = dateNow - timedelta(days=7)
        dateNow = dateNow.strftime("%Y-%m-%d 00:00:00")
        datePastDay = datePastDay.strftime("%Y-%m-%d 00:00:00")
        data = []
        try:
            cursor.execute("SELECT id, temperature, humidity, CAST(added_at AS CHAR) FROM mesure WHERE added_at BETWEEN '%s' AND '%s' ORDER BY added_at DESC" %(datePastDay, dateNow))
            data = cursor.fetchall()
            return jsonify(data)  
        except:
            feedback = "La requête a echouée"
            return feedback

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
        Return probe informations
        :param id:
        """
        try :
            cursor.execute("SELECT * FROM sonde WHERE id=%s", id)
            data = cursor.fetchall()
            return data
        except:
            feedback = "La requête a echouée"
            return feedback

#### Ajouter une sonde
posts_sonde = reqparse.RequestParser()
posts_sonde.add_argument('name')
posts_sonde.add_argument('pos_longitude')
posts_sonde.add_argument('pos_latitude')
sonde_post = api.model('Sonde Post Informations', {
    'name': fields.String,
    'pos_longitude': fields.Float(),
    'pos_latitude': fields.Float(),
})

@api.route("/api/v1/sonde/add")
class SondeAdd(Resource):
    @api.expect(sonde_post)
    def post(self):
        """
        Create a new probe
        """
        name = api.payload['name']
        pos_latitude = api.payload['pos_latitude']
        pos_longitude = api.payload['pos_longitude']
        try:
            cursor.execute("INSERT INTO sonde (sonde_name, pos_latitude, pos_longitude, active) VALUES ('%s', '%s', '%s', 0);" % (name, pos_latitude, pos_longitude))
            db.commit()
            cursor.execute("SELECT * FROM sonde ORDER BY id DESC LIMIT 1")
            values = cursor.fetchall()
            return jsonify(values)
        except:
            feedback = "La requête a échouée"
            return feedback

put_auth_sonde = reqparse.RequestParser()
put_auth_sonde.add_argument('active', type=int)
put_auth_sonde.add_argument('id', type=int)
put_auth_sonde.add_argument('token')
argsauth = api.model('Sonde Put Information with Auth', {
    'active': fields.Integer,
    'id' :fields.Integer,
    'token' : fields.String
})

@api.route("/api/v1/sonde/auth/<id>")
class SondeUpdate(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Error')
    @api.expect(argsauth)
    def put(self, id):
        """
        Update 'active' probe information
        :param sonde.id:
        :param token:
        :param users.id:
        """
        users_id = api.payload['id']
        user_token = api.payload['token']
        active = api.payload['active']

        #recupère le token user en fonction de users.id 
        cursor.execute("SELECT token FROM users WHERE id=%s", users_id)
        token = cursor.fetchone()
        token = str(token)
        user_token = "('" + user_token + "',)"
        #si token user == token passé en paramètres
        if token == user_token:
            cursor.execute("SELECT id FROM sonde WHERE id=%s", id)
            cursor.execute("UPDATE sonde SET active = %s WHERE id=%s" % (active, id))
            db.commit()
            last_id = cursor.lastrowid
            return jsonify(last_id)
        else:
            feedback = "Utilisateur ou token invalide"
            return feedback


del_sonde = reqparse.RequestParser()
del_sonde.add_argument('active', type=int)
del_sonde.add_argument('id', type=int)
del_sonde.add_argument('token')
argsdel = api.model('Delete probe Information with Auth', {
    'id' :fields.Integer,
    'token' : fields.String
})
@api.route("/api/v1/sonde/delete/<id>")
class DeleteSonde(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Error')
    @api.expect(argsdel)
    def delete(self, id):
        """
        Delete a probe
        :param sonde.id:
        :param user.id:
        :param token:
        """

        users_id = api.payload['id']
        user_token = api.payload['token']
        #recupère le token user en fonction de users.id 
        cursor.execute("SELECT token FROM users WHERE id=%s", users_id)
        token = cursor.fetchone()
        token = str(token)
        user_token = "('" + user_token + "',)"
        #si token user == token passé en paramètres
        if token == user_token:
            cursor.execute("DELETE FROM sonde WHERE id = %s" % id)
            db.commit()
            feedback = "La donnée à bien été supprimée"
            return feedback
        else:
            feedback = "User ou token invalide, impossible de supprimer la donnée"
            return feedback


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
