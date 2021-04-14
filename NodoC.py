#!/usr/bin/env python
## asegura que se ejecute como codigo de python

#Nodo C. Envia a F, recibe de A

#se importan las librerias
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16

#Creacion del publisher
pub = rospy.Publisher('FuzzyC', String, queue_size=10) 
#variable a leer:
dato=0;
def callback(data):
    global dato;
    dato= data.data

#tratamiento del dato leido, se tienen 3 funciones dependiendo del valor del dato leido.
def talker():
    global dato
    rospy.init_node('NodoC', anonymous=True) 
    rospy.Subscriber('DatoInt', Int16, callback)
    while not rospy.is_shutdown():
	    #funcion bajo
	    
	    if dato<=20:
		bajo="100"
	    if dato> 20:
		if dato<40:
			bajo=-5*(dato-20)+100
			bajo= str(bajo)
	    	else:
			bajo= "0"

	    #funcion medio
	    if dato<=30 or dato>=70:
		medio="0"
	    if dato> 30 and dato<50:
		medio=5*(dato-30)
		medio= str(medio)
	    if dato >=50 and dato <70:
		medio=-5*(dato-50)+100
		medio= str(medio)

	    #funcion alto
	    if dato<=60:
		alto="0"
	    if dato> 60 and dato<80:
		alto=5*(dato-60)
		alto= str(alto)
	    if dato>= 80: 
		alto= "100"
            "publi es el string a publicar.
	    publi= "bajo= "+ bajo +" medio="+ medio +" alto= "+alto
	    rospy.loginfo(publi)
	    pub.publish("bajo="+bajo+"/medio="+ medio +"/alto="+alto)
	    rate = rospy.Rate(1) # 10hz
	    rate.sleep()     






    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    
