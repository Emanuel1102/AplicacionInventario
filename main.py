from src.product_functions import add_product as add, view_inventory as view, generate_report as report, search_product as search, update_product as update, delete_product as delete

while True:
    try:
        menu=int(input('''
        -----------------------------------------------------------------------------
                    Selecciona una opcion (digita el número):
                    1. Agregar un producto
                    2. Ver inventario
                    3. Actualizar producto
                    4. Eliminar un producto
                    5. Consultar producto
                    6. Generar reporte
                    7. Salir
                    => '''))
        
        if menu == 7:
            print('Proceso terminado')
            break
        elif menu>0 and menu<7:
            while True:
                match menu:
                    case 1 :
                        add()
                        break
                    case 2:
                        view()
                        break
                    case 3:
                        update()
                        break
                    case 4: 
                        delete()
                        break
                    case 5:
                        search()
                        break
                    case 6:
                        report()
                        break
        else:
            print('No se reconoce la opcion')
            
    except ValueError:
        print('Se esperaba un valor numérico y se obtuvo un valor diferente, intenta nuevamente')

