#!/usr/bin/env python 

import rospy 
from std_srvs.srv import Trigger,TriggerResponse

def trigger_response(request):
    with open("stock.txt","r") as f:
         lines=f.read()         
    return TriggerResponse(
        success = True,
        message = lines
)

    
rospy.init_node('booklist')
my_service = rospy.Service('/booklist',Trigger,trigger_response)
rospy.spin()
