# Step13_example2.py

'''
    html/index.html  외부에 있는 template 파일을 읽어와서
    data 를 연결해서 원하는 문자열을 얻어내서
    콘솔창에 출력하는 예제( 나중에는 콘솔창이 아니고 클라이언트의 웹브라우저에 출력하게 된다 )
'''


from jinja2 import Environment, FileSystemLoader, Template


# 템플릿 파일이 위치한 폴더 설정
file_loader = FileSystemLoader("html")

# 환경 객체(외부 파일에서 읽어올 환경 설정을 한다)
env = Environment(loader=file_loader)

# 템플릿 파일을 로딩한 Template 객체 얻어 내기
temp:Template = env.get_template("index.html")

# 템플릿에 렌더링할 데이터 (실제로는 DB 에서 읽어오게 된다)
notice_data = {
    "title":"오늘의 공지사항",
    "notice": ["드디어 오늘 불금입니다","주말에는 푹 쉬시길 바랍니다"]
}

# 데이터를 전달해서 렌더링 하기
result:str = temp.render(notice_data)

# 출력하기
print(result)