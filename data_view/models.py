from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext as _
import pandas as pd
from sqlalchemy import create_engine
from django.contrib.auth.models import User
import os
import csv
import psycopg2



from django.db.models import Sum, Max, Min, Avg, StdDev
from django.db.models.aggregates import StdDev
from django.views.generic import ListView

# Create your models here.
#from django.contrib.auth.models import User

class CustomBooleanField(models.BooleanField):
    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return int(value) # return 0/1

# Create your models here.


class immo_bienny(models.Model):

    id_lot = models.CharField(_("id_lot"), max_length=255, blank=True, null=True)
    nb_piece = models.IntegerField(_("nb_piece"))
    typologie = models.CharField(_("typologie"), max_length=150, default='', blank=True, null=False)
    prix_tva_reduite = models.DecimalField(_("prix_tva_reduite"), max_digits=10, decimal_places=2)
    prix_tva_normale = models.DecimalField(_("prix_tva_normale"), max_digits=10, decimal_places=2)
    prix_ht = models.DecimalField(_("prix_ht"), max_digits=10, decimal_places=2)
    prix_m2_ht = models.DecimalField(_("prix_m2_ht"), max_digits=10, decimal_places=2)
    prix_m2_ttc = models.PositiveIntegerField(_("prix_m2_ttc"))
    surface = models.DecimalField(_("surface"), max_digits=10, decimal_places=2)
    etage = models.IntegerField(_("etage"))
    orientation = models.CharField(_("orientation"),max_length=30, default='', blank=True, null=False)
    exterieur = models.BooleanField(_("exterieur"))
    balcony = models.BooleanField(_("balcony"))
    garden = models.BooleanField(_("garden"))
    parking = models.BooleanField(_("parking"))
    nom_programme = models.CharField(_("nom_programme"),max_length=100, default='', blank=True, null=False)
    ville = models.CharField(_("ville"),max_length=150, default='', blank=True, null=False)
    departement = models.IntegerField(_("departement"))
    date_fin_programme = models.DateField(_("date_fin_programme"))
    adresse_entiere = models.TextField(_("adresse_entiere"),max_length=150)
    promoteur = models.CharField(_("promoteur"),max_length=150, default='', blank=True, null=False)
    date_extraction = models.DateField(_("date_extraction"))


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_lot', 
            'nb_piece', 'typologie', 'prix_tva_reduite',
             'prix_tva_normale', 'prix_ht', 'prix_m2_ht', 'prix_m2_ttc',
               'surface', 'etage', 'orientation', 'exterieur', 'balcony', 'garden',
               'parking', 'nom_programme', 'ville', 'departement', 'date_fin_programme',
               'adresse_entiere', 'promoteur', 'date_extraction' ], name='unique_immo_name')
        ]
        db_table = 'immo_bienny'

class Contact(models.Model):
    name =models.CharField(max_length=200, default='', null=False)
    contact_number=models.IntegerField(blank=True, unique=True)
    email=models.EmailField(max_length=100, default='', null=False)
    subject=models.CharField(max_length=250)
    message = models.TextField()
    added_on =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact"
        

    #def __str__(self):
        ###db_table="immo_bienny"
