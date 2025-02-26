def calculate_birth_year(age):
    try:
        birth_year = 2024 - int(age)
        print(f"{age}살이라면, 출생 연도는 {birth_year}년이겠네요!")
    except ValueError:
        print("올바른 숫자를 입력하세요!")

    return birth_year

if __name__ == "__main__":
    calculate_birth_year(20)