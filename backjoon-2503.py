n = int(input())
hints = [list(map(int, input().split(' '))) for _ in range(n)]

answer = 0

for a in range(1, 10):
    for b in range(10):
        for c in range(10):

            if (a==b or b==c or c==a):
                continue
            
            cnt = 0

            for arr in hints:
                number = arr[0]
                strike = arr[1]
                ball = arr[2]

                strike_count = 0
                ball_count = 0

                target = str(a) + str(b) + str(c)

                for i in range(0, 3):
                    if target[i] == str(number)[i]:
                        strike_count += 1

                for i in range(0, 3):
                    if target[i] in str(number) and target[i] != str(number)[i]:
                        ball_count += 1
                    
                if ball == ball_count and strike == strike_count:
                    cnt += 1

            if cnt == n:
                answer += 1

print(answer)