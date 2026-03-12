products=[]

def add_product(product):        
    products.append(product)

def view_inventory():
    print(f"| {'-'*30} |")
    print(f"| Product... | cant... |")
    print(f"| {'-'*30} |")
    for product in products:
        print(f"| {product['product_name']}     |    {product['product_quantity']}    |")
        print(f"| {'_'*30} |")
            
def generate_report():
    total_products = sum([product['product_quantity'] for product in products])
    total_capital = sum([product['product_total'] for product in products])
    print(f'Total de productos {len(products)}')
    print(f'Total de unidades: {total_products}')
    print(f'Capital en materia prima: ${total_capital}')

