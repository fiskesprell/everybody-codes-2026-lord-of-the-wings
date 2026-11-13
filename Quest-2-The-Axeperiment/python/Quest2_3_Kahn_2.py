# ---------------+ Classes +----------------+ Classes +----------------- #

class Alloy:
    def __init__(self, alloy_number: str):
        self.alloy_number       : str           = alloy_number
        self.im_smaller_than    : list[str]     = []
        self.im_larger_than     : list[str]     = []
    
    def get_im_smaller_than(self) -> list[str]:
        return self.im_smaller_than
    
    def get_im_larger_than(self) -> list[str]:
        return self.im_larger_than 

    def reset_values(self) -> None:
        self.im_smaller_than    = []
        self.im_larger_than     = []
    
    def parse_battle(self, battle: str):
        # Battle must be in string format like: "1>2"
        im_on_the_right : bool  = False

        # Check whether current alloy is on left or right
        if (battle[0] == self.alloy_number):
            im_on_the_right = False
        elif (battle[2] == self.alloy_number):
            im_on_the_right = True
        else:
            print("Error #1 - battle wrong format or number not in battle")
            print(f"""
                    Battle          = {battle}
                    Alloy_number    = {self.alloy_number}
                    """)
        
        match im_on_the_right:
            case True:
                if battle[1] == "<":
                    self.im_larger_than.append(battle[0])
                elif battle[1] == ">":
                    self.im_smaller_than.append(battle[0])
                else:
                    print("Error #2 - in Alloy > parse_battle > match im_on_the_right > case TRUE")
                    print(f"""
                    Battle          = {battle}
                    Alloy_number    = {self.alloy_number}
                    """)

            case False:
                if battle[1] == ">":
                    self.im_larger_than.append(battle[2])
                elif battle[1] == "<":
                    self.im_smaller_than.append(battle[2])
                else:
                    print("Error #3 - in Alloy > parse_battle > match im_on_the_right > case FALSE")
                    print(f"""
                    Battle          = {battle}
                    Alloy_number    = {self.alloy_number}
                    """)




# ---------------+ Functions +----------------+ Functions +------------- #

def return_input():
    with open("my_notes_p3.txt", "r") as file:
        return(file.read())

def return_test_input():
    return """3>1 1>2 1<5 4<2 3>5
    2>1 2<5 3>1 4>3 2<4 5<3
    5>1 3<4 1>2 3>5
    """
    # Correct checksums:
    #   35124
    #   43521
    #   43512

def assign_values(
        battle  : str,  # looks like "4>2"
        one     : Alloy,
        two     : Alloy,
        three   : Alloy,
        four    : Alloy,
        five    : Alloy,
        six     : Alloy,
        seven   : Alloy,
        eight   : Alloy,
        nine    : Alloy
    ) -> None:

    if battle[0] == "1":
        one.parse_battle(battle)
    elif battle[0] == "2":
        two.parse_battle(battle)
    elif battle[0] == "3":
        three.parse_battle(battle)
    elif battle[0] == "4":
        four.parse_battle(battle)
    elif battle[0] == "5":
        five.parse_battle(battle)
    elif battle[0] == "6":
        six.parse_battle(battle)
    elif battle[0] == "7":
        seven.parse_battle(battle)
    elif battle[0] == "8":
        eight.parse_battle(battle)
    elif battle[0] == "9":
        nine.parse_battle(battle)
    else:
        print(f"Error in assign_values - (unknown value) battle[0] = {battle[0]} <- 何これ？")

    if battle[2] == "1":
        one.parse_battle(battle)
    elif battle[2] == "2":
        two.parse_battle(battle)
    elif battle[2] == "3":
        three.parse_battle(battle)
    elif battle[2] == "4":
        four.parse_battle(battle)
    elif battle[2] == "5":
        five.parse_battle(battle)
    elif battle[2] == "6":
        six.parse_battle(battle)
    elif battle[2] == "7":
        seven.parse_battle(battle)
    elif battle[2] == "8":
        eight.parse_battle(battle)
    elif battle[2] == "9":
        nine.parse_battle(battle)
    else:
        print(f"Error in assign_values - (unknown value) battle[2] = {battle[2]} <- 何これ？")


""" TODO: Implement at end
def kahns_algorithm( 
        one     : Alloy,
        two     : Alloy,
        three   : Alloy,
        four    : Alloy,
        five    : Alloy,
        six     : Alloy,
        seven   : Alloy,
        eight   : Alloy,
        nine    : Alloy
    ) -> int:


    # Remember to reset all Alloys at end
    reset_all_alloys()

    return topological_order
"""

def reset_all_alloys(
        one     : Alloy,
        two     : Alloy,
        three   : Alloy,
        four    : Alloy,
        five    : Alloy,
        six     : Alloy,
        seven   : Alloy,
        eight   : Alloy,
        nine    : Alloy
    ) -> None:
    one.reset_values()
    two.reset_values()
    three.reset_values()
    four.reset_values()
    five.reset_values()
    six.reset_values()
    seven.reset_values()
    eight.reset_values()
    nine.reset_values()

# ---------------+ Main +-----------------------+ Main +---------------- #

if __name__ == "__main__":
    
    input = return_input()
    accepted_characters    : list[str]          = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ">", "<", "\n"]
    current_battle_row     : str                = ""
    all_battle_rows        : list[str]          = [] # should only contain current_battle_rows
    all_checksums          : list[int]          = [] # should look like: [123456789, 912345678, 987654321]

    # TODO: Delete this and any mention of it
    round_number = 0
    # Populate all_battle_rows
    for char in input:
        if char not in accepted_characters:
            continue

        if "\n" != char:
            current_battle_row += (char)
        else:
            all_battle_rows.append(current_battle_row)
            print(current_battle_row)
            current_battle_row = ""
            round_number += 1
        if round_number == 2:
            break

    round_number = 1
    for row in all_battle_rows:
        one     : Alloy      = Alloy(alloy_number="1")
        two     : Alloy      = Alloy(alloy_number="2")
        three   : Alloy      = Alloy(alloy_number="3")
        four    : Alloy      = Alloy(alloy_number="4")
        five    : Alloy      = Alloy(alloy_number="5")
        six     : Alloy      = Alloy(alloy_number="6")
        seven   : Alloy      = Alloy(alloy_number="7")
        eight   : Alloy      = Alloy(alloy_number="8")
        nine    : Alloy      = Alloy(alloy_number="9")

        current_battle : str = ""
        i = 0
        for char in row:
            if 3 == i:
                assign_values(current_battle, one, two, three, four, five, six, seven, eight, nine)
                current_battle = ""
                i = 0
            
            current_battle += char
            i += 1
        
        print(f"""
            +------+-----+ ROUND {round_number} OVER +----+-----+
            |   Stats:
            |       - one
            |           larger_than  : {one.get_im_larger_than()}
            |           smaller_than : {one.get_im_smaller_than()}
            |       - two
            |           larger_than  : {two.get_im_larger_than()}
            |           smaller_than : {two.get_im_smaller_than()}
            |       - three
            |           larger_than  : {three.get_im_larger_than()}
            |           smaller_than : {three.get_im_smaller_than()}
            |       - four
            |           larger_than  : {four.get_im_larger_than()}
            |           smaller_than : {four.get_im_smaller_than()}
            |       - five
            |           larger_than  : {five.get_im_larger_than()}
            |           smaller_than : {five.get_im_smaller_than()}
            |       - six
            |           larger_than  : {six.get_im_larger_than()}
            |           smaller_than : {six.get_im_smaller_than()}
            |       - seven
            |           larger_than  : {seven.get_im_larger_than()}
            |           smaller_than : {seven.get_im_smaller_than()}
            |       - eight                         
            |           larger_than  : {eight.get_im_larger_than()}
            |           smaller_than : {eight.get_im_smaller_than()}
            |       - nine
            |           larger_than  : {nine.get_im_larger_than()}
            |           smaller_than : {nine.get_im_smaller_than()}
            +------------+--------------+-----------+--------------+
        
            """)
        round_number += 1
        if round_number > 3:
            break
        
        """
        all_checksums = kahns_algorithm(one, two, three, four, five, six, seven, eight, nine) #TODO: Implement
        """
    print(all_checksums)




""" TODO TOMORROW:
    - Make kahns_algorithm transform the Alloys (nodes) into the correct order
    - transform that order (of strings) into a number (int)
    - append that number to all_checksums
    - calculate all_cheksums (just iterate it)
        -> print the final number 
"""