from rich import print
from rich.prompt import Prompt
from rich.table import Table

class Calculadora:
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        if self.valor2 == 0:
            return "No se puede dividir por cero"
        return self.valor1 / self.valor2

calculadora = Calculadora()

while True:
    table = Table(title="Calculadora", title_style="bold magenta")
    table.add_column("Operación", style="cyan")
    table.add_column("Descripción")

    table.add_row("1", "Suma")
    table.add_row("2", "Resta")
    table.add_row("3", "Multiplicación")
    table.add_row("4", "División")
    table.add_row("5", "Salir")

    print(table)

    opcion = Prompt.ask("Seleccione una opción (1/2/3/4/5): ", choices=["1", "2", "3", "4", "5"])

    if opcion == "5":
        break

    valor1 = float(Prompt.ask("Ingrese el primer valor: "))
    valor2 = float(Prompt.ask("Ingrese el segundo valor: "))

    calculadora.valor1 = valor1
    calculadora.valor2 = valor2

    if opcion == "1":
        resultado = calculadora.suma()
        operacion = "Suma"
    elif opcion == "2":
        resultado = calculadora.resta()
        operacion = "Resta"
    elif opcion == "3":
        resultado = calculadora.multiplicacion()
        operacion = "Multiplicación"
    elif opcion == "4":
        resultado = calculadora.division()
        operacion = "División"

    print(f"Resultado de {operacion}: [bold cyan]{resultado}[/bold cyan]\n")

