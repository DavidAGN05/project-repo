def main():
    variable_name = input("camelCase: ")
    print(f"snake_case: {convert(variable_name)}")
    

def convert(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

main()