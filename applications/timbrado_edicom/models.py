from django.db import models

# Create your models here.

class Cfdi(models.Model):
    id = models.BigAutoField(primary_key=True) #id = models.CharField(primary_key=True, max_length=255)  #models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateTimeField()
    #url = models.CharField(max_length=255)
    xml_name = models.CharField(max_length=255)
    xml = models.TextField()
    timbrado = models.DateTimeField()
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    uuid = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'cfdi'

        
