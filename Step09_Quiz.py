# Step09_Quiz.py

'''
    비밀번호를 입력 받아서 입력한 비밀번호가 8자 이상이면,
    "사용 가능한 비밀번호 입니다"
    그렇지 않으면
    "사용 불가 입니다"
    를 출력하는 간단한 프로그래밍을 해보세요.
    - hint : len()
'''

# 비밀번호 입력 받기
input_passowrd: str= input("설정할 비밀번호를 입력하세요:")
password = len(input_passowrd)

if password >= 8 :
    print("사용 가능한 비밀번호 입니다")
else :
    print("사용 불가 입니다")

print("\n종료됩니다")