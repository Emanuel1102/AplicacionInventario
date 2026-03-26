from src.services import (add_product as add,
                          view_inventory as view,
                          generate_report as report,
                          search_product as search, 
                          update_product as update, 
                          delete_product as delete,
                          products)

from src.files import (save_csv as save,
                       charge_csv as charge)

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
                    7. Guardar csv
                    8. Cargar csv
                    9. Salir
                    => '''))
        
        if menu == 9:
            print('Proceso terminado')
            break
        elif menu>0 and menu<9:
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
                    case 7:
                        save(products)
                        break
                    case 8:
                        charge()
                        break
        else:
            print('No se reconoce la opcion')
            
    except ValueError:
        print('Se esperaba un valor numérico y se obtuvo un valor diferente, intenta nuevamente')

