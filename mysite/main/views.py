# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import mysql.connector
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.


def index(request):
    if request.GET.get('Name') and request.GET.get('Email') and request.GET.get('Subject') and request.GET.get('Message'):
        name = request.GET.get('Name')
        email = request.GET.get('Email')
        subject = request.GET.get('Subject')
        message = request.GET.get('Message')
        write_to_database(name,email,subject,message)
        return  redirect('/')
    else:
        return render(request,'web/index.html')


def write_to_database(name,email,subject,message):
    cnx = mysql.connector.connect(user='root', password='****', database='mysite') # Enter your mysql database password, make sure you create database and table before
    cursor = cnx.cursor()
    add_data = "INSERT INTO messages " "(name,email,subject,message) " "VALUES (%s,%s,%s,%s)"
    data = (name,email,subject,message)
    cursor.execute(add_data, data)
    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()
