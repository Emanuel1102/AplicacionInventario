
from src.add_product import add 

products=[]

menu=int(input('''Selecciona una opcion 
               1. Agregar un producto
               2. Ver inventario
               3. Actualizar producto
               4. Eliminar un producto
               5. Buscar producto
               6. Generar reporte (total de productos y capital en materia prima)
               => '''))


product_name=input('Nombre del producto => ')
product_quantity=input('Cantidad del producto => ')
unitary_price=input('Ingresa el nombre del producto => ')

if menu == 1 :
    add(product_name, product_quantity, unitary_price)

print(products)
