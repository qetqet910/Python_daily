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

# 나무 자르기 (이분 탐색)

###################################################### -- python 3 통과

N, M = map(int, input().split())
woods = list(map(int, input().split()))
left, right = 0, max(woods)

result = []

while not right < left:
    length = 0
    mid = (left + right) // 2

    #

    length = sum(i-mid if i > mid else 0 for i in woods)

    if length == M:
        result.append(mid)
        break
    elif length > M:
        result.append(mid)
        left = mid + 1
    else:
        right = mid - 1

print(max(result))

###################################################### -- python 3 시간 초과

N, M = map(int, input().split())
woods = list(map(int, input().split()))
start, end = 1, max(woods)

while not end < start:
    log = 0
    mid = (start + end) // 2

    for i in woods:
        if(i >= mid):
            log += i - mid

    if log >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)

######################################################

# 둘 코드의 다른 점 은... 제일 큰 시간 단축의 코드는 length = sum(i-mid if i > mid else 0 for i in woods) 인 것 같다.
# 나중에 더 알아보자 (12월 01일 이분 탐색)

# 마인크래프트 아직 풀이를 잘 모르겠음 나중에 해석

from sys import stdin
from collections import Counter

input = stdin.readline

def minecraft(g, b):
    gg = Counter(g)
    ret = []
    for h in range(max(gg.keys()), -1, -1):
        gt = 0
        inventory = b
        needed = 0
        for gh, gc in gg.items():
            if h < gh:
                inventory += (gh - h) * gc
                gt += 2 * (gh - h) * gc
            elif h > gh:
                needed += (h - gh) * gc
                gt += (h - gh) * gc
        if inventory >= needed:
            ret.append([gt, h])
    ret.sort(key=lambda x: (x[0], -x[1]))
    return ret[0]


if __name__ == "__main__":
    N, M, B = map(int, input().split())
    grounds = []
    for _ in range(N):
        grounds.extend(list(map(int, input().split())))
    res = minecraft(grounds, B)
    print(res[0], res[1])

# 팰린드롬 만들기

s=input()

for i in range(len(s)):
    if s[i:]==s[i:][::-1]:
        print(len(s)+i)
        break
    
# s[i:] 왼쪽부터 줄여나감
# abab, bab, ab, b

# s[i:][::-1] 왼쪽부터
# 줄여나가지만 뒤집은 상태임
# baba, bab, ba, b 

# ex) qwerty ytrewq
# ex) werty ytrew
# ex) erty ytre
# ex) rty ytr
# ex) ty yt
# ex) y == y

# 부분 팰린드롭 공식
# for i in range(len(s)):
#     s[i:]==s[i:][::-1]

# 큐

import sys

N = int(sys.stdin.readline())

numlist = []

for i in range(N):
    nums = sys.stdin.readline().split()
    
    if(nums[0] == 'push'):
        numlist.append(nums[1])
    elif(nums[0] == 'pop'):
        if(len(numlist) == 0):
            print(-1)
        else:
            print(numlist.pop(0))
    elif(nums[0] == 'size'):
        print(len(numlist))
    elif(nums[0] == 'empty'):
        if(len(numlist) == 0):
            print(1)
        else:
            print(0)
    elif(nums[0] == 'front'):
        if(len(numlist) == 0):
            print(-1)
        else:
            print(numlist[0])
    elif(nums[0] == 'back'):
        if(len(numlist) == 0):
            print(-1)
        else:
            print(numlist[-1])


# 백준 2609번 최대공약수와 최소공배수

nums= list(map(int, input().split())) 
# 유클리드의 호제법 사용을 위해 A > B or A < B 를 알아야 함
# list로 받아서 A, B로 해주는 것이 if문을 줄일 수 있음

A = max(nums)
B = min(nums)
# 입력받은 수 A > B

gop = A * B
# A * B == A와 B의 (최대공약수) * (최소공배수)
# while문을 통과하면 A, B의 값이 변질되기 때문에 미리 만듦

while B:
    # 나머지가 0이 되면 멈춤
    A, B = B, A % B
    # ex) A % B = r | B % r = r1 | r % r1 = r2 ...
    # => A = B, B = A % r

print(A, gop // A)
# 나머지가 0일 때 나누는 수 = A
# gop // A == A, B의 최소공배수
