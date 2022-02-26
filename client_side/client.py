import random
import hashlib
import eel
import string
import mysql.connector as sql
import json


@eel.expose
def login(username, password):
    global user
    user = username
    cursor.execute(
        f'select salt, password from user_info where username = "{username}"')
    value = cursor.fetchall()
    if value:
        salt, database_password = value[0]
        final_password = password + f'$!Wpm' + salt
        hash_value = hashlib.sha256(final_password.encode("utf-8")).hexdigest()
        if hash_value == database_password:
            return 1
        else:
            return 0
    else:
        return 0


@eel.expose
def create(username, password):
    global user
    cursor.execute(f'select * from user_info where username = "{username}"')
    if cursor.fetchall():
        return 0
    else:
        user = username
        salt = salt_generator()
        final_password = password + f'$!Wpm' + salt
        hash_value = hashlib.sha256(final_password.encode("utf-8")).hexdigest()
        cursor.execute(
            f'insert into user_info values("{username}",  "{salt}", "{hash_value}", NULL, NULL)')
        mydb.commit()
        return 1


@eel.expose()
def update_data(data, column):
    command = f"update user_info set {column} = '{data}' where username = '{user}'"
    cursor.execute(command)
    mydb.commit()
    return 1


def salt_generator():
    char_set = string.digits + string.ascii_letters + string.punctuation
    salt = ''
    for i in range(5):
        salt += random.choice(char_set)
    return salt


@eel.expose()
def content():
    cursor.execute(
        f"select topics, websites from user_info where username = '{user}' ")
    result = cursor.fetchone()
    topics = eval(result[0])
    websites = eval(result[1])
    articles = []
    query = "select data from articles where (topic in ( '" + "', '".join(
        topics) + "') and outlet in ( '" + "', '".join(websites) + "')) order by pub_date DESC"
    cursor.execute(query)
    for article in cursor.fetchall():
        articles.append(json.loads(article[0]))

    return json.dumps(articles)


mydb = sql.connect(
    host='localhost',
    user='root',
    passwd='oneminutenineseconds',
    database='news')

cursor = mydb.cursor()
user = ''
eel.init('gui')
eel.start('main.html', cmdline_args=['--incognito'])
