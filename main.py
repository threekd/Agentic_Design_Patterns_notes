#!/usr/bin/env python3
"""
验证 OpenAI 兼容的第三方站点是否可用
使用方法:
    1. 安装 openai: pip install openai
    2. 根据实际情况修改下方 YOUR_BASE_URL 和 YOUR_API_KEY
    3. 运行脚本: python check_openai_compatible.py
"""

from openai import OpenAI
import sys

# ========== 配置区域 ==========
BASE_URL = "https://api.gptsapi.net"   # 例如: https://api.example.com/v1
API_KEY = "sk-Doc810b84539c54f3faba57bd2e94ca37ee3541aec7kpW0U"     # 第三方站点的 API Key
MODEL = "gpt-4o"      # 选择一个该站点支持的模型名称
# =============================

def test_connection():
    """测试连接和认证"""
    # 创建客户端，传入自定义 base_url 和 api_key
    client = OpenAI(
        base_url=BASE_URL,
        api_key=API_KEY,
        timeout=30.0,          # 超时时间（秒）
    )

    try:
        # 发送一个极简的聊天请求
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": "Hello, this is a connectivity test. Please reply with 'OK'."}
            ],
            max_tokens=5,
            temperature=0.0,
        )

        # 提取回复内容
        reply = response.choices[0].message.content
        print("✅ 连接成功！")
        print(f"模型回复: {reply}")
        return True

    except Exception as e:
        print(f"❌ 连接失败: {e}")
        return False

if __name__ == "__main__":
    print(f"测试目标: {BASE_URL}")
    success = test_connection()
    sys.exit(0 if success else 1)