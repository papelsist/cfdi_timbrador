from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CuentaPorPagar, RembolsoDet, Rembolso , MovimientoDeCuenta,Requisicion,RequisicionDet, CuentaPorCobrar, AplicacionDeCobro,Cobro
from django.db import connections



@api_view(['GET'])
def get_cuentas_por_pagar(request):
    print(request.query_params)

    sql_gastos = f"""select c.uuid, m.fecha as fecha_pago, m.referencia as referencia, m.forma_de_pago as forma_de_pago ,m.tipo_de_cambio as tipo_de_cambio_pago
    from cuenta_por_pagar c join rembolso_det r on (c.id = r.cxp_id) join rembolso e on (r.rembolso_id = e.id) join movimiento_de_cuenta m on (e.egreso_id = m.id) 
    where 
        c.fecha between '{request.query_params['fecha_inicial']}' and '{request.query_params['fecha_final']}'
    """
    print(sql_gastos)

    sql_compras = f"""select c.uuid, m.fecha as fecha_pago, m.referencia as referencia, m.forma_de_pago as forma_de_pago,m.tipo_de_cambio as tipo_de_cambio_pago
    from cuenta_por_pagar c join requisicion_det r on (c.id = r.cxp_id) join requisicion e on (r.requisicion_id = e.id) join movimiento_de_cuenta m on (e.egreso = m.id)
    where c.fecha between  '{request.query_params['fecha_inicial']}' and '{request.query_params['fecha_final']}'
    """
    print(sql_compras)
    
    with connections['siipapx'].cursor() as cursor:
        cursor.execute(
            sql_gastos
        )
        rows = cursor.fetchall()
        columnas = [col[0] for col in cursor.description]
        lista = []
        for row in rows:
            reg=dict(zip(columnas,row))
            lista.append(reg) 

        cursor.execute(
            sql_compras
        )
        rows = cursor.fetchall()
        columnas = [col[0] for col in cursor.description]
        for row in rows:
            reg=dict(zip(columnas,row))
            lista.append(reg)

        print(lista)
        print(len(lista))
    
    return Response({"data":lista,"Message":"Test successfully"})

@api_view(['GET'])
def get_cuentas_por_cobrar(request):
    print(request.query_params)

    sql = f"""select c.uuid,a.fecha as fecha_aplicacion,c.forma_de_pago, o.fecha as fecha_cobro, o.referencia, c.tipo, s.nombre as sucursal, o.tipo_de_cambio as tipo_de_cambio_cobro
        from cuenta_por_cobrar c join aplicacion_de_cobro a on (a.cuenta_por_cobrar_id = c.id) join cobro o on (a.cobro_id = o.id) join  sucursal s on (s.id = c.sucursal_id)
		where c.fecha between '{request.query_params['fecha_inicial']}' and '{request.query_params['fecha_final']}'
        """

    with connections['siipapx'].cursor() as cursor:
        cursor.execute(
            sql
        )
        rows = cursor.fetchall()
        columnas = [col[0] for col in cursor.description]
        lista = []
        for row in rows:
            reg=dict(zip(columnas,row))
            lista.append(reg) 
        print(lista)
        print(len(lista))

    return Response({"data":lista,"Message":"Test successfully"})