import json
import requests
from flask import render_template, flash, redirect
from app import application, db, models
from .forms import LoginForm
from .foo import *

def makingStrings():
    return 'I am making ' + str(1) + ' string!!'

def tempReq(playerName):
    tempURL = 'https://na.api.riotgames.com/api/lol/NA/v1.4/summoner/by-name/'#Chinchilla?api_key='
    apiKey = 'RGAPI-83876d54-625e-4554-a8ee-32b1875becd9'
    URL = tempURL + playerName + '?api_key=' + apiKey
    response = requests.get(URL)
    return response.json()

#def getName(jsonObj):
#    sumName = jsonObj[sumName]['id']

@application.route('/')
@application.route('/index')
def index():
    user = {'nickname': 'Laurence'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

@application.route('/league')
def league():
    user = {'nickname': 'Summoner'}
    baz = makingStrings()
    bar = makeString()
    summonerName = 'trippinzdawg'
 #   testString = reqURL()
    responseJSON = tempReq(summonerName)
    #sumID = responseJSON['chinchilla']['id']
    #sumName = responseJSON['chinchilla']['name']
    #sumLevel = responseJSON['chinchilla']['summonerLevel']
    sumID = responseJSON[summonerName]['id']
    sumName = responseJSON[summonerName]['name']
    sumLevel = responseJSON[summonerName]['summonerLevel']
    sumID = str(sumID)
    sumName = str(sumName)
    sumLevel = int(sumLevel)

    u = models.Player(name=sumName, level=sumLevel)
    k = models.Player(name='Keep Chasing', level=30)
#    db.session.add(k)
    #db.session.add(u)
    #db.session.commit()

    playerOne = models.Player.query.get(1)

    players = models.Player.query.all()


    return render_template('league.html',
                           title='LeagueTool',
                           user=user,
                           baz=baz,
                           bar=bar,
#                           testString=testString,
                           responseJSON=responseJSON,
                           summonerName=summonerName,
                           sumID=sumID,
                           sumName=sumName,
                           sumLevel=sumLevel,
                           u=u,
                           k=k,
                           playerOne=playerOne,
                           players=players)