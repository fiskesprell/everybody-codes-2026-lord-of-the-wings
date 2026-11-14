class Alloy:
    def __init__(self, alloy_number: str):
        self.alloy_number       : str           = alloy_number
        self.im_smaller_than    : list[str]     = []
        self.im_larger_than     : list[str]     = []
    
    def is_unused(self) -> bool:
        return ((0 == len(self.im_larger_than)) and (0 == len(self.im_smaller_than)))

    def get_alloy_number(self) -> str:
        return self.alloy_number

    def set_alloy(self, str: str):
        self.alloy_number = str
    
    def get_alloy(self) -> str:
        return self.alloy_number

    def append_larger(self, number: str) -> None:
        self.im_larger_than.append(number)
    
    def append_smaller(self, number: str) -> None:
        self.im_smaller_than.append(number)
    
    def reset(self) -> None:
        self.im_smaller_than = []
        self.im_larger_than  = []


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

    active_alloys: list[Alloy] = [one, two, three, four, five, six, seven, eight, nine]

    # Remove unused alloys
    for alloy in active_alloys:
        print(f"I am {alloy.get_alloy_number()}")
        print(f"-> I am unused: {alloy.is_unused()}")
        if alloy.is_unused():
            print(f"BEFORE: active_alloys - {active_alloys}")
            active_alloys.remove(alloy)
            print(f"AFTER: active_alloys - {active_alloys}")
    
    # Testing
    active_alloys_as_string: list[str] = []
    for alloy in active_alloys:
        active_alloys_as_string.append(alloy.get_alloy_number())

    print(active_alloys_as_string)
    return 1 #TODO: change



# populate 1-4, leave out others.
one     : Alloy      = Alloy(alloy_number="1")
two     : Alloy      = Alloy(alloy_number="2")
three   : Alloy      = Alloy(alloy_number="3")
four    : Alloy      = Alloy(alloy_number="4")
five    : Alloy      = Alloy(alloy_number="5")
six     : Alloy      = Alloy(alloy_number="6")
seven   : Alloy      = Alloy(alloy_number="7")
eight   : Alloy      = Alloy(alloy_number="8")
nine    : Alloy      = Alloy(alloy_number="9")

one.append_larger("1")
two.append_larger("1")
three.append_larger("1")
four.append_larger("1")

int_list = (kahns_algorithm(one, two, three, four, five, six, seven, eight, nine))

## +------- Earlier Tests ---------+
'''
    test_alloy = Alloy("1")

    print(f"""--- Test 1 ---
        - All lists Empty
        - Expected: False
        - Real    : {test_alloy.is_used()}
        """)

    test_alloy.append_smaller("3")

    print(f"""--- Test 2 ---
        - Smaller full, bigger empty
        - Expected: True
        - Real    : {test_alloy.is_used()}
        """)
    test_alloy.reset()
    test_alloy.append_larger("3")

    print(f"""--- Test 3 ---
        - Bigger full, smaller empty
        - Expected: True
        - Real    : {test_alloy.is_used()}
        """)
    test_alloy.reset()

    test_alloy.append_smaller("3")
    test_alloy.append_larger("3")

    print(f"""--- Test 4 ---
        - All lists Full
        - Expected: True
        - Real    : {test_alloy.is_used()}
        """)

'''

"""
2>4 3>6 1<9 3<1 1>2 6<4 9>5 6>8 7>2 5>7 4<7 6<5 5<3 2>8 7<3 2<9
6>3 1<8 6<1 1>3 7>1 2>9 6<7 6<4 9>7 6<8 7>4 4>8 5>7 3<7 7>8 5>2 2>7
"""
"""
    9 > 1 > 3 > 5 > 7 > 2 > 4 > 6 > 8
"""