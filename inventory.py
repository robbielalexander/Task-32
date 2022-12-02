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

new_shoes = Shoes("UK", "3422", "Airmax", 34.99, 40)

print(new_shoes)

new_shoes.update_quantity(40)
new_shoes.update_cost(59.99)

print(new_shoes)
