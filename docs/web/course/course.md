# 课表

## WEB下拉取课表

> https://api.dida365.com/api/v1/course/timetable

*请求方法：GET*

**成功响应**

```
[
  {
    "id": "65409cea8b306aeab6c1f0eb",
    "name": "大三上",
    "startDate": "2023-09-06T16:00:00.000+0000",
    "reminders": [
      "TRIGGER:-PT10M"
    ],
    "courses": [
      {
        "id": "65409dfa8b306aeab6c1f125",
        "name": "计算机网络原理[03]",
        "color": "#F1C231",
        "items": [
          {
            "room": "6-208",
            "teacher": "",
            "weekday": 2,
            "startLesson": 9,
            "endLesson": 10,
            "weeks": [
              15,
              13,
              11,
              9
            ]
          },
          {
            "room": "临港校区六号楼120",
            "teacher": "张毅",
            "weekday": 2,
            "startLesson": 3,
            "endLesson": 4,
            "weeks": [
              17,
              16,
              15,
              14,
              13,
              12,
              11,
              10,
              9,
              8,
              7,
              6,
              5,
              4,
              3,
              2
            ]
          },
          {
            "room": "临港校区六号楼218",
            "teacher": "张毅",
            "weekday": 4,
            "startLesson": 5,
            "endLesson": 6,
            "weeks": [
              17,
              15,
              13,
              11,
              9,
              7,
              5,
              3
            ]
          }
        ]
      },
      {
        "id": "65409eca8b306aeab6c1f140",
        "name": "软件设计与体系结构[01]",
        "color": "#6FE9BE",
        "items": [
          {
            "room": "6-311",
            "teacher": "",
            "weekday": 2,
            "startLesson": 5,
            "endLesson": 6,
            "weeks": [
              16,
              14,
              13,
              11,
              10,
              9
            ]
          },
          {
            "room": "临港校区六号楼120",
            "teacher": "任春华",
            "weekday": 4,
            "startLesson": 3,
            "endLesson": 4,
            "weeks": [
              17,
              16,
              15,
              14,
              13,
              12,
              11,
              10,
              9,
              8,
              7,
              6,
              5,
              4,
              3,
              2
            ]
          }
        ]
      },
      {
        "id": "65409f188b306aeab6c1f14d",
        "name": "软件质量保证与测试[01]",
        "color": "#6CBE5E",
        "items": [
          {
            "room": "6-312",
            "teacher": "",
            "weekday": 4,
            "startLesson": 9,
            "endLesson": 10,
            "weeks": [
              15,
              13,
              9
            ]
          },
          {
            "room": "临港校区六号楼104",
            "teacher": "周耀东",
            "weekday": 5,
            "startLesson": 5,
            "endLesson": 6,
            "weeks": [
              17,
              16,
              15,
              14,
              13,
              12,
              11,
              10,
              9,
              8,
              7,
              6,
              5,
              4,
              3,
              2
            ]
          }
        ]
      },
      {
        "id": "65409f518b306aeab6c1f15a",
        "name": "Java Web程序设计[02]",
        "color": "#FFE599",
        "items": [
          {
            "room": "6-304",
            "teacher": "",
            "weekday": 2,
            "startLesson": 5,
            "endLesson": 6,
            "weeks": [
              17,
              16,
              14,
              13,
              12,
              10,
              9
            ]
          },
          {
            "room": "临港校区六号楼120",
            "teacher": "唐自力",
            "weekday": 2,
            "startLesson": 1,
            "endLesson": 2,
            "weeks": [
              17,
              16,
              15,
              14,
              13,
              12,
              11,
              10,
              9,
              8,
              7,
              6,
              5,
              4,
              3,
              2
            ]
          }
        ]
      },
      {
        "id": "654257318b30d264beb73947",
        "name": "煞笔指导",
        "color": "#A0BB31",
        "items": [
          {
            "room": "6218",
            "teacher": "煞笔",
            "weekday": 4,
            "startLesson": 1,
            "endLesson": 2,
            "weeks": [
              9,
              10,
              11,
              12,
              13,
              14
            ]
          }
        ]
      },
      {
        "id": "65437e928b30d26411453743",
        "name": "Linux编程及应用[02]",
        "color": "#F1C231",
        "items": [
          {
            "room": "6-313",
            "teacher": "",
            "weekday": 5,
            "startLesson": 1,
            "endLesson": 2,
            "weeks": [
              9,
              10,
              11,
              12,
              13,
              14
            ]
          },
          {
            "room": "临港校区六号楼120",
            "teacher": "宋敏,武笛",
            "weekday": 5,
            "startLesson": 3,
            "endLesson": 4,
            "weeks": [
              17,
              16,
              15,
              14,
              13,
              12,
              11,
              10,
              9,
              8,
              7,
              6,
              5,
              4,
              3,
              2
            ]
          },
          {
            "room": "临港校区六号楼120",
            "teacher": "宋敏,武笛",
            "weekday": 1,
            "startLesson": 5,
            "endLesson": 6,
            "weeks": [
              16,
              14,
              12,
              10,
              8,
              6,
              4,
              2
            ]
          }
        ]
      }
    ],
    "lessonTimes": {
      "1": [
        "08:30",
        "09:15"
      ],
      "2": [
        "09:20",
        "10:05"
      ],
      "3": [
        "10:25",
        "11:10"
      ],
      "4": [
        "11:15",
        "12:00"
      ],
      "5": [
        "14:25",
        "15:10"
      ],
      "6": [
        "15:20",
        "16:05"
      ],
      "7": [
        "16:25",
        "17:10"
      ],
      "8": [
        "17:15",
        "18:00"
      ],
      "9": [
        "19:00",
        "19:45"
      ],
      "10": []
    },
    "weekCount": 25,
    "sortOrder": 1099511693312,
    "createdTime": "2023-10-31T06:22:01.771+0000",
    "etag": "vpononae"
  }
]
```

