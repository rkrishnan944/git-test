#!/usr/bin/env python

from library.srv import BookData,BookDataResponse
import rospy

def handle_book_data(req):
    books = {1:"Harry Potter", 2:"Jane Eyre"}
    print ("Returning Book ID:%s" %(req.ID))
    return BookDataResponse(books[req.ID])

def book_data_server():
    rospy.init_node('book_data_server')
    s = rospy.Service('book_data', BookData, handle_book_data)
    print ("Ready to print details of books")
    rospy.spin()

if __name__ == "__main__":
    book_data_server()
