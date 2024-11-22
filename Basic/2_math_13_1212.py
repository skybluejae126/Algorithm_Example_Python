# 문제) 8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.

# 입력) 첫째 줄에 8진수가 주어진다. 주어지는 수의 길이는 333,334을 넘지 않는다.

# 출력) 첫째 줄에 주어진 수를 2진수로 변환하여 출력한다. 수가 0인 경우를 제외하고는 반드시 1로 시작해야 한다.

# 문제 소스) 백준 - https://www.acmicpc.net/problem/1212

#///////////////////////////////////////////////////////////////////////////



# qus = input()
# result = []
# ans = ""

# for i in qus:
#     for _ in range(3):
#         result.append(str(int(i) % 2))
#         i = int(i) // 2
#     result = result[::-1]

#     ans += ''.join(result)

# print(int(ans))

print(bin(int(input(), 8))[2:])
