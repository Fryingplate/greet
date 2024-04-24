# greet.py

def greet():
    name = input("Enter your name: ")
    return f"Hello, {name}!"

if __name__ == "__main__":
    greeting = greet()
    print(greeting)
