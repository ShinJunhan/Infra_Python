# BinaryTest/test03.py

# 비트연산 AND, OR, XOR, NOT
a = 0b1100
b = 0b1010

# bit AND 연산 (자리수 별로 모두가 1일 때, 결과가 1이 됨)
print(a&b) # 결과 >> 8
print(bin(a&b)) # 결과 >> 0b1000
print("------------")

# bit OR 연산 (둘 중 하나라도 1이면, 결과가 1이 됨)
print(a|b) # 결과 >> 14
print(bin(a|b)) # 결과 >> 0b1110
print("------------")

# bit XOR 연산 (두 수가 같으면 0, 다르면 1이 됨)
print(a^b) # 결과 >> 6
print(bin(a^b)) # 결과 >> 0b110 (0110인데, 앞 쪽 0은 표기 안함)
print("------------")

# bit NOT 연산
print(bin(~a)) # 결과 >> -0b1101 / a=12, ~12 = -(12+1) / ~N = -(N+1)
print(bin(~b)) # 결과 >> -0b1011

# NOT 연산 결과를 깔끔하게 보고 싶으면
print(bin(~a & 0xF)) # 결과 >> 0b11 (0011인데, 앞 쪽 00은 표기 안함)

