import json,os

def read_inventory(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def write_inventory(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def create_item(inventory, item):
    inventory.append(item)

def update_item(inventory, item_index, new_item_data):
    if 0 <= item_index < len(inventory):
        inventory[item_index].update(new_item_data)

def delete_item(inventory, item_index):
    if 0 <= item_index < len(inventory):
        del inventory[item_index]


def main():
    print("hello")
    
    # Read existing inventory data
    current_directory = os.path.dirname(os.path.abspath(__file__))
    inventory_filename = os.path.join(current_directory, "inventory.db.json")
    inventory = read_inventory(inventory_filename)
    print(inventory)
    # Create a new item
    new_item = {
        "name": "New Item",
        "quantity": 10,
        "price": 5.99
    }
    
    # Add the new item to the inventory
    create_item(inventory, new_item)
    
    # Write the updated inventory back to the file
    write_inventory(inventory, inventory_filename)

if __name__ == "__main__":
    main()

