# 付费版和免费版的区别

> https://api.dida365.com/api/v2/configs/limits



*请求方式：GET*

**成功响应**

```json
{
  "free": {
    "projectNumber": 9,
    "projectTaskNumber": 99,
    "subtaskNumber": 19,
    "shareUserNumber": 2,
    "dailyUploadNumber": 1,
    "taskAttachmentNumber": 20,
    "reminderNumber": 2,
    "dailyReminderNumber": 2,
    "attachmentSize": 10485760,
    "habitNumber": 5,
    "kanbanNumber": 19,
    "teamNumber": 1,
    "teamMemberNumber": 999,
    "habitSectionNumber": 18,
    "timerNumber": 3,
    "visitorNumber": 1
  },
  "pro": {
    "projectNumber": 299,
    "projectTaskNumber": 999,
    "subtaskNumber": 199,
    "shareUserNumber": 29,
    "dailyUploadNumber": 99,
    "taskAttachmentNumber": 20,
    "reminderNumber": 5,
    "dailyReminderNumber": 65535,
    "attachmentSize": 20971520,
    "habitNumber": 299,
    "kanbanNumber": 19,
    "teamNumber": 1,
    "teamMemberNumber": 999,
    "habitSectionNumber": 18,
    "timerNumber": 49,
    "visitorNumber": 29
  },
  "team": {
    "projectNumber": 499,
    "projectTaskNumber": 999,
    "subtaskNumber": 199,
    "shareUserNumber": 29,
    "dailyUploadNumber": 999,
    "taskAttachmentNumber": 99,
    "reminderNumber": 5,
    "dailyReminderNumber": 65535,
    "attachmentSize": 52428800,
    "habitNumber": 299,
    "kanbanNumber": 19,
    "teamNumber": 1,
    "teamMemberNumber": 999,
    "habitSectionNumber": 18,
    "timerNumber": 49,
    "visitorNumber": 29
  }
}
```

账户有三种类型

免费，会员，团购版 

字段说明

| 字段名               | 值   | 作用                               |
| -------------------- | ---- | ---------------------------------- |
| projectNumber        |      |                                    |
| projectTaskNumber    |      |                                    |
| subtaskNumber        |      |                                    |
| shareUserNumber      |      |                                    |
| dailyUploadNumber    |      |                                    |
| taskAttachmentNumber |      | 任务的附件最大的大小               |
| reminderNumber       |      |                                    |
| dailyReminderNumber  |      |                                    |
| habitNumber          |      |                                    |
| kanbanNumber         |      | 看板最大数量（这个命名：我要吐槽） |
| teamNumber           |      |                                    |
| teamMemberNumber     |      |                                    |
| habitSectionNumber   |      |                                    |
| timerNumber          |      |                                    |
| visitorNumber        |      |                                    |