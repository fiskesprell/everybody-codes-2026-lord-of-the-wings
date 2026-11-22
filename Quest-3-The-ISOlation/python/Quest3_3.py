# +--------------+ FUNCTIONS +-------functions-------+ FUNCTIONS +--------------+

from typing import Any


def return_votes() -> str:
    with open("p3_notes.txt", "r") as file:
        return file.read()

def extract_votes(votes_file: str) -> list[list[str]]:
    accepted_numbers    : list[str]         = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ones_and_twos       : list[list[str]]   = []    
    current_one         : str               = ""
    current_two         : str               = ""
    which_number        : int               = 1

    for char in votes_file:

        if "\n" == char:
            ones_and_twos.append([current_one, current_two])
            current_one = ""
            current_two = ""
            which_number = 1
        
        if ' ' == char:
            which_number = 2

        if char in accepted_numbers:
            match which_number:
                case 1:
                    current_one += char
                case 2:
                    current_two += char
    
    ones_and_twos.append([current_one, current_two])
                
    return ones_and_twos

def ISO_to_decimal(vote: list[str]) -> list[str | int]:
    # Example iso: 'ISO-34 140856'
    # list[0] ----------^^ ^^^^^^
    # list[1] ------------´´´´´´
    
    row_1   : str     = vote[0]
    row_2   : str     = vote[1]

    if (len(row_1) != len(row_2)):
        new_row_1   : str   = ""
        iterator    : int   = len(row_1) - 1
        while len(new_row_1) != len(row_2):
            new_row_1 += row_1[iterator]
            if (iterator == 0):
                iterator = (len(row_1) - 1)
            else:
                iterator -= 1
        row_1 = new_row_1[::-1]
    
    converted_fragment : list[int] = []
    for i in range(0, len(row_2)):
        converted_fragment.append((int(row_2[i]) * (int(row_1[i]) ** (len(row_2) - (i + 1)))))
    

    returnString: str = f"ISO2-{row_1} {row_2}"
    returnList: list[int | str] = [sum(converted_fragment), returnString]
    return returnList


if __name__ == '__main__':
    votes_file              : str               = return_votes()
    seperated_iso_numbers   : list[list[str]]   = extract_votes(votes_file=votes_file)
    result_of_votes         : dict[int, str]    = {}

    for vote in seperated_iso_numbers:
        potential_append = ISO_to_decimal(vote)
        pot_key: int = potential_append[0]
        pot_str: str = potential_append[1]

        if pot_key in result_of_votes:
            current_str = result_of_votes[pot_key]
            if len(current_str) > len(pot_str):
                result_of_votes.update({pot_key: pot_str})
        else:
            result_of_votes.update({pot_key: pot_str})
    
    total_value = 0
    for key in result_of_votes:
        total_value += key

    print(total_value)


# PLAN FOR PART 3:
# Look through input
# save each value in hashmap saved_values: { value: string }
# if two string with same value:
#   if len(string) in saved_values[value] is higher than len(new_string)
#       replace string in saved_values
#   else do_nothing
# 
# then for each in saved_values
#   total_value += value
#
#
# Honestly just CBA to do this today, sorry folks.