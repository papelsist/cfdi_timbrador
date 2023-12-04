from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cfdi
from .services.edicom_service import EdicomService
from .services.cfdi_services import getXmlData
import base64
from datetime import datetime


@api_view(['GET'])
def timbrar_impap(request):
    #print(request)
    #print(request.query_params)
    #print(request.query_params['id'])
    cfdi = Cfdi.objects.get(pk=request.query_params['id'])
    #print(cfdi.__dict__)
    #print(cfdi.xml)
    service = EdicomService()
    xmlTxt = service.getCfdi(cfdi.xml)
    #print(xmlTxt)
    uuid,fecha_timbrado = getXmlData(xmlTxt)
    print(uuid)
    ''' xmlBase64 = base64.b64encode(str.encode(xmlTxt))
    xml_bytes = str.encode(xmlTxt) '''
    cfdi.uuid = uuid
    cfdi.xml =  xmlTxt
    cfdi.timbrado = datetime.fromisoformat(fecha_timbrado)
    cfdi.xml_name = f"SIGN_{cfdi.xml_name}"
    cfdi.save()

    return Response({"Mesagge":"Correcto"})


@api_view(['GET'])
def timbrar_rh(request):
    cfdi = Cfdi.objects.using('rh').get(pk=request.query_params['id'])
    #print(cfdi.__dict__)
    #print(cfdi.xml)
    service = EdicomService()
    xmlTxt = service.getCfdi(cfdi.xml)
    #print(xmlTxt)
    uuid,fecha_timbrado = getXmlData(xmlTxt)
    print(uuid)
    ''' xmlBase64 = base64.b64encode(str.encode(xmlTxt))
    xml_bytes = str.encode(xmlTxt) '''
    cfdi.uuid = uuid
    cfdi.xml =  xmlTxt
    cfdi.timbrado = datetime.fromisoformat(fecha_timbrado)
    cfdi.xml_name = f"SIGN_{cfdi.xml_name}"
    cfdi.save(using="rh")
    return Response({"Mesagge":"Correcto"})


@api_view(['GET'])
def timbrar_paper(request):
    cfdi = Cfdi.objects.using('paper').get(pk=request.query_params['id'])
    #print(cfdi.__dict__)
    #print(cfdi.xml)
    service = EdicomService()
    xmlTxt = service.getCfdi(cfdi.xml)
    #print(xmlTxt)
    uuid,fecha_timbrado = getXmlData(xmlTxt)
    #print(uuid)
    ''' xmlBase64 = base64.b64encode(str.encode(xmlTxt))
    xml_bytes = str.encode(xmlTxt) '''
    cfdi.uuid = uuid
    cfdi.xml =  xmlTxt
    cfdi.timbrado = datetime.fromisoformat(fecha_timbrado)
    cfdi.xml_name = f"SIGN_{cfdi.xml_name}"
    cfdi.save(using="paper")
    return Response({"Mesagge":"Correcto"})

@api_view(['GET'])
def timbrar_mobix(request):
    #print(request)
    #print(request.query_params)
    #print(request.query_params['id'])
    cfdi = Cfdi.objects.using('mobix').get(pk=request.query_params['id'])
    #print(cfdi.__dict__)
    #print("*"*50)
    #print(request.query_params)
    #print("*"*50)
    #print(cfdi.xml)
    service = EdicomService()
    xmlTxt = service.getCfdi(cfdi.xml)
    #print(xmlTxt)
    uuid,fecha_timbrado = getXmlData(xmlTxt)
    print(uuid)
    ''' xmlBase64 = base64.b64encode(str.encode(xmlTxt))
    xml_bytes = str.encode(xmlTxt) '''
    cfdi.uuid = uuid
    cfdi.xml =  xmlTxt
    cfdi.timbrado = datetime.fromisoformat(fecha_timbrado)
    cfdi.xml_name = f"SIGN_{cfdi.xml_name}"
    cfdi.save(using="mobix")
    return Response({"Mesagge":"Correcto"})

# Timbrado de Prueba

@api_view(['GET'])
def timbrar_impap_test(request):
    #print(request)
    #print(request.query_params)
    #print(request.query_params['id'])
    cfdi = Cfdi.objects.get(pk=request.query_params['id'])
    #print(cfdi.__dict__)
    #print(cfdi.xml)
    service = EdicomService()
    xmlTxt = service.getCfdiTest(cfdi.xml)
    #print(xmlTxt)
    uuid,fecha_timbrado = getXmlData(xmlTxt)
    print(uuid)
    ''' xmlBase64 = base64.b64encode(str.encode(xmlTxt))
    xml_bytes = str.encode(xmlTxt) '''
    cfdi.uuid = uuid
    cfdi.xml =  xmlTxt
    cfdi.timbrado = datetime.fromisoformat(fecha_timbrado)
    cfdi.xml_name = f"SIGN_{cfdi.xml_name}"
    cfdi.save()

    return Response({"Mesagge":"Correcto"})


@api_view(['GET'])
def timbrar_rh_test(request):
    cfdi = Cfdi.objects.using('rh').get(pk=request.query_params['id'])
    #print(cfdi.__dict__)
    #print(cfdi.xml)
    service = EdicomService()
    xmlTxt = service.getCfdiTest(cfdi.xml)
    #print(xmlTxt)
    uuid,fecha_timbrado = getXmlData(xmlTxt)
    print(uuid)
    ''' xmlBase64 = base64.b64encode(str.encode(xmlTxt))
    xml_bytes = str.encode(xmlTxt) '''
    cfdi.uuid = uuid
    cfdi.xml =  xmlTxt
    cfdi.timbrado = datetime.fromisoformat(fecha_timbrado)
    cfdi.xml_name = f"SIGN_{cfdi.xml_name}"
    cfdi.save(using="rh")
    return Response({"Mesagge":"Correcto"})


@api_view(['GET'])
def timbrar_paper_test(request):
    cfdi = Cfdi.objects.using('paper').get(pk=request.query_params['id'])
    #print(cfdi.__dict__)
    #print(cfdi.xml)
    service = EdicomService()
    xmlTxt = service.getCfdiTest(cfdi.xml)
    #print(xmlTxt)
    uuid,fecha_timbrado = getXmlData(xmlTxt)
    #print(uuid)
    ''' xmlBase64 = base64.b64encode(str.encode(xmlTxt))
    xml_bytes = str.encode(xmlTxt) '''
    cfdi.uuid = uuid
    cfdi.xml =  xmlTxt
    cfdi.timbrado = datetime.fromisoformat(fecha_timbrado)
    cfdi.xml_name = f"SIGN_{cfdi.xml_name}"
    cfdi.save(using="paper")
    return Response({"Mesagge":"Correcto"})

@api_view(['GET'])
def timbrar_mobix_test(request):
    #print(request)
    #print(request.query_params)
    #print(request.query_params['id'])
    cfdi = Cfdi.objects.using('mobix').get(pk=request.query_params['id'])
    #print(cfdi.__dict__)
    #print("*"*50)
    #print(request.query_params)
    #print("*"*50)
    #print(cfdi.xml)
    service = EdicomService()
    xmlTxt = service.getCfdiTest(cfdi.xml)
    #print(xmlTxt)
    uuid,fecha_timbrado = getXmlData(xmlTxt)
    print(uuid)
    ''' xmlBase64 = base64.b64encode(str.encode(xmlTxt))
    xml_bytes = str.encode(xmlTxt) '''
    cfdi.uuid = uuid
    cfdi.xml =  xmlTxt
    cfdi.timbrado = datetime.fromisoformat(fecha_timbrado)
    cfdi.xml_name = f"SIGN_{cfdi.xml_name}"
    cfdi.save(using="mobix")
    return Response({"Mesagge":"Correcto"})
