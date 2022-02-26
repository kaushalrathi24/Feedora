import mysql.connector as sql

mydb =sql.connect(
    host="localhost",
    user="root",
    charset="utf8",
    passwd="prithvi321",auth_plugin='mysql_native_password',
    database= "project")

mycursor = mydb.cursor()

'''mycursor.execute("create table user(SL_No int auto_increment,user_id varchar(15) primary key,password varchar(256)")
mycursor.execute("create table preference(SL_No int primary key auto_increment,user_id varchar(15),topics varchar(128),outlet varchar(128),foreign key(user_id) references user(user_id)")
mycursor.execute("create table salt(SL_No int primary key auto_increment,user_id varchar(15),salt_values varchar(256),foreign key (user_id) references user(user_id))")
mycursor.execute("create table articles(SL_No int primary key auto_increment,Article varchar(1000),Topic varchar(20),Outlet varchar(20))")
mycursor.execute("create table rss_feeds(SL_No int primary key auto_increment,outlet varchar(20),topic varchar(20),url varchar(100))")
'''

with open("urls.txt","w") as f:
    mycursor.execute("select outlet,topic,url from rss_feeds")
    records = mycursor.fetchall()
    for record in records:
        f.write(str(record))

f.close()
#mydb.commit()
