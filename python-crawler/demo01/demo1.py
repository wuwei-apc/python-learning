"""
@FileName：demo1.py
@Description：you description
@Author：zpc20 
@productName: PyCharm
@Time：2024/3/8 9:54
"""
import execjs
import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Origin': 'https://www.qimingpian.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'channel_name': '24新声',
    'page': '1',
    'num': '20',
    'unionid': 'aXnjbCchqf7lnji5LArYT4rXzarFZmk8j/ibpk0d2Yazzc9yFcLJqW+C98bgblcseJWqqIs6kiQsM8IbOYgM5A==',
}

response = requests.post('https://vipapi.qimingpian.cn/Activity/channelInformationByChannelName', headers=headers, data=data).json()
encrypt_data = response['encrypt_data']
# print(encrypt_data)
decode_data = execjs.compile(open('./demo.js','r',encoding='utf-8').read()).call('s',encrypt_data)
print(decode_data)