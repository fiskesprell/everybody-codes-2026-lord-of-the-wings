from operator import itemgetter    

def read_input():
    with open("my_notes.txt", "r") as file:
        return(file.read())

def reset_wins():
    global one
    global two
    global three
    global four
    global five

    one[0]      = 0
    two[0]      = 0
    three[0]    = 0
    four[0]     = 0
    five[0]     = 0

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

    # find checksum number
    checksum_list = [one, two, three, four, five]
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

    valid_characters = ["1", "2", "3", "4", "5", ">", "<"]

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

    valid_char_in_row   = 0
    comparison_counter  = 0
    checksum_total      = 0
    comparator          = ""
    val_1               = ""
    val_2               = ""

    for character in my_notes:

        if valid_char_in_row < 3:
            parse_character(character)

        if valid_char_in_row == 3:
            compare()
        
        if (comparison_counter > 9):
            group_complete()
    
    print(checksum_total)