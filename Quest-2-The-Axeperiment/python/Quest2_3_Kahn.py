# ---------------+ Classes +----------------+ Classes +----------------- #

class Alloy:
    def __init__(self, alloy_number: str):
        self.alloy_number       : str           = alloy_number
        self.im_smaller_than    : list[str]     = []
        self.im_larger_than     : list[str]     = []
        self.position_correct   : bool          = False
    
    def append_im_smaller_than(self, number_as_string: str) -> None:
        self.im_smaller_than.append(number_as_string)
    
    def append_im_larger_than(self, number_as_string: str) -> None:
        self.im_larger_than.append(number_as_string)

    # just use this for both of them?
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

# Holy moly. This is the definition of overcomplicating things.
class Character_parser:
    def __init__(self) -> None:
        self.first_number       : str   = ""
        self.comparator         : str   = ""
        self.second_number      : str   = ""
        self.new_line_spotted   : bool  = False
        self.is_fully_populated : bool  = False
    
    def reset_values(self) -> None:
        self.first_number       : str   = ""
        self.comparator         : str   = ""
        self.second_number      : str   = ""
        self.new_line_spotted   : bool  = False
        self.is_fully_populated : bool  = False
    
    def set_first_number(self, number: str) -> None:
        self.first_number = number
    
    def set_comparator(self, comparator: str) -> None:
        self.comparator = comparator
    
    def set_second_number(self, number: str) -> None:
        self.second_number = number

    def set_new_line(self, bool: bool) -> None:
        self.new_line_spotted = bool

    def set_is_fully_populated(self, bool: bool) -> None:
        self.is_fully_populated = bool

    def get_first_number(self) -> str:
        return self.first_number
    
    def get_comparator(self) -> str:
        return self.comparator
    
    def get_second_number(self) -> str:
        return self.second_number
    
    def get_new_line_spotted(self) -> bool:
        return self.new_line_spotted
    
    def get_is_fully_populated(self) -> bool:
        return self.is_fully_populated

    def parse(self, character: str) -> None:


        match character:
            case ">" | "<":
                self.set_comparator(comparator=character)
            case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                if "" == (self.get_first_number()):
                    self.set_first_number(number=character)
                elif "" == (self.get_second_number()):
                    self.set_second_number(number=character)
                    self.set_is_fully_populated(True)
                else:
                    print(f"""Error: Character_parser > parse() > else - something went wrong here.
                            character     - '{character}', 
                            first_number  - '{self.get_first_number()}' 
                            comparator    - '{self.get_comparator()}'
                            second_number - '{self.get_second_number()}'
                           """)
            case "\n":
                self.set_new_line(bool=True)
            case _:
                print(f"Error: Character_parser > parse() > case _: - unknown value '{character}'")
    


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

def check_for_new_line(current_char: str, current_battle_row: list[str]) -> bool:
    # Checks for VALID new line.
    if ("\n" == char) and (3 < len(current_battle_row)):
        return True
    else:
        return False

""" TODO: Implement at end
def sort_row_topologically_return_order_as_int(battle_row) -> int:
    one     : Alloy      = Alloy(alloy_number="1")
    two     : Alloy      = Alloy(alloy_number="2")
    three   : Alloy      = Alloy(alloy_number="3")
    four    : Alloy      = Alloy(alloy_number="4")
    five    : Alloy      = Alloy(alloy_number="5")
    six     : Alloy      = Alloy(alloy_number="6")
    seven   : Alloy      = Alloy(alloy_number="7")
    eight   : Alloy      = Alloy(alloy_number="8")
    nine    : Alloy      = Alloy(alloy_number="9")
"""
# ---------------+ Main +-----------------------+ Main +---------------- #

if __name__ == "__main__":
    
    input = return_test_input()
    parser                 : Character_parser   = Character_parser()
    accepted_characters    : list[str]          = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ">", "<", "\n"]
    current_battle_row     : list[str]          = []
    all_battle_rows        : list[list[str]]    = [] # should only contain current_battle_rows
    all_checksums          : list[int]          = [] # should look like: [123456789, 912345678, 987654321]


    # Populate all_battle_rows
    for char in input:
        
        # chars that aren't in accepted list are not worth processing. Go to next one immediately.
        if char not in accepted_characters:
            continue


        # Add current_battle_row to all_battle_rows
        # Clear current_battle_row
        # Clear new_line_spotted
        # Clear parser
        #
        # NOTE:
        #   This is going to run AFTER a new line has been spotted. "6>4'\n'3>9"
        #                                                   You are here ---^
        #       Meaning: char == 3 AFTER new_line_spotted == True.
        #             -> This loop will now do TWO things:
        #             -> 1) Transfer current_battle_row => all_battle_rows
        #             -> 2) parse the next number AS A START OF THE NEW current_battle_row
        #       ERGO: !!DO NOT!! use continue here
        if (parser.get_new_line_spotted()):
            all_battle_rows.append(current_battle_row)
            current_battle_row = []
            parser.reset_values()
        
        if (parser.get_is_fully_populated()):
            battle = ""
            battle += parser.get_first_number()
            battle += parser.get_comparator()
            battle += parser.get_second_number()

            current_battle_row.append(battle)
            parser.reset_values()
            continue
        
        parser.parse(character=char)
        
        # Might not be needed. If it's needed add "and (3 < len(current_battle_row))" to the get_is_fully_populated() if statement.
        """
        if "\n" != char:
            parser.set_new_line(bool=False)
        """
    print(all_battle_rows)
    
    """
    for row in all_battle_rows:
        # Implement Kahn's algorithm
    """

