<h1 align="center">滴答清单-API收集整理</h1>
<h3 align="center">野生API文档</h3>
<h3 align="center">不断更新中....</h3>
本项目旨在对 滴答清单 WEB、APP、手表、桌面、插件 等客户端中，散落在世界各地的野生 API 进行收集整理，研究使用方法并对其进行说明，运用了黑箱法、控制变量法、代码逆向分析、拆包及反编译法、网络抓包法等研究办法。

**⚠️声明**

1. 本项目遵守 CC-BY-NC 4.0 协议，禁止一切商业使用，如需转载请注明作者 ID
2. **请勿滥用，本项目仅用于学习和测试！请勿滥用，本项目仅用于学习和测试！请勿滥用，本项目仅用于学习和测试！**
3. 利用本项目提供的接口、文档等造成不良影响及后果与本人无关
4. 由于本项目的特殊性，可能随时停止开发或删档
5. 本项目为开源项目，不接受任何形式的催单和索取行为，更不容许存在付费内容

## 🍴目录


- [ ] [文档模板](docs/template.md)
- [ ] [web端](docs/web)

  - [ ] [请求头](docs/web.header.md)
  - [ ] [登录](docs/web/login/signon.md)
  - [x] [退出登录](docs/web/login/signout.md)
  - [ ] [获取清单信息](docs/web/获取清单信息.md)
  - [ ] [清单任务](docs/web/task/task.md)
  - [ ] [统计](docs/web/统计.md)
  - [ ] [番茄专注](docs/web/pomodoros/pomodoros.md)
  - [ ] [cookie续命](docs/web/cookie续命.md)
  - [ ] [系统消息通知](docs/web/notify/notify.md)
  - [ ] [获取习惯信息](docs/web/habit/habit.md)
  - [ ] [课程](docs/web/course/course.md)
  - [ ] [版本对比](docs/web/limit/limit.md)
  - [ ] [隐藏的信息](docs/web/隐藏信息.md)

- [ ] [win10桌面端](docs/win10)

## ✨鸣谢

项目学习模仿来自易姐的[BAC](https://github.com/SocialSisterYi/bilibili-API-collect)


## 👀 demo(场景驱动更新, 欢迎提issues)
单纯收集没意思, 以下是一些具体场景, 目前只支持python

### 前置工作
版本: `python>=3.6`

依赖:
```shell
pip install didabox
```
环境: 在[demo/config.py](demo/config.py)中配置`账号密码`即可

### 场景
- [x] [查看清单信息](demo/查看清单信息.py)
- [x] [过滤标签](demo/过滤标签.py)
- [x] [添加任务到收集箱](demo/添加任务到收集箱.py)
- [x] [123木头人](demo/木头人.py)
- [x] [动态任务信息](demo/动态任务信息.py)

