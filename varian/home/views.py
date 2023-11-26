from django.shortcuts import render, redirect
from .forms import LoginForm, RegForm, DataAssign
from .SQLconnector import sqlconnector_account, sqlconnector_patient
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime
# Create your views here.



def home(response):
    return render(response, "main/index.html", {})

def set_session(request):
    request.session["logged"] = True
    return redirect('/home/')

def get_session(request):
    request.session["logged"] = request.session.get('logged', False)
    if request.session["logged"] is True:
        return redirect('/home/')
    return redirect('/login/')

@csrf_exempt
def login(response):
    msg = ""
    if response.method == "POST":
        print("Entered to post")
        form = LoginForm(response.POST)
        if form.is_valid():
            us = form.cleaned_data["account_id"]
            pw = form.cleaned_data["account_pass"]
            sqlcon = sqlconnector_account('root', '', '127.0.0.1')
            state, msg, value, perm, email = sqlcon.check_login(us, pw)
            if perm == 1:
                return redirect('/doctor/')
            if state:
                response.session["userdatas"] = [us,email]
                return redirect('/setsession/')
        else:
            print(f"Form is not valid\n{form.is_valid()}\n{form.errors}")
    else:
        print("Not entered to post : " + response.method)
        form = LoginForm()

    return render(response, "main/log.html", {"form": form, "msg": msg})

@csrf_exempt
def signup(response):
    message = ""
    if response.method == "POST":
        form = RegForm(response.POST)
        if form.is_valid():
            us = form.cleaned_data["a_id"]
            pw = form.cleaned_data["a_pass"]
            pw_check = form.cleaned_data["a_check_pass"]
            a_email = form.cleaned_data["a_email"]
            if pw == pw_check:
                sqlcon = sqlconnector_account('root','','127.0.0.1')
                state, message = sqlcon.register(us,pw,a_email)
            else:
                message = "The passwords are not match, please check them and try again!"
        else:
            print(f"Registration form is not valid\n{form.errors}")
            message = "The passwords are not long enough, min 8 character!"
    else:
        form = RegForm()
    return render(response, "main/reg.html", {"form": form, "Message": message})

from django.core.mail import send_mail
from django.conf import settings

def index(request):
    if request.method == "POST":
        msg = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(name,msg,'settings.EMAIL_HOST_USER', [email, 'tothdani04@gmail.com'],fail_silently=False)
    return render(request, "main/mail.html")
@csrf_exempt
def settings(request):
    error = ""
    message = ""
    print("entered settings def")
    user, email = request.session["userdatas"]
    if request.method == "POST":
        print("entered settings post")
        form = DataAssign(request.POST)
        if form.is_valid():
            print("entered settings post is valid true")
            height = form.cleaned_data["height"]
            weight = form.cleaned_data["weight"]
            allergies = form.cleaned_data["allergies"]
            others = form.cleaned_data["others"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            taj = form.cleaned_data["taj"]
            age = form.cleaned_data["age"]
            sex = form.cleaned_data["sex"]
            region = form.cleaned_data["region"]
            tick = form.cleaned_data["tick"]
            password = form.cleaned_data["password"]
            checkPassword = form.cleaned_data["checkPassword"]
            email = form.cleaned_data["email"]
            if (password or checkPassword) != "" and password == checkPassword:
                sqlcon = sqlconnector_account('root', '', '127.0.0.1')
                if sqlcon.update_password(user,password):
                    message = f"{user}'s password has been successfully updated!"
                else:
                    error = form.errors
            if (height and weight and allergies and others and first_name and last_name and taj and
            age) != None or "":
                sqlcon_patient = sqlconnector_patient('root', '', '127.0.0.1')
                sqlcon_account = sqlconnector_account('root','','127.0.0.1')
                id = int(sqlcon_account.querry_account_by_us(user)[5])
                if sqlcon_patient.add_patient_to_queue(id, height,weight,age,sex,region,f"{first_name} {last_name}",taj, allergies, others):
                    message = "Your data has been successfully sent to the server, check your email for updates"
                else:
                    error = "Unknown error"
        else:
            error = form.errors
    return render(request, "main/setting.html", {"user": user, "email":email, "error":error, "message":message})



    