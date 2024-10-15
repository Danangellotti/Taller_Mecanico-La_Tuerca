from django.db import models

class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'Clientes'

class Vehiculo(models.Model):
    vehiculo_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    matricula = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.matricula})"

    class Meta:
        db_table = 'Vehiculos'

class Servicio(models.Model):
    servicio_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'Servicios'

class Orden(models.Model):
    orden_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField(null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Orden {self.orden_id} - {self.cliente}"

    class Meta:
        db_table = 'Ordenes'

class DetalleOrden(models.Model):
    detalle_id = models.AutoField(primary_key=True)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.orden} - {self.servicio}"

    class Meta:
        db_table = 'Detalles_Orden'
