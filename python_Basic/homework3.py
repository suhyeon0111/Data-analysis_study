import random

def make_random_number():
    res = []
    for i in range(3):
        num = random.randint(0,9)
        while num in res:
            num = random.randint(0,9)
        res.append(num)
    
    x0 = res.pop()
    x1 = res.pop()
    x2 = res.pop()

    return [x0,x1,x2]

def check_strike_ball(secret_number, answer_number):
    strike = ball = 0
    for i in range(3):
        if secret_number[i] == answer_number[i]:
            strike += 1
        else:
            for j in range(3):
                if secret_number[i] == answer_number[j]:
                    ball += 1

    return [strike, ball]

secret_number = make_random_number() #랜덤 숫자 생성
cnt = 0
while 1:
    cnt += 1 #시도 횟수 증가
    answer_number = list(map(int,input('Your answer is...'))) #입력
    result = check_strike_ball(secret_number, answer_number) #비교
    print("%d strike and %d ball" %(result[0] ,result[1]))

    if result[0] == 3:
        print("The number of trials is %d" % cnt)
        print("The answer is ", end='', sep='')
        print(secret_number)
        break

