import os
from datetime import datetime

def get_file_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "log.txt")

def get_study_info():
    while True:
        content = input("今天学了什么,用逗号分隔").strip()
        if content:
            break
        else:
            print("你输入的内容为空，请重新输入")

    content_list = []
    for content1 in content.split(","):
        clean_item = content1.strip()
        if clean_item:
            content_list.append(clean_item)
            
    print(f"我正在学习: {', '.join(content_list)}")

    while True:
        hours_raw = input("学了多少小时？").strip()
        try:
            hours_value = float(hours_raw)
            if hours_value > 0:
                break
            else:
                print("学习时长必须大于0，请重新输入")
        except ValueError:
            print("学习时长必须是数字，请重新输入")

    return content_list, hours_value

def save_record(content_list, hours):
    file_path = get_file_path()
    today = datetime.now().strftime("%Y-%m-%d")

    with open(file_path, "a",encoding="utf-8") as file:
        file.write(f"日期: {today}\n")
        file.write("今日学习内容:\n")
        for item in content_list:
            file.write(f"- {item}\n")
        file.write(f"学习时长: {hours}小时\n")
        file.write("--------------------------------\n")

def calculate_total_hours():
    file_path = get_file_path()
    total_hours=0.0

    if not os.path.exists(file_path):
        return total_hours

    with open(file_path, "r",encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if "学习时长" in clean_line:
                hours_text = clean_line.replace("学习时长: ", "")
                hours_text = hours_text.replace("小时", "")
                hours_text = hours_text.replace("学习时长:", "")
                hours_text = hours_text.strip()
                try:
                        total_hours += float(hours_text)
                except ValueError:
                        pass
    return total_hours
def show_log():
    file_path = get_file_path()
    if not os.path.exists(file_path):
        print("暂无学习记录")
        return
    with open(file_path, "r",encoding="utf-8") as file:
         content = file.read()
         print("=====学习日志=====")
         print(content)
       
def show_recent_record():
    file_path = get_file_path()
    if not os.path.exists(file_path):
        print("暂无学习记录")
        return
    with open(file_path, "r",encoding="utf-8") as file:
        content = file.read()
        
        records = content.split("--------------------------------")
        clean_records = []
        for record in records:
            record = record.strip().split("\n")
            
            if record:
                clean_records.append(record)
                recent_record = clean_records[-5:]
        
        print("\n=====最近 5 条学习记录=====")
        if not recent_record:
            print("暂无学习记录")
            return
        for record in recent_record:
            print(record)
            print("--------------------------------")

def show_menu():
    print("=====学习跟踪系统=====")
    print("1. 记录学习")
    print("2. 查看学习记录")
    print("3. 查看累计学习时长")
    print("4. 查看最近学习记录")


def main():
    while True:
         show_menu()
         choice=input("请选择功能(1-3,0退出): ").strip()
         if choice == "0":
            print("再见!")
            break
         elif choice == "1":
            content_list, hours = get_study_info()
            save_record(content_list, hours)
            print("学习记录已保存")
         elif choice == "2":
            show_log()
         elif choice == "3":
            total_hours = calculate_total_hours()
            print(f"累计学习时长: {total_hours}小时")
         elif choice == "4":
            show_recent_record()
         else:
            print("无效选择，请重新选择")

  


if __name__ == "__main__":
    main()

