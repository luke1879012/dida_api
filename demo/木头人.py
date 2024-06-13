# -*- coding: utf-8 -*-

"""
@Project : dida_api 
@File    : 木头人.py
@Date    : 2024/6/12 16:33:21
@Author  : luke
@Desc    : 
"""
import random
import time
from datetime import datetime, timedelta

from didabox.main import DidaBox


def wooden_man(user_name, password, cookies):
    """循环「1」,「2」,「3」,「木头人」,发送到指定清单中"""
    if cookies:
        dida = DidaBox(cookies=cookies)
    else:
        dida = DidaBox(cookies={})
        dida.sign_on(user_name, password)

    res = dida.base_info()
    data = res.json()
    project_id = data['inboxId']
    # 准备发送到 「计划」 清单中, 未找到该清单，则发送到「收集箱」
    for project in data['projectProfiles'] or []:
        print("清单名", project['name'], "清单id", project['id'],
              '类型', project['kind'], "所属文件夹id", project['groupId'], '归档', project['closed'])

        if "计划" in project['name'] and project['kind'] == 'TASK' and (not project['closed']):
            project_id = project['id']
            break

    if project_id == data['inboxId']:
        print("消息将发送到「收集箱」中")

    while True:
        for msg in ['1', '2', '3', '木头人']:
            now = datetime.now()
            trigger_time = now + timedelta(minutes=10)  # 10分钟后提醒
            result = dida.add_simple_task(
                project_id=project_id, title="阿伟大叫", content=msg,
                trigger_time=trigger_time.strftime('%Y-%m-%d %H:%M:%S')
            )
            print(result)
            print(result.text)
            # 随机等待60~120s
            time.sleep(random.uniform(60, 120))


if __name__ == '__main__':
    from demo.config import USER_NAME, PASSWORD, COOKIES

    wooden_man(user_name=USER_NAME, password=PASSWORD, cookies=COOKIES)
