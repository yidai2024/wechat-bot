#!/bin/bash
# 微信机器人启动脚本

echo "=========================================="
echo "   微信自动回复机器人 - 启动脚本"
echo "=========================================="

# 检查Python环境
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装"
    echo "请先安装Python3: sudo apt install python3"
    exit 1
fi

# 检查pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 未安装"
    echo "请先安装pip3: sudo apt install python3-pip"
    exit 1
fi

# 安装依赖
echo "📦 正在安装依赖..."
pip3 install -r requirements.txt -q

# 创建必要的目录
mkdir -p logs

# 清理旧的登录状态（可选）
if [ -f "itchat.pkl" ]; then
    echo "🗑️  清理旧的登录状态..."
    rm -f itchat.pkl
fi

echo ""
echo "🚀 正在启动机器人..."
echo ""

# 启动机器人
python3 main.py
