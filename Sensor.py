def chequearSensor(sensor,umbral):
    if sensor > umbral:
        print('ALARMA')
    else:
        print('Temperatura OK')

temperatura1=100
temperatura2=50

chequearSensor(temperatura1,90)
chequearSensor(temperatura2,110)