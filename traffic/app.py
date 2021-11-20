from flask import Flask, request, jsonify, redirect, url_for,send_file
from flask_cors import CORS
from flask_mail import *
import mysql.connector
import datetime
import xlwt
import os
import pandas.io.sql as sql

app = Flask(__name__)
CORS(app)
app.config["MAIL_SERVER"]='smtp.gmail.com'
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = 'trafficcontrolportal.project@gmail.com'
app.config['MAIL_PASSWORD'] = 'beproject'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="traffic"
)

@app.route('/display', methods=['GET','POST'])
def helloWorld():
    json_data = request.json['a']
    json_data1 = request.json['b']
    json_data2 = request.json['c']
    json_data3 = request.json['d']
    flag = request.json['flag']
    print("Flag")
    print(flag)
    act = [json_data, json_data1, json_data2, json_data3]
    print(act[0])
    print(act[1])
    print(act[2])
    print(act[3])
    today = datetime.datetime.now()

    if flag == 1:
        mycursor = mydb.cursor()
        for x in range(4):
          rn = act[x][0]
          jf = float(act[x][1])
          print(type(jf))
          if jf < 0:
              jf = jf * -1
          ts = float(act[x][2])
          if ts < 0:
              ts = ts * -1
          perf = float(act[x][3])
          if perf < 0:
              perf = perf * -1
          sql = "INSERT INTO statistics (road_name,jam_factor,time_saved,date,status) VALUES (%s, %s, %s, %s, %s)"
          val = (rn,jf,ts,today,perf)
          mycursor.execute(sql, val)
          mydb.commit()
          print(mycursor.rowcount, "Inserted Successfully")
          print("Jam Factor: ")
    #print(send)
    #print(response.json())
    import numpy
    import pickle
    import pandas as pd
    import random

    #saving model to disk
    filename = 'trained_model.pkl'
    loaded_model = pickle.load(open(filename, 'rb'))
    person = pd.DataFrame()
    rand1 = random.uniform(1.0, 10.0)
    rand2 = random.uniform(1.0, 10.0)
    rand3 = random.uniform(1.0, 10.0)
    rand4 = random.uniform(1.0, 10.0)
    person['road_1'] = [rand1]
    person['road_2'] = [rand2]
    person['road_3'] = [rand3]
    person['road_4'] = [rand4]
    person['road_5'] = [rand1]
    person['road_6'] = [rand2]
    person['road_7'] = [rand3]
    person['road_8'] = [rand4]
    print(person)
    # the data is stored in Datadrame person
    predicted_y = loaded_model.predict(person)
    print(predicted_y[0])

    c = predicted_y[0]

    timer1 = timer2 = timer3 = timer4 = 15
    data1=person.values.tolist();
    j1 = data1[0][0]
    j2 = data1[0][1]
    j3 = data1[0][2]
    j4 = data1[0][3]
    global jam_factor
    jam_factor = [j1,j2,j3,j4]
    print(jam_factor)
    if c == 0:
        timer1 = 15
        timer2 = 15
        timer3 = 15
        timer4 = 15
    if c == 1:
        if j4 >= 5 and j4 <= 7:
            timer4 = 25
        if j4 >= 7:
            timer4 = 30
        if j2<=4:
            timer2 = 15
        if j2>4:
            timer2 = 20
        if j3<=4:
            timer3 = 15
        if j3>4:
            timer3 = 20
        if j1<=4:
            timer1 = 15
        if j1>4:
            timer1 = 20

    if c == 2:
        if j3 >= 5 and j3 <= 7:
            timer3 = 25
        if j3 >= 7:
            timer3 = 30
        if j1<=4:
            timer1 = 15
        if j1>4:
            timer1 = 20
        if j2<=4:
            timer2 = 15
        if j2>4:
            timer2 = 20
        if j4<=4:
            timer4 = 15
        if j4>4:
            timer4 = 20
    if c == 3:
        if j4 >= 5 and j4 <= 7:
            timer4 = 25
        if j4 >= 7:
            timer4 = 30
        if j3 >= 5 and j3 <= 7:
            timer3 = 25
        if j3 >= 7:
            timer3 = 30
        if j1<=4:
            timer1 = 15
        if j1>4:
            timer1 = 20
        if j2<=4:
            timer2 = 15
        if j2>4:
            timer2 = 20
    if c == 4:
        if j2 >= 5 and j2 <= 7:
            timer2 = 25
        if j2 >= 7:
            timer2 = 30
        if j1<=4:
            timer1 = 15
        if j1>4:
            timer1 = 20
        if j3<=4:
            timer3 = 15
        if j3>4:
            timer3 = 20
        if j4<=4:
            timer4 = 15
        if j4>4:
            timer4 = 20
    if c == 5:
        if j2 >= 5 and j2 <= 7:
            timer2 = 25
        if j2 >= 7:
            timer2 = 30
        if j4 >= 5 and j4 <= 7:
            timer4 = 25
        if j4 >= 7:
            timer4 = 30
        if j1<=4:
            timer1 = 15
        if j1>4:
            timer1 = 20
        if j3<=4:
            timer3 = 15
        if j3>4:
            timer3 = 20
    if c == 6:
        if j4 >= 5 and j4 <= 7:
            timer4 = 25
        if j4 >= 7:
            timer4 = 30
        if j3 >= 5 and j3 <= 7:
            timer3 = 25
        if j3 >= 7:
            timer3 = 30
        if j1<=4:
            timer1 = 15
        if j1>4:
            timer1 = 20
        if j2<=4:
            timer2 = 15
        if j2>4:
            timer2 = 20
    if c == 7:
        if j4 >= 5 and j4 <= 7:
            timer4 = 25
        if j4 >= 7:
            timer4 = 30
        if j3 >= 5 and j3 <= 7:
            timer3 = 25
        if j3 >= 7 :
            timer3 = 30
        if j2 >= 5 and j2 <= 7:
            timer2 = 25
        if j2 >= 7 :
            timer2 = 30
        if j1<=4:
            timer1 = 15
        if j1>4:
            timer1 = 20
    if c == 8:
        if j1 >= 5 and j1 <= 7:
            timer1 = 25
        if j1 >= 7 :
            timer1 = 30
        if j2<=4:
            timer2 = 15
        if j2>4:
            timer2 = 20
        if j3<=4:
            timer3 = 15
        if j3>4:
            timer3 = 20
        if j4<=4:
            timer4 = 15
        if j4>4:
            timer4 = 20
    if c == 9:
        if j1 >= 5 and j1 <= 7:
            timer1 = 25
        if j1 >= 7:
            timer1 = 30
        if j4 >= 5 and j4 <= 7:
            timer4 = 25
        if j4 >= 7 :
            timer4 = 30
        if j2<=4:
            timer2 = 15
        if j2>4:
            timer2 = 20
        if j3<=4:
            timer3 = 15
        if j3>4:
            timer3 = 20
    if c == 10:
        if j1 >= 5 and j1 <= 7:
            timer1 = 25
        if j1 >= 7 :
            timer1 = 30
        if j3 >= 5 and j3 <= 7:
            timer3 = 25
        if j3 >= 7 :
            timer3 = 30
        if j2<=4:
            timer2 = 15
        if j2>4:
            timer2 = 20
        if j4<=4:
            timer4 = 15
        if j4>4:
            timer4 = 20
    if c == 11:
        if j1 >= 5 and j1 <= 7:
            timer1 = 25
        if j1 >= 7:
            timer1 = 30
        if j3 >= 5 and j3 <= 7:
            timer3 = 25
        if j3 >= 7:
            timer3 = 30
        if j4 >= 5 and j4 <= 7:
            timer4 = 25
        if j4 >= 7 :
            timer4 = 30
        if j2<=4:
            timer2 = 15
        if j2>4:
            timer2 = 20
    if c == 12:
        if j1 >= 5 and j1 <= 7:
            timer1 = 25
        if j1 >= 7 :
            timer1 = 30
        if j2 >= 5 and j2 <= 7:
            timer2 = 25
        if j2 >= 7 :
            timer2 = 30
        if j3 <= 4:
            timer3 = 15
        if j3 > 4:
            timer3 = 20
        if j4 <= 4:
            timer4 = 15
        if j4 > 4:
            timer4 = 20
    if c == 13:
        if j1 >= 5 and j1 <= 7:
            timer1 = 25
        if j1 >= 7:
            timer1 = 30
        if j2 >= 5 and j2 <= 7:
            timer2 = 25
        if j2 >= 7:
            timer2 = 30
        if j4 >= 5 and j4 <= 7:
            timer4 = 25
        if j4 >= 7:
            timer4 = 30
        if j3<=4:
            timer3 = 15
        if j3>4:
            timer3 = 20
    if c == 14:
        if j1 >= 5 and j1 <= 7:
            timer1 = 25
        if j1 >= 7:
            timer1 = 30
        if j2 >= 5 and j2 <= 7:
            timer2 = 25
        if j2 >= 7:
            timer2 = 30
        if j3 >= 5 and j3 <= 7:
            timer3 = 25
        if j3 >= 7:
            timer3 = 30
        if j4<=4:
            timer4 = 15
        if j4>4:
            timer4 = 20
    if c == 15:
        if j1 >= 5 and j1 <= 7:
            timer1 = 25
        if j1 >= 7:
            timer1 = 30
        if j2 >= 5 and j2 <= 7:
            timer2 = 25
        if j2 >= 7:
            timer2 = 30
        if j3 >= 5 and j3 <= 7:
            timer3 = 25
        if j3 >= 7:
            timer3 = 30
        if j4 >= 5 and j4 <= 7:
            timer4 = 25
        if j4 >= 7:
            timer4 = 30
    t1 = 15-timer1
    t2 = 15-timer2
    t3 = 15-timer3
    t4 = 15-timer4
    global time_saved
    time_saved = [t1,t2,t3,t4]
    global roads
    roads = ['Nana warsi','MG Road','David Road','Gokul Road']
    a = [[timer1,roads[0]],[timer2,roads[1]],[timer3,roads[2]],[timer4,roads[3]]]
    a.sort(key = lambda a: a[0])
    a.sort(reverse = True)
    print(a)
    nj1 = nj2 = nj3 = nj4 = 0
    totaltime = timer1 + timer2 + timer3 + timer4
    global cars
    cars = 0
    if (j1>=5 and j1<=7) or (j2>=5 and j2<=7) or (j3>=5 and j3<=7) or (j4>=5 and j4<=7):
       nj1 = j1-1
       nj2 = j2-1
       nj3 = j3-1
       nj4 = j4-1
       cars = random.randint(18, 22)
    if j1> 7 or j2> 7 or j3> 7 or j4> 7:
       nj1 = j1-2
       nj2 = j2-2
       nj3 = j3-2
       nj4 = j4-2
       cars = random.randint(30, 35)
    if(nj1 < 0):
        nj1 = nj1 * -1
    if(nj2 < 0):
        nj2 = nj2 * -1
    if(nj3 < 0):
        nj3 = nj3 * -1
    if(nj4 < 0):
        nj4 = nj4 * -1

    per1=((j1 - nj1)/j1)*100
    per2=((j2-nj2)/j2)*100
    per3=((j3-nj3)/j3)*100
    per4=((j4-nj4)/j4)*100
    new_jam=[nj1,nj2,nj3,nj4]
    perc = [per1,per2,per3,per4]
    print(j1)
    print(j2)
    print(j3)
    print(j4)
    print(cars)
    print("Total time")
    if flag != 1:
        mycursor = mydb.cursor()
        for x in range(4):
          rn = roads[x]
          jf = float(new_jam[x])
          if jf < 0:
              jf = jf * -1
          ts = float(time_saved[x])
          if ts < 0:
              ts = ts * -1
          perf = float(perc[x])
          if perf < 0:
              perf = perf * -1
          print(rn)
          print(jf)
          print(ts)
          print(perf)
          sql = "INSERT INTO statistics (road_name,jam_factor,time_saved,date,status) VALUES (%s, %s, %s, %s, %s)"
          val = (rn,jf,ts,today,perf)
          mycursor.execute(sql, val)
          mydb.commit()
          print(mycursor.rowcount, "Inserted Successfully")
          print("Jam Factor: ")
    response = jsonify({"t1": a[0][0],"r1": a[0][1],"t2": a[1][0],"r2":a[1][1],"t3": a[2][0],"r3":a[2][1],"t4": a[3][0],"r4":a[3][1]})
    return response


@app.route('/data')
def hello():
    # import the modules
    import xlwt
    import pandas.io.sql as sql
    #con=connect(user="root",password="",host="localhost",database="traffic")
    # read the data
    df=sql.read_sql('select * from statistics',mydb)
    # print the data
    print("In Export function")
    print(df)
    # export the data into the excel sheet
    df = df.to_excel('ds.xls')
    path = 'ds.xls'
    return send_file(os.path.join('ds.xls'), as_attachment=True)

@app.route('/mail1', methods=['GET','POST'])
def mail1():
    import xlwt
    import pandas.io.sql as sql
    # connect the mysql with the python
    #con=connect(user="root",password="",host="localhost",database="traffic")
    # read the data
    df=sql.read_sql('select * from statistics',mydb)
    # print the data
    print(df)
    # export the data into the excel sheet
    df = df.to_excel('ds.xls')
    email = request.json
    print(email)
    msg = Message(subject = "Traffic Analysis Data Report", body = "Traffic Analysis Report", sender = "trafficcontrolportal.project@gmail.com", recipients = [email])
    with app.open_resource("ds.xls") as fp:
        msg.attach("ds.xls","application/vnd.ms-excel",fp.read())
        mail.send(msg)
    return "sent"
