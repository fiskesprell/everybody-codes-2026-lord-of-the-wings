from operator import itemgetter

def read_input():
    with open("my_notes_p2.txt", "r") as file:
        return(file.read())

def read_test_input():
    return """
    2<5 3>1 1>2 1<5 4<1 3>2 4<2 3>5 4<5
    2>1 3>2 1<5 4>5 2<5 3>1 4>3 2<4 5<3
    5>1 5>2 4>1 3>2 3<4 1>2 3>5 1<3 4>5
    """
    # 3 & 5 have same points: 3 > 5 exists (give point to 3)
    # 3 & 4 have same points: 4 > 3 exists (give point to 4) 
    # 3 & 4 have same points: 3 < 4 exists (give point to 4)

def add_current_comparison_to_list():
    global val_1
    global val_2
    global comparator
    global current_row

    current_row.append(f"{val_1}{comparator}{val_2}")

def give_bonus_point(value_1, value_2):
    global current_row
    

    # finds the one comparison that uses both values
    # checks which one wins
    # awards that value a bonus point
    for comparison in current_row:
        if (
            ((comparison[0] == value_1) and (comparison[2] == value_2)) or ((comparison[0] == value_2) and (comparison[2] == value_1))
            ):
            if (comparison[1] == ">"):
                give_point(comparison[0])
            else:
                give_point(comparison[2])


def reset_wins():
    global one
    global two
    global three
    global four
    global five
    global current_row

    one[0]      = 0
    two[0]      = 0
    three[0]    = 0
    four[0]     = 0
    five[0]     = 0
    six[0]      = 0
    seven[0]    = 0
    eight[0]    = 0
    nine[0]     = 0
    current_row = []

def reset_compares():
    global comparator
    global val_1
    global val_2
    global valid_char_in_row
    
    val_1       = ""
    val_2       = ""
    comparator  = ""
    valid_char_in_row = 0


def give_point(number):
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine

    match number:
        case "1":
            one[0]      = one[0]     + 1
        case "2":
            two[0]      = two[0]     + 1
        case "3":
            three[0]    = three[0]   + 1
        case "4":
            four[0]     = four[0]    + 1
        case "5":
            five[0]     = five[0]    + 1
        case "6":
            six[0]      = six[0]     + 1
        case "7":
            seven[0]    = seven[0]   + 1
        case "8":
            eight[0]    = eight[0]   + 1
        case "9":
            nine[0]     = nine[0]    + 1

def compare():
    global comparator
    global comparison_counter

    if comparator == ">":
        give_point(val_1)
    else:
        give_point(val_2)
    
    comparison_counter += 1
    reset_compares()

def checksum_list_to_number(checksum_list):
    return_number = []                          # return_number = [one[X,1], two[X,2], three[X,3] etc.]
    for number in checksum_list:
        return_number.append(number[1])
                                                # return_number = [1, 4, 5, 2, 3]
    return_number = ''.join(return_number)      # return_number = "14523"
    return_number = int(return_number)          # return_number = 14523
    return return_number


def group_complete():
    global checksum_total
    global comparison_counter
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    
    # --- How I plan to tackle this task ---
    # On read of comparison > Save to list current_group
    # On group complete > Find two numbers in checksum list with same value
    # select top 2 numbers in checksum_list > 
    #   look through current_group for those two comparing against each other >
    #   give point to winner of that comparison

    # find checksum number
    checksum_list = [one, two, three, four, five, six, seven, eight, nine]
    checksum_list = sorted(checksum_list, key=itemgetter(0), reverse = True)
    # After checksum_list is sorted
    # Check top 2 (always have the same points)
    # Award bonus point to the stronger one
    # Then re-sort in case checksum_list[1] > checksum_List[0]
    give_bonus_point(checksum_list[0][1], checksum_list[1][1])
    checksum_list = sorted(checksum_list, key=itemgetter(0), reverse = True)


    
    # extract
    checksum_number = checksum_list_to_number(checksum_list)
    
    # add it to total
    checksum_total += checksum_number
    
    # resetting for good measure
    comparison_counter = 0
    reset_wins()

def parse_character(character):
    global val_1
    global val_2
    global comparator
    global valid_char_in_row

    valid_characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ">", "<"]

    if character in valid_characters:
        match valid_char_in_row:
            case 0:
                val_1 = character
            case 1:
                comparator = character
            case 2:
                val_2 = character
        valid_char_in_row += 1
    else:
        valid_char_in_row = 0



if __name__ == '__main__':
    my_notes = read_input()

    # [0] = Wins (variable)
    # [1] = numerical value (do not change, please)
    one     = [0, "1"]
    two     = [0, "2"]
    three   = [0, "3"]
    four    = [0, "4"]
    five    = [0, "5"]
    six     = [0, "6"]
    seven   = [0, "7"]
    eight   = [0, "8"]
    nine    = [0, "9"]

    valid_char_in_row   = 0
    comparison_counter  = 0
    checksum_total      = 0
    comparator          = ""
    val_1               = ""
    val_2               = ""
    current_row         = []

    test_i = 0

    for character in my_notes:

        if valid_char_in_row < 3:
            parse_character(character)

        if valid_char_in_row == 3:
            add_current_comparison_to_list()
            compare()
        
        if (comparison_counter > 34): # had to manually count that out. Definitely a better way to do it. But it worked, so whatever.
            test_i += 1
            group_complete()

    
    print(checksum_total)