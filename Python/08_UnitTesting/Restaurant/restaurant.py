class Table:
    def __init__(self, number_of_people):
        self.number_of_people = number_of_people
        self.bill = []

    def order(self, item, price, quantity=1):
        self.bill.append({
            'item': item,
            'price': price,
            'quantity': quantity})        

    def remove(self, item, price, quantity=1):
        for item_dict in self.bill:
            if item_dict['item'] == item and item_dict['price'] == price:
                if item_dict['quantity'] > quantity:
                    item_dict['quantity'] -= quantity
                elif item_dict['quantity'] == quantity:
                    self.bill.remove(item_dict)
                return True
        return False        

    def get_subtotal(self):
        subtotal = 0
        for item_dict in self.bill:
            subtotal += item_dict['price'] * item_dict['quantity']
        return round(subtotal, 2)        

    def get_total(self, service_charge_rate):
        subtotal = self.get_subtotal()
        service_charge = round(subtotal * service_charge_rate, 2)
        total = subtotal + service_charge
        return {
        'Sub Total': f'£{subtotal:.2f}',
        'Service Charge': f'£{service_charge:.2f}',
        'Total': f'£{total:.2f}'}  

    def split_bill(self):
        subtotal = self.get_subtotal()
        split_amount = round(subtotal / self.number_of_people, 2)
        return split_amount