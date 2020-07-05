#DBConnect.py handles connections to the SQL world database
#pymysql is the object used to interact with the database
import pymysql.cursors



#function that will connect to the database every time it is called
conn = pymysql.connect(host='localhost',
                             user='root',
                             password='success',
                             db='world',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
#Test to check db connection is good and print confirmation
print ("test for connect()")

       


#MENU Choice 1: View all people
def view_people():
    with conn:
        cursor = conn.cursor()  
        sql = ('Select * from person;') 
        cursor.execute(sql)
        data = cursor.fetchall()
#for loop to iterate through the data and print in a formatted way      
        for row in data:

             print (row["personID"], ":", row["personname"] ,":",row["age"] ) 
             
#MENU Choice 2: Input IndepYear to view Countries 
def find_IndepYear(IndepYear):
    print("Search for Independence Year: ", IndepYear)
    with conn:
        cursor = conn.cursor()  
#sql query to return all columns from table 'country'
#%%%s%% is a wildcard for string values, it represents a parameter that will
#be passed later to the query
        sql = ("SELECT * from country where IndepYear LIKE '%%%s%%' " % (IndepYear,) )
        cursor.execute(sql)
        data = cursor.fetchall()
 #for loop to iterate through the data and print the required fields in a formatted way
        for row in data:
             print (row["Name"], ":", row["Continent"] ,":", row["IndepYear"])

#MENU Choice 3: Add new person to world database
def newperson(personname, age):
    with conn:
        try:
            cursor = conn.cursor()  
#sql query to pass in parameters into the columns identified as %s
#this helps prevent sql injection attack (when user input sql query may manipulate the database)
#and provides error handling
            sql = ("Insert into person (personname, age) VALUES (%s, %s)")  
            cursor.execute(sql, (personname, age))
            cursor.close()
#print confirmation that insert has been successful
            print("New Records Accepted into worldDB")
#If the user enters a name that already exists in the database, the person should not be added to
#the database, and an error message will be displayed            
        except pymysql.err.IntegrityError as e:
            print("****Error***:",personname, "already exists" )
#If the user does not enter a number into the age parameter, the input should not be added to
#the database, and an error message should be displayed:                      
        except pymysql.err.InternalError as e:   
            print("***ERROR:",age,"invalid input, please re-enter an integer***") 
#final catch-all error message for any other errors/exceptions that may be thrown up            
        except Exception as e:
            print("***ERROR***")
      
#MENU Choice 4: Input Name to view Countries
#The user is asked to enter a country name, or part thereof.
#Any country that contains those letters should be displayed            
def find_Country(country):
    with conn:
        cursor = conn.cursor()  
#sql query to return all columns from table 'country'
#%%%s%% is a wildcard for string values, it represents a parameter that will
#be passed later to the query
        sql = ("SELECT * from country where Name LIKE '%%%s%%' " % (country,) )
        cursor.execute(sql)
        data = cursor.fetchall()
#for loop to iterate through the data and print the required fields in a formatted way
        for row in data:
             print (row["Name"], ":", row["Continent"] ,":", row["Population"],":", row["HeadOfState"])
             
             

#MENU Choice 5: view country by population
def country_Population(operator,population):

    with conn:
        cursor = conn.cursor()  
#sql query to return the required fields from the country table and reference them to the 
#operator and population as input by user       
        sql = ('Select Code, Name, Continent,Population from country where population %s %s'% (operator, population)) 
        cursor.execute(sql)
        data = cursor.fetchall()
#for loop to iterate through the data and print in a formatted way
        for row in data:
            print (row["Code"], ":", row["Name"] ,":", row["Continent"],":", row["Population"])
 
