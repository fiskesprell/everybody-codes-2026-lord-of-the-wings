from typing import Any


def return_votes() -> str:
    with open("p2_test_notes.txt", "r") as file:
        return file.read()

def extract_votes(votes_file: str) -> list[str]:
    list_of_votes: list[str] = []
    current_vote: str = ""

    for char in votes_file:

        match char:
            case "\n":
                list_of_votes.append(current_vote)
                current_vote = ""
            case _:
                current_vote += char
    
    list_of_votes.append(current_vote)
    
    return list_of_votes

def ISO_to_decimal(vote: str) -> int:
    # Example iso: 'ISO-3210 7654'
    # one       =    3210
    # one_1     = ---^ ^
    # one_3     = -----'
    # two       =    7654
    # two_1     = ---^ ^
    # two_3     = -----'

    one_1: int = int(vote[4])
    one_2: int = int(vote[5])
    one_3: int = int(vote[6])
    one_4: int = int(vote[7])
    two_1: int = int(vote[9])
    two_2: int = int(vote[10])
    two_3: int = int(vote[11])
    two_4: int = int(vote[12])

    first_number    : int    = (two_1 * (one_1 ** 3)) 
    second_number   : int    = (two_2 * (one_2 ** 2)) 
    third_number    : int    = (two_3 * (one_3 ** 1)) 
    fourth_number   : int    = (two_4 * (one_4 ** 0))
    
    return first_number + second_number + third_number + fourth_number


if __name__ == '__main__':
    all_votes               : str           = return_votes()
    list_of_votes           : list[str]     = extract_votes(votes_file=all_votes)
    result_of_votes         : list[int]     = []

    for vote in list_of_votes:
        result_of_votes.append(ISO_to_decimal(vote))

    print(result_of_votes)
    print(sum(result_of_votes))