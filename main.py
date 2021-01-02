from bs4 import BeautifulSoup
import requests

url = "https://www.basketball-reference.com/leagues/NBA_2021_per_game.html"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'lxml')
list = ''
f = open("NBAoutput.txt", "w", encoding="utf8")
for tr in soup.find('table', id='per_game_stats').find_all('tr', class_='full_table'):
    td_list = tr.find_all('td')
    print(td_list[0].text + "," + td_list[1].text + "," + td_list[2].text + "\n")
    sen = td_list[0].text + "," + td_list[1].text + "," + td_list[2].text + "\n"
    f.write(sen)
f.close()

