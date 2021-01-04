from bs4 import BeautifulSoup
import requests
import pymysql

# Open database connection
db = pymysql.connect("198.38.92.158","directf2_devuser","WELcome!@#123","directf2_dev_fra" )
try:
    print("connection succeeded")
except:
    print("connection failed")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to DELETE required records
deleteSQL = "DELETE FROM playerdetails;"
try:
   # Execute the SQL command
   cursor.execute(deleteSQL)
   print("delete succeeded")
   # Commit your changes in the database
   db.commit()
except:
   print("delete failed")
   ## Rollback in case there is any error
   db.rollback()


url = "https://www.basketball-reference.com/leagues/NBA_2021_per_game.html"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'lxml')
list = ''
f = open("NBAoutput.txt", "w", encoding="utf8")

for tr in soup.find('table', id='per_game_stats').find_all('tr', class_='full_table'):
    td_list = tr.find_all('td')
    th_id = tr.find('th')
    insertSQL = "INSERT INTO playerdetails (Player_id,Player_name, Player_pos, Player_age, Player_team) VALUES (" + th_id.text +",\""+ td_list[0].text + "\",\"" + td_list[1].text + "\"," + td_list[2].text + ",\"" + td_list[3].text + "\");\n"
    ##print(insertSQL)
    try:
        # Execute the SQL command
        cursor.execute(insertSQL)
        # Commit your changes in the database
        db.commit()
    except (db.Error, db.Warning) as e:
        print(e)
    except:

        # Rollback in case there is any error
        db.rollback()

    f.write(insertSQL)
# disconnect from server
db.close()
f.close()