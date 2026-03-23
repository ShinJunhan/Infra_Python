# BinaryTest/test01.py

# python에서 2진수 다루기

# 2진수 표현법 : prefix 로 0b (숫자 0, 알파벳 b)
num1 = 0b1010 # 10진수로 환산했을 때, 10이 된다

result = num1 + 5
print(result) # 결과 >> 15

# 10진수를 2진수로 변환
num2 = 150
result2:str = bin(num2) #bin() 함수를 호출하면서 10진수를 넣어주면 2진수 형태로 변환
print(f"값 : {result2}, 타입: {type(result2)}") # 결과 >> 값 : 0b10010110, 타입: <class 'str'>

print("-------------------------------------")

line = "abcde12345"
# 5번 인덱스 이상, 10번 인덱스 미만 인덱스의 문자열 얻어내기
print(line[5:10]) # 결과 >> 12345

# 위의 result2 문자열에서 (0bxxxxx)에서 0b 를 제거한 순수 2진수 형태의 문자열만 얻어내려면?
print(result2[2:]) # 결과 >> 10010110