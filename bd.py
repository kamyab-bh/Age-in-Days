from flask import Flask, request, render_template
from datetime import date 
today = None
age = None
year = None
today = date.today()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():

    name = request.form['name']
    date = request.form['date']
    # print(name)
    

    # Python3 code to calculate age in years 
    # Driver code
    x = date.split("-")

    y = int(x[0])
    m = int(x[1])
    d = int(x[2])

    age = today.year - y
    years = age
    monthsx = today.month - m
    daysx = today.day - d

    dz=0
    if monthsx >= 1:
        dz +=1
    elif monthsx >= 2:
        dz -=2
    elif monthsx >= 3 or 4:
        dz +=1
    elif monthsx >= 5 or 6:
        dz +=1
    elif monthsx >= 7:
        dz +=1
    elif monthsx >= 8 or 9:
        dz +=1
    elif monthsx >= 10 or 11:
        dz +=1
    elif monthsx >= 12:
        dz +=1


    L = 0
    for i in range(y,today.year):
        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
            L += 1

    days = years * 365 + (monthsx * 30) + daysx + L +dz
    return render_template('pass.html',n=name, a=age, days=days)
