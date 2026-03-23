# gui03.py

'''
    1단계 : 2 진수 8자리를 입력하고 변환 버튼을 누르면 입력한 숫자가 아래의 Label 에 출력되도록 해보세요
    2단계 : 2 진수 8자리를 입력하고 변환 버튼을 누르면 입력한 숫자를 10진수로 변경해서
           아래의 Label 에 출력되도록 해보세요
    3단계 : 2 진수 8자리를 입력하고 변환 버튼을 누르면 입력한 숫자를 10진수로 변경해서 아래의 Label 에 출력되도록 해보세요
    
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
    if not input_value:
        messagebox.showwarning("Warnning!", "값을 입력하세요!")
        return   # 함수를 호출한 곳으로 실행의 흐름을 돌려준다(함수는 여기서 종료된다)

    try:
        # 만일 입력한 수에 0과 1이외의 문자를 입력했다면 함수 종료 시키기
        if not set(input_value).issubset({"0","1"}):
            result_lable.config(text="0과 1만 입력 가능합니다.", fg="red")
            return
        
        # 8자리 인지 확인
        if len(input_value) > 8:
            result_lable.config(text="8자리까지만 입력 가능합니다", fg="red")
            return

        # 2진수 문자열을 10진수 정수로 변환
        decimal_number = int(input_value,2)
        # 출력하기
        result_lable.config(text=f"10진수: {decimal_number}", fg="blue")

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
    label = tk.Label(root, text="2진수 8자리를 10진수로 변환")
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