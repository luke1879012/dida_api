# -*- coding: utf-8 -*-

"""
@Project : dida_api 
@File    : 过滤标签.py
@Date    : 2024/4/3 15:22:18
@Author  : luke
@Desc    : 
"""
from datetime import datetime

import pytz
from didabox.main import DidaBox


def filter_task(user_name, password, cookies):
    if cookies:
        dida = DidaBox(cookies=cookies)
    else:
        dida = DidaBox(cookies={})
        dida.sign_on(user_name, password)
    res_info = dida.base_info()
    info_data = res_info.json()
    # 可以拿到未完成的任务
    undo_task = info_data['syncTaskBean']['update']
    # 获取一定时间范围内，所有已完成的订单
    start_time = "2024-01-01 00:00:00"
    end_time = "2024-04-01 00:00:00"
    # 根据条件查询已完成的任务
    done_task = []
    completion_time = end_time
    for _ in range(60):
        res_done = dida.get_completed_tasks(to_date=completion_time, limit=200)
        done_data = res_done.json()
        earliest_data = min(done_data, key=lambda x: x['completedTime'])
        # 对比时需要做时区转换
        shanghai_tz = pytz.timezone(dida.req.tz)
        completion_time = datetime.strptime(earliest_data['completedTime'], "%Y-%m-%dT%H:%M:%S.%f%z")
        completion_time = completion_time.astimezone(shanghai_tz).strftime("%Y-%m-%d %H:%M:%S")
        print("最早完成时间:", completion_time)
        done_task.extend(done_data)
        if completion_time < start_time:
            break
    else:
        raise Exception("超过次数")
    all_task = undo_task + done_task

    for i in all_task:
        # 查询 2024 标签
        if i.get('tags') and '2024' in i['tags']:
            print(i)
    print('over')


if __name__ == '__main__':
    from demo.config import USER_NAME, PASSWORD, COOKIES

    filter_task(user_name=USER_NAME, password=PASSWORD, cookies=COOKIES)
