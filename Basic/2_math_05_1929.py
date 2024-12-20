# 문제) M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력) 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 
#       하나 이상 있는 입력만 주어진다.

# 출력) 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 문제 소스) 백준 - https://www.acmicpc.net/problem/1929

#///////////////////////////////////////////////////////////////////////////



# 변수
A, B = map(int, input().split())
count = 0


# 개수 찾기
if A == 1:
    A += 1
for i in range(A, B+1):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)


