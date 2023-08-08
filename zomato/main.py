import json , os
# import datetime

# current_date = datetime.datetime.now().date()
# print(current_date)
# formatted_date = current_date.strftime("%B %d, %Y")
# print(formatted_date)
current_order_id = 1

class Dish:
    def __init__(self, dishId, dishName, dishPrice, dishAvailability):
        self.dishId = dishId
        self.dishName = dishName
        self.dishPrice = dishPrice
        self.dishAvailability = dishAvailability


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
        if (item["dishId"] == itemId):
            data.remove(item)
    return data

def orderItem(data,itemId):
    item1 =""
    for item in data:
        if(item["dishId"]==itemId):
            item1=item
    return item1

def findorderItem(data,itemId):
    item1 =""
    for item in data:
        if(item["OrderID"]==itemId):
            item1=item
    return item1
def UpdateItem(data, itemId):
    for item in data:
        if (item["dishId"] == itemId):
            if (item["dishAvailability"] == "yes"):
                item["dishAvailability"] = "no"
            else:
                item["dishAvailability"] = "yes"
    return data

def indexpresent(data,itemId):
    for item in data:
        if (item["dishId"] == itemId):
            return True
    return False

def Orderindexpresent(data,itemId):
    for item in data:
        if (item["OrderID"] == itemId):
            return True
    return False

def UpdateOrder(data, itemId,status):
    for item in data:
        if (item["OrderID"] == itemId):
            item["Status"] = status
    return data

def main():
    print("----------------------------------------")
    print("Welcome To Zesty Zomato")

    current_directory = os.path.dirname(os.path.abspath(__file__))
    inventory_filename = os.path.join(current_directory,"inventory.db.json")
    order_filename = os.path.join(current_directory,"order.db.json")
    
    while True:
        print("1: Display Menu")
        print("2: Add Dish")
        print("3: Remove Dish")
        print("4: Update Dish")
        print("5: Order Dish")
        print("6: Trace a Order By Id")
        print("7: Update the Order")
        print("8: details of All Order")
        print("9: Exit")
        print("------------------------")

        user_input = input("Please Enter a Number:--")

        # Display Menu
        if user_input == "1":
            inventory = read_inventory(inventory_filename)
            if (len(inventory) == 0):
                print("No Menu Data")
                print("---------------------------------")
            else:
                for dish in inventory:
                    print("---------------------------------")
                    print(f"dish id :- {dish['dishId']}")
                    print(f"dishName:- {dish['dishName']} ")
                    print(f"dishPrice:- {dish['dishPrice']}")
                    print(f"dishAvailability:-{dish['dishAvailability']} ")
                    print("---------------------------------")

        # Add Dish
        elif user_input == "2":
            dishId = input("Enter the dish ID: ")
            dishName = input("Enter the dish Name: ")
            dishPrice = float(input("Enter the dish Price: "))
            dishAvailability = (input("Enter the dish Availability: "))

            dish = Dish(dishId, dishName, dishPrice, dishAvailability)
            inventory = read_inventory(inventory_filename)
            inventory.append(dish.__dict__)
            write_inventory(inventory, inventory_filename)
            print("dish added to inventory.")
            print("---------------------------------")

        # Remove Dish
        elif user_input == "3":
            inventory = read_inventory(inventory_filename)
            if (len(inventory) == 0):
                print("No item in Menu")
                print("---------------------------------")
            else:
                dishId = input("Enter the dish ID: ")
                check = indexpresent(inventory,dishId)
                if(check):
                    remove = removeItem(inventory, dishId)
                    write_inventory(remove, inventory_filename)
                    print("dish Removed from inventory.")
                    print("---------------------------------")
                else:
                    print(f"No Dish With {dishId} is present in Inventory")
                    print("---------------------------------")

        # Update Dish
        elif user_input == "4":
            inventory = read_inventory(inventory_filename)
            if (len(inventory) == 0):
                print("No item in Menu")
                print("---------------------------------")
            else:
                dishId = input("Enter the dish ID: ")
                check = indexpresent(inventory,dishId)
                if(check):
                 updated = UpdateItem(inventory, dishId)
                 write_inventory(updated, inventory_filename)
                 print("dish Updated from inventory.")
                 print("---------------------------------")
                else:
                    print(f"No Dish With {dishId} is present in Inventory")
                    print("---------------------------------")
        
        # place a Order
        elif user_input =="5":
            global current_order_id
            inventory = read_inventory(inventory_filename)
            dishId = input("Enter the dish ID: ")
            check = indexpresent(inventory,dishId)
            if(check):
             name = input("Enter Your Name:-")
             order = orderItem(inventory,dishId)
             if(order['dishAvailability']=="no"):
                print("Item is not Avilable for Order")
                print("---------------------------------")
             else:
                quantity = float(input("Enter The Quantity:-"))
                soldinventory = read_inventory(order_filename)
                item={}
                item["OrderID"]=str(current_order_id)
                current_order_id+=1
                item["Name"]=name
                item["dishName"]=order['dishName']
                item['Price']=order['dishPrice']*quantity
                item['Status']="Preparing....."
                soldinventory.append(item)
                write_inventory(soldinventory, order_filename)
                print("Order is Placed And Your Food Is Preparing>...")
                print("---------------------------------")
            else:
                print(f"No Dish With {dishId} is present in Inventory")
                print("---------------------------------")
        elif user_input=="6":
            OrderId = input("Enter a OrderID:-")
            soldinventory = read_inventory(order_filename)
            check = Orderindexpresent(soldinventory,OrderId)
            if(check):
                item = findorderItem(soldinventory,OrderId)
                print("---------------------------------")
                print(f"OrderId :- {item['OrderID']}")
                print(f"Person Name :- {item['Name']}")
                print(f"Dish Name :- {item['dishName']} ")
                print(f"Price :- {item['Price']} ")
                print(f"Order Status :- {item['Status']}")
                print("-------------")
            else:
                print(f"No Order With {OrderId} is present")
                print("---------------------------------")
        elif user_input == "7":
            inventory = read_inventory(order_filename)
            if (len(inventory) == 0):
                print("No Order Is There!")
                print("---------------------------------")
            else:
                OrderId = input("Enter the Order ID: ")
                check = Orderindexpresent(inventory,OrderId)
                if(check):
                 status = input("Enter the Status Of Order:-")
                 print(status)
                 updated = UpdateOrder(inventory, OrderId,status)
                 write_inventory(updated, order_filename)
                 print("dish Updated from inventory.")
                 print("---------------------------------")
                else:
                    print(f"No Order With {OrderId} is present")
                    print("---------------------------------")
        elif user_input == "8":
            inventory = read_inventory(order_filename)
            if (len(inventory) == 0):
                print("No Order")
                print("---------------------------------")
            else:
                for dish in inventory:
                    print("---------------------------------")
                    print(f"Order id :- {dish['OrderID']}")
                    print(f"Name:- {dish['Name']} ")
                    print(f"Dish Name:- {dish['dishName']}")
                    print(f"Price:- {dish['Price']}")
                    print(f"Status:-{dish['Status']} ")
                    print("---------------------------------")
        elif user_input=="9":
            print("Thanks For Visting Zesty Zomato")
            print("----------------------------------")
            break
        else:
            print("Enter A Valid Number!")
            print("------------------------")




if __name__ == "__main__":
    main()