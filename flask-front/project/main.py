from flask import Flask, render_template, flash, redirect, url_for, jsonify
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_bootstrap import Bootstrap
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from markupsafe import escape
from flask_nav import Nav
import requests
from api_wrapper import get_articles, get_articles_from

nav = Nav()
application = Flask(__name__)
# api_baseurl = "http://localhost:5000/api/v1"
api_baseurl = "http://flask-api:5000/api/v1"

def get_authors():
    r = requests.get(api_baseurl+"/users")
    authors_list = ['Auteurs']
    for item in r.json():
        author_name = item['first_name']+" "+item['last_name']
        print(author_name)
        authors_list.append(Link(author_name, "/author/"+str(author_name)))
    return authors_list
def nav_bar():
    nav.renderer()
    authors_list = get_authors()
    subgroup_items = Subgroup(*authors_list)
    items = [View('Home', '.index'), subgroup_items, Link('API', '/api')]
    return Navbar('My Blog', *items)

nav.register_element('frontend_top', nav_bar())

app = Flask(__name__)
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
nav.init_app(app)

@app.route('/')
def index():
    content_list = get_articles()
    return render_template('index.html', content_list=content_list)

@app.route("/author/<string:author>")
def author(author):
    content_list = get_articles_from(author)
    return render_template('index.html', content_list=content_list)

if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port="5001")
