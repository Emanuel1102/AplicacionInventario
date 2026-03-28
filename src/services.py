products=[]

def add_product():   
    while True:
        try:
            product_name=input('Nombre del producto => ').lower()
            if product_name:
                unitary_price=float(input('Precio unitario => $'))
                product_quantity=int(input('Cantidad del producto => '))

                exists = False

                for product in products:
                    if product['product_name'] == product_name:
                        exists = True
                        break

                if exists:
                    print('¡El producto ya está en el inventario!')
                    break
                else:
                    new_product={
                            'product_name':product_name,
                            'unitary_price': unitary_price,
                            'product_quantity':product_quantity
                    }    
                    products.append(new_product)
                    print('Producto agregado exitosamente')
                    break
            else:
                confirm = input('¡No ingresaste el nombre del producto!, ¿deseas cancelar el proceso? si/no => ')
                if confirm == 'si' or confirm == 's':
                    print('¡Proceso cancelado!')
                    break
        except ValueError:
            print('¡Ingresaste algo que NO es un número en un campo numérico, intenta nuevamente!') 

def view_inventory():
    if len(products) > 0:
        print(f"|{'-'*24}|")
        print(f"|   Product  |  Quantity |")
        print(f"|{'-'*24}|")
        for product in products:
            print(f"| {product['product_name']}     |    {product['product_quantity']}     |")
            print(f"|{'-'*24}|")
    else:
        print('¡Inventario vacío, nada que mostrar!')
            
def generate_report():
    if len(products) > 0:
        total_products = sum([product['product_quantity'] for product in products])
        more_expensive_product = max(products, key=lambda p : p['unitary_price'])
        largest_stock = max(products, key=lambda p : p['product_quantity'])
        total_capital = sum(p['unitary_price'] * p['product_quantity'] for p in products)
        print(f"Total de productos: {len(products)}")
        print(f"Total de unidades: {total_products}")
        print(f"Producto mas caro: {more_expensive_product['product_name']} | ${more_expensive_product['unitary_price']} | {more_expensive_product['product_quantity']}")
        print(f"Producto con mayor stock: {largest_stock['product_name']} | ${largest_stock['unitary_price']} | {largest_stock['product_quantity']}")
        print(f"Capital en materia prima: ${total_capital}")
    else:
        print('¡Inventario vacío, nada que reportar!')

def search_product():
    if len(products) > 0:
        while True:
            name = input('¿Que producto quieres consultar (nombre)? => ')
            if name:
                for product in products:
                    if product['product_name'] == name:
                        print(f"|{'-'*38}|")
                        print(f"| Product | Quantity | Price  |")
                        print(f"|{'-'*38}|")
                        print(f"| {product['product_name']}  |    {product['product_quantity']}    |  ${product['unitary_price']} |")
                        print(f"|{'_'*38}|")
                        break
                else:
                    print('¡Producto no encontrado!')
                break          
            else:
                confirm = input('No ingresaste el nombre del producto, deseas cancelar el proceso? si/no => ')
                if confirm == 'si' or confirm == 's':
                    print('¡Proceso cancelado!')
                    break
    else:
        print('¡Inventario vacío, nada que consultar!')

def update_product():
    if len(products) > 0:
        while True:
            name = input('¿Que producto quieres actualizar (nombre)? => ')
            if name:
                for product in products:
                    if product['product_name'] == name:
                        print(f'{"#"*38}')
                        print('Producto para actualizar: ')
                        print(f'{"#"*38}')
                        print(f"|{'-'*38}|")
                        print(f"| Product | Quantity | Price  |")
                        print(f"|{'-'*38}|")
                        print(f"| {product['product_name']}  |    {product['product_quantity']}    |  ${product['unitary_price']}  |")
                        print(f"|{'_'*38}|")
                        while True:
                            try:
                                new_price = float(input('Ingresa el nuevo precio => $'))
                                new_quantity = int(input('Ingresa la nueva cantidad => '))
                                nuevos_datos = {
                                    'unitary_price': new_price,
                                    'product_quantity': new_quantity
                                }
                                product.update(nuevos_datos)
                                print('Producto actualizado con éxito')
                                break
                            except ValueError:
                                try_again = input('¡Los datos deben ser de tipo numerico!, ¿quieres intentar nuevamente? si/no => ').lower()
                                if try_again != 'si':
                                    print('¡Proceso cancelado!')
                                    break
                        break
                else:
                    print('¡Producto no encontrado!')
                break
            else:
                confirm = input('¡No ingresaste el nombre del producto!, ¿deseas cancelar el proceso? si/no => ')
                if confirm == 'si' or confirm == 's':
                    print('¡Proceso cancelado!')
                    break     
    else:
        print('¡Inventario vacio, nada que actualizar!')
        
def delete_product():
    if len(products) > 0:
        while True:
            name = input('¿Que producto quieres eliminar (nombre)? => ')
            if name:
                for product in products:
                    if product['product_name'] == name:
                        print(f'{"#"*38}')
                        print('Producto para eliminar: ')
                        print(f'{"#"*38}')
                        print(f"|{'-'*38}|")
                        print(f"| Product | Quantity | Price  |")
                        print(f"|{'-'*38}|")
                        print(f"| {product['product_name']}  |    {product['product_quantity']}    |  ${product['unitary_price']}  |")
                        print(f"|{'_'*38}|")
                        confirm = input('Seguro que quieres eliminar este producto? si/no => ').lower()
                        if confirm == 'si' or confirm == 's':
                            products.remove(product) 
                            print('Producto eliminado con éxito')
                        else:
                            print('¡Proceso cancelado!')

                        break
                else:
                    print('¡Producto no encontrado!')
                break
            else:
                confirm = input('¡No ingresaste el nombre del producto!, ¿deseas cancelar el proceso? si/no => ')
                if confirm == 'si' or confirm == 's':
                    print('¡Proceso cancelado!')
                    break
    else:
        print('¡Inventario vacío, no hay nada que eliminar!')
