# 习惯

## WEB拉取全部习惯

> https://api.dida365.com/api/v2/habits

*请求的方式：GET*

请求头需要带上的cookie

| 字段       | 值                | 必要性 | 作用       |
| ---------- | ----------------- | ------ |----------|
| t          | 登录成功后的token | 必要   |          |
| AWSALB     | 不明              |        | 亚马逊的负载均衡(无用)  |
| AWSALBCORS | 不明              |        | 亚马逊的负载均衡(无用) |
| eid01 | 不明 | |  |

*请求体：无*

*响应体：JSON*


**成功响应**

```
[
  {
    "id": "6479c37c8b30d2a86b574307",
    "name": "锻炼",
    "iconRes": "habit_exercising",
    "color": "#BF8AF5",
    "sortOrder": -786432,
    "status": 0,
    "encouragement": "始终保持激情",
    "totalCheckIns": 45,
    "createdTime": "2023-06-02T10:25:00.000+0000",
    "modifiedTime": "2023-11-25T10:32:21.847+0000",
    "archivedTime": "2023-10-29T10:39:59.903+0000",
    "type": "Boolean",
    "goal": 1.0,
    "step": 0.0,
    "unit": "Count",
    "etag": "o32mywtg",
    "repeatRule": "RRULE:FREQ=WEEKLY;INTERVAL=1;TT_TIMES=2",
    "reminders": [],
    "recordEnable": false,
    "sectionId": "-1",
    "targetDays": 0,
    "targetStartDate": 20230602,
    "completedCycles": 0,
    "exDates": null
  }
]
```

*成功响应体体字段说明*

| 字段名          | 值                         | 作用                       |
| --------------- | -------------------------- | -------------------------- |
| id              | 一堆数字和字符组合         | 习惯唯一ID                 |
| name            | 习惯名字                   |                            |
| iconRes         |                            |                            |
| color           |                            | 也许人的激情和颜色相关联吧 |
| sortOrder       |                            |                            |
| status          | 0、1                       | 表示这个习惯是否已经完成   |
| encouragement   | 习惯的激励语句             |                            |
| totalCheckIns   |                            |                            |
| createdTime     | UTC时间                    |                            |
| modifiedTime    | UTC时间                    |                            |
| archivedTime    | UTC时间                    |                            |
| type            |                            |                            |
| goal            |                            |                            |
| step            |                            |                            |
| unit            |                            |                            |
| etag            |                            |                            |
| repeatRule      |                            |                            |
| reminders       |                            |                            |
| recordEnable    |                            |                            |
| sectionId       |                            |                            |
| targetDays      |                            |                            |
| targetStartDate | 开始时间（格式为20230602） |                            |
| completedCycles |                            |                            |
| exDates         |                            |                            |
