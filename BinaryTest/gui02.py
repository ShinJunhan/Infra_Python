# gui02.py

'''
    1단계 : 10 진수 숫자를 입력하고 전송 버튼을 누르면 입력한 숫자가 아래의 Label 에 출력되도록 해보세요
    2단계 : 10 진수 숫자를 입력하고 전송 버튼을 누르면 입력한 숫자를 2진수로 변경해서
           아래의 Label 에 출력되도록 해보세요
    3단계 : 10 진수 숫자를 입력하고 전송 버튼을 누르면 입력한 숫자를 2진수로 변경해서 아래의 Label 에 출력되도록 해보세요 (2진수 8 자리로 변경해서 )
    
    전제조건 : 0~255 사이의 숫자를 입력했을때
    4단계 : 0~ 255 사이의 숫자가 아니면 경고 알림 띄우기

'''

# ui ToolKit 을 사용할수 있는 interface 객체 import 하기
import tkinter as tk
from tkinter import messagebox

def clicked():
    print("버튼을 클릭했네요?")
    # Entry(입력창) 에 입력한 문자열 읽어오기
    input_value=entry.get().strip() # strip() >> 좌우 공백제거
    
    # 빈 값일 때, 안내 문구 확인
    if not input_value :
        return   # 함수를 호출한 곳으로 실행의 흐름을 돌려준다(함수는 여기서 종료된다)

    try:
        # 입력한 문자열을 정수로 변환
        num = int(input_value)
        # 만일 입력한 수가 0 <= num <= 255사이가 아니면 경고 알림 띄우기
        if not (0 <= num <= 255):
            messagebox.showerror("Error!", "0~255 사이의 숫자를 입력해 주세요!")
            return

        # 2진수 형태의 문자열로 변경해서
        binary_result = f"{num:08b}"
        # 출력하기
        result_lable.config(text=binary_result, fg="blue")

    except Exception as e :
        result_lable.config(text="숫자만 입력 가능 합니다", fg='red')

if __name__ == "__main__":
    # root 창 생성
    root = tk.Tk()
    # 제목 설정
    root.title("나의 App")
    # 창의 크기
    root.geometry("400x200")

    # 레이블
    label = tk.Label(root, text="10진수를 2진수로 변환")
    # pady => padding y => y축 padding => 위아래 padding / padx도 있음
    label.pack(pady=20)

    # 입력창
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    entry.focus() # 포커스 주기

    # 버튼
    btn = tk.Button(root, text="변환", command=clicked, width=10, bg="lightgray")
    btn.pack(pady=15)

    # 결과 값을 출력할 Lable1
    result_lable = tk.Label(root, text="결과...")
    result_lable.pack(pady=20)

    # 창이 닫힐때 까지 무한 대기
    root.mainloop()