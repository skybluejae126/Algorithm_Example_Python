# 문제) 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력) 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력) 주어진 수들 중 소수의 개수를 출력한다.

# 문제 소스) 백준 - https://www.acmicpc.net/problem/1978

#///////////////////////////////////////////////////////////////////////////



# 변수
N = int(input())
num = map(int, input().split())
count = 0


# 개수 찾기
for i in num:
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                count += 1

            break

print(count)
