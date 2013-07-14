#!/usr/bin/python
'''
##################################################################################
#                          PHYTHON BACKLIGHT CONTROL                             #
##################################################################################
# Desarrollado por Ricardo Arana Reyes Guerrero                                  #
# twitter @rickyrish                                                             #
# Programa para gestionar el brillo de la pantalla de algunas portatiles como    #
# Acer, Dell, entre otras por medio del comando xrandr                           #
#                                                                                #
##################################################################################
Editar la ruta del archivo

'''

ruta='/home/ricardo/Documentos/pbl/dato.txt'


import time, sys, subprocess,os
import sys
nivel = sys.argv[1]

archi=open(ruta,'r')
linea=archi.readline()
linea=float(linea)
archi.close()

if linea>=0.4 and linea<=1:
  
	if nivel=="-a" and linea!=1:
		archi=open(ruta,'w')
		comando = "xrandr --output LVDS1 --brightness "+str(linea+0.1)
		proceso = subprocess.Popen(comando , shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		archi.write(str(linea+0.1))
	elif nivel=="-b" and linea!=0.4:
		archi=open(ruta,'w')
		comando = "xrandr --output LVDS1 --brightness "+str(linea-0.1)
		proceso = subprocess.Popen(comando , shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		archi.write(str(linea-0.1))
	archi.close()

