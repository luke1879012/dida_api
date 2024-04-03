# -*- coding: utf-8 -*-

"""
@Project : dida_api 
@File    : 查看清单信息.py
@Date    : 2024/3/29 13:43:30
@Author  : luke
@Desc    : 
"""
from didabox.main import DidaBox


def show_list(user_name, password, cookies):
    if cookies:
        dida = DidaBox(cookies=cookies)
    else:
        dida = DidaBox(cookies={})
        dida.sign_on(user_name, password)
    res = dida.base_info()
    data = res.json()
    print("清单信息")
    for project in data['projectProfiles'] or []:
        print("清单名", project['name'], "清单id", project['id'],
              '类型', project['kind'], "所属文件夹id", project['groupId'])
    print("清单文件夹信息")
    for project_group in data['projectGroups'] or []:
        print("文件夹名", project_group['name'], "文件夹id", project_group['id'])
    print("过滤器")
    for f in data['filters'] or []:
        print("过滤器名", f['name'], "过滤器id", f['id'])
        # print("过滤器名", f['name'], "过滤器id", f['id'], "过滤器规则", f['rule'])
    print("标签")
    for tag in data['tags']:
        # [note] 优先使用name
        # 展示用label，后端存储用name，目前发现大小写可能会有区别
        print("标签名", tag["name"], "父标签", tag.get('parent'))
        # print("标签名(显示)", tag['label'], "标签名(底层)", tag["name"], "父标签", tag.get('parent'))
    print("over")


if __name__ == '__main__':
    from demo.config import USER_NAME, PASSWORD, COOKIES

    show_list(user_name=USER_NAME, password=PASSWORD, cookies=COOKIES)
