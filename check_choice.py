def check_choice(choice, num_list):
    # Check if choice is within num_list and not existing choice
    # get options of choice
    # remove X and O from num_list

    temp_list = num_list
    temp_list = [ele for ele in temp_list if ele != 'X']
    temp_list = [ele for ele in temp_list if ele != 'O']
    print(temp_list)

    #check if choice is in temp_list
    if int(choice) in temp_list:
        #valid choice
        print("Valid")
        return
        # return
    # Else ask user for new choice
    else:
        choice = input("Invalid, Enter a new box to mark:")
        check_choice(choice, temp_list)







choice = '1'
array = ['X', 2, 'O', 4, 5, 'X', 7, 8, 9]

check_choice(choice, array)
