class Items():

    def __init__(self, item_id: str, item_name: str, category_name: str, quantity: int) -> None:
        self.item_id = item_id
        self.item_name = item_name
        self.category_name = category_name
        self.quantity = quantity

    def __str__(self) -> str:
        return f"Item ID: {self.item_id}\n \
            Item Name: {self.item_name}\n \
                Category: {self.category_name}\n \
                    Quantity: {self.quantity}"