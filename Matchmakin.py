#importing modules
import pandas as pd 
import datetime
import mysql.connector as my 
import time


# functions
def delay(x=2):
    time.sleep(x)




#connection
con=my.connect(host='localhost',user='root',passwd='iphone',database='project')
mycursor = con.cursor()


# while a=="y":
print()
print("We welcome you".center(70,' '))
print("to our Match-Making Program".center(70,"-"))
print()
print("_".center(70,"_"))
print()
print('''1.signup                        2.Already having your account.(Login)'''.center(30,"-"))
print("_".center(70,"_"))
print()
siglog=int(input('Enter your choice-:'))

if siglog==1:
    print("_".center(70,"_"))
    print()
    print("SIGNUP".center(70," "))
    print("_".center(70,"_"))
    print()
    ui=input("Create your USERNAME-:")
    pas=input('PASSWORD-:')
    repas=input('Re-Enter your PASSWORD-:')    
    while pas!=repas:
        repas=input('Re-Enter your PASSWORD-:')

    
    


    verification_query=f"select * from signup where userid= '{ui}' "
    retrieved_data=pd.read_sql(verification_query,con)

    if retrieved_data.empty==True:
        sql = "INSERT INTO signup (userid,pass) VALUES (%s, %s)"
        sql_2 = "INSERT INTO profile (userid) VALUES (%s)"
        
        val_1 = (ui,pas)
        val_2 = [ui]
        mycursor.execute(sql_2,val_2)
        mycursor.execute(sql, val_1)

        con.commit()
        print('-'.center(70,'-'))
        print(''' Signup Completed.  '''.center(70,' '))
        print('*'.center(70,'*'))
        print()
    else:
        print('-'.center(70,'-'))
        print("user already exist from this user id")
        print('*'.center(70,'*'))
        print()
    siglog=2


elif siglog!=2:
    print('Wrong input.')
 

if siglog==2:
    print("_".center(70,"_"))
    print()
    print("LOGIN".center(70," "))
    print("_".center(70,"_"))
    print()
    ui=input('USERNAME-:')
    pas=input('PASSWORD-:')

    query=f'Select * from signup where userid="{ui}";'
    df=pd.read_sql(query,con)


    repas=df.iat[0,1]
    while pas!=repas:
        pas=input('Re-Enter your PASSWORD-:')

    if df.empty==True:
        print("No user found.")



    elif df.iat[0,1]==pas:
        query_2=f'select name,dob from profile where userid ="{ui}"'
        retrieved_data=pd.read_sql(query_2,con)
        #print(retrieved_data.empty)

        if retrieved_data.iat[0,0]==None:
            print("_".center(70,"_"))
            print()
            print("PROFILE SETUP ".center(70," "))
            print("_".center(70,"_"))
            print()
            name=input('Full Name :-')
            dob=input('Enter your date of birth(yyyy/mm/dd) -:')
            # age=datetime.date.now()
            gen=input('Enter your gender/sex (M/F) -:')
            #print('Your gender:',gender)
            age=int(input('Age :-'))
            stream=input('Carrer approach :-')
            print()
            print('''Now,fill the requirement.'''.center(70,'-'))
            print()
            insta=input('Instagram username :-')
            a3=input('Favourite song genre :-')
            a1=input('''Which sports are you interested in :-''')
            a2=input('''Hobbies you are into practise :- ''')
            a4=input('''The topic, you would like to debate :-''')
            a5=input('''Your favourite Dating destination in India :- ''')
            
            sql1 = "update profile set name=%s, gender=%s,age=%s,insta_id=%s,stream=%s,sports=%s,hobbies=%s,song=%s,topic=%s,destination=%s,dob=%s where userid=%s;"
            val1 = (name,gen,age,insta,stream,a1,a2,a3,a4,a5,dob,ui)
            mycursor.execute(sql1,val1)
            con.commit()
            print()
            print("Your Profile is Succesfully built. ")
            print()
            print("Now we are searching a match for you. ")
            print(" ".center(30,'*'))
            delay(5)

            match_making_query=f'select name , insta_id from profile where gender not in ("{gen}") and destination="{a5}" and age between {age-10} and {age+10};'
            data_2=pd.read_sql(match_making_query,con)

            if data_2.empty==True:
                print("No Matches Found")
                print('We are not having sufficient data to find your match.\nTry login after sometime.')
                exi=input('Press Enter to exit.')

            else:
                user_input=""
                while user_input=="":

                    data_3=data_2.sample()
                    name_1=f'select name from profile where userid="{ui}";'
                    matchname_1=pd.read_sql(name_1,con)
                    matchname_1=matchname_1.iat[0,0]
                    matchname_2=data_3.iat[0,0]
                    print('Congratulations.'.center(30,'-'))
                    print('Hey,',matchname_1,'\nWe have found',matchname_2,'for you.')
                    print('You can Proceed your personal chats/talks.\nUse this Instagram ID : ',data_3.iat[0,1]) 
                    #print(data_2)

                    print()
                    user_input=(input("If not Satisfied , press enter for more or else press '0'."))
        elif retrieved_data.empty==False:
            print()
            print('Hey,',retrieved_data.iat[0,0])
            print('You have already built your profile earlier.')
            print('Just for confirmation, your DOB is',retrieved_data.iat[0,1])
            print()
            print("Now we are searching for your match. ")
            print(''.center(30,'-'))
            delay(5)

            retrieved_data_1=f'select gender,destination,age from profile where userid="{ui}";'
            retrieved_dataframe=pd.read_sql(retrieved_data_1,con)
            gen=retrieved_dataframe.iat[0,0]
            a5=retrieved_dataframe.iat[0,1]
            age=retrieved_dataframe.iat[0,2]

            match_making_query=f'select name , insta_id from profile where gender not in ("{gen}") and destination="{a5}" and age between {age-10} and {age+10};'
            data_2=pd.read_sql(match_making_query,con)
            #print(data_2)

            if data_2.empty==True:
                print("No Match Found")
                print('We are not having sufficient data to find your match.\nTry login after sometime.')
                print()
                exi=input('Press enter to exit.')

            else:
                user_input=""
                while user_input=="":

                    data_3=data_2.sample()
                    #print(data_2)
                    name_1=f'select name from profile where userid="{ui}";'
                    matchname_1=pd.read_sql(name_1,con)
                    matchname_1=matchname_1.iat[0,0]
                    matchname_2=data_3.iat[0,0]
                    print()
                    print('Congratulations.'.center(70,'-'))
                    print()
                    print('Hey,',matchname_1,'\nWe have found',matchname_2,'for you.')
                    print('You can Proceed your personal chats/talks.')
                    print('Use this Instagram ID : ',data_3.iat[0,1]) 
                    #print(data_2)

                    print()
                    user_input=(input("If not Satisfied , press enter for more or else press '0'."))
                    print("_".center(70,"_"))
                    







