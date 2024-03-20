from flask import render_template, request, redirect, url_for, make_response
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

@is_member
def schedule(username, userUUID,id):
    data =db.groups.find_one({"group_uuid":id})
    if(data):
        myschedule = "0,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0"
        bin_list = convert_binary(myschedule)
        
        schedule = ["0,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0",
                    "1,1,2,3,3,5,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,65,0,0,0",
                    "1,0,2,3,4,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,65,0,0,0",
                    "1,1,2,3,4,5,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,65,0,0,0"]
        
        cnt_list = get_cnt_list(schedule)

<<<<<<< HEAD
        return render_template('schedul.html',myschedule=bin_list,all_schedule=cnt_list,groupId=id,title=data['title'],username=username)
    return
=======
@is_member
def schedule(username, userUUId, group_code):
    myschedule = "0,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0"
    bin_list = convert_binary(myschedule)
    
    schedule = ["0,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0",
                "1,1,2,3,3,5,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,65,0,0,0",
                "1,0,2,3,4,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,65,0,0,0",
                "1,1,2,3,4,5,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,65,0,0,0"]
    
    cnt_list = get_cnt_list(schedule)
>>>>>>> hyun

    

@is_member
def schedule_post(username, userUUID,id):
    myschedule = "0,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0"
    split_list = myschedule.split(',')

    print(split_list)
    bin_list = []
    for row in split_list:
        bin_list.append(format(int(row),'b').zfill(7))
    print(bin_list)
    data = db.schedule.find_one({'userUUID':userUUID,'group_uuid':id})
    if(data):
        db.schedule.update_one(data,{"$set":{"active":bin_list}})
    response = make_response(redirect(url_for('schedule/'+id))) 
    return response

schedule_routes = {
    'schedule': schedule,
    'schedule_post': schedule_post
}
