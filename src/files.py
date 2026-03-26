import csv
from src.services import products

def save_csv(inventory, path='data/inventario.csv'):
    campos = ['product_name', 'unitary_price', 'product_quantity']
    with open(path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        writer.writerows(inventory)
        inventory.clear()
        print('Guardado')


def charge_csv(path='data/inventario.csv'):
    global products
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        products = list(reader)
        print('Cargado con éxito')

    
