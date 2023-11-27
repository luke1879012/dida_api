# 任务

## WEB任务添加

> https://api.dida365.com/api/v2/batch/task

*请求方式：POST*

请求头需要带上的cookie

| 字段       | 值                | 必要性 | 作用       |
| ---------- | ----------------- | ------ |----------|
| t          | 登录成功后的token | 必要   |          |
| AWSALB     | 不明              |        | 亚马逊的负载均衡(无用)  |
| AWSALBCORS | 不明              |        | 亚马逊的负载均衡(无用) |
| eid01 | 不明 | |  |

*请求体：JSON*

```json
{
  "add": [
    {
      "items": [],
      "reminders": [],
      "exDate": [],
      "dueDate": null,
      "priority": 0,
      "progress": 0,
      "assignee": null,
      "sortOrder": -2199023452160,
      "startDate": null,
      "isFloating": false,
      "columnId": "65386870dc5ce07c20bfb127",
      "status": 0,
      "projectId": "inbox1020398808",
      "kind": null,
      "createdTime": "2023-11-27T04:30:40.000+0000",
      "modifiedTime": "2023-11-27T04:30:40.000+0000",
      "title": "one",
      "tags": [],
      "timeZone": "Asia/Shanghai",
      "content": "",
      "id": "65641b704c90c073c33e4fa6"
    }
  ],
  "update": [],
  "delete": [],
  "addAttachments": [],
  "updateAttachments": [],
  "deleteAttachments": []
}
```

*请求体字段说明*

| 字段名            |       值       | 必要性 | 作用                     |
| ----------------- | :------------: | ------ | ------------------------ |
| add               |                | 必要   |                          |
| items             |                |        |                          |
| reminders         |                |        |                          |
| exDate            |                |        |                          |
| dueDate           |                |        |                          |
| priority          |                |        |                          |
| assignee          |                |        |                          |
| sortOrder         |                | 必要   |                          |
| startDate         |                |        |                          |
| isFloating        |                |        |                          |
| columnId          | 一个随机字符串 |        |                          |
| status            |                |        |                          |
| projectId         |    清单的ID    |        | 把这个任务添加到哪个清单 |
| kind              |                |        |                          |
| createdTime       |                |        |                          |
| modifiedTime      |                |        |                          |
| title             |      标题      | 非必要 |                          |
| tags              |                |        |                          |
| timeZone          |      时区      |        |                          |
| content           |      内容      | 非必要 |                          |
| id                |                |        | 用于后续的查询和修改     |
| update            |                |        |                          |
| delete            |                |        |                          |
| addAttachments    |                |        |                          |
| updateAttachments |                |        |                          |
| deleteAttachments |                |        |                          |
|                   |                |        |                          |
|                   |                |        |                          |
|                   |                |        |                          |

*响应体：JSON*

**失败响应**

```json
```

*失败响应字段说明*

| 字段名 | 值   | 作用 |
| ------ | ---- | ---- |
|        |      |      |
|        |      |      |
|        |      |      |
|        |      |      |

**成功响应**

```json
{
  "id2etag": {
    "65641b704c90c073c33e4fa6": "j01e6kqf"
  },
  "id2error": {}
}
```

*成功响应字段说明*

| 字段名   | 值   | 作用 |
| -------- | ---- | ---- |
| id2etag  |      |      |
| id2error |      |      |