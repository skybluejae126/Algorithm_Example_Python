# 문제) (n, m)의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.

# 입력) 첫째 줄에 정수 n, m (0 <= m <= n <= 2,000,000,000, n != 0) 이 들어온다.

# 출력) 첫째 줄에 (n, m) 의 끝자리 0 의 개수를 출력한다. 

# 문제 소스) 백준 - https://www.acmicpc.net/problem/2004

#///////////////////////////////////////////////////////////////////////////


# 정수 N 받기
n, m = map(int, input().split())

# 팩토리얼 계산
def fact_5or2_cnt(num, t):
    cnt = 0
    while num > 0:
        cnt += num // t
        num //= t
    return cnt

cnt_5 = fact_5or2_cnt(n, 5) - fact_5or2_cnt(m, 5) - fact_5or2_cnt(n-m, 5)
cnt_2 = fact_5or2_cnt(n, 2) - fact_5or2_cnt(m, 2) - fact_5or2_cnt(n-m, 2)

ans = min(cnt_5, cnt_2)
print(ans)