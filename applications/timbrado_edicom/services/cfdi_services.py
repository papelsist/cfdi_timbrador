
import base64
from ..models import Cfdi
import xmltodict
import json
from mailjet_rest import Client
#from .print_service import imprimir_carta_porte_envio
import xml.etree.ElementTree as ET


def getXml(cfdiId):
    cfdi = Cfdi.objects.get(id = cfdiId )
    #print(cfdi.cadena)
    xml = base64.b64decode(cfdi.xml)
    #print(xml)
    return xml

def getXmlDictionary(embarque):
    print('*'*50)
    print(embarque)
    print('*'*50)
    cfdi = Cfdi.objects.get(origen = embarque) 
    xml = getXml(cfdi.id)
    xmlDict = xmltodict.parse(xml['xml'])
    #print(xmlDict)
    xmlJson = json.dumps(xmlDict)
    #print(xmlJson)

    return xmlDict

def getXmlDictionaryFromXml(xml):
    xmlDict = xmltodict.parse(xml)
    xmlJson = json.dumps(xmlDict)
    return xmlDict

def getXmlData(xml):
    ns = {'cfdi': "http://www.sat.gob.mx/cfd/4" ,'cartaporte20':'http://www.sat.gob.mx/CartaPorte20','tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital'}
    tree = ET.fromstring(xml) 
    timbrado = tree.find('.//tfd:TimbreFiscalDigital', ns).attrib
    UUID = timbrado['UUID']
    fecha_timbrado = timbrado['FechaTimbrado']
    return (UUID,fecha_timbrado)