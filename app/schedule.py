from flask import render_template, request, redirect, url_for
from app.db import db
from app.checkLogin import is_member

def convert_binary(code):
    split_list = code.split(',')
    bin_list = []
    for row in split_list:
        bin_list.append(format(int(row),'b').zfill(7))

    return bin_list


def get_cnt_list(code_list):
    cnt = [[0 for w in range(7)] for h in range(25)]

    for code in code_list:
        bin_list = convert_binary(code)
        for row in range(25):
            for cell in range(7):
                cnt[row][cell] += int(bin_list[row][cell])
    length = len(code_list)
    for row in range(25):
        for cell in range(7):
            cnt[row][cell] = round(cnt[row][cell]/length,1)
    return cnt


def schedule():
    myschedule = "0,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0"
    bin_list = convert_binary(myschedule)
    
    schedule = ["0,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0",
                "1,1,2,3,3,5,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,65,0,0,0",
                "1,0,2,3,4,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,65,0,0,0",
                "1,1,2,3,4,5,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,65,0,0,0"]
    
    cnt_list = get_cnt_list(schedule)

    return render_template('schedul.html',myschedule=bin_list,all_schedule=cnt_list)

@is_member
def schedule_post(username, userUUID):
    myschedule = "0,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0"

    split_list = myschedule.split(',')
    print(split_list)
    bin_list = []
    for row in split_list:
        bin_list.append(format(int(row),'b').zfill(7))
    print(bin_list)
    response = make_response(redirect(url_for('lobby', username=username))) 
    return render_template('schedul.html',myschedule=bin_list)

schedule_routes = {
    'schedule': schedule,
    'schedule_post': schedule_post
}
