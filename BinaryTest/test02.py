# BinaryTest/test02.py

a = 0b1100
b = 0b1010

# a 와 b 를 비트 AND 연산 (자리수 별로 모두가 1일 때, 결과가 1이 됨)
print(a&b) # 결과 >> 8
print(bin(a&b)) # 결과 >> 0b1000
print("------------")

# a 와 b 를 비트 OR 연산 (둘 중 하나라도 1이면, 결과가 1이 됨)
print(a|b) # 결과 >> 14
print(bin(a|b)) # 결과 >> 0b1110
print("------------")

# a 와 b 를 비트 XOR 연산 (두 수가 같으면 1, 다르면 0이 됨)
print(a^b) # 결과 >> 14
print(bin(a^b)) # 결과 >> 0b1110
print("------------")


info = 0b1111_1111_1111_0000 # 언더바를 붙여도 2진수로 간주됨
print(info) # 결과 >> 65520
print(bin(info)) # 결과 >> 0b1111111111110000
print("------------")

data1 = 0b1100_0011_1010_0001
data2 = 0b1100_0011_1010_0010
data3 = 0b1100_0011_1010_1011
data4 = 0b1100_0011_1010_1100
data5 = 0b1111_0000_1010_1111

print(bin(info&data1)) # 결과 >> 0b1100001110100000
print(bin(info&data2)) # 결과 >> 0b1100001110100000
print(bin(info&data3)) # 결과 >> 0b1100001110100000
print(bin(info&data4)) # 결과 >> 0b1100001110100000
print(bin(info&data5)) # 결과 >> 0b1111000010100000
print("------------")


