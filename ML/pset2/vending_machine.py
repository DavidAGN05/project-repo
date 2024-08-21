def main():
    ### Initial Prompt
    print("Welcome to the Vending Machine!\n" 
          "Enter your choice by # and input cash amount, repeatedly (^d to end).")
    profit = 0.00
    items_amount = [5, 5, 5]
    items = {
        "cola": 0.75,
        "candybar" : 1.25,
        "popcorn" : 0.50
    }
    
    display_items(items, items_amount, profit)
    user_input = input()
    valid_input = test_inputs(user_input)
    ### Initial Prompt

    # returns True or False depending on valid inputs
    while valid_input == True:
        item_num, money = splitting_numbers(user_input)
        profit = dispenser(item_num, money, items, profit) 
        items_amount = counter(item_num, items_amount)
        display_items(items, items_amount, profit)
        user_input = input()
        valid_input = test_inputs(user_input)
    



def display_items(items, items_amount, profit):
    
    for item_num, name in enumerate(items.keys()):
        print(f"[{item_num}] {items_amount[item_num]} {name} left: cost is ${items[name]:.2f}")
    print(f"Money made so far is: ${profit:.2f}")
    # ensure that it takes only two inputs that are 0, 1, 2, & valid money using new function

def counter(item_num, current_item_amount):
    if current_item_amount[item_num] == 0:
        print("invalid item") # zero items left over
        return current_item_amount
    current_item_amount[item_num] -= 1
    return current_item_amount

def test_inputs(user_input):
    if user_input == 'exit':
        print("Thanks for your patronage")
        exit(0)
    characters = user_input.split()
    if is_even(len(characters)):
        for char in characters: ## check
            if char.isdigit() == True: # use 'try' and 'except'
                converted_num = int(char)
                if 2 >= converted_num >= 0:
                    return True
                else:
                    print("invalid item") # checks if user's item selection is valid
                    return False
            else:
                print("malformed expression")
                return False
    else:
        print("incorrect amount of inputs")
        return False
    
            

def is_even(n):
    return n % 2 == 0
    

def splitting_numbers(user_input):
    # Split the input string into two parts
    seperated_input = []
    for i, char in enumerate(user_input.split()):
        if is_even(i):
            try:
                seperated_input.append(int(char)) # Convert the split strings to integers
            except ValueError:
                print("malformed expression")
                exit(0)
        else:
            try:
                seperated_input.append(float(char)) # Convert the split strings to integers
            except ValueError:
                print("malformed expression")
                exit(0)
            
        ### HAS TO BE EVERY OTHER NUMBER, SAME WITH MONEY BUT CONVERT TO FLOAT
    return seperated_input

def dispenser(item_num, money, items, current_profit):
    for i, name in enumerate(items.keys()):
        if item_num == i:
            change = money - items[name]
            print(f"{name} is dispensed and ${change:.2f} returned")
            current_profit += items[name]
            return current_profit



main()