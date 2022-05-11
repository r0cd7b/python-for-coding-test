# 파이썬으로 웹 요청하기
import requests

target = "http://google.com"
response = requests.get(url=target)
print(response.text)
