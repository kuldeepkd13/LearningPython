import json
import os


class Snack:
    def __init__(self, snackId, snackName, snackPrice, snackAvailability):
        self.snackId = snackId
        self.snackName = snackName
        self.snackPrice = snackPrice
        self.snackAvailability = snackAvailability


def read_inventory(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    else:
        return []


def write_inventory(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def removeItem(data, itemId):
    for item in data:
        if (item["snackId"] == itemId):
            data.remove(item)
    return data

def orderItem(data,itemId):
    item1 =""
    for item in data:
        if(item["snackId"]==itemId):
            item1=item
    return item1


def UpdateItem(data, itemId):
    for item in data:
        if (item["snackId"] == itemId):
            if (item["snackAvailability"] == "yes"):
                item["snackAvailability"] = "no"
            else:
                item["snackAvailability"] = "yes"
    return data


def main():
    print("---------------------------------")
    print("Welcome to Mumbai Munchies")
    current_directory = os.path.dirname(os.path.abspath(__file__))
    inventory_filename = os.path.join(current_directory, "inventory.db.json")
    sold_filename = os.path.join(current_directory,"sold.db.json")
    while True:
        print("1: Display Menu")
        print("2: Add Item")
        print("3: Remove Item")
        print("4: Updated Item")
        print("5: Order a item")
        print("6: Snack Sold")
        print("7: Exit")
        print("---------------------------------")

        user_input = input("Enter the Number: ")

        if user_input == "1":
            inventory = read_inventory(inventory_filename)
            if (len(inventory) == 0):
                print("No Menu Data")
                print("---------------------------------")
            else:
                for snack in inventory:
                    print("---------------------------------")
                    print(f"Snack id :- {snack['snackId']}")
                    print(f"snackName:- {snack['snackName']} ")
                    print(f"snackPrice:- {snack['snackPrice']}")
                    print(f"snackAvailability:-{snack['snackAvailability']} ")
                    print("---------------------------------")

        elif user_input == "2":
            snackId = input("Enter the Snack ID: ")
            snackName = input("Enter the Snack Name: ")
            snackPrice = float(input("Enter the Snack Price: "))
            snackAvailability = (input("Enter the Snack Availability: "))

            snack = Snack(snackId, snackName, snackPrice, snackAvailability)
            inventory = read_inventory(inventory_filename)
            inventory.append(snack.__dict__)
            write_inventory(inventory, inventory_filename)
            print("Snack added to inventory.")
            print("---------------------------------")
        elif user_input == "3":
            inventory = read_inventory(inventory_filename)
            if (len(inventory) == 0):
                print("No item in Menu")
                print("---------------------------------")
            else:
                snackId = input("Enter the Snack ID: ")
                remove = removeItem(inventory, snackId)
                write_inventory(remove, inventory_filename)
            print("Snack Removed from inventory.")
            print("---------------------------------")
        elif user_input == "4":
            inventory = read_inventory(inventory_filename)
            if (len(inventory) == 0):
                print("No item in Menu")
                print("---------------------------------")
            else:
                snackId = input("Enter the Snack ID: ")
                updated = UpdateItem(inventory, snackId)
                write_inventory(updated, inventory_filename)
            print("Snack Updated from inventory.")
            print("---------------------------------")
        elif user_input =="5":
            inventory = read_inventory(inventory_filename)
            snackId = input("Enter the Snack ID: ")
            name = input("Enter Your Name:-")
            order = orderItem(inventory,snackId)
            if(order['snackAvailability']=="no"):
                print("Item is not Avilable for Order")
                print("---------------------------------")
            else:
                soldinventory = read_inventory(sold_filename)
                item={}
                item["OrderID"]=order['snackId']
                item["Name"]=name
                item["snackName"]=order['snackName']
                item['Price']=order['snackPrice']
                soldinventory.append(item)
                write_inventory(soldinventory, sold_filename)
                print("Order is Placed")
                print("---------------------------------")
        elif user_input =="6":
            inventory = read_inventory(sold_filename)
            if (len(inventory) == 0):
                print("No SoldData")
                print("---------------------------------")
            else:
                for snack in inventory:
                    print("---------------------------------")
                    print(f"Order id :- {snack['OrderID']}")
                    print(f"Person Name:- {snack['Name']} ")
                    print(f"Item Order:- {snack['snackName']}")
                    print(f"Item Price:-{snack['Price']} ")
                    print("---------------------------------")
 
        elif user_input == "7":
            print("Goodbye!")
            print("---------------------------------")
            break
        else:
            print("Please! Enter a valid Number")
            print("---------------------------------")

if __name__ == "__main__":
    main()
