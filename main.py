from dfs_agent.modes import text_mode, random_mode, graphic_mode

def print_menu():
    print("\n=== DFS Agent ===")
    print("1 - text (read from file)")
    print("2 - random (text output with random map)")
    print("3 - graphic (pygame visualization)")
    print("-1 - exit")

def main():
    while True:
        print_menu()
        num = input("Enter your number: ").strip()
        if num == "1":
            text_mode()
        elif num == "2":
            random_mode()
        elif num == "3":
            graphic_mode()
        elif num == "-1":
            print("Bye 👋")
            break
        else:
            print("Invalid input. Please enter 1, 2, 3, or -1.")

if __name__ == "__main__":
    main()
