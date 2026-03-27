import csv
from src.services import view_inventory

def save_csv(inventory, path='data/inventario.csv'):
    fields = ['product_name', 'unitary_price', 'product_quantity']
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(inventory)
        inventory.clear()
        print(f'Guardado en {path}')


def charge_csv(inventory, path='data/inventario.csv'):
    action_choosen = 'Carga de archivo'
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
            print('Opción no reconocida')
            

    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        products = list(reader)

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

            print('Productos cargados:')            
            view_inventory()
            print(f'{invalid_rows} fila(s) invalida(s) omitida(s)')
            print(f'Acción: {action_choosen}')
                    
        else:
            print('Cabecera invalida')
                        

            
        

    
