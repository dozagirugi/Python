#기초코딩 과제 8장

#1번

a = input("문자열: ")
print("문자열 길이: ", len(a))
print("첫 번째 문자: ", a[0])
print("두 번째 문자: ", a[1])
print("마지막 문자: ", a[-1])

#2번
print()

a = input("문자열2: ")

print("개별 문자 출력: ")
for str in range(len(a)):
    print(a[str], end="")

print()

print("역순 개별 문자 출력: ")
for str2 in range(len(a)-1, -1, -1):
    print(a[str2], end="")


#3번
print()

score=int(input("점수: "))

if 90 <= score <= 100:
    print(score,": A")
elif 80 <= score <= 89:
    print(score,": B")
elif 70 <= score <= 79:
    print(score,": C")
elif 60 <= score <= 69:
    print(score,": D")
elif 0 <= score <= 59:
    print(score,": F")
else:
    print("입력 가능한 점수 범위는 0~100입니다.")

#4번
print()

dict = {10:'A', 9:'A', 8:'B', 7:'C', 6:'D', 5:'F', 4:'F', 3:'F', 2:'F', 1:'F', 0:'F',}
score2=int(input("점수2: "))
a= score2//10
print(score2,": ",dict[a])

# 5번
print()

items = {"라면": 650, "우유": 1100, "콜라": 1200, "캔커피": 500, "과자": 700}

s = 0
while True:
    it = input("제품명: ")

    if not it:
        break
    elif it not in items:
        print(it, "는 미등록 제품입니다.")
    else:
        s += items[it]
        print("[%s:%d] > %d" % (it, items[it], s))

print("총 급액: ", s)

# 6번
print()

engkor_dict = dict()

while True:
    a = input("영어 단어: ")
    b = input("한글 단어: ")
    engkor_dict[a] = b

    if a in [""] and b in [""]:
        del engkor_dict[""]
        print(engkor_dict)
        break


# 7번
print()

engkor_dict2 = dict()

while True:
    s = input("영어 단어: ")

    if dict==None:
        print("사전이 비어 있습니다.\n단어를 추가합니다.")
        x = input("한글 단어: ")
        engkor_dict2[s] = x

    elif s in engkor_dict2:
        print(engkor_dict2[s])

    elif s=='':
        break

    else:
        print(s,"단어가 등록되어 있지 않습니다.\n단어를 추가합니다.")
        x = input("한글 단어: ")
        engkor_dict2[s]=x

print(engkor_dict2)

#8번
print()

import time
for i in range(1,6):
    print(i, end=" ")

time.sleep(1)

#9번
print()

import math

a = float(input("실수: "))

print(a, ":", math.ceil(a))
print(a, ":", math.floor(a))
print(a, ":", math.trunc(a))