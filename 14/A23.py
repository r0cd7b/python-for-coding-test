# 국영수
from sys import stdin

n = int(stdin.readline())
students = []
for _ in range(n):
    strings: list = stdin.readline().split()
    for i in range(1, len(strings)):
        strings[i] = int(strings[i])
    students.append(strings)
students.sort(key=lambda s: s[0])
students.sort(key=lambda s: s[3], reverse=True)
students.sort(key=lambda s: s[2])
students.sort(key=lambda s: s[1], reverse=True)
for student in students:
    print(student[0])

"""
입력 예시
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sungyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
출력 예시
Donghyuk
Sangkeun
Sungyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
"""
