# This is a capstone project, intended to show off my knowledge of classes 

class Shoes():

    def __init__(self, country: str, 
                        code: str, 
                        product: str, 
                        cost: float, 
                        quantity: int):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def __str__(self) -> str:
        return f"""The shoe {self.product} is from {self.country} with 
        code {self.code} costs £{self.cost} and there are {self.quantity}
        in stock."""

    def get_cost(self) -> float:
        """This function returns the cost of the shoes"""
        return self.cost

    def get_quantity(self) -> int:
        """This function returns the quantity of the shoes"""
        return self.quantity

    def update_cost(self, new_price: float) -> None:
        """This function updates the price of the shoes"""
        self.cost = new_price

    def update_quantity(self, quantity_change: int) -> None:
        """This function is used to update the stock level"""
        # I don't want the quantity to be negative, so this check 
        # has been put in place to have a lower limit of 0. 
        if self.quantity + quantity_change < 0:
            self.quantity = 0
        else:
            self.quantity += quantity_change


def read_shoes_data() -> list:
    """This function reads the inventory file and adds all the data 
    to a list as Shoe objects."""
    # initialise an empty list 
    shoes_list = []
    # read the file 
    with open("./Task 32/inventory.txt", 'r') as shoe_file:
        for line in shoe_file:
            country, code, product, cost, quantity = interpret_inventory_file_line(line)
            shoes_list.append(Shoes(country, code, product, cost, quantity))
    return shoes_list

def interpret_inventory_file_line(input_line: str) -> list:
    """This is used to change """
    line = input_line.replace("\n", "").split(",")
    print(line)
    return [item for item in line]

def capture_shoes():
    pass

def view_all():
    pass

def restock_shoe():
    pass

def search_shoe():
    pass

def value_per_item():
    pass

def highest_quantity():
    pass 

def menu(shoes_list: list) -> None:
    """This is the main menu for the program"""
    while True:
        menu_options()
        user_selection = input()
        menu_divider()
        if "1" in user_selection:
            capture_shoes()
        elif "2" in user_selection:
            view_all()
        elif "3" in user_selection:
            restock_shoe()
        elif "4" in user_selection:
            search_shoe()
        elif "5" in user_selection:
            value_per_item()
        elif "6" in user_selection:
            highest_quantity()
        elif "7" in user_selection:
            exit()
        else:
            menu_divider()
            print("I have not understood your selection. Please try again")
            menu_divider()
        
def menu_options():
    """This displays the menu options the user can choose."""
    print("Please select from the following options:")
    print("1 - add new shoe;")
    print("2 - view all shoe information;")
    print("3 - restock shoes;")
    print("4 - search for shoe;")
    print("5 - show inventory value;")
    print("6 - show shoe with highest quantity;")
    print("7 - quit program.")

def menu_divider():
    print("-" * 60)

def main():
    """This is the main program that runs."""
    # in the first place create the empty shoe list 
    shoes_list = read_shoes_data()
    # Then I will read the inventory text file and populate this 
    # empty list 

    # Then I will show the menu, through which the user can 
    # select what they want to do. 
    menu(shoes_list)







main()