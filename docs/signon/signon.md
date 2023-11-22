# 登录滴答清单

## WEB密码登录

> https://api.dida365.com/api/v2/user/signon?wc=true&remember=true

*请求方式：POST*

参数

| 参数名   | 值   | 作用 | 必要性 |
| -------- | ---- | :--: | ------ |
| wc       | true |  -   | -      |
| remember | true |  -   | -      |
|          |      |      |        |



*请求体：JSON*

```json
{
  "password": "密码",
  "username": "登录账户"
}
```

*响应体：JSON*

**失败响应**

```
{
  "errorId": "ebesfofw@ctw5",
  "errorCode": "username_password_not_match",
  "errorMessage": "xxx@outlook.com",
  "data": {
    "remainderTimes": 7
  }
}
```

字段说明

| 字段名         | 字段值       | 作用           |
| -------------- | ------------ | -------------- |
| errorId        | -            | -              |
| errorCode      | 错误原因     | 表示错误的类型 |
| errorMessage   | 登录的账户名 | -              |
| remainderTimes | -数字        | -              |

**成功响应**

```json
{
  "token": "8B0120E62ADDD9E6160214D6FCE61B60997EDE2A806FFAE59D019D379C57D0CABABE007B030151002FFD8A51141A473C07DC8B58CA6BFA85E04DA4A3577D008B9751E954783FE7921F3BAF20594B793D34375051271D0F6AF0AB23C0B",
  "userId": "1020318808",
  "userCode": "731e59d510ea4c4b863225b469a612dc",
  "username": "xxx@outlook.com",
  "teamPro": false,
  "proStartDate": "2022-11-21T01:19:08.000+0000",
  "proEndDate": "2023-02-19T04:49:43.000+0000",
  "needSubscribe": true,
  "inboxId": "inbox1020298808",
  "teamUser": false,
  "activeTeamUser": false,
  "freeTrial": false,
  "pro": false,
  "ds": false
}
```

字段说明

| 字段名         | 字段值             | 作用     |
| -------------- | ------------------ | -------- |
| token          | 账户token字符串    | 验证账户 |
| userId         | 用户唯一ID         | -        |
| userCode       | -                  | -        |
| username       | 账户名             | -        |
| teamPro        | 高级会员           | -        |
| proStartDate   | -                  | -        |
| proEndDate     | -                  | -        |
| needSubscribe  | -                  | -        |
| inboxId        | 默认任务添加清单ID | -        |
| teamUser       | 团队用户           | -        |
| activeTeamUser | -                  | -        |
| freeTrial      | -                  | -        |
| pro            | -                  | -        |
| ds             | -                  | -        |





