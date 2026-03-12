from src.product_functions import add_product as add, view_inventory as view, generate_report as report

while True:
    try:
        menu=int(input('''
        -----------------------------------------------------------------------------
                    Selecciona una opcion 
                    1. Agregar un producto
                    2. Ver inventario
                    3. Actualizar producto
                    4. Eliminar un producto
                    5. Buscar producto
                    6. Generar reporte
                    7. Salir
                    => '''))
        
        if menu == 7:
            print('Proceso terminado')
            break
        elif menu>0 and menu<7:
            while True:
                try:
                    match menu:
                        case 1 :
                            product_name=input('Nombre del producto => ').lower()
                            unitary_price=float(input('Precio unitario => $'))
                            product_quantity=int(input('Cantidad del producto => '))
                            new_product={
                                    'product_name':product_name,
                                    'unitary_price': unitary_price,
                                    'product_quantity':product_quantity,
                                    'product_total': product_quantity*unitary_price 
                            }
                            add(new_product)
                            print('Producto agregado exitosamente')
                            break
                        case 2:
                            view()
                            break
                        case 3:
                            print('Aun no disponible')
                            break
                        case 4: 
                            print('Aun no disponible')
                            break
                        case 5:
                            print('Aun no disponible')
                            break
                        case 6:
                            report()
                            break
                except ValueError:
                    print('Ingresaste algo que NO es un número en un campo numérico, intenta nuevamente')
        else:
            print('No se reconoce la opcion')
            
    except ValueError:
        print('Se esperaba un valor numérico y se obtuvo un valor diferente, intenta nuevamente')

