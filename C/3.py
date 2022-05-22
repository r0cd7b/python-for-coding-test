# JSON 디코딩 예시
import json

user = {"id": "gildong", "password": "192837", "hobby": ["football", "programming"]}
json_data = json.dumps(user)
data = json.loads(json_data)
print(data)
