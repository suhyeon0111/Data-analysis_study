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

print(check_strike_ball([1, 2, 3],[1, 3, 2]))
print(check_strike_ball([1, 2, 3],[4, 5, 6]))