# Step13_jinja2_list2

# 게시글 목록이 담긴 리스트
from jinja2 import Template



'''
    위의 posts에 담긴 데이터를 이용해서 아래와 같이 출력되도록 해보세요.
    글 목록입니다
    - 글번호: 1, 작성자: 작성자1, 제목: 제목1
    - 글번호: 2, 작성자: 작성자2, 제목: 제목2
    - 글번호: 3, 작성자: 작성자3, 제목: 제목3
'''

posts_template:str = '''
    글 목록입니다
    {% for post in posts %}
    - 글번호: {{ post.id }}, 작성자: {{ post.writer }}, 제목: {{ post.title }}
    {% endfor %}
'''

temp: Template = Template(posts_template)

posts:list = [
    {"id":1,"writer":"작성자1", "title":"제목1"},
    {"id":2,"writer":"작성자2", "title":"제목2"},
    {"id":3,"writer":"작성자3", "title":"제목3"}
]

result:str = temp.render(posts=posts)

print(result)
