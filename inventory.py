# This is a capstone project, intended to show off my knowledge of classes 

class Shoes():

    def __init__(self, country: str, 
                        code: str, 
                        product: str, 
                        cost: int, 
                        quantity: int):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def __str__(self) -> str:
        return f"""The shoe {self.product} is from {self.country} with 
        code {self.code} costs R{self.cost} and there are {self.quantity}
        in stock."""

    def get_cost(self) -> int:
        """This function returns the cost of the shoes"""
        return self.cost

    def get_quantity(self) -> int:
        """This function returns the quantity of the shoes"""
        return self.quantity

    def update_cost(self, new_price: int) -> None:
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
    try:
        with open("./Task 32/inventory.txt", 'r') as shoe_file:
            for line in shoe_file:
                country, code, product, cost, quantity = interpret_inventory_file_line(line)
                shoes_list.append(Shoes(country, code, product, cost, quantity))
    # Since the header is included in this list, when I return the shoes list, 
    # I will not include the header. 
        return shoes_list[1:]
    except:
        # if the file isn't found, just return an empty list
        print("No inventory data found.")
        return shoes_list

def interpret_inventory_file_line(input_line: str) -> tuple:
    """This is used to change the input line from the file 
    into a useful form to be put into the shoe object."""
    line = input_line.replace("\n", "").split(",")
    country = line[0]
    code = line[1]
    product = line[2]
    cost = int(line[3]) if line[3].isdigit() else line[3]
    quantity = int(line[4]) if line[4].isdigit() else line[4]
    return country, code, product, cost, quantity

def capture_shoes(shoe_list: list) -> list:
    """This lets a user add information about a shoe to the shoe list"""
    print("With this option you can add shoe information to the shoe list")
    while True: 
        country = input("Enter the country the shoes are from: ")
        code = input("Enter the code for the shoes: ")
        product = input("Enter the product name: ")
        cost = int_check("Enter the cost of the product: ")
        quantity = int_check("Enter the quantity of the product: ")
        new_shoe = Shoes(country, code, product, cost, quantity)
        print(new_shoe)
        menu_divider()
        print("Is the above information correct? (y/n)")
        user_choice = input().lower()
        if user_choice in ["y", "yes"]:
            print("The information has been added to the database.")
            break
    # Add the new shoe information to the list. 
    shoe_list.append(new_shoe) 
    return shoe_list

def int_check(message: str) -> int:
    """This function is used to ensure the user enters an int"""
    while True:
        input_number = input(message)
        try:
            input_number = int(input_number)
            return input_number
        except ValueError:
            print("The input has not been recognised as a number, try again.")

def view_all(shoes_list: list) -> None:
    """This prints out all the shoe information"""
    for shoe in shoes_list:
        print(shoe)
        menu_divider()

def restock_shoe(shoes_list: list) -> list:
    """This functino finds the shoes which have the lowest stock and then 
    allows the user to update with the amount of stock they want to add"""
    min_quantity = 10000
    index_of_min_quantity = 0
    for index, shoe in enumerate(shoes_list):
        if shoe.quantity < min_quantity:
            min_quantity = shoe.quantity
            index_of_min_quantity = index
    low_stock_shoe = shoes_list[index_of_min_quantity]
    print(f"""{low_stock_shoe.product} is low on stock and there are only 
    {low_stock_shoe.quantity} pairs left.""")
    menu_divider()
    # ask the user if they want to restock the shoe.
    while True:
        user_choice = input("Do you want to restock this shoe? (y/n)")
        if user_choice in ["y", "yes"]:
            restock_amount = int_check("How many do you want to order? ")
            shoes_list[index_of_min_quantity].update_quantity(restock_amount)
            break
        elif user_choice in ["n", "no"]:
            break
        else:
            print("I didn't understand your choice.")
    menu_divider()
    return shoes_list
    

def search_shoe(shoes_list: list) -> None:
    """This function searches the shoe list for a shoe based 
    on the input code and then prints out the information for 
    the user."""
    shoe_found = False
    while True:
        shoe_code = input("Enter the product code: ")
        for shoe in shoes_list:
            if shoe.code == shoe_code:
                # if the shoe is found print it out.
                menu_divider()
                print(shoe)
                menu_divider()
                shoe_found = True
                break 
        # if the shoe was found or not, present the user with the options.
        if shoe_found:
            print("Do you want to search for another shoe? (y/n)")
        else:
            print("No shoe found. Do you want to try again? (y/n)")
        # based on the user choice, let them search for another shoe or 
        # go back to the main menu.
        user_choice = input().lower()
        if user_choice not in ["y", "yes"]:
            break

def value_per_item(shoes_list: list) -> None:
    """This prints the value for each product using the 
    formula cost * quantity"""
    for index, shoe in enumerate(shoes_list):
        value = shoe.cost * shoe.quantity
        print(f"{index + 1}: {shoe.product} has the value R{value}.")
        menu_divider()

def highest_quantity(shoes_list: list, percent_discount: float) -> list:
    """This function finds the shoe with the highest quantity and 
    then offers it for sale"""
    max_quantity = 0
    index_of_max_quantity = 0
    for index, shoe in enumerate(shoes_list):
        if shoe.quantity > max_quantity:
            max_quantity = shoe.quantity
            index_of_max_quantity = index
    # print out the shoe 
    sale_shoe = shoes_list[index_of_max_quantity]
    sale_shoe_price = int(sale_shoe.cost - (percent_discount * sale_shoe.cost))
    print(f"""{sale_shoe.product} ({sale_shoe.code}) is now for sale for R{sale_shoe_price}, 
    down from R{sale_shoe.cost}, a {percent_discount*100}% reduction.""")
    menu_divider()
    # update the shoe information in the list
    shoes_list[index_of_max_quantity].update_cost(sale_shoe_price)
    return shoes_list

def menu(shoes_list: list) -> None:
    """This is the main menu for the program"""
    while True:
        menu_options()
        user_selection = input()
        menu_divider()
        if "1" in user_selection:
            # let the user add a shoe to the list
            shoes_list = capture_shoes(shoes_list)
        elif "2" in user_selection:
            # display all the shoe information for the user
            view_all(shoes_list)
        elif "3" in user_selection:
            # This function allows a user to restock a shoe
            shoes_list = restock_shoe(shoes_list)
        elif "4" in user_selection:
            # Finds shoe information based on the shoe code
            search_shoe(shoes_list)
        elif "5" in user_selection:
            # returns the total value of the shoe in the database
            value_per_item(shoes_list)
        elif "6" in user_selection:
            # puts the shoe with the highest stock level on sale 
            # and reduces the price by the indicated percentage. 
            shoes_list = highest_quantity(shoes_list, 0.3)
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
    """This function adds a line of dashes to the terminal, to break 
    up display text. """
    print("-" * 60)

def inventory_program():
    """This is the main program that runs."""
    # When starting the program each time, I read the inventory file. 
    shoes_list = read_shoes_data()
    # Then I will show the menu, through which the user can 
    # select what they want to do. 
    menu(shoes_list)

inventory_program()
