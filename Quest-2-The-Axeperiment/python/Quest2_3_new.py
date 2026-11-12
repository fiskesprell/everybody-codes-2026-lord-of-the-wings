# ---------------+ Classes +----------------+ Classes +----------------- #


class Alloy:
    def __init__(self, alloy_number: str):
        self.alloy_number       : str           = alloy_number
        self.im_smaller_than    : list[str]     = []
        self.im_larger_than     : list[str]     = []
        self.position_correct   : bool          = False

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
                    self.im_larger_than.append(battle[0])
                elif battle[1] == "<":
                    self.im_smaller_than.append(battle[0])
                else:
                    print("Error #3 - in Alloy > parse_battle > match im_on_the_right > case FALSE")
                    print(f"""
                    Battle          = {battle}
                    Alloy_number    = {self.alloy_number}
                    """)

class Battle_manager:
    def __init__(self)              -> None:
        self.accepted_characters    : list[str]     = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ">", "<", "\n"]
        self.current_battle_row     : list[str]     = []
        self.all_checksums          : list[str]     = [] # Should look like: ["12345", "54321"] TODO: Get total by iterating this list > convert to numbers
        self.current_checksum       : list[str]     = []
        self.current_char           : str           = ""
    
    def check_for_new_line(self.current_char) -> bool:
        # Checks for VALID new line.
        if ("\n" == char) and (3 < len(self.current_battle_row)):
            return True
        else:
            return False

    def parse_character(self):
        
        if char not in self.accepted_characters:
            continue
        
        if check_for_new_line(char):
            # close_battle_row()
            # Takes all battles in current_battle_row 
            # -> iterate them, stop when all alloys are in correct place inside current_checksum
            # -> convert current_checksum from string to number
            # -> add current_checksum to all_checksums 
            close_battle_row() 
        
        if 
        









# ---------------+ Functions +----------------+ Functions +------------- #

def return_input():
    with open("my_notes_p2.txt", "r") as file:
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

# ---------------+ Main +-----------------------+ Main +---------------- #

if __name__ == "__main__":
    
    input = return_test_input()
    battle_manager = Battle_manager()

    one     = Alloy("1")
    two     = Alloy("2")
    three   = Alloy("3")
    four    = Alloy("4")
    five    = Alloy("5")
    six     = Alloy("6")
    seven   = Alloy("7")
    eight   = Alloy("8")
    nine    = Alloy("9")


    for char in input:
        
        battle_manager.parse(char)


