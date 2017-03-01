# -*- coding: utf-8 -*-

import json
with open('resumen-accidentes-2015.json') as data_file:
    data = json.load(data_file)

print "LISTA DE ACCIDENTES PRODUCIDOS EN EL AÑO 2015."
print ""

for accidente in data:
    print "FECHA:",accidente["FECHA"]
    print "HORA:",accidente["HORA"]
    print "TIPO DE ACCIDENTE:",accidente["TIPO DE ACCIDENTE"]
    print ""
