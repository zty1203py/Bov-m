import os  # 确保导入 os 模块
import sys

def execute_command(command):
    try:
        os.system(command)
    except Exception as e:
        print(f"Error executing command: {e}")

def main():
    print("Welcome to the bos -m!")
    print("Type 'exit' to quit.")

    while True:
        # 显示提示符
        command = input("~$ ")

        # 退出命令
        if command.lower() == 'exit':
            print("Exiting the terminal.")
            break

        # 执行命令
        execute_command(command)

if __name__ == "__main__":
    main()