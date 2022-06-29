from django.db import models

# Create your models here.

class Orte(models.Model):
    plz = models.CharField(max_length=10, primary_key=True)
    ort = models.CharField(max_length=255)
    def __str__(self):
        return self.plz+" "+self.ort

class Betrieb(models.Model):
    firma = models.CharField(max_length=255)
    bemerkung = models.CharField(max_length=255, blank=True)
    telefon_zentrale = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.firma+" ("+str(self.id)+")"

class Teilnehmer(models.Model):
    edv_nummer = models.CharField(max_length=20, primary_key=True)
    plz = models.ForeignKey('Orte', on_delete=models.RESTRICT)
    vname = models.CharField(max_length=255)
    nname = models.CharField(max_length=255)
    strasse = models.CharField(max_length=255)
    def __str__(self) :
        return self.nname+', '+self.vname

class Az_zustaendigkeit(models.Model):
    kuerzel = models.CharField(max_length=20, primary_key=True)
    bezeichnung = models.CharField(max_length=255)
    dauer = models.IntegerField('Dauer in Monaten')
    def __str__(self) :
        return self.kuerzel+' - '+self.bezeichnung

class Baz(models.Model):
    ausbildungszweig = models.ForeignKey('Az_zustaendigkeit', on_delete=models.RESTRICT)
    firma = models.ForeignKey('Betrieb', on_delete=models.RESTRICT)
    def __str__(self):
        return self.firma.firma + "/" + self.ausbildungszweig.kuerzel

class Standort(models.Model):
    bezeichnung = models.CharField(max_length=255)
    firma = models.ForeignKey('Betrieb', on_delete=models.RESTRICT)
    plz = models.ForeignKey('Orte', on_delete=models.RESTRICT)
    strasse = models.CharField(max_length=255)
    telefon_zentrale = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.firma.firma + "/" + self.bezeichnung
""" 
class Teilnehmer(models.Model):
    edv_nummer = models.CharField(max_length=20, primary_key=True)
    plz = models.ForeignKey('Orte', on_delete=models.RESTRICT)
    vname = models.CharField(max_length=255)
    nname = models.CharField(max_length=255)
    strasse = models.CharField(max_length=255)
    def __str__(self):
        return self.nname+", "+self.vname """

class Bewerbung(models.Model):
    firma =  models.ForeignKey('Betrieb', on_delete=models.RESTRICT)
    teilnehmer =  models.ForeignKey('Teilnehmer', on_delete=models.RESTRICT)
    datum = models.DateField()
    reaktionszeit = models.IntegerField('Reaktionszeit in Tagen')
    def __str__(self):
        return str(self.teilnehmer)+"/ "+str(self.firma)


class Praktikum(models.Model):
    teilnehmer =  models.ForeignKey('Teilnehmer', on_delete=models.RESTRICT)
    bewerbung =  models.ForeignKey('Bewerbung', on_delete=models.RESTRICT)
    ausbildungszweig = models.ForeignKey('Az_zustaendigkeit', on_delete=models.RESTRICT)
    firma = models.ForeignKey('Betrieb', on_delete=models.RESTRICT)
    beginn = models.DateField()
    ende = models.DateField()
    def __str__(self):
        return str(self.teilnehmer)+"/ "+str(self.firma)


class Bewertung(models.Model):
    teilnehmer = models.ForeignKey('Teilnehmer', on_delete=models.RESTRICT)
    bewertung = models.IntegerField('Schulnoten 7 erfolglos')
    bemerkung = models.TextField()

class BewertungBetrieb(Bewertung):
    betrieb = models.ForeignKey('Betrieb', on_delete=models.RESTRICT)
    def __str__(self):
        return str(self.teilnehmer)+"/"+str(self.betrieb)+"/"+str(self.bewertung)
        
class BewertungPraktikum(Bewertung):
    praktikum = models.ForeignKey('Praktikum', on_delete=models.RESTRICT)
    def __str__(self):
        return str(self.teilnehmer)+"/"+str(self.praktikum.firma)+"/"+str(self.bewertung)
        
class Ansprechpartner(models.Model):
    firma = models.ForeignKey('Betrieb', on_delete=models.RESTRICT)
    anrede = models.CharField(max_length=20)
    titel = models.CharField(max_length=20, blank=True)
    vname = models.CharField(max_length=255, blank=True)
    nname = models.CharField(max_length=255)
    telefon = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    bemerkung = models.TextField(blank=True)  
    
class Aaz(models.Model):
    zustaendigkeit = models.ForeignKey('Az_zustaendigkeit', on_delete=models.RESTRICT)
    ansprechpartner = models.ForeignKey('Ansprechpartner', on_delete=models.RESTRICT)

class Ausbildung(models.Model):
    ausbildungszweig = models.ForeignKey('Az_zustaendigkeit', on_delete=models.RESTRICT)
    teilnehmer = models.ForeignKey('Teilnehmer', on_delete=models.RESTRICT)
    beginn = models.DateField()
    ende = models.DateField()
    abschluss = models.BooleanField(blank=True)
