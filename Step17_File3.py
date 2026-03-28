# Step17_File3.py

import os


if __name__ == "__main__":
    # 읽어올 txt 문서의 경로 구성하기
    letter_path = os.path.join(os.getcwd(), "my_letter.txt")

    with open(letter_path, "r", encoding="utf-8") as f:
        # 문자열을 한 줄씩 읽기
        print(f.readline()) #f.readline()에 이미 개행기호가 포함되어 있다.
        print(f.readline())
        print(f.readline())
        print(f.readline().strip()) # 좌우 공백이나 개행기호를 없애고 싶으면 .strip()까지 호출한다
        print(f.readline().strip())
        print(f.readline().strip())

    print("--- 반복문으로 처리(텍스트행이 무수히 많거나 알 수 없을 때) ---")

    with open(letter_path, "r", encoding="utf-8") as f:
        for line in f :
            print(line.strip())
