import ssl
from datetime import datetime
import pymongo
import yagmail

MAILER = 'nandan.199776'


def start_mail():
    file = open("db_user.txt", "r")
    username = file.read()

    file = open("db_password.txt", "r")
    password = file.read()

    connection_url = "mongodb+srv://" + username + ":" + password + "@cluster0-nw856.mongodb.net/test?retryWrites=true&w=majority"

    print(connection_url)

    client = pymongo.MongoClient(connection_url, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
    database = client['mailer-db']
    collection = database['employee']

    today = datetime.today()

    query = {"birthday": str(today.day) + "/" + str(today.month)}
    for doc in collection.find(query):
        send_birthday_wishes(doc['name'], doc['email'])

    query = {"anniversary": str(today.day) + "/" + str(today.month)}
    for doc in collection.find(query):
        send_anniversery_wishes(doc['name'], doc['email'])


def send_birthday_wishes(name, email):
    html = open('birthday.html').read()
    contents = [
        html
    ]
    yagmail.SMTP(MAILER).send(email, 'Happy Birthday ' + name + '!', contents)


def send_anniversery_wishes(name, email):
    html = open('anniversary.html').read()
    contents = [
        html
    ]
    yagmail.SMTP(MAILER).send(email, 'Happy Anniversary ' + name + '!', contents)


def main():
    start_mail()


if __name__ == '__main__':
    main()
