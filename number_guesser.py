



num_tries = 5
too_low = 0
too_high = 0

min_num = 0
max_num = 100


win = False
lose = False

while win == False:
    binary = int((max_num + min_num) / 2)

    answer = input(f"Is the number {binary}? (Y/N)")
    
    if answer.lower() == "y":
            win = True
            print("I win!!")
    elif answer.lower() == "n":
        height = input("Is the right number higher or lower?")
        if height.lower() == "lower":
            max_num = binary
        elif height.lower() == "higher":
            min_num = binary




