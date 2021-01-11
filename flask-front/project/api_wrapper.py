import requests
import json

# api_baseurl = "http://localhost:5000/api/v1"
api_baseurl = "http://flask-api:5000/api/v1"

def get_articles():
    content_list = []
    r = requests.get(api_baseurl+"/articles")
    for item in r.json():
        author_name = requests.get(api_baseurl+"/user/"+str(item['author_id'])).json()
        author_name = author_name['first_name']+ " " + author_name['last_name']
        article = {'title':item['title'],
                   'date':item['date'],
                   'author':str(author_name),
                   'description':item['description'],
                   'content':item['content']}
        content_list.append(article)
    return content_list

def get_articles_from(author_name):
    firstname = author_name.split(" ")[0]
    print(firstname)
    content_list = []
    r = requests.get(api_baseurl+"/articles?author_firstname="+firstname)
    print(json.dumps(r.json(), indent=4))
    for item in r.json():
        print(item['author'])
        # author_name = requests.get(api_baseurl+"/user/"+str(item['author_id'])).json()
        # author_name = author_name['first_name']+ " " + author_name['last_name']
        article = {'title':item['title'],
                   'date':item['date'],
                   'author':str(author_name),
                   'description':item['description'],
                   'content':item['content']}
        content_list.append(article)
    return content_list

if __name__ == '__main__':
    print("debug")
    print(get_articles_from("Julien TOUTAIN"))
