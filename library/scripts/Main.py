#!/usr/bin/env python 
import ListSplit
import rospy
import booklistserver

from std_srvs.srv import *


def start():
    while(True):                    
        try:
       
            rospy.init_node('booklist')
            rospy.wait_for_service('/booklist')  
            booklist_request = rospy.ServiceProxy('/booklist',Trigger)
            books = TriggerRequest()
            result = booklist_request(books)
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)



start()






