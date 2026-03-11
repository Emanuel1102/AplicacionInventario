import main

def add(name, quantity, price):
    if name and price and quantity:
        new_product={
            'product_name':name,
            'unitary_price': price,
            'product_quantity':quantity,
            'product_total': price*quantity
        }
        main.products.append(new_product)
    else:
        print('No se pudo realizar el proceso, dejaste un campo sin llenar')