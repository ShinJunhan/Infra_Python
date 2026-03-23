# Step14_TryExcept.py


# main 으로 실행 했을 때(현재 파일에서 run 했을 때), 실행할 코드 블럭
if __name__ == "__main__":
    
    # 예외처리
    try:
         # 문자열
        num1_str: str = input("젯수 입력:")
        num2_str: str = input("피젯수 입력:")

        # 입력한 문자열 int형으로 형변환
        num1: int = int(num1_str)
        num2: int = int(num2_str)

        result = num2/num1
        # 결과 출력
        print(f"{num2} 를 {num1} 으로 나눈 결과값 : {result}")    
    except ValueError as ve: # ve 에는 에러 정보가 들어 있음
        print(ve)
        print("숫자 형식으로 입력해 주세요!")
    except ZeroDivisionError as zde:
        print(zde)
        print("어떤 수를 0으로 나눌 수는 없습니다!")

    # 어떤 중요한 마무리 작업
    print("중요한 마무리 작업을 합니다")


