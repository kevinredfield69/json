# -*- coding: utf-8 -*-

import json
with open('resumen-accidentes-2015.json') as data_file:
    data = json.load(data_file)

calzada=raw_input("INTRODUCIR NOMBRE DE UNA CALZADA (CALZADA 1): ").upper()

print ""

print "LISTA DE ACCIDENTES PRODUCIDOS EN LA CALZADA",calzada,"EN EL AÑO 2015."

print ""

for accidente in data:
    if accidente["CALZADA 1"] == calzada:
        print "FECHA:",accidente["FECHA"]
        print "HORA:",accidente["HORA"]
        print ""