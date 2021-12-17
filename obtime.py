import datetime


def otime() :
    jour = "Nous sommes le " + str(datetime.datetime.now())
    return jour

def clic(nombre):
    nombre += 1
    return nombre
