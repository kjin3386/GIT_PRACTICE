# 간단한 Python 프로그램: 사용자 정보 입력 및 출력
def get_user_info():
    name = input("이름을 입력하세요: ")
    age = input("나이를 입력하세요: ")
    return name, age

def print_greeting(name, age):
    print(f"안녕하세요, {name}님! 당신의 나이는 {age}살이군요.")

def main():
    name, age = get_user_info()
    print_greeting(name, age)

if __name__ == "__main__":
    main()