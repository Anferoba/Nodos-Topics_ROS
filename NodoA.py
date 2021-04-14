#!/usr/bin/env python
## asegura que se ejecute como codigo de python

#Nodo A. Envia datos a B, C D. Recibe del arduino.

#se importan las librerias
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
from std_msgs.msg import Int16
from std_msgs.msg import Float32

#variables de los valores bool, entero y flotante
db= 0
di= 0
df=0.0
#creacion de los tres publisher
pub = rospy.Publisher('DatoBool', Bool, queue_size=10)
pub2 = rospy.Publisher('DatoInt', Int16, queue_size=10)
pub3 = rospy.Publisher('DatoFloat', Float32, queue_size=10) 


#Callback# guarda el valor booleano, entero o float segun corresponde.

def callback1(data):

    global db;
        
    db= data.data
    if  db ==1:
	db= True
    else:
	db= False

    

def callback2(data):

    global di;
        
    di= data.data
    

def callback3(data):

    global df;
        
    df= data.data
    

# Funcion en la cual se ejecuta el nodo, se llama a los callback y se publica.
def talker():
	global db
	global di
	global df
	#3 subscriber, por los topics con los que se comunica el nodo arduino con este nodo.
	rospy.init_node('NodoA', anonymous=True) 
	rospy.Subscriber('databool', Int16, callback1)
	rospy.Subscriber('dataint', Int16, callback2)
	rospy.Subscriber('datafloat', Float32, callback3)
	while not rospy.is_shutdown():
	
		rospy.loginfo("db: %s",db)
		rospy.loginfo("di: %s",di)
		rospy.loginfo("df: %s",df)
		pub.publish(db)
		pub2.publish(di)
		pub3.publish(df)
				
		rate = rospy.Rate(10) # 10hz  (frecuencia del nodo)   
	        rate.sleep()

#inicia la funcion de talker.
    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    
