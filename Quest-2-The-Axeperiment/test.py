class Alloy:
    def __init__(self, alloy_number: str):
        self.alloy_number       : str           = alloy_number

    def set_alloy(self, str: str):
        self.alloy_number = str
    def get_alloy(self) -> str:
        return self.alloy_number
        

def test_function(alloy: Alloy):
    alloy.set_alloy("420")

all_battle_rows = [["1", "2"]]

for row in all_battle_rows:
        one     : Alloy      = Alloy(alloy_number="1")

        for char in row:
            test_function(one)
        
        print(one.get_alloy())