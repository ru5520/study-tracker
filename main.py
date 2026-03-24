import os

def get_study_info():
    content = input("今天学了什么,用逗号分隔")
    content_list = content.split(",")
    for content1 in content_list:
        print(f"我正在学习: {content1.strip()}")
    hours = int(input("学了多少小时？"))
    return content_list, hours

def save_record(content_list, hours):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "log.txt")
    
    with open(file_path, "a",encoding="utf-8") as file:
        file.write(f"学习了{hours}小时\n")
        file.write(f"学习了{content_list}\n")
        file.write("--------------------------------\n")

def main():
    content, hours = get_study_info()
    save_record(content, hours)
    print("学习记录已保存")
    print(f"学习记录已保存到{file_path}")

main()

