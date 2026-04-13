#!/usr/bin/env python3
"""
微信自动回复机器人
使用 itchat 库实现网页版微信接入
"""

import itchat
import time
import os
from datetime import datetime

# 导入配置
try:
    from config import *
except ImportError:
    # 默认配置
    AUTO_REPLY_ENABLED = True
    REPLY_DELAY = 1
    KEYWORD_REPLY = {
        "你好": "你好！我是微信自动回复机器人",
        "在吗": "在的，请问有什么可以帮你的？",
        "进度": "当前项目进度：开发中，预计下周完成。",
        "价格": "基础版¥99，专业版¥299，企业版¥999",
        "帮助": "我是自动回复机器人，你可以发送：你好、进度、价格、帮助",
    }
    DEFAULT_REPLY = "收到你的消息！我是自动回复机器人，暂时无法处理复杂问题。"
    GROUP_REPLY_ENABLED = True
    GROUP_KEYWORD = "@机器人"


def generate_reply(content, is_group=False):
    """根据消息内容生成回复"""
    if not AUTO_REPLY_ENABLED:
        return None
    
    # 群聊处理
    if is_group:
        if not GROUP_REPLY_ENABLED:
            return None
        if GROUP_KEYWORD not in content:
            return None
        content = content.replace(GROUP_KEYWORD, "").strip()
    
    # 关键词匹配
    for keyword, reply in KEYWORD_REPLY.items():
        if keyword in content:
            return reply
    
    return DEFAULT_REPLY


@itchat.msg_register('Text')
def handle_text_message(msg):
    """处理私聊消息"""
    sender = msg['User'].get('NickName', '未知')
    content = msg['Text']
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] [私聊] {sender}: {content}")
    
    # 记录日志
    log_message("私聊", sender, content)
    
    reply = generate_reply(content, is_group=False)
    if reply:
        time.sleep(REPLY_DELAY)
        return reply
    return None


@itchat.msg_register('Text', isGroupChat=True)
def handle_group_message(msg):
    """处理群聊消息"""
    group_name = msg['User'].get('NickName', '未知群')
    sender = msg['ActualNickName'] or msg['User'].get('NickName', '未知')
    content = msg['Text']
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] [群聊] {group_name} - {sender}: {content}")
    
    # 记录日志
    log_message(f"群聊({group_name})", sender, content)
    
    reply = generate_reply(content, is_group=True)
    if reply:
        time.sleep(REPLY_DELAY)
        return reply
    return None


def log_message(msg_type, sender, content):
    """记录消息日志"""
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, f"wechat_bot_{datetime.now().strftime('%Y%m%d')}.log")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    log_entry = f"[{timestamp}] [{msg_type}] {sender}: {content}\n"
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)


def main():
    """主函数"""
    print("=" * 60)
    print("        微信自动回复机器人")
    print("=" * 60)
    print(f"启动时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n配置:")
    print(f"• 自动回复: {'开启' if AUTO_REPLY_ENABLED else '关闭'}")
    print(f"• 回复延迟: {REPLY_DELAY}秒")
    print(f"• 群聊回复: {'开启' if GROUP_REPLY_ENABLED else '关闭'}")
    print(f"• 群聊触发词: {GROUP_KEYWORD}")
    
    print("\n支持的关键词:")
    for keyword, reply in KEYWORD_REPLY.items():
        print(f"• {keyword} → {reply[:30]}...")
    
    print("\n⚠️  注意事项:")
    print("1. 网页版微信可能已关闭，不一定能登录成功")
    print("2. 建议使用2021年前注册的老微信账号")
    print("3. 请勿频繁发送消息，避免账号被封")
    print("4. 按 Ctrl+C 停止机器人")
    print("=" * 60)
    
    print("\n正在启动微信机器人...")
    print("请准备用微信扫描二维码登录")
    
    try:
        # 登录
        itchat.auto_login(hotReload=True)
        
        print("\n✅ 登录成功！机器人已启动")
        print("等待消息中...按Ctrl+C停止")
        
        # 开始监听
        itchat.run(debug=False, blockThread=True)
        
    except KeyboardInterrupt:
        print("\n\n👋 机器人已停止")
    except Exception as e:
        print(f"\n❌ 启动失败: {e}")
        print("\n可能原因:")
        print("1. 你的微信账号不支持网页版登录")
        print("2. 网络连接问题")
        print("3. 微信网页版服务已关闭")
        print("\n建议:")
        print("• 使用2021年前注册的老微信账号")
        print("• 尝试使用手机热点")
        print("• 考虑使用企业微信方案")


if __name__ == "__main__":
    main()
