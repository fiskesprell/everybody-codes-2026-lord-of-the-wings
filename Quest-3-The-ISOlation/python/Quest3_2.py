# +--------------+ FUNCTIONS +-------functions-------+ FUNCTIONS +--------------+

def return_votes() -> str:
    with open("p2_test_notes.txt", "r") as file:
        return file.read()

def extract_votes(votes_file: str) -> list[list[str]]:
    accepted_numbers    : list[str]         = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    ones_and_twos       : list[list[str]]   = []
    current_one_and_two : list[str]         = []
    
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

# TODO: Implement
def ISO_to_decimal(vote: list[str]) -> int:
    # Example iso: 'ISO-34 140856'

    
    return 1 


if __name__ == '__main__':
    votes_file              : str               = return_votes()
    seperated_iso_numbers   : list[list[str]]   = extract_votes(votes_file=votes_file)
    result_of_votes         : list[int]         = []

    for vote in seperated_iso_numbers:
        result_of_votes.append(ISO_to_decimal(vote))