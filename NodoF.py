#!/usr/bin/env python
## asegura que se ejecute como codigo de python

## Nodo F, recibe de C y envia a H
#Los nodos E,F,G funcionan de manera parecida en la recepcion de los datos

#se importan las librerias
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Char

#incializacion del publisher
pub = rospy.Publisher('CharF', String, queue_size=1) 
rta='e'

#callback toma el dato string y lo separa para hallar el valor bajo medio y alto enviado mediante split()
def callback(data):
    global rta;
 
    dato= data.data
    partes1= dato.split('/')
    for i in [0,1,2]:

	partes2= partes1[i].split('=')
	tipo1=partes2[0]
	if tipo1=="bajo":
		bajo=int((partes2[1]))
	if tipo1=="medio":
		medio=int((partes2[1]))
	if tipo1=="alto":
		alto=int((partes2[1]))

#opciones para respuesta baja
    if  bajo>alto and bajo> medio:
	rta='b'
#opciones para alto'
    if medio< alto and bajo<alto :
	rta= 'a'
#opciones para medio
    if (medio>alto and medio> bajo) or (bajo==medio and medio>alto) or (alto==medio and medio>bajo) :
        rta= 'm'
    

#funcion talker, inicializa el nodo, el subscriber y publica a rta
def talker():
    global rta;
    rospy.init_node('NodoF', anonymous=True) 
    rospy.Subscriber('FuzzyC', String, callback)    
    while not rospy.is_shutdown():
    	rate = rospy.Rate(0.5) #0.5z
    	rospy.loginfo(rta)
    	pub.publish(rta)
    	rate.sleep()  





    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    
