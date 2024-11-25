# 문제) 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

# 입력) 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

# 출력) N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

# 문제 소스) 백준 - https://www.acmicpc.net/problem/11653

#///////////////////////////////////////////////////////////////////////////


# N = int(input())

# a = 2

# while N != 1:
#     if N // a == 0:
#         print(a)
#         N = N / a
#     else:
#         a += 1
#     if a > N:
#         break

N = int(input())

for i in range(2, int(N ** 0.5) + 1):
    while N % i == 0:
        print(i)
        N //= i

if N > 1:
    print(N)
