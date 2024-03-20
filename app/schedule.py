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
def schedule(username, userUUID,group_code):
    data =db.groups.find_one({"group_uuid":group_code})
    if(data):
        schedule = db.schedule.find_one({'userUUID':userUUID,'group_uuid':group_code})
        if(schedule is None):
            init_code = "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
            schedule = db.schedule.insert_one({
                'userUUID':userUUID,'group_uuid':group_code,'active_code':init_code
            })
        active_code = schedule["active_code"]
        print('액티브',active_code)
        bin_list = convert_binary(active_code)
        
        schedule = ["0,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0",
                    "1,1,2,3,3,5,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,65,0,0,0",
                    "1,0,2,3,4,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,65,0,0,0",
                    "1,1,2,3,4,5,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,65,0,0,0"]
        
        cnt_list = get_cnt_list(schedule)

        return render_template('schedul.html',myschedule=bin_list,all_schedule=cnt_list,groupId=group_code,title=data['title'],username=username)
    return

    

@is_member
def schedule_post(username, userUUID,group_code):
    myschedule = "0,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0"
    active_code = request.json['my_schedule']
    # split_list = active_code.split(',')

    # print(split_list)
    # bin_list = []
    # for row in split_list:
    #     bin_list.append(format(int(row),'b').zfill(7))
    # print(bin_list)
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
