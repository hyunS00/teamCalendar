from flask import render_template, request, redirect, url_for, make_response
from app.db import db
from bson.objectid import ObjectId
from app.checkLogin import is_member
import datetime as dt

def convert_binary(code):
    split_list = code.split(',')
    bin_list = []
    for row in split_list:
        bin_list.append(format(int(row),'b').zfill(7))

    return bin_list

week_name = ['월','화','수','목','금','토','일']

def get_cal_date(date):
    currnet_date = dt.datetime.strptime(date,"%Y-%m-%d")
    date_list = []
    weeks = []
    for i in range(7):
        date_list.append(str(currnet_date.month)+'.'+str(currnet_date.day))
        weeks.append(week_name[currnet_date.weekday()])
        currnet_date += dt.timedelta(days=1)
    
    return date_list,weeks


def get_cnt_list(code_list):
    cnt = [[0 for w in range(7)] for h in range(25)]
    active_user = [[[] for w in range(7)] for h in range(25)]
    print(code_list[0])
    for code in code_list:
        bin_list = convert_binary(code['active_code'])
        user_name = db.users.find_one({'_id': ObjectId(code['userUUID'])})['username']

        for row in range(25):
            for cell in range(7):
                binary = int(bin_list[row][cell])
                cnt[row][cell] += binary
                if(binary == 1):
                    active_user[row][cell].append(user_name)
    length = len(code_list)
    for row in range(25):
        for cell in range(7):
            cnt[row][cell] = round(cnt[row][cell]/length,1)

    
    return cnt, active_user

@is_member
def schedule(username, userUUID,group_code):
    data =db.groups.find_one({"group_uuid":group_code})
    print(data)
    days, weeks = get_cal_date(data["date"])
    if(data):
        schedule = db.schedule.find_one({'userUUID':userUUID,'group_uuid':group_code})
        if(schedule is None):
            init_code = "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
            result = db.schedule.insert_one({
                'userUUID':userUUID,'group_uuid':group_code,'active_code':init_code
            })
            schedule = db.schedule.find_one({'_id': result.inserted_id})

        active_code = schedule["active_code"]
        bin_list = convert_binary(active_code)
        
        schedule_list = list(db.schedule.find({'group_uuid':group_code}))
        cnt_list, active_user_list = get_cnt_list(schedule_list)
        user_len = len(schedule_list)

        return render_template('schedul.html',myschedule=bin_list,all_schedule=cnt_list,groupId=group_code,title=data['title']
                               ,username=username, active_user_list =active_user_list,user_len = user_len
                               ,days=days, weeks=weeks
                               )
    
    response = make_response(redirect(url_for('lobby',group_code=group_code))) 
    return response

    

@is_member
def schedule_post(username, userUUID,group_code):
    active_code = request.json['my_schedule']

    data = db.schedule.find_one({'userUUID':userUUID,'group_uuid':group_code})
    if(data):
        db.schedule.update_one(data,{"$set":{"active_code":active_code}})
    else:
        db.schedule.insert_one({
            'userUUID':userUUID,'group_uuid':group_code,'active_code':active_code
        })
    response = make_response(redirect(url_for('schedule',group_code=group_code))) 
    return response

schedule_routes = {
    'schedule': schedule,
    'schedule_post': schedule_post
}
