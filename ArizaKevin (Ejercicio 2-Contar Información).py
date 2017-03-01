# -*- coding: utf-8 -*-

import json
with open('resumen-accidentes-2015.json') as data_file:
    data = json.load(data_file)

lista=[]

for accidente in data:
    lista.append(accidente["MES"])

print "EL MES DE ENERO DE 2015 TUVO",lista.count(1),"ACCIDENTES TOTALES."
print "EL MES DE FEBRERO DE 2015 TUVO",lista.count(2),"ACCIDENTES TOTALES."
print "EL MES DE MARZO DE 2015 TUVO",lista.count(3),"ACCIDENTES TOTALES."
print "EL MES DE ABRIL DE 2015 TUVO",lista.count(4),"ACCIDENTES TOTALES."
print "EL MES DE MAYO DE 2015 TUVO",lista.count(5),"ACCIDENTES TOTALES."
print "EL MES DE JUNIO DE 2015 TUVO",lista.count(6),"ACCIDENTES TOTALES."
print "EL MES DE JULIO DE 2015 TUVO",lista.count(7),"ACCIDENTES TOTALES."
print "EL MES DE AGOSTO DE 2015 TUVO",lista.count(8),"ACCIDENTES TOTALES."
print "EL MES DE SEPTIEMBRE DE 2015 TUVO",lista.count(9),"ACCIDENTES TOTALES."
print "EL MES DE OCTUBRE DE 2015 TUVO",lista.count(10),"ACCIDENTES TOTALES."
print "EL MES DE NOVIEMBRE DE 2015 TUVO",lista.count(11),"ACCIDENTES TOTALES."
print "EL MES DE DICIEMBRE DE 2015 TUVO",lista.count(12),"ACCIDENTES TOTALES."




