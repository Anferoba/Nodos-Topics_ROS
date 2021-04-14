#!/usr/bin/env python
## asegura que se ejecute como codigo de python

#Nodo H. recibe de E,F,G y envia al arduino un porcentaje de 0 a 100

#se importan las librerias
import rospy
from std_msgs.msg import String
from std_msgs.msg import Char
from std_msgs.msg import Int16


#incializacion del publisher
pub = rospy.Publisher('DatoFinal', Int16, queue_size=10)

db= ''
di=''
df=''

#Funciones callback para almacenar los datos leidos que cada nodo envio.
def callback1(data):
    global db;
    db= data.data
    #rospy.loginfo(db)

def callback2(data):
    global di;
    di= data.data
   # rospy.loginfo(di)

def callback3(data):
    global df;
    df= data.data
    #rospy.loginfo(df)


#funcion talker, inicializa el nodo, el subscriber y publica a rta
#el valor de rta corresponde a un valor, en este caso entre 10 y 80 dado segun una logica establecida...
#... acorde a los 3 valores leidos
#el valor rta =0 ocurre si no se recibe ningun valor en algun nodo.
def talker():
    rospy.init_node('NodoH', anonymous=True) 
    rospy.Subscriber('CharE', String, callback1)    
    rospy.Subscriber('CharF', String, callback2)    
    rospy.Subscriber('CharG', String, callback3)    
    while not rospy.is_shutdown():
    
#una vez se hayan leido las tres variables

     #entradas al 10%
	if (db=="a" and df=="a") or (db=='b' and di=='a' and df=='a'):
		rta= 10
     #entradas al 20%
	if (db =="b" and df =="a" and di !='a') or (db=='a' and di=='a' and df=='m'):
		rta= 20
     #entradas al 30%
	if (db=='a' and di=='a' and df=='b') or (db=='a' and di=='m' and df!='a') or (db=='a' and di=='b' and df=='m'):
		rta= 30
	if (db=='b' and di=='a'and df!='a'):
		rta=30
     #entradas al 50%
	if (db=='a' and di=='b' and df=='b') or (db=='b' and di=='m' and df!='a') or (db=='b' and di=='b' and df=='m'):
		rta= 50
     #entradas al 80%
	if (db=='b' and di=='b' and df=='b'):
		rta= 80
     #sin entradas:
        if (db==''  or di=='' or df==''):
 		rta=0
        rospy.loginfo(rta)
    	pub.publish(rta)
        rate = rospy.Rate(0.2) # 0.2hz
        rate.sleep()


  
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    
