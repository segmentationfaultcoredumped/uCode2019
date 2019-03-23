from django.db import models
import datetime

# Create your models here.


class Session(models.Model):
    BOOL_CHOICES = ((True, 'Natural'), (False, 'Artificial'))

    # General info
    name = models.CharField(max_length=64)
    training = models.TextField(max_length=500, blank=True)
    date = models.DateField(default=datetime.date.today)
    place = models.CharField(max_length=32, blank=True)
    # Environment conditions
    grass = models.BooleanField(choices=BOOL_CHOICES, blank=True)
    wet = models.BooleanField(blank=True)
    temp = models.IntegerField(blank=True)
    hum = models.IntegerField(blank=True)
    additional_info = models.TextField(max_length=240, blank=True)

    def __str__(self):
        return "id:{0} name:{1}".format(str(self.pk), str(self.name))


class Athlete(models.Model):
    # General data
    nickname = models.CharField(max_length=16)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    data_consent = models.BooleanField()
    # Interest data
    age = models.IntegerField()
    foot_size = models.IntegerField()
    weight = models.IntegerField(help_text="Weight in Kg")
    height = models.IntegerField(help_text="Height in cm")

    def __str__(self):
        return "session:{0} name:{1}".format(str(self.session), str(self.nickname))


class Sensor(models.Model):
    code = models.CharField(max_length=32)

    def __str__(self):
        return "code:{0}".format(str(self.code))


class SensorAthlete(models.Model):
    id_athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    position = models.CharField(max_length=32)

    def __str__(self):
        return "athlete: {1} sensor:{2} position:{0}".format(str(self.position), str(self.id_athlete),
                                                             str(self.id_sensor))


class AthleteVest(models.Model):
    id_athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    vest_num = models.IntegerField()
    time = models.CharField(max_length=8)

    def __str__(self):
        return "athlete: {1} vest:{0} time: {2}".format(str(self.vest_num), str(self.id_athlete),
                                                        str(self.time))
