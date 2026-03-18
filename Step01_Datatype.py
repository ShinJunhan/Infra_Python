# 한 줄 주석

"""
    여기는 여러줄 주석
"""

print("step01,start")


# python의 여러가지 데이터 type에 대해 알아보기

# int type
num1 = 10

#float type
num2 = 10.1

# str type
myName = '신준한'
yourName = "Chihiro"
ourName = """
KT Cloud Infra
"""

# 순서가 중요한 여러 개의 데이터를 관리하고 싶다면...
# 내가 좋아하는 음식 목록 3가지를 하나의 변수에 순서대로 담고 싶다면...
food1 = '삼겹살'
food2 = '김밥'
food3 = '피자'

foods = ["삼겹살", "김밥", "피자"] 
# foods의 type은 [list type] / value는?
# list type >> [값1, 값2, 값3, ...] / 순서가 중요하므로 순번 0, 1, 2 로 부여

# 순서가 중요치 않지만 여러 개의 데이터를 관리하고 싶다면...
# 회원 1명의 정보
num=1
name="Junhan"
addr="유성구"

mem1 = {"num":1, "name":"Junhan", "addr" : "유성구"} 
# mem1의 type은 {dict type} / value는? 
# dict type >> {"key":value, "key2":value2, ....} / 순서 상관없이 key값으로 부여


# 순서가 중요치 않은 데이터를 하나의 묶음으로 관리(키값 없이)...
mySet = {"빨강사탕", "초록사탕", "노랑사탕"}
# mySet의 type은 {set type} / value는? 
# set type >> {value, value2, value3, ....}

print(foods)
print(mem1)
print(mySet)

# 특정 코드 블럭을 필요한 시점에 일괄 실행하고 싶다면? 함수 필요
# funtion 만들기 / 특정 시점에 일괄 실행할 코드 블럭
def store(): # 함수 생성 / python 에서는 코드 블럭은 콜론(:)과 들여쓰기로
    print("----------------")
    print("냉장고 문을 연다")
    print("물건을 저장한다")
    print("냉장고 문을 닫는다")

    print("마무리")


# store의 type : function (함수도 데이터 타입의 일종) / 참조값=instance

#함수를 만드는 것과 실행(호출)은 별개다
store() # 함수 호출(실행) = 함수을 call 한다 / heap 영역에 store() 함수 내용 저장
returnValue = store() # 함수 실행하고 return 할 때, 반드시 어떤 데이터(return 값)를 가지고 온다

print(returnValue)



# 어떤 변수를 빈 상태로 만들고 값을 나중에 넣고 싶다면? None (빈 값)
a = None
print("어떤 작업을 하고")
print("필요할 때, 값을 넣는다")
a = "test"
print(a)

# 참과 거짓을 나타내는 data type (Bool)

isMan=True
isWoman=False
isDifferent=True
isRun=False
canEat=True