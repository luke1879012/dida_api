# -*- coding: utf-8 -*-

"""
@Project : dida_api 
@File    : 添加任务到收集箱.py
@Date    : 2024/6/12 16:33:32
@Author  : luke
@Desc    : 
"""
from datetime import datetime, timedelta

from didabox.main import DidaBox


def add_task(user_name, password, cookies):
    if cookies:
        dida = DidaBox(cookies=cookies)
    else:
        dida = DidaBox(cookies={})
        dida.sign_on(user_name, password)

    res = dida.base_info()
    data = res.json()
    # 查询收集箱的project_id
    collection_box_id = data['inboxId']

    now = datetime.now()
    trigger_time = now + timedelta(minutes=10)  # 10分钟后提醒
    result = dida.add_simple_task(
        project_id=collection_box_id, title="这是标题", content="内容",
        trigger_time=trigger_time.strftime('%Y-%m-%d %H:%M:%S')
    )
    print(result)
    print(result.text)


if __name__ == '__main__':
    from demo.config import USER_NAME, PASSWORD, COOKIES

    add_task(user_name=USER_NAME, password=PASSWORD, cookies=COOKIES)
