def create_profile():
    print("=== User Profile Generator ===")

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    interest = input("Enter your main interest (IT, games, design, etc.): ")

    print("\n--- Profile ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Interest: {interest}")
    print("Status: Beginner developer 🚀")


if __name__ == "__main__":
    create_profile()
