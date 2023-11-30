# 通知

## WEB获取系统通知信息

> https://api.dida365.com/api/v2/notification?autoMarkRead=false

*请求的方式：GET*

*请求体：无*

*响应体：JSON*

```json
[
  {
    "id": "63eb12e762fdd96daa91af04",
    "title": "寒酥 成功激活，5天高级会员奖励已自动发放到你的账户。",
    "type": "refer",
    "data": {
      "kind": "activation",
      "name": "寒酥",
      "days": "5",
      "users": "1"
    },
    "actionStatus": 0,
    "createdTime": "2023-02-14T04:49:43.368+0000",
    "category": null,
    "unread": null
  },
  {
    "id": "6381689cb408da72043b8d97",
    "title": "你的高级账户将于今天到期。",
    "type": "PayReminder",
    "data": {
      "expiryDate": "2022-11-26T01:19:08.000+0000"
    },
    "actionStatus": 0,
    "createdTime": "2022-11-26T01:15:08.523+0000",
    "category": null,
    "unread": null
  },
  {
    "id": "637ad20bd0631f1feb2fff26",
    "title": "随意 成功激活，5天高级会员奖励已自动发放到你的账户。",
    "type": "refer",
    "data": {
      "kind": "activation",
      "name": "随意",
      "days": "5",
      "users": "1"
    },
    "actionStatus": 0,
    "createdTime": "2022-11-21T01:19:07.887+0000",
    "category": null,
    "unread": null
  }
]
```



*成功响应体体字段说明*

| 字段名       | 值                       | 作用       |
| ------------ | ------------------------ | ---------- |
| id           |                          | 消息唯一ID |
| title        |                          |            |
| type         | 提醒的类型               |            |
| kind         |                          |            |
| name         | 被邀请的人的名字         |            |
| days         | 邀请成功后获得的会员天数 |            |
| users        | 邀请成功的用户人数       |            |
| actionStatus |                          |            |
| createdTime  |                          |            |
| category     |                          |            |
| unread       |                          |            |

