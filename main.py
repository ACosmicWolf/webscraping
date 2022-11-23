import requests
from bs4 import BeautifulSoup
import random
import datetime
import sys

def random_quote():
    URL = "http://www.values.com/inspirational-quotes"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')
    quotes = []

    table = soup.find('div', attrs={'id': 'all_quotes'})

    for a in table.find_all('img'):
        q = a.get('alt')
        q = q.split('#<')[0]
        quotes.append(q)

    return quotes[random.randint(0, len(quotes))]

def get_weather():
    url = "https://www.accuweather.com/en/in/dharamshala/3018757/current-weather/3018757"
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0"
    }
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content,'html5lib')

    info = {}

    info['place'] = "Dharamshala, HP, India"
    info['temp'] = soup.find_all("div",class_='display-temp')[0].text.split('\n')[0]
    info['weather'] = soup.find_all("div",class_='phrase')[0].text
    info['date'] = str(datetime.date.today())

    return info

def printArgs():
    print("--help   -h Show available arguments")
    print("quote    Print A Random Quote")
    print("weather  Print the weather")
    print("           available arguments: place temp weather date")

args = sys.argv[1:]

if(len(args)>0):
    if args[0] == '-h' or args[0] == '--help':
        printArgs()
    elif args[0] == 'quote':
        print(random_quote())
    elif args[0] == 'weather':
        if len(args) > 1:
            if args[1] == 'place':
                print(get_weather()['place'])
            elif args[1] == 'temp':
                print(get_weather()['temp'])
            elif args[1] == 'weather':
                print(get_weather()['weather'])
            elif args[1] == 'date':
                print(get_weather()['date']) 
        else:
            info = get_weather()
            print(info['place'])
            print(info['temp'])
            print(info['weather'])
            print(info['date'])
    else:
        print("Please give a valid argument")
        print("type --help or -h for available arguments")

