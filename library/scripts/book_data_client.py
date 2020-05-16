#!/usr/bin/env python

import sys
import rospy
from library.srv import BookData

def book_data_client(ID):
    rospy.wait_for_service('book_data')
    try:
        book_data = rospy.ServiceProxy('book_data', BookData)
        resp = book_data(ID)
        return (resp.Name)
    except rospy.ServiceException, e:
        print ("Service call failed: %s"%e)

def usage():
    return "%s [ID]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        ID = int(sys.argv[1])
    else:
        print (usage())
        sys.exit(1)
    print ("Requesting Book ID:%s"%(ID))
    print ("Book Name: %s"%(book_data_client(ID)))
