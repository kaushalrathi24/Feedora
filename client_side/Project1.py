import random
import hashlib
import mysql.connector as sql

mydb =sql.connect(
    host="localhost",
    user="root",
    charset="utf8",
    passwd="prithvi321",auth_plugin='mysql_native_password',
    database= "project")

mycursor = mydb.cursor()
nu_str = ("insert into user(SL_No,user_id,password) values(%s,%s,%s)")
nu_salt = ("insert into Salt(SL_No,user_id,salt_values) values(%s,%s,%s)")

'''-------------------------------------------------------------------------------'''
'''def RetrieveArticles(top_list,out_list):
    choice = int(input("Enter to view articles sorted by \n 1 - Outlet \n 2 - Topic \n "))
    if choice == 1:
        print("| ")
        for i in out_list:
            print(i,end=" | ")
            
        out = input("Enter the outlet you wish to view. \n")
        mycursor.execute("select Article,Outlet from Articles where Outlet =" + "('" + out + "')")
        articles = mycursor.fetchall()
        print(articles)
        ind = 0
        while 1:
            print(articles[ind])
            shift_next = int(input("Enter \n 1 - To view next article \n 2 - To view next topic or outlet \n 3 - Quit \n "))
            
            if shift_next == 1:
                ind += 1
                
                if (ind == (len(articles)-1)):
                    print("All articles of this topic/outlet have been viewed.")
                    opt = int(input("Enter \n 1 - View next topic/outlet 2 - Quit \n"))
                    if opt == 1:
                        return RetrieveArticles(top_list,out_list)
                    elif opt == 2:
                        exit()
                    else:
                        print("Please enter a valid choice.")
                        
            elif shift_next == 2:
                return RetrieveArticles(top_list,out_list)
            elif shift_next == 3:
                exit()
            else :
                print("Enter a valid choice.")
        #print(articles)

    elif choice == 2:
        print("| ")
        for j in top_list:
            print(j,end=" | ")
        top = input("Enter the topic you wish to view. \n")
        mycursor.execute("select Article,Outlet from Articles where Topic =" + "('" + top + "')")
        articles = mycursor.fetchall()
        ind = 0
        
        while 1:
            print(articles[ind])
            shift_next = int(input("Enter \n 1 - To view next article \n 2 - To view next topic or outlet \n 3 - Quit \n "))
            
            if shift_next == 1:
                ind += 1
                
                if (ind == (len(articles)-1)):
                    print("All articles of this topic/outlet have been viewed.")
                    opt = int(input("Enter \n 1 - View next topic/outlet 2 - Quit \n"))
                    if opt == 1:
                        return RetrieveArticles(top_list,out_list)
                    elif opt == 2:
                        exit()
                    else:
                        print("Please enter a valid choice.")
                        
            elif shift_next == 2:
                return RetrieveArticles(top_list,out_list)
            elif shift_next == 3:
                exit()
            else :
                print("Enter a valid choice.")
        #print(articles)

    else :
        print("Enter a valid choice.")
        
def RetrievePref(user):
    
    str1 = ("select topic,outlet from preference where user_id = ")
    mycursor.execute(str1 + "('" + user + "')")
    topics,outlets = mycursor.fetchone()
    top_list = topics.split(",")
    out_list = outlets.split(",")
    return RetrieveArticles(top_list[1:],out_list[1:])'''

def Top_Out(user):
    choice = int(input("Enter \n 1 - To view by topic \n 2 - To view by outlet \n"))
    if choice == 1:
        mycursor.execute("select topic from preference where user_id = '" + username + "'")
        top = list(mycursor.fetchone())
        top_tup = tuple(top[0].split(",")[1:])
        return Select(top_tup,"Topic",user)
    
    elif choice == 2:
        mycursor.execute("select outlet from preference where user_id = '" + username + "'")
        out = list(mycursor.fetchone())
        out_tup = tuple(out[0].split(",")[1:])
        return Select(out_tup,"Outlet",user)
    
    else :
        print("Please enter a valid choic.")
        return Top_Out(user)

def Select(pref,sortby,user):
    print(" | ")
    for i in pref:
        print(i,end = " | ")
    print()
    while 1:
        choice = input("Enter Topic of choice. \n")
        if choice in pref :
            mycursor.execute("select Article,Topic,Outlet from articles where " + sortby + " = '" + choice + "'")
            articles = mycursor.fetchall()
            return Display(articles,user)

        else:
            print("Enter a valid choice.")
        
def Display(articles,user):
    if len(articles) == 0:
        print("There are no. articles left in this topic.")
        return Top_Out(user)
    else:
        print(articles[0])
        val =int(input("Enter \n 1 - to view next article \n 2 - to view next topic/outlet \n 3 - Quit \n"))
        if val == 1:
            return Display(articles[1:],user)
        elif val == 2:
            return Top_Out(user)
        elif val == 3:
            exit()
        else :
            print("Enter a valid choice.")
            return Display(articles,user)

def Pref(user):
    
    topics_dict = {'top1':1,"top2":2,"top3":3}
    ValDict1 = {1:'top1',2:"top2",3:"top3"}
    print("| ",end = "")
    
    for top in topics_dict:
        print(top,"( Value : ",topics_dict[top]," )",end = " | ")
    print(" \n")
    
    vals = eval(input("Enter the corresponding of the topics of your preference as a list"))
    topics = ""
    
    for i in vals:
        topics += "," + ValDict1[i]
    #print(topics)
        
    outlets_dict = {'out1':1,"out2":2,"out3":3}
    ValDict2 = {1:'out1',2:"out2",3:"out3"}
    print("| ",end = "")
    
    for out in outlets_dict:
        print(out,"( Value : ",outlets_dict[out]," )",end = " | ")
    print(" \n")
    
    vals = eval(input("Enter the corresponding value of the outlets of your preference as a list"))
    outlets = ""
    
    for i in vals:
        outlets += "," + ValDict2[i]
    #print(outlets)

    str1 = ("insert into preference(user_id,topic,outlet) values(%s,%s,%s)")
    tup1 = (user,topics,outlets)
    mycursor.execute(str1,tup1)
    print()
    
def Hash(pwd):
    h_str = hashlib.sha256(pwd.encode("utf-8")).hexdigest()
    return h_str

def Validation(uid,pwd):
    confirmed = 0
    list1 = []
    str1 = ''
    if len(uid) < 3:
        str1 = uid
    else :
        for i in range(0,2):
            str1 += uid[i]
        
    string = ("select user_id from user where user_id like ")
    mycursor.execute(string + '"' + str1 + '%"')
    res = mycursor.fetchall()
    if len(res) == 0:
        confirmed = 0
    
    else :
        for i in res :
            if uid == i[0]:
                p_select = ("select password from user where user_id like ")
                mycursor.execute(p_select + '"' + uid + '%"')
                pass1 = mycursor.fetchone()[0]
                salt_select = ("select salt_values from Salt where user_id like ")
                mycursor.execute(salt_select + '"' + uid + '%"')
                salt1 = mycursor.fetchone()
                pass2 = hashlib.sha256(pwd.encode("utf-8")).hexdigest() + salt1[0]
                if pass1 == pass2:
                    confirmed = 1
            else :
                continue
    return confirmed

def Salt():
    a = 0
    salt_str = ''
    for i in range(0,5):
        a= random.randrange(34,126)
        salt_str += chr(a)
    return salt_str

def Values(srln,uid,hash1) :
    list1 = []
    list1.append(srln)
    list1.append(uid)
    list1.append(hash1)
    val = tuple(list1)
    return val
'''---------------------------------------------------------------------'''
while 1:
    choice = int(input("enter : \n 1- Login \n 2- Sign Up \n 3- Quit \n"))

    
    if choice == 1:
        username = input("enter username")
        password = input("enter password")
        print()
        for j in range (0,5):
            confirm = -1
            confirm = Validation(username,password)
            if confirm != 1:
                print("INVALID USERNAME OR PASWORD")
                print((4 - j)," ATTEMPT(S) LEFT. \n")
                username = input("re-enter username")
                password = input("re-enter password")
                print()
                
            else :
                print("LOGIN AUTH. \n")
                conf = 1
                break

            if j == 4:
                print("LOGIN FAILED. \n RETURNING TO HOME.")
        if conf == 1:
            #RetrievePref(username)
            Top_Out(username)
        
    elif choice == 2:
        username = input("enter user name : ")
        password = input("enter the password : ")
        confirm = input("confirm password : ")
        
        while 1:
            if password != confirm :
                print("Password does not match confirmation.")
                password = input("reenter password : ")
                confirm = input("confirm password : ")
            else :
                break
            
        mycursor.execute("select max(SL_No) from user")
        serial = mycursor.fetchone()[0]
        if serial == None:
            serial = 1
        else:
            serial += 1
            
        salt = Salt()
        pass1 = Hash(password) + Hash(salt)
        nu_val = Values(serial,username,pass1)
        salt_val = Values(serial,username,Hash(salt))
        mycursor.execute(nu_str,nu_val)
        mycursor.execute(nu_salt,salt_val)

        Pref(username)
        mydb.commit()

    elif choice == 3:
        exit()

    else:
        print("PLEASE ENTER A VALID CHOICE. \n")

'''-----------------------------------------------------------------------------'''

