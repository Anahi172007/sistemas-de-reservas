class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} (Cédula: {self.cedula})"

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación {self.numero} ({self.tipo}) - {estado} - ${self.precio}/noche"

class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def confirmar_reserva(self):
        if self.habitacion.disponible:
            self.habitacion.disponible = False
            print(f"Reserva confirmada para {self.cliente.nombre} en habitación {self.habitacion.numero} por {self.dias} días.")
        else:
            print("La habitación ya está ocupada.")

# Prueba del sistema
cliente1 = Cliente("Ana Martínez", "0106048002")
habitacion1 = Habitacion(207, "Suite", 140.0)

print(habitacion1)
reserva1 = Reserva(cliente1, habitacion1, 4)
reserva1.confirmar_reserva()
print(habitacion1)
