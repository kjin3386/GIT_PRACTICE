def save_user_info(name, age):
    with open("user_info.txt", "w") as file:
        file.write(f"name: {name}\nage: {age}\n")
    print("사용자 정보가 user_info.txt 파일에 저장되었습니다.")



if __name__ == "__main__":
    save_user_info("noname",20)