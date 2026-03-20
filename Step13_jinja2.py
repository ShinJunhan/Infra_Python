# Step13_jinja2.py

'''
    Template 문자열을 정의하고 어떤 데이터를 Template 문자열에 전달해서
    결과 문자열을 얻어내는 작업을 jinja2를 이용해서 테스트 해보자
'''

# 테스트용 template 만들기

from jinja2 import Template


my_template = """
    번호 : {{ num }}
    이름 : {{ name }}
    주소 : {{ addr }}
"""

# template 에 출력할 데이터 준비
mem1 = {"num":1, "name":"shin", "addr":"Yuseong"}
mem2 = {"num":2, "name":"shim", "addr":"Daejeon"}

# import한 Template 클래스의 생성자에 my_template 문자열을 넣어서 객체를 생성
temp: Template = Template(my_template)
result1 = temp.render(mem1)
print(result1)

result2 = temp.render(mem2)
print(result2)

