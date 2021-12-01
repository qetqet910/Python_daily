# 백준 4문제

# 분해합

N = int(input())
result = 0
for i in range(1, N + 1):
    A = sum(map(int, str(i)))
    result = i + A
    if(result == N):
        print(i)
        break
    
    if(i == N):
        print(0)

#팰린드롬수

while True:
    n = input()

    if(n == '0'):
        break

    if(n == n[::-1]):
        print("yes")
    else:
        print("no")

# Hashing

L = int(input())
alpha = input()
result = 0

for i in range(L):
    result += (ord(alpha[i]) - 96) * (31 ** i)

print(result % 1234567891)

# 이항 계수

N, K = map(int, input().split())

def Fac(num):
    Fac = 1
    for i in range(1, num + 1):
        Fac *= i
    return Fac

result = Fac(N) // (Fac(K) * Fac(N - K))

print(result)

# 단어 정렬

N = int(input())
words = []

for i in range(N):
    words.append(input())
    
set_list = set(words)    
words = list(set_list)
words.sort()
words.sort(key = len)

for I in words:
    print(I)

# 소수 구하기

M, N = map(int, input().split())

def prime(num):
    if num == 1:
        return False
    else:
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True

for i in range(M, N + 1):
    if prime(i):
        print(i)