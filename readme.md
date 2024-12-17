# kknd

一个用于检测 Telegram 用户在线状态并通过机器人发送通知的 Python 脚本。


## 配置说明

需要配置以下变量:
```
API_ID = 'your_api_id'  # Telegram API ID
API_HASH = 'your_api_hash'  # Telegram API Hash
BOT_TOKEN = 'your_bot_token'  # 机器人 Token
USERNAMES = ['User1', 'User2', 'User3']  # 用户名列表
BOT_CHAT_ID = 'your_chat_id'  # 接收通知的聊天 ID
```

## 使用方法

1. 安装依赖:
```bash
pip3 install telethon requests
```

2. 运行脚本:
```bash
python3 main.py
```

## 通知格式
```
[2024-01-01 12:34:56] @username is now Online/Offline
```