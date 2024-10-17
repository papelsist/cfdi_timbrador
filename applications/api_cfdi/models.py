from django.db import models

# Create your models here.

class Proveedor(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo = models.TextField()  # This field type is a guess.
    clave = models.CharField(unique=True, max_length=255)
    cuenta_bancaria = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    nacional = models.TextField()  # This field type is a guess.
    nombre = models.CharField(unique=True, max_length=255)
    rfc = models.CharField(max_length=13)
    sw2 = models.BigIntegerField(blank=True, null=True)
    telefono1 = models.CharField(max_length=30, blank=True, null=True)
    telefono2 = models.CharField(max_length=30, blank=True, null=True)
    telefono3 = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.CharField(max_length=26)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    plazo = models.IntegerField()
    fecha_revision = models.TextField()  # This field type is a guess.
    imprimir_costo = models.TextField()  # This field type is a guess.
    descuentof = models.BigIntegerField()
    diasdf = models.BigIntegerField()
    limite_de_credito = models.DecimalField(max_digits=19, decimal_places=2)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    banco = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'

class ComprobanteFiscal(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    forma_de_pago = models.CharField(max_length=50)
    uuid = models.CharField(unique=True, max_length=255)
    last_updated = models.DateTimeField()
    emisor = models.CharField(max_length=255)
    tipo_de_comprobante = models.CharField(max_length=8)
    serie = models.CharField(max_length=30, blank=True, null=True)
    rfc = models.CharField(max_length=255, blank=True, null=True)
    file_name = models.CharField(max_length=150)
    original_name = models.CharField(max_length=150)
    folio = models.CharField(max_length=30, blank=True, null=True)
    fecha = models.DateTimeField()
    url = models.CharField(max_length=255)
    receptor_rfc = models.CharField(max_length=13)
    metodo_de_pago = models.CharField(max_length=30)
    emisor_rfc = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'comprobante_fiscal'





class Banco(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    nacional = models.TextField(blank=True, null=True)  # This field type is a guess.
    banco_sat = models.ForeignKey('BancoSat', models.DO_NOTHING, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    nombre = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'banco'


class BancoSat(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    clave = models.CharField(unique=True, max_length=20)
    nombre_corto = models.CharField(max_length=255)
    razon_social = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_sat'

class CuentaDeBanco(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo = models.TextField()  # This field type is a guess.
    banco_sat = models.ForeignKey(BancoSat, models.DO_NOTHING, blank=True, null=True)
    clave = models.CharField(unique=True, max_length=30)
    descripcion = models.CharField(max_length=255)
    impresion_template = models.CharField(max_length=50, blank=True, null=True)
    moneda = models.CharField(max_length=255)
    numero = models.CharField(max_length=30)
    sub_cuenta_operativa = models.CharField(max_length=4, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=9, blank=True, null=True)
    disponible_en_venta = models.TextField()  # This field type is a guess.
    disponible_en_pagos = models.TextField(blank=True, null=True)  # This field type is a guess.
    proximo_cheque = models.BigIntegerField(blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    comision_por_transferencia = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    cuenta_concentradora = models.TextField(blank=True, null=True)  # This field type is a guess.
    rendimiento_tasa = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    plazo = models.IntegerField(blank=True, null=True)
    inversion = models.TextField(blank=True, null=True)  # This field type is a guess.
    tasa_isr = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    rfc = models.CharField(max_length=15, blank=True, null=True)
    banco = models.ForeignKey(Banco, models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'cuenta_de_banco'

class Cheque(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    entregado = models.DateField(blank=True, null=True)
    last_updated = models.DateTimeField()
    confidencial = models.TextField()  # This field type is a guess.
    update_user = models.CharField(max_length=255, blank=True, null=True)
    cobrado = models.DateField(blank=True, null=True)
    liberado = models.DateField(blank=True, null=True)
    folio = models.BigIntegerField()
    cancelado_comentario = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField()
    impresion = models.DateTimeField(blank=True, null=True)
  
    cancelado = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=255)
   
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255, blank=True, null=True)

    fecha_devolucion = models.DateTimeField(blank=True, null=True)
    cancelacion = models.DateTimeField(blank=True, null=True)
    comentario_cancelacion = models.CharField(max_length=255, blank=True, null=True)
    asignado = models.CharField(max_length=255, blank=True, null=True)
    fecha_transito = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cheque'


class CuentaPorPagar(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    impuesto_trasladado = models.DecimalField(max_digits=19, decimal_places=4)
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=4)
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    impuesto_retenido = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    serie = models.CharField(max_length=30, blank=True, null=True)
    moneda = models.CharField(max_length=5)
    descuento_financiero_vto = models.DateField(blank=True, null=True)
    descuento_financiero = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    update_user = models.CharField(max_length=255)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    folio = models.CharField(max_length=255, blank=True, null=True)
    comprobante_fiscal = models.ForeignKey('ComprobanteFiscal', models.DO_NOTHING, blank=True, null=True)
    tipo = models.CharField(max_length=15)
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    vencimiento = models.DateField()
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    analizada = models.TextField()  # This field type is a guess.
    nombre = models.CharField(max_length=255)
    sub_total = models.DecimalField(max_digits=19, decimal_places=4)
    create_user = models.CharField(max_length=255)
    #importe_por_pagar = models.DecimalField(max_digits=19, decimal_places=2)
    comprobante_id = models.BigIntegerField(unique=True, blank=True, null=True)
    descuentof_vto = models.DateField(blank=True, null=True)
    #tc_contable = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    #contrarecibo = models.BigIntegerField(blank=True, null=True)
    ''' diferencia_fecha = models.DateField(blank=True, null=True)
    diferencia = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    impuesto_retenido_isr = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    impuesto_retenido_iva = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    gasto_analizado_fecha = models.DateField(blank=True, null=True)
    gasto_analizado = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True) '''

    class Meta:
        managed = False
        db_table = 'cuenta_por_pagar'
      


class MovimientoDeCuenta(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    forma_de_pago = models.CharField(max_length=255)
    last_updated = models.DateTimeField()
    referencia = models.CharField(max_length=255, blank=True, null=True)
    moneda = models.CharField(max_length=255)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    tipo = models.CharField(max_length=255)
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    afavor = models.CharField(max_length=255)
    concepto = models.CharField(max_length=50, blank=True, null=True)
    concepto_reporte = models.CharField(max_length=255, blank=True, null=True)
    cuenta = models.ForeignKey(CuentaDeBanco, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=4)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    cheque = models.OneToOneField(Cheque, models.DO_NOTHING, blank=True, null=True)
    sucursal = models.CharField(max_length=255, blank=True, null=True)
    por_identificar = models.TextField(blank=True, null=True)  # This field type is a guess.
    fecha_deposito = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimiento_de_cuenta'


class Rembolso(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=4)
    forma_de_pago = models.CharField(max_length=13)
    moneda = models.CharField(max_length=255)
    apagar = models.DecimalField(max_digits=19, decimal_places=4)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    update_user = models.CharField(max_length=255)
    fecha_de_pago = models.DateField()
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    egreso_id = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    create_user = models.CharField(max_length=255)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, blank=True, null=True)
    concepto = models.CharField(max_length=17)


    class Meta:
        managed = False
        db_table = 'rembolso'


class RembolsoDet(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    cxp_id = models.CharField(max_length=255, blank=True, null=True)
    documento_serie = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    rembolso_id = models.CharField(max_length=255)
    apagar = models.DecimalField(max_digits=19, decimal_places=2)
    documento_folio = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    documento_fecha = models.DateTimeField(blank=True, null=True)
    create_user = models.CharField(max_length=255)
    partidas_idx = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    concepto = models.CharField(max_length=255, blank=True, null=True)
    sucursal = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rembolso_det'


class Requisicion(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=4)
    forma_de_pago = models.CharField(max_length=13)
    last_updated = models.DateTimeField()
    moneda = models.CharField(max_length=255)
    apagar = models.DecimalField(max_digits=19, decimal_places=4)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    update_user = models.CharField(max_length=255)
    folio = models.BigIntegerField()
    fecha_de_pago = models.DateField()
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    cerrada = models.DateField(blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=255)
    create_user = models.CharField(max_length=255)
    class_field = models.CharField(db_column='class', max_length=255)  # Field renamed because it was a Python reserved word.
    descuentof = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuentof_importe = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    pagada = models.DateField(blank=True, null=True)
    egreso = models.CharField(max_length=255, blank=True, null=True)
    aplicada = models.DateField(blank=True, null=True)
    por_comprobar = models.TextField(blank=True, null=True)  # This field type is a guess.


    class Meta:
        managed = False
        db_table = 'requisicion'


    
class RequisicionDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    cxp_id = models.CharField(max_length=255, blank=True, null=True)
    documento_serie = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    documento_total = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    requisicion_id = models.CharField(max_length=255)
    apagar = models.DecimalField(max_digits=19, decimal_places=2)
    documento_folio = models.CharField(max_length=255, blank=True, null=True)
    acuse = models.CharField(max_length=255, blank=True, null=True)
    descuentof = models.DecimalField(max_digits=19, decimal_places=2)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    documento_fecha = models.DateTimeField(blank=True, null=True)
    descuentof_importe = models.DecimalField(max_digits=19, decimal_places=2)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requisicion_det'


class CuentaPorCobrar(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    tipo_documento = models.CharField(max_length=18)
    forma_de_pago = models.CharField(max_length=255)
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)



    class Meta:
        managed = False
        db_table = 'cuenta_por_cobrar'


class AplicacionDeCobro(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    cobro_id = models.CharField(max_length=255)
    last_updated = models.DateTimeField()
    update_user = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField()
    cuenta_por_cobrar_id = models.CharField(max_length=255)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    forma_de_pago = models.CharField(max_length=255, blank=True, null=True)
    nota_de_credito_id = models.BigIntegerField(blank=True, null=True)
    recibo = models.CharField(max_length=255, blank=True, null=True)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=8, blank=True, null=True)
    moneda = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aplicacion_de_cobro'


class Cobro(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    diferencia_fecha = models.DateField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    anticipo = models.TextField()  # This field type is a guess.
    forma_de_pago = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    referencia = models.CharField(max_length=255, blank=True, null=True)
    moneda = models.CharField(max_length=255)
    primera_aplicacion = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    diferencia = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    tipo = models.CharField(max_length=3)
    fecha = models.DateField()
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    cancelacion_motivo = models.CharField(max_length=255, blank=True, null=True)
    recibo_anterior = models.CharField(max_length=100, blank=True, null=True)
    anticipo_sat = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cobro'