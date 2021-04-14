#!/usr/bin/env python
## asegura que se ejecute como codigo de python

# Nodo D, recibe de A, Envia a G

#se importan las librerias
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32

#Publisher FuzzyD
pub = rospy.Publisher('FuzzyD', String, queue_size=10) 
#Dato recibido
dato=0;

#se guarda el dato leido
def callback(data):
    global dato;
    dato= data.data

#este talker funciona de forma parecida al talker del nodo C
def talker():
    rospy.init_node('NodoD', anonymous=True) 
    rospy.Subscriber('DatoFloat', Float32, callback)    
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
	    rate = rospy.Rate(1) # 10hz
	    rospy.loginfo("bajo= "+ bajo +" medio="+ medio +" alto= "+alto)
	    pub.publish(bajo+"/"+ medio +"/"+alto)
	    rate.sleep()  


    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    
