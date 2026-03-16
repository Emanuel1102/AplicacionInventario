products=[
    {
        'product_name':'camisa',
        'unitary_price': 12,
        'product_quantity':2
    },
    {
        'product_name':'camisa',
        'unitary_price': 12,
        'product_quantity':2
    }
]

def add_product():   
    while True:
        try:
            product_name=input('Nombre del producto => ').lower()
            unitary_price=float(input('Precio unitario => $'))
            product_quantity=int(input('Cantidad del producto => '))
            new_product={
                    'product_name':product_name,
                    'unitary_price': unitary_price,
                    'product_quantity':product_quantity,
                    'product_total': product_quantity*unitary_price 
            }    
            products.append(new_product)
            print('Producto agregado exitosamente')
            break
        except ValueError:
            print('Ingresaste algo que NO es un número en un campo numérico, intenta nuevamente') 


def view_inventory():
    if len(products) > 0:
        print(f"| {'-'*30} |")
        print(f"| Product... | cant... |")
        print(f"| {'-'*30} |")
        for product in products:
            print(f"| {product['product_name']}     |    {product['product_quantity']}    |")
            print(f"| {'_'*30} |")
    else:
        print('Inventario vacío')
            
def generate_report():
    if len(products) > 0:
        total_products = sum([product['product_quantity'] for product in products])
        total_capital = sum([product['product_total'] for product in products])
        print(f'Total de productos: {len(products)}')
        print(f'Total de unidades: {total_products}')
        print(f'Capital en materia prima: ${total_capital}')
    else:
        print('Nada que reportar')

def search_product():
    name = input('¿Que producto quieres buscar? => ')
    for product in products:
        if product['product_name'] == name:
            print(product)

