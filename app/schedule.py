from flask import render_template, request, redirect, url_for
from app.db import db


def schedule():
    myschedule = "0,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0"

    split_list = myschedule.split(',')
    print(split_list)
    bin_list = []
    for row in split_list:
        bin_list.append(format(int(row),'b').zfill(7))
    print(bin_list)
    
    return render_template('schedul.html',myschedule=bin_list)

def schedule_post():
    myschedule = "0,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0"

    split_list = myschedule.split(',')
    print(split_list)
    bin_list = []
    for row in split_list:
        bin_list.append(format(int(row),'b').zfill(7))
    print(bin_list)
    
    return render_template('schedul.html',myschedule=bin_list)

schedule_routes = {
    'schedule': schedule,
    'schedule_post': schedule_post
}
