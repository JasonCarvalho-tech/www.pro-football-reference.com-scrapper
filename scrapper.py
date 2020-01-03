from bs4 import BeautifulSoup
import requests
import csv

players = open('players.csv','w',newline='')
players_w = csv.writer(players)

players_w.writerow(['name','height','years'])


for j in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    source = requests.get('https://www.pro-football-reference.com/players/' + j +'/')
    playersPage = BeautifulSoup(source.text, 'lxml')
    playerList = playersPage.find('div',{'id':'div_players'})

    for i in playerList.find_all('b') :
        activePlayer = i.parent
        name = activePlayer.a.text
        year = activePlayer.text[-9:]
        playerPageLink = 'https://www.pro-football-reference.com' + activePlayer.a['href']
        playerDetailPage = requests.get(playerPageLink)
        playerDetails = BeautifulSoup(playerDetailPage.text, 'lxml')
        height = playerDetails.find('span',{'itemprop':'height'}).text
        players_w.writerow([name, height, year])
        print(name)
        print(height)
        print(year)
        print()