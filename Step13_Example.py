# Step13_example.py



'''
    위의 info 안에 들어 있는 데이터를 이용해서 아래와 같은 형식의 문자열을 출력해 보세요.
    번호 : 1
    이름 : 김구라
    키 : 180 cm
    몸무게 : 80 kg
    취미 : 
        - 피아노
        - 당구
        - 프로그래밍

'''

from jinja2 import Template

info_template = """
    번호 : {{num}}
    이름 : {{name}}
    키 : {{body.height}} cm
    몸무게 : {{body.weight}} kg
    취미 :
        {% for a in hobby %}
        - {{a}}
        {% endfor %}
"""
info:dict = {
    "num":1,
    "name": "Shin",
    "body": {
        "height": 180,
        "weight": 80
    },
    "hobby": ["피아노","당구","프로그래밍"]
}

temp: Template = Template(info_template)

result:str = temp.render(info)

print(result)