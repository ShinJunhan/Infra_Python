# dict type

#회원 1명의 데이터
mem1 = {"num":1, "name":"Junhan","isMan":True}

#회원 1명의 데이터
info1 = [1,"Junhan",True] #list로 사용하기 불편함

print(mem1["num"])
print(mem1["name"])
print(mem1["isMan"])

# dict안의 내용을 참조해서 변수에 담기
a = mem1["num"]
b = mem1["name"]
c = mem1["isMan"]

# dict 안의 내용을 수정하기
mem1["num"] = 2
mem1["name"] = "Chihiro"
mem1["isMan"] = False


#특정 키 값으로 저장된 내용 삭제
del mem1["isMan"]

#모든 값 삭제
mem1.clear()


print("종료됩니다")

