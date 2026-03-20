# Step11_Class.py

'''
    1. 클래스는 객체를 생성할 수 있는 설계도 역할
    2. Data type의 역할

    객체는 속성(저장소)와 기능(함수)로 이뤄진다.
'''

class Car: # 1. Class를 통한 객체의 설계도 작성
    
    def drive(self):
       print("달려요!")

if __name__ == "__main__":
  # Car() 는 Car 클래스로 객체(인스턴스)를 생성하는 표현식
  c1: Car = Car() # 2. 클래스 Car를 이용해서 객체(실체) 생성
  c1.drive() # 3. Class Car에 있는 주소값을 이용해서 drive()라는 기능 호출

  c2: Car = Car()
  c3: Car = Car()

