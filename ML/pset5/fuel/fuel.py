def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    str1, str2 = fraction.split('/')

    if not (str1.isdigit() and str2.isdigit()):
        raise ValueError()
    
    x = int(str1)
    y = int(str2)
 
    if y == 0:
        raise ZeroDivisionError
    
    elif x > y:
        raise ValueError  
      
    percentage = (x / y) * 100
    return round(percentage)


def gauge(percentage):
    if  percentage <= 1:
        return f"E"
    elif  percentage >= 99:
        return f"F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()