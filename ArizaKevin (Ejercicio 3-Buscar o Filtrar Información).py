# -*- coding: utf-8 -*-

import json
with open('resumen-accidentes-2015.json') as data_file:
    data = json.load(data_file)

mes=int(raw_input("Introducir Número De Mes: "))

if mes < 1 or mes > 12:
    print ""
    print "El mes introducido es incorrecto. Por favor, vuelve a ejecutar el programa."
else:
    print ""
    print "LISTA DE ACCIDENTES PRODUCIDOS EN EL MES",mes,"DE 2015 EN ESPAÑA."
    print ""
    for accidente in data:
        if accidente["MES"] == mes:
            print "FECHA:",accidente["FECHA"]
            print "HORA:",accidente["HORA"]
            print "CALZADA:",accidente["CALZADA 1"]
            print ""
