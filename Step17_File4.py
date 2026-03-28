# Step17_File4.py


import os
import re


if __name__ == "__main__":
    # 문자열 한 줄, 한 줄을 저장할 list
    updated_lines = []

    # SELINUX=xxxxxx pattern의 문자열을 찾을 정규 표현식
    pattern=r"^SELINUX=[a-zA-Z]+"

    # 읽어들일 파일의 경로
    file_path = os.path.join(os.getcwd(), "config.txt")

    # 읽기 전용으로 읽어 들이기
    with open(file_path, "r", encoding="utf-8") as f :
        # 반복문 돌면서 문자열을 한줄씩 읽어들인다
        for line in f :
            # 만일 pattern 에 매칭되는 line 이면
            if re.match(pattern, line) :
                # SELINUX=xxxx 를 SELINUX=disabled 로 치환(substitution)하기
                result=re.sub(pattern, "SELINUX=disabled", line)
                # 바꾼 결과값을 list 에 추가(저장) 하기
                updated_lines.append(result)
                pass
            else:
                # 매칭되는게 없다면 그대로 추가
                updated_lines.append(line)
    
    print(updated_lines)

    # list 에 저장된 문자열을 이용해서 file 을 새로 만든다.
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)
   
    print("config.txt 파일을 수정 했습니다")