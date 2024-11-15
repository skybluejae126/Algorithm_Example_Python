# 문제) N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

# 입력) 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

# 출력) 첫째 줄에 구한 0의 개수를 출력한다.

# 문제 소스) 백준 - https://www.acmicpc.net/problem/1676

#///////////////////////////////////////////////////////////////////////////


# # 정수 N 받기
# N = int(input())

# # 팩토리얼 계산
# def fact_cal(N):
#     ans = 1
#     if N > 0:
#         ans = N * fact_cal(N-1)
#     return ans

# # 0 개수 확인
# cnt = 0
# ans = fact_cal(N)

# while True:
#     if ans % 10 == 0:
#         cnt += 1
#         ans = ans / 10
#     else:
#         break

# print(cnt)

N = int(input())
print(N // 5 + N // 25 + N // 125)