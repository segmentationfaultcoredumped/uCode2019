import os
from django.core.management.base import BaseCommand
from data.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        make_database()


def make_database():
    path = os.getcwd()
    add_sensors(path + '/data/sensor.data')
    add_sessions(path + '/data/session.data')
    add_athletes(path + '/data/athlete.data')
    add_sensors_athletes(path + '/data/sensorathlete.data')
    add_athletes_vests(path + '/data/athletevest.data')


def add_sensors(filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            params = line.split('|')
            add_sensor(i, params[0])


def add_sessions(filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            params = line.split('|')
            add_session(i, params[0], params[1], params[2], params[3], params[4], params[5], params[6],
                       params[7], params[8], params[9])


def add_athletes(filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            params = line.split('|')
            add_athlete(i, params[0], params[1], params[2], params[3], params[4], params[5], params[6],
                       params[7])


def add_sensors_athletes(filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            params = line.split('|')
            add_sensor_athlete(i, params[0], params[1], params[2], params[3])


def add_athletes_vests(filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            params = line.split('|')
            add_athlete_vest(i, params[0], params[1], params[2], params[3])


def add_sensor(index, code):
    degree = Sensor(code=code)
    degree.id = index
    degree.save()


def add_session(index, name, training, date, place, grass, wet, temp,
                hum, additional_info):
    session = Session(name=name, training=training, date=date, place=place,
                      grass=grass, wet=wet, temp=temp, hum=hum,
                      additional_info=additional_info)
    session.id = index
    session.save()


def add_athlete(index, nickname, session, data_consent, age, foot_size,
                weight, height):
    athlete = Athlete(nickname=nickname, session=session, data_consent=data_consent,
                      age=age, foot_size=foot_size, weight=weight, height=height)
    athlete.id = index
    athlete.save()


def add_sensor_athlete(index, id_athlete, id_sensor, position):
    sensor_athlete = SensorAthlete(id_athlete=id_athlete, id_sensor=id_sensor, position=position)
    sensor_athlete.id = index
    sensor_athlete.save()


def add_athlete_vest(index, id_athlete, vest_num, time):
    athlete_vest = AthleteVest(id_athlete=id_athlete, vest_num=vest_num, time=time)
    athlete_vest.id = index
    athlete_vest.save()
