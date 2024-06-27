from django.db import models
from django.contrib.auth.models import AbstractUser


class Region(models.Model):
    descripcion = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)

    def __str__(self):
        return self.descripcion


class Comuna(models.Model):
    descripcion = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


class Rol(models.Model):
    descripcion = models.CharField(max_length=100)
    permisos = models.IntegerField()

    def __str__(self):
        return self.descripcion


class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    dv = models.CharField(max_length=1)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    comuna = models.ForeignKey(Comuna, null=True, on_delete=models.SET_NULL)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    rol = models.ForeignKey(Rol, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.username


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    dv = models.CharField(max_length=1)
    direccion = models.CharField(max_length=255)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    comuna = models.ForeignKey(Comuna, null=True, on_delete=models.SET_NULL)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    rol = models.ForeignKey(Rol, null=True, on_delete=models.SET_NULL)
    contrasena = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Proveedor(models.Model):
    razon_social = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    dv = models.CharField(max_length=1)
    direccion = models.CharField(max_length=255)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    comuna = models.ForeignKey(Comuna, null=True, on_delete=models.SET_NULL)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return self.razon_social


class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class Extra(models.Model):
    descripcion = models.CharField(max_length=100)
    recargo = models.IntegerField()

    def __str__(self):
        return self.descripcion


class Servicio(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    extra = models.ForeignKey(Extra, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.descripcion


class Evento(models.Model):
    descripcion = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    aforo = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


class MetodoPago(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class EstadoCot(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class Cotizacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    detalle_venta = models.TextField()
    estado = models.ForeignKey(EstadoCot, on_delete=models.CASCADE)
    fecha = models.DateField()
    subtotal = models.IntegerField()

    def __str__(self):
        return f"Cotizacion {self.id} - {self.cliente}"


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    fecha = models.DateField()
    subtotal = models.IntegerField()
    iva = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f"Venta {self.id} - {self.cliente}"


class Reserva(models.Model):
    porcentaje = models.IntegerField()

    def __str__(self):
        return f"Reserva {self.id}"
