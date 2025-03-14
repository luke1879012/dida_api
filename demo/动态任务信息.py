# -*- coding: utf-8 -*-

"""
@Project : dida_api 
@File    : 动态任务信息.py
@Date    : 2025/3/14 10:15:43
@Author  : luke
@Desc    : 
"""

from didabox.main import DidaBox


def minutes_to_hours(minutes):
    """分钟转换为小时"""
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}:{remaining_minutes}"


def dynamic_task_information(user_name, password, cookies):
    """已存在每天18点的「推代码」的任务, 需要在任务详情里面更新今天专注情况"""
    if cookies:
        dida = DidaBox(cookies=cookies)
    else:
        dida = DidaBox(cookies={})
        dida.sign_on(user_name, password)
    # 获取番茄专注下面的概览信息
    p_view = dida.pomodoros_overview()
    print(p_view.json())
    p_view = p_view.json()

    today_pomo_duration = p_view['todayPomoDuration']
    today_pomo_duration_hm = minutes_to_hours(today_pomo_duration)
    total_pomo_duration = p_view['totalPomoDuration']
    total_pomo_duration_hm = minutes_to_hours(total_pomo_duration)

    # 自定义格式
    new_content = (f"今天番茄: {p_view['todayPomoCount']}个, "
                   f"今天专注时长: {today_pomo_duration}({today_pomo_duration_hm})\n"
                   f"总番茄: {p_view['totalPomoCount']}个, "
                   f"总专注时长: {total_pomo_duration}({total_pomo_duration_hm})")
    print(new_content)

    # 更新「推代码」任务的内容
    result = dida.update_content('推代码', new_content)
    print(result)


if __name__ == '__main__':
    from demo.config import USER_NAME, PASSWORD, COOKIES

    dynamic_task_information(user_name=USER_NAME, password=PASSWORD, cookies=COOKIES)
