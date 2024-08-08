greeting = str.strip(str.casefold(input("Enter Greeting: ")))
start_letter = greeting.find("h")
hello_location = greeting.find("hello")

if hello_location == 0:
    print("$0")
elif start_letter == 0:
    print("$20")
else:
    print("$100")