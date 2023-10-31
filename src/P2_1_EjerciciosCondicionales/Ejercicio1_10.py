# Este ejercicio se podía resolver con funciones que no devolviesen nada y que se llamasen entre ellas,
# he preferido crear funciones que se llamasen en el main y que devolviesen algo para poder comprobarlas con pytest
# ¿Hace buen uso de las funciones este código?
def imprimir_ticket(tipo: str, pizza: list):
    print("Su pizza", tipo.lower(), "lleva:", end="")
    for ingrediente in pizza:
        if pizza[len(pizza) - 1] == ingrediente:
            print(" y " + ingrediente + ".")
        else:
            print(" " + ingrediente + ",", end="")


def crear_pizza(ingrediente):
    return ["tomate", "mozzarella", ingrediente]


def sacar_lista_ingredientes(tipo: str):
    if tipo == "VEGETAL":
        return ["pimiento", "tofu"]
    elif tipo == "CONCARNE":
        return ["peperoni", "jamon", "salmon"]


def elegir_ingredientes(ingredientes: list):
    print("Elige tu ingrediente")
    for ingrediente in ingredientes:
        print("-->", ingrediente)
    eleccion = input("Cual quieres? ")
    while eleccion.replace(" ", "").lower() not in ingredientes:
        print("no tenemos", eleccion, "elige un ingrediente de la lista")
        eleccion = input("Cual quieres? ")
    return eleccion


def elegir_tipo_pizza():
    tipo_pizza = input("Quiere su pizza vegetal o con carne? ").upper().replace(" ", "")
    while tipo_pizza != "VEGETAL" and tipo_pizza != "CONCARNE":
        print("No hemos entendido su pedido, debe escribir (vegetal) o (con carne)")
        tipo_pizza = input("Quiere su pizza vegetal o con carne? ").upper().replace(" ", "")
    return tipo_pizza


def main():
    print("Bienvenido a Bella Napoli")
    tipo_pizza = elegir_tipo_pizza()
    ingrediente = elegir_ingredientes(sacar_lista_ingredientes(tipo_pizza))
    pizza = crear_pizza(ingrediente)
    imprimir_ticket(tipo_pizza, pizza)


if __name__ == "__main__":
    main()
