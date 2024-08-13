def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    user_input = input("Date: ")
    year = ''
    month = ''
    day = ''

    while valid_input(user_input, months) is False:    
        user_input = input("Date: ")
    
    year, month, day = convert(user_input)

    print(f"{year}-{month}-{day}")

def valid_input(prompt, list):
    if prompt in list:
        return True
    else:
        char = prompt.split("/")
        for i in range(len(char)):
            if char[i].isdigit():
                continue
            else:
                return False
        return True

def convert(string):
    year, month, day = string.split("/")
    return year, month, day


main()