# -*- coding: utf-8 -*-

"""
@Project : dida_api 
@File    : 导出笔记.py
@Date    : 2025/4/22 10:52:35
@Author  : luke
@Desc    : 
"""
import json
import os
from collections import defaultdict

from didabox.main import DidaBox


def output_note(user_name, password, cookies):
    """导出「日记」清单下面笔记, 每个分组导出一份markdown"""
    cookies_file = 'dida_cookies.txt'
    if cookies:
        dida = DidaBox(cookies=cookies)
    elif os.path.exists(cookies_file):
        with open(cookies_file, 'r', encoding='utf-8') as f:
            cookies = json.loads(f.read())
        dida = DidaBox(cookies=cookies)
    else:
        if (not user_name) or (not password):
            user_name = input("请输入手机号: ")
            password = input("请输入密码: ")
        dida = DidaBox(cookies={})
        dida.sign_on(user_name, password)

    with open(cookies_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(dida.req.cookies))

    # 获取基本信息
    res = dida.base_info()
    base_info_data = res.json()
    for idx, project in enumerate(base_info_data['projectProfiles']):
        print("[" + str(idx) + "] 清单名", project['name'])
    # 找到对应的清单
    need_project_idx = input("请输入清单名称前面的数字(比如2): ")
    need_project_info = None
    for idx, project in enumerate(base_info_data['projectProfiles']):
        if idx == int(need_project_idx):
            print("find -> 清单名", project['name'], "清单id", project['id'], '类型', project['kind'])
            need_project_info = project
    # 筛选出对应任务/笔记
    all_data = base_info_data['syncTaskBean']['update']
    need_data = []
    for row in all_data:
        if row['projectId'] == need_project_info['id']:
            need_data.append(row)

    # 查询所有的分组情况
    column_info_res = dida.column_info()
    column_info = column_info_res.json()
    need_column_info = []
    for col in column_info['update']:
        if col['projectId'] == need_project_info['id']:
            need_column_info.append(col)

    result_data = defaultdict(list)
    for col in need_column_info:
        for row in need_data:
            if row['columnId'] == col['id']:
                res = "### " + row['title']
                content = row['content']
                if content:
                    res += "\n" + content
                desc = row['desc']
                if desc:
                    res += "\n" + desc
                result_data[col['name']].append(res)

    file_dir = "output"
    os.makedirs(file_dir, exist_ok=True)
    for column_name, data in result_data.items():
        file_name = need_project_idx + "_" + column_name + ".md"
        with open(os.path.join(file_dir, file_name), "w", encoding='utf-8') as f:
            data_str = "\n\n\n\n".join(data)
            f.write(data_str)

    print("已导出 -> " + file_dir + "文件夹")


if __name__ == '__main__':
    from demo.config import USER_NAME, PASSWORD, COOKIES

    output_note(user_name=USER_NAME, password=PASSWORD, cookies=COOKIES)
