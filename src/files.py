import csv
import os
from src.services import view_inventory


def validate_load_rows(products, inventory):
    if len(products[0]) == 3:
            invalid_rows = 0
            for i in range(1, len(products)):
                current_product = products[i]
                if len(current_product) == 3:
                    try:
                        name = current_product[0]
                        price = float(current_product[1]) 
                        quantity = int(current_product[2])
                        if price > 0 and quantity > 0:
                            product_to_charge = {
                                'product_name':name,
                                'unitary_price': price,
                                'product_quantity': quantity
                            }
                            inventory.append(product_to_charge)
                        else:
                            invalid_rows += 1
                    except ValueError:
                        invalid_rows += 1
                else:
                    invalid_rows += 1
            print('\nProductos cargados:')            
            view_inventory()
            if invalid_rows > 0:
                print(f'{invalid_rows} fila(s) inválida(s) omitida(s)')        
    else:
        print('Cabecera invalida, debe contener 3 columnas')




def overwrite_create_file(path, inventory, fields):
    try:
        with open(path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(inventory)
            inventory.clear()
            print(f'\nGuardado en {path}')
    except FileNotFoundError:
        print(f'\n¡Archivo {path} no encontrado, asegurate de que la ruta exista!')




def save_csv(inventory, name_file):
    
    path = f'data/{name_file.split('.')[0]}.csv'

    fields = ['product_name', 'unitary_price', 'product_quantity']

    if os.path.exists(path):
        action = input(f'''{path} ya existe (escribe el numero de la opcion o presiona enter para descartaruu)
              1. Sobrescribir
              2. Fusionar
              => ''')
        match action:
            case '1':
                overwrite_create_file(path, inventory, fields)
            case '2':
                with open(path, 'a', newline='', encoding='utf-8') as file:
                    add = csv.writer(file)
                    for product in inventory:
                        row_to_file = [product['product_name'], product['unitary_price'], product['product_quantity']]
                        add.writerow(row_to_file)
                    inventory.clear()
                    print(f'Items agregados en {path}')
            case _:
                print('''¡Opción no reconocida, cambios no guardados!.
                      Puede intentar nuevamente''')
    else:
        overwrite_create_file(path, inventory, fields)

     


def charge_csv(inventory, name_file):

    path = f'data/{name_file.split('.')[0]}.csv'

    action_choosen = 'Carga de archivo'
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            if len(inventory) > 0:
                print('Actualmente el inventario tiene los siguientes productos:')
                view_inventory()
                action = input('''¿Que deseas hacer con lo que tienes actualmente en tu inventario? (ingresa el número de la opción):
                            1. Sobrescribir
                            2. Fusionar
                            => ''')
                if action == '1':
                    inventory.clear()
                    action_choosen = 'Sobrescribir'
                elif action == '2':
                    action_choosen = 'Fusión'
                else:
                    print('\nOpción no reconocida')   
            reader = csv.reader(file)
            products = list(reader)

            validate_load_rows(products, inventory)
            print(f'Acción: {action_choosen}')    
    except FileNotFoundError:
        print(f'\n¡Archivo {path} no encontrado, asegurate de que la ruta/archivo exista!')
