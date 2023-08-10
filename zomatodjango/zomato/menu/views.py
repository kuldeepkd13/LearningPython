from django.shortcuts import render,redirect
import json
from django.http import Http404


def menu_list(request):
    with open('menu.json') as menu_file:
        menu_data = json.load(menu_file)
    
    return render(request, 'menu_list.html', {'menu_data': menu_data})


def add_dish(request):
    if request.method == "POST":
        dishId = request.POST['dishId']
        dishName = request.POST['dishName']
        dishPrice = request.POST['dishPrice']
        dishAvailability = request.POST['dishAvailability']

        newDish = {
            'dishId':dishId,
            'dishName': dishName,
            'dishPrice':float(dishPrice),
            'dishAvailability':dishAvailability
        }

        with open('menu.json') as menu_file:
         menu_data = json.load(menu_file)

        menu_data.append(newDish)
        with open('menu.json', 'w') as menu_file:
         json.dump(menu_data, menu_file, indent=4)

        return redirect('menu_list')

    return render(request, 'add.html')


def remove_dish(request, dishId):
    with open('menu.json') as menu_file:
        menu_data = json.load(menu_file)
    
    updated_menu_data = [dish for dish in menu_data if dish['dishId'] != dishId]
    
    with open('menu.json', 'w') as menu_file:
        json.dump(updated_menu_data, menu_file, indent=4)
    
    return redirect('menu_list')

def update_dish(request, dishId):
    if request.method == 'POST':
        with open('menu.json') as menu_file:
            menu_data = json.load(menu_file)
    
        # Find the dish with the specified dishId
        for dish in menu_data:
            if dish['dishId'] == dishId:
                dish['dishAvailability'] = 'yes' if dish['dishAvailability'] == 'no' else 'no'
                break
    
        with open('menu.json', 'w') as menu_file:
            json.dump(menu_data, menu_file, indent=4)
    
    return redirect('menu_list')


def order_list(request):
    with open('order.json') as order_file:
        order_data = json.load(order_file)
    
    return render(request, 'order_list.html', {'order_data': order_data})

def take_order(request):
    if request.method == 'POST':
        CustomerName = request.POST['CustomerName']
        dishId = request.POST['dishId']
        
        # Check if the selected dish is available
        with open('menu.json') as menu_file:
            menu_data = json.load(menu_file)
        
        selected_dish = None
        for dish in menu_data:
            if dish['dishId'] == dishId and dish['dishAvailability'] == 'yes':
                selected_dish = dish
                break
        
        if not selected_dish:
            return render(request, 'order_unavailable.html', {'unavailable_dishes': [dishId]})
        
        # Process the order
        with open('order.json') as order_file:
            order_data = json.load(order_file)
  
        order_id = str(len(order_data) + 1)
        new_order = {
            'OrderId': order_id,
            'CustomerName': CustomerName,
            'dishName': selected_dish['dishName'],
            'Price': selected_dish["dishPrice"],
            'Status': 'Preparing'
        }
        order_data.append(new_order)
        
        with open('order.json', 'w') as order_file:
            json.dump(order_data, order_file, indent=4)

    with open('menu.json') as menu_file:
        menu_data = json.load(menu_file)

    return render(request, 'take_order.html', {'menu_data': menu_data})



def update_order_status(request, OrderId):
    if request.method == 'POST':
        new_status = request.POST.get('status')
        
        with open('order.json') as order_file:
            order_data = json.load(order_file)
        
        order_found = False
        for order in order_data:
            if order['OrderId'] == str(OrderId):
                order['Status'] = new_status
                order_found = True
                break
        
        with open('order.json', 'w') as order_file:
            json.dump(order_data, order_file, indent=4)
    
        return redirect('order_list')

    return render(request, 'order_list.html')  

def filter(request, status):
    with open('order.json') as order_file:
        order_data = json.load(order_file)

    updated_order_data = [order for order in order_data if order['Status'] == status]

    return render(request, 'order_list.html', {'order_data': updated_order_data})
