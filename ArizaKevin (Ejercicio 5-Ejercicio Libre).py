# -*- coding: utf-8 -*-

import json
with open('resumen-accidentes-2015.json') as data_file:
    data = json.load(data_file)

mes=int(raw_input("INTRODUCIR NÚMERO DE MES: "))
ilesos=raw_input("INTRODUCIR NÚMERO DE ILESOS: ")

if mes < 1 or mes > 12:
    print ""
    print "El mes introducido es incorrecto. Por favor, vuelve a ejecutar el programa."
else:
    print ""
    print "LISTA DE ACCIDENTES PRODUCIDOS EN EL MES",mes,"DE ACUERDO A",ilesos,"ILESOS EN ESPAÑA EN 2015."
    for accidente in data:
        if accidente["MES"] == mes:
            if accidente["ILESOS"] == ilesos:
                print ""
                print "Fecha:",accidente["FECHA"]
                print "Hora:",accidente["HORA"]

                if accidente["LEVES"] and accidente["GRAVES"] == "0":
                    print "NO HA HABIDO ILESOS LEVES Y GRAVES"
                else:
                    if accidente["LEVES"] == "0":
                        print "NO HA HABIDO ILESOS LEVES."
                    else:
                        print "PERSONAS CON LESIONES LEVES:",accidente["LEVES"]
                    if accidente["GRAVES"] == "0":
                        print "NO HA HABIDO ILESOS GRAVES."
                    else:
                        print "PERSONAS CON LESIONES GRAVES:",accidente["GRAVES"]