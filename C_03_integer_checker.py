while True:

    error = "please enter an integer that is 13 or more."

    try:
        my_num = int(input("enter an integer: "))


        # checks that the number is more than / equal to 13
        if my_num < 13:
            print(error)
        else:
            print("your number is ", my_num)

    except ValueError:
        print(error)
