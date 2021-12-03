from django.db import models

class Afocha(models.Model):
    """
    A model to represent the Afochas
    to which the deceased Person belongs
    to.
    """
    name = models.CharField("Afocha Name", max_length=200, unique=True, blank=False)

    def __str__(self):
        return self.name

class Deceased(models.Model):
    """
    This models holds a data about the
    Deceased Person. Information like
    Name, Gender, grave_number, Longitude, and
    Latitude
    """
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]

    efname = models.CharField("English First Name", max_length=100, blank=False)
    elname = models.CharField("English Last  Name", max_length=100, blank=False)

    role_num = models.IntegerField("Role Number", unique=True,)
    gender = models.CharField("Gender", max_length=10, choices=GENDER_CHOICES)
    dod = models.DateField("Date of Death")
    grave_number = models.IntegerField("Grave Number")

    afocha_name = models.ForeignKey(Afocha, on_delete=models.CASCADE, blank=False)

    qebele = models.IntegerField("Qebele")

    lon = models.FloatField()
    lat = models.FloatField()


    def __str__(self):
        return f"{self.efname} {self.elname}"

    def full_name(self):
        return str(self)
