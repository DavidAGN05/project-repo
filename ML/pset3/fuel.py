def main():
    while True:
        user_input = input("Fraction: ")
        try:
            str1, str2 = user_input.split('/')
            x = int(str1)
            y = int(str2)
            if x > y:
                pass
            elif x/y == 1:
                print("F")
                break
            elif x/y <= 1:
                print("E")
                break
            else:
                print(f'{(x / y * 100):.0f}%')
                break
        except (ValueError, ZeroDivisionError):
            pass



main()