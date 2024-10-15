from django.contrib import admin
from .models import Cliente, Vehiculo, Servicio, Orden, DetalleOrden

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'correo_electronico')
    search_fields = ('nombre', 'apellido', 'telefono')

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'anio', 'matricula', 'cliente')
    list_filter = ('marca', 'modelo', 'anio')
    search_fields = ('matricula', 'cliente__nombre', 'cliente__apellido')

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'precio')
    search_fields = ('descripcion',)

class DetalleOrdenInline(admin.TabularInline):
    model = DetalleOrden
    extra = 1

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('orden_id', 'cliente', 'vehiculo', 'fecha_ingreso', 'fecha_salida', 'total')
    list_filter = ('fecha_ingreso', 'fecha_salida')
    search_fields = ('cliente__nombre', 'cliente__apellido', 'vehiculo__matricula')
    inlines = [DetalleOrdenInline]

@admin.register(DetalleOrden)
class DetalleOrdenAdmin(admin.ModelAdmin):
    list_display = ('orden', 'servicio', 'cantidad')
    list_filter = ('servicio',)
    search_fields = ('orden__cliente__nombre', 'orden__cliente__apellido', 'servicio__descripcion')
# Register your models here.
