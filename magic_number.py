number = float(input("Choose a number between 1 and 100: "))
is_valid = True

if number > 100:
    print("Invalid input. The number must be less than or equal to 100.")
    is_valid = False
elif number < 1:
    print("Invalid input. The number must be greater than or equal to 1.")
    is_valid = False

if is_valid:
    input("Now, multiply that number by 2. Press Enter when ready.")
    step1_result = number * 2
    
    input("Now, add 30 to that number. Press Enter when ready.")
    step2_result = step1_result + 30
    
    input("Now, divide that number by 2. Press Enter when ready.")
    step3_result = step2_result / 2
    
    final_result = step3_result - number
    input("Are you ready for your mind to be blown? Press Enter when ready.")
    print(f"Your final number is always 15!")
