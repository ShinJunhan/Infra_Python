# test05.py

# 2진수 문자열
source = "11110000"

# 2진수 문자열을 10진수로 변환
print(int(source,2))

source2 = "11110003"

# source 문자열 하나하나를 set 로 만들어서 {"0", "1"} 로만 이뤄져 있는 여부 알아내기
result1 = set(source).issubset({"0", "1"})
result2 = set(source2).issubset({"0", "1"})
print(f"{source} 이 0 과 1 로 되어 있는 여부 : {result1}")
print(f"{source2} 이 0 과 1 로 되어 있는 여부 : {result2}")
print(f"{source} 가 8자리 초과인지 여부 : {len(source) > 8}")
