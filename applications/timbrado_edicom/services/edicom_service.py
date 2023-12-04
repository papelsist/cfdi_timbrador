
from suds.client import Client
import ssl
import base64
import zipfile
import json
import io
from django.core.exceptions import ImproperlyConfigured


class EdicomService:
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    wsdl = "https://cfdiws.sedeb2b.com/EdiwinWS/services/CFDi?wsdl"
    client = Client(wsdl)

   
    
    def getCfdiTest(self, xml):
        xmlStr = xml.decode('utf-8')
        xmlBase64 = base64.b64encode(str.encode(xmlStr))
        stringB64 = xmlBase64.decode()
        #print(stringB64)
        #self.client.add_prefix('xmlns:cfdi','http://cfdi.service.ediwinws.edicom.com')
        result = self.client.service.getCfdiTest('PAP830101CR3','yqjvqfofb',stringB64)
        archivoZip = base64.b64decode(result)
        with zipfile.ZipFile(io.BytesIO(archivoZip)) as thezip:
            for zipinfo in thezip.infolist():
                with thezip.open(zipinfo) as thefile:
                    #print(thefile)
                    xmlTxt = thefile.read().decode('utf-8')
                    #print(xmlTxt)
                    return xmlTxt


    def getCfdi(self, xml):
        xmlStr = xml.decode('utf-8')
        xmlBase64 = base64.b64encode(str.encode(xmlStr))
        stringB64 = xmlBase64.decode()
        #print(stringB64)
        #self.client.add_prefix('xmlns:cfdi','http://cfdi.service.ediwinws.edicom.com')
        result = self.client.service.getCfdi('PAP830101CR3','yqjvqfofb',stringB64)
        archivoZip = base64.b64decode(result)
        with zipfile.ZipFile(io.BytesIO(archivoZip)) as thezip:
            for zipinfo in thezip.infolist():
                with thezip.open(zipinfo) as thefile:
                    #print(thefile)
                    xmlTxt = thefile.read().decode('utf-8')
                    #print(xmlTxt)
                    return xmlTxt


    def cancelCfdi_old(self, cancelacion):
        #print(cancelacion)
        self.client.add_prefix('xmlns:cfdi','http://cfdi.service.ediwinws.edicom.com')
        user = self.USER,
        password = self.PASSWORD
        rfcE = cancelacion["rfc_emisor"]
        rfcR = cancelacion["rfc_receptor"]
        uuid = cancelacion["uuid"]
        total = cancelacion["total"]

        cert_file = open("applications/cfdi/cfdi_sat/data/cfdiSello2020/papelCfdi2020.pfx","rb").read()
        cert = base64.b64encode(cert_file)  
        pfx= cert.decode() 
        #pfx= base64.b64encode(empresa.certificado_digital_pfx)
        pfxPassword = 'Pap315a'
        test = False
        #result = self.client.service.cancelCFDiAsync(user, password, rfcE, rfcR, uuid, total, pfx, pfxPassword, test)
        #print(result)
        #archivoZip = base64.b64decode(result)
        #print(archivoZip)
        # 

    def cancelCfdi(self, cancelacion, facturista):
        print("Cancelando el CFDI")
        self.client.add_prefix('xmlns:cfdi','http://cfdi.service.ediwinws.edicom.com')
        user = self.USER,
        password = self.PASSWORD
        rfcE = cancelacion.emisor_rfc
        rfcR = cancelacion.receptor_rfc
        uuid = 'C6526106-7E57-11EE-9ADA-5711C98CE2FB'
        total = cancelacion.total
        cert_file = facturista.certificado_digital_pfx
        cert = base64.b64encode(cert_file)  
        pfx= cert.decode() 
        pfxPassword = 'Pap315a'
        test = True
        result = self.client.service.cancelCFDiAsync(user, password, rfcE, rfcR, uuid, total, pfx, pfxPassword,'03','',test)
        print(result)
        archivoZip = base64.b64decode(result)
        print(archivoZip)

    def get_config(self,variable, config = None):
        if config ==None:
            config = self.configuration
        try:
            return config[variable]
        except:
            msg = "La Variable no Existe"
            raise ImproperlyConfigured(msg)

        

    def getUUID(self):
        user = self.USER,
        password = self.PASSWORD
        uuid ="C6526106-7E57-11EE-9ADA-5711C98CE2FB"
        rfc ="OILJ710506MV4"
        result = self.client.service.getCfdiFromUUID(user, password, rfc, uuid);
        archivoZip = base64.b64decode(result)
        with zipfile.ZipFile(io.BytesIO(archivoZip)) as thezip:
            for zipinfo in thezip.infolist():
                with thezip.open(zipinfo) as thefile:
                    #print(thefile)
                    xmlTxt = thefile.read().decode('utf-8')
                    print(xmlTxt)
                    return xmlTxt
                    with open(f"xml/zip/myFAc.xml",'w') as xml:
                        xml.write(xmlTxt)
        return result