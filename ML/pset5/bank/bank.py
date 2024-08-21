def main():
    greeting = input("Enter Greeting: ")
    print(value(greeting))

def value(greeting = "nothing"):
    try:
        new_greeting = str.strip(str.casefold(greeting))
        hello_location = new_greeting.find("hello")
        start_letter = new_greeting.find("h")
        if hello_location == 0:
            return f"$0"
        elif start_letter == 0:
            return f"$20"
        else:
            return f"$100"
    except TypeError:
        return f"$100"

if __name__ == "__main__":
    main()