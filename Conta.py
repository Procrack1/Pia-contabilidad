def leer_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print(" Ingresa un valor positivo.")
                continue
            return valor
        except ValueError:
            print(" Error: Ingresa un número válido.")


def punto_equilibrio():
    print("\n--- Punto de Equilibrio ---")
    costo_fijo = leer_float("Costo fijo total: $")
    precio_venta = leer_float("Precio de venta por unidad: $")
    costo_variable = leer_float("Costo variable por unidad: $")
    if precio_venta <= costo_variable:
        print(" El precio de venta debe ser mayor al costo variable.")
        return
    unidades = costo_fijo / (precio_venta - costo_variable)
    pesos = unidades * precio_venta
    print(f"\n Punto de equilibrio:")
    print(f"→ Unidades: {unidades:.2f}")
    print(f"→ Pesos: ${pesos:.2f}")


def unidades_vender_impuestos():
    print("\n--- Unidades a Vender (Antes y Después de Impuestos) ---")
    utilidad_deseada = leer_float("Utilidad deseada antes de impuestos: $")
    tasa_impuesto = leer_float("Tasa de impuesto (%): ")
    costo_fijo = leer_float("Costo fijo total: $")
    precio_venta = leer_float("Precio de venta por unidad: $")
    costo_variable = leer_float("Costo variable por unidad: $")
    if precio_venta <= costo_variable:
        print(" El precio de venta debe ser mayor al costo variable.")
        return
    unidades_antes = (costo_fijo + utilidad_deseada) / (precio_venta - costo_variable)
    utilidad_antes = utilidad_deseada / (1 - tasa_impuesto / 100)
    unidades_despues = (costo_fijo + utilidad_antes) / (precio_venta - costo_variable)
    print(f"\n Unidades necesarias:")
    print(f"→ Antes de impuestos: {unidades_antes:.2f}")
    print(f"→ Después de impuestos: {unidades_despues:.2f}")


def presupuesto_ventas_produccion():
    print("\n--- Presupuesto de Ventas y Producción ---")
    ventas_esperadas = leer_float("Unidades a vender: ")
    inventario_inicial = leer_float("Inventario inicial (unidades): ")
    inventario_final_deseado = leer_float("Inventario final deseado (unidades): ")
    produccion_necesaria = ventas_esperadas + inventario_final_deseado - inventario_inicial
    print(f"\n Presupuesto de Producción:")
    print(f"→ Ventas esperadas: {ventas_esperadas:.2f}")
    print(f"→ Producción necesaria: {produccion_necesaria:.2f}")


def analisis_cvu():
    print("\n--- Análisis Costo-Volumen-Utilidad ---")
    precio_venta = leer_float("Precio de venta por unidad: $")
    costo_variable = leer_float("Costo variable por unidad: $")
    costo_fijo = leer_float("Costo fijo total: $")
    ventas = leer_float("Unidades vendidas: ")
    margen_contribucion_unitaria = precio_venta - costo_variable
    margen_total = margen_contribucion_unitaria * ventas
    utilidad_operativa = margen_total - costo_fijo
    print(f"\n Análisis CVU:")
    print(f"→ Margen de contribución por unidad: ${margen_contribucion_unitaria:.2f}")
    print(f"→ Margen total: ${margen_total:.2f}")
    print(f"→ Utilidad operativa: ${utilidad_operativa:.2f}")


def presupuesto_gastos_operativos():
    print("\n--- Presupuesto de Gastos Operativos ---")
    sueldos = leer_float("Sueldos y salarios: $")
    renta = leer_float("Renta del local: $")
    servicios = leer_float("Servicios (agua, luz, internet, etc.): $")
    publicidad = leer_float("Publicidad y promoción: $")
    otros = leer_float("Otros gastos: $")
    total_gastos = sueldos + renta + servicios + publicidad + otros
    print(f"\n Total de gastos operativos: ${total_gastos:.2f}")


def menu():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Punto de equilibrio (unidades/pesos)")
        print("2. Unidades a vender (antes y después de impuestos)")
        print("3. Presupuesto de Ventas y Producción")
        print("4. Análisis Costo-Volumen-Utilidad")
        print("5. Presupuesto de Gastos Operativos")
        print("6. Salir")
        print("====================================")
        opcion = input("Selecciona una opción (1-6): ")
        if opcion == "1":
            punto_equilibrio()
        elif opcion == "2":
            unidades_vender_impuestos()
        elif opcion == "3":
            presupuesto_ventas_produccion()
        elif opcion == "4":
            analisis_cvu()
        elif opcion == "5":
            presupuesto_gastos_operativos()
        elif opcion == "6":
            print(" Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print(" Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
