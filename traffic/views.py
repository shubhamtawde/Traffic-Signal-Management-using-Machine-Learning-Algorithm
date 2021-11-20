from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import mysql.connector
from pymsgbox import *
from pymysql import *
from .forms import CreateUserForm
# Create your views here.
lat=0.0
lon=0.0
roads=[]
jam_factor = []
time_saved = []
cars = 0

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="traffic"
)
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html',{
        'time1':'20'});
def location(h):
    import json
    import requests
    lat = lon = 0.0
    response = requests.get("https://geocode.search.hereapi.com/v1/geocode?q="+h+"&apiKey=0k30d8NNE3Pz6plpwT6YE6WJsiAwQ3ulsVjudVvZk_Q")
    data= json.loads(response.text)
    for i in data["items"]:
      for m, n in i["position"].items():
            if m == 'lat':
                lat = n
            if m == 'lng':
                lon = n
    coordinates=[lat,lon]
    return coordinates
@login_required(login_url='login')
def place(request):
    h=request.GET['place']
    coordinates=location(h)
    if (coordinates[0]==0.0 and coordinates[1]==0.0):
        return render(request, 'index.html', {'lat':'Not available', 'color':'black'})
    else:
        global lat
        lat=coordinates[0]
        global lon
        lon=coordinates[1]
        print(lat)
        print(lon)
        return render(request, 'index.html', {'lat':lat,'lon':lon, 'color':'black'})

@login_required(login_url='login')
def fetch(request):
    #import requests
    #global lat
    #global lon
    #lat1=str(lat)
    #lon1=str(lon)
    #print(lat1,lon1)
    #response = requests.get("https://traffic.ls.hereapi.com//traffic/6.2/flow.json?bbox="+str(lat1)+"%2C"+str(lon1)+"%3B"+str(lat1)+"%2C"+str(lon1)+"&apiKey=0k30d8NNE3Pz6plpwT6YE6WJsiAwQ3ulsVjudVvZk_Q")
    #response = requests.get(url)
    #print(response.status_code)
    #print(response.json())
    import numpy
    import pickle
    import pandas as pd
    import random

    #saving model to disk
    filename = 'traffic/trained_model.pkl'
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

    #c contains the predicted output class based on the input
    c = predicted_y[0]

    #default time for all the timers (15 secs)
    timer1 = timer2 = timer3 = timer4 = 15
    data1=person.values.tolist();
    j1 = data1[0][0]
    j2 = data1[0][1]
    j3 = data1[0][2]
    j4 = data1[0][3]
    global jam_factor
    jam_factor = [j1,j2,j3,j4]
    print(jam_factor)
    #All conditions of our output classess
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
    totaltime = timer1 + timer2 + timer3 + timer4
    save_time = t1 + t2 + t3 + t4
    j1 = jam_factor[0]
    j2 = jam_factor[1]
    j3 = jam_factor[2]
    j4 = jam_factor[3]
    nj1 = nj2 = nj3 = nj4 = 0
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
    per1=((nj1-j1)/j1)*100
    per2=((nj2-j2)/j2)*100
    per3=((nj3-j3)/j3)*100
    per4=((nj4-j4)/j4)*100
    new_jam=[nj1,nj2,nj3,nj4]
    perc = [per1,per2,per3,per4]
    print(j1)
    print(j2)
    print(j3)
    print(j4)
    print(cars)
    print("Total time")
    total_time = time_saved[0] + time_saved[1] + time_saved[2] + time_saved[3]
    db = [[roads[0], nj1, time_saved[0], perc[0]], [roads[1], nj2, time_saved[1], perc[1]],[roads[2], nj3, time_saved[2], perc[2]],[roads[3], nj4, time_saved[3], perc[3]]]
    print(db)
    return render(request, 'index.html',{'message':'Data fetched!','data':a, 'totaltime': totaltime, 'savetime': save_time, 'db': db})
def register(request):
    form= CreateUserForm()
    if request.method =='POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            firstname = form.cleaned_data.get('first_name')
            password = form.cleaned_data.get('password1')
            email= form.cleaned_data.get('email')
            messages.success(request,'Account is created for '+ firstname)
            return redirect('login')
    context={'form':form}
    return render(request, 'register.html',context);
def login(request):
    if request.method =='POST':
       email= request.POST.get('email')
       password= request.POST.get('password')
       username = User.objects.get(email=email.lower()).username
       user= authenticate(request, username=username, password=password)

       if user is not None:
           auth_login(request,user)
           send_mail(
            'Login into Traffic Control Portal',
            'This is to notify that your account has been logged in from our portal. If the activity is not done by you, please report to the authorities',
            'trafficcontrolportal.project@gmail.com',
            [email],
            fail_silently=False,
            )
           return redirect('home')
       else:
           send_mail(
            'Unusual activity detected on Traffic Control Portal',
            'An activity to login to your account on Traffic Control Portal is attempted. If the activity is not done by you, please report to the authorities',
            'trafficcontrolportal.project@gmail.com',
            [email],
            fail_silently=False,
            )
           messages.info(request,'Login credentials are incorrect')
    return render(request, 'login.html');
def logout(request):
    auth_logout(request)
    return redirect('login')
@login_required(login_url='login')
def stats(request):
    import random
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM statistics ORDER BY id DESC LIMIT 4")
    myresult = mycursor.fetchall()
    print(myresult)
    cursor1 = mydb.cursor()
    cursor1.execute("SELECT SUM(time_saved) AS time_saved FROM statistics")
    time_tot = cursor1.fetchone()
    global cars
    global time_saved
    print("Total time")
    print(time_tot)
    total_time = time_saved[0] + time_saved[1] + time_saved[2] + time_saved[3]
    total_time = total_time * -1
    return render(request, 'stats.html', {'data':myresult ,'car':cars, 'total_time':total_time, 'time_tot':time_tot});
@login_required(login_url='login')
def export(request):
    # import the modules

    import xlwt
    import pandas.io.sql as sql
    # connect the mysql with the python
    con=connect(user="root",password="",host="localhost",database="traffic")
    # read the data
    df=sql.read_sql('select * from statistics',con)
    # print the data
    print(df)
    # export the data into the excel sheet
    df = df.to_excel('traffic/ds.xls')
    path = 'traffic/ds.xls'
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
