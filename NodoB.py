#!/usr/bin/env python
## asegura que se ejecute como codigo de python

#Nodo B, Recibe de A. Envia a E

#se importan las librerias
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool

#creacion del publicador, nombre: FuzzyB
pub = rospy.Publisher('FuzzyB', String, queue_size=10) 
#rta es la variable leida expresada en string
rta="error"

#Funcion Callback que trata los datos leidos 
def callback(data):
    global rta
    dato= data.data
    if dato==True:
       rta= "100"
    if dato== False:
	rta="0"
    

#Talker inicializa el nodo y llama al callback. Publica en el while not.
def talker():
    #send es el string a publicar.
    send=("bajo="+"0"+"/medio="+ "0" +"/alto="+"0")
    global rta
    rospy.init_node('NodoB', anonymous=True) 
    rospy.Subscriber('DatoBool', Bool, callback)    
    while not rospy.is_shutdown():

	
	    rate = rospy.Rate(1) # 1hz
	    
            if rta=="100":
	    	send=("bajo="+"0"+"/medio="+ "0" +"/alto="+"100")
	    if rta=="0":
	    	send=("bajo="+"100"+"/medio="+ "0" +"/alto="+"0")
	    rospy.loginfo(send)
      	    pub.publish(send)
    	    rate.sleep() 





    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    
