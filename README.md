# 微信自动回复机器人

使用 itchat 库实现的微信网页版机器人，支持私聊和群聊自动回复。

## 功能特性

✅ 私聊自动回复  
✅ 群聊自动回复（需@机器人）  
✅ 关键词匹配回复  
✅ 可配置回复内容  
✅ 消息日志记录  
✅ 热重载（短时间内重启不用重新扫码）  

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/yidai2024/wechat-bot.git
cd wechat-bot
```

### 2. 安装依赖

```bash
pip3 install -r requirements.txt
```

### 3. 启动机器人

```bash
bash run.sh
```

或者直接运行：

```bash
python3 main.py
```

### 4. 扫码登录

程序启动后，终端会显示二维码，用微信扫描登录即可。

## 配置说明

编辑 `config.py` 文件来自定义机器人行为：

```python
# 基本配置
AUTO_REPLY_ENABLED = True  # 是否开启自动回复
REPLY_DELAY = 1  # 回复延迟（秒）

# 关键词回复配置
KEYWORD_REPLY = {
    "你好": "你好！我是微信自动回复机器人",
    "进度": "当前项目进度：开发中",
    # 添加更多关键词...
}

# 群聊配置
GROUP_REPLY_ENABLED = True
GROUP_KEYWORD = "@机器人"  # 群聊触发关键词
```

## 使用说明

1. **私聊**：收到消息自动回复
2. **群聊**：需要@机器人才会回复
3. **日志**：消息记录保存在 `logs/` 目录

## 注意事项

⚠️ 重要提醒：
- 微信网页版功能受限，部分账号可能无法登录
- 建议使用2021年前注册的老微信账号
- 请勿频繁发送消息，避免账号被封
- 建议使用小号测试

## 文件结构

```
wechat-bot/
├── main.py          # 主程序
├── config.py        # 配置文件
├── requirements.txt # 依赖列表
├── run.sh           # 启动脚本
├── README.md        # 说明文档
└── logs/            # 日志目录（运行后生成）
```

## 常见问题

### Q: 扫码后提示"登录失败"
A: 可能是你的微信账号不支持网页版登录，尝试换一个2021年前注册的老账号。

### Q: 机器人没有回复
A: 检查：
1. `AUTO_REPLY_ENABLED` 是否为 `True`
2. 群聊是否@了机器人
3. 网络连接是否正常

### Q: 如何停止机器人
A: 按 `Ctrl+C` 停止运行

### Q: 如何修改回复内容
A: 编辑 `config.py` 文件中的 `KEYWORD_REPLY` 字典

## 扩展功能

你可以修改代码添加更多功能：
- 接入 AI 对话（调用 OpenAI API）
- 定时发送消息
- 消息转发
- 自动通过好友请求
- 群管理功能

## 许可证

MIT License

## 作者

yidai2024
