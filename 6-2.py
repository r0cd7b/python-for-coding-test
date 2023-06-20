# 성적이 낮은 순서로 학생 출력하기
from sys import stdin

students = [stdin.readline().split() for _ in range(int(stdin.readline()))]
students.sort(key=lambda student_: int(student_[1]))
for name, _ in students:
    print(name, end=' ')
'''
2
홍길동 95
이순신 77

이순신 홍길동
'''
