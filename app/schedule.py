from flask import render_template, request, redirect, url_for
from app.db import db

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
    return cnt

def schedul():
    myschedule = "0,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0"
    bin_list = convert_binary(myschedule)
    

    schedule = ["1,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0",
                "1,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0",
                "1,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0",
                "1,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0"]
    
    cnt_list = get_cnt_list(schedule)
   
    print(cnt_list)

    return render_template('schedul.html',myschedule=bin_list,all_schedule=cnt_list)

scedul_routes = {
    'schedul': schedul
}
