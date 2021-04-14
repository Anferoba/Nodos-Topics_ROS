#!/usr/bin/env python
## asegura que se ejecute como codigo de python

## Nodo G, recibe de D y envia a H
#Los nodos E,F,G funcionan de manera parecida en la recepcion de los datos

#se importan las librerias
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Char

#incializacion del publisher
pub = rospy.Publisher('CharG', String, queue_size=1) 
rta="";

#callback toma el dato string y lo separa para hallar el valor bajo medio y alto enviado mediante split()
def callback(data):

    global rta;
    dato= data.data
    partes= dato.split('/')
    bajo=float((partes[0]))

    medio=float((partes[1]))

    alto=float((partes[2]))



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
    rospy.init_node('NodoG', anonymous=True) 
    rospy.Subscriber('FuzzyD', String, callback)    
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
    
