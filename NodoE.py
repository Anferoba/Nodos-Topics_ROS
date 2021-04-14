#!/usr/bin/env python
## asegura que se ejecute como codigo de python

## Nodo E, recibe de B y envia a H
#Los nodos E,F,G funcionan de manera parecida en la recepcion de los datos
#se importan las librerias
import rospy
from std_msgs.msg import String
from std_msgs.msg import Char

#incializacion del publisher
pub = rospy.Publisher('CharE', String, queue_size=1) 
dato=""
rta=""

#callback toma el dato string y lo separa para hallar el valor bajo medio y alto enviado mediante split()
def callback(data):
    global dato;
    global rta;
    dato= data.data
    partes1= dato.split('/')
    for i in [0,1,2]:
 	rospy.loginfo(dato)
	partes2= partes1[i].split('=')
	tipo1=partes2[0]
	if tipo1=="bajo":
		bajo=int((partes2[1]))
	if tipo1=="medio":
		medio=int((partes2[1]))
	if tipo1=="alto":
		alto=int((partes2[1]))
#en este caso el valor booleano solo puede ser o 100% alto o 100% bajo
    if bajo>alto:
	rta='b'
    else:
	rta='a'

#funcion talker, inicializa el nodo, el subscriber y publica a rta
def talker():
    rospy.init_node('NodoE', anonymous=True) 
    rospy.Subscriber('FuzzyB', String, callback)    
    while not rospy.is_shutdown():
	    global rta
	    rate = rospy.Rate(0.5) #0.5z
	    rospy.loginfo(rta)
	    pub.publish(rta)
	    rate.sleep() 

    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    
