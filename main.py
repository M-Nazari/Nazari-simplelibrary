# -*- coding: utf-8 -*-
"""
 main.py
Created on Fri Aug  8 10:27:52 2025

@author: /mahjoobe Nazari
"""
from library import Library

libe = Library()
libe.Add_book("1984", "George Orwell")
libe.show_books()



## there is a dirict way to implement object


if __name__ =="__main__" :
    
    lib = Library()
    
    ## add books in lib
    
    lib.Add_book("Farsi", "bashash")
    lib.Add_book("Riazi", "Ahmadi")
    lib.Add_book("Arabi", "Firoozi")
    lib.Add_book("Fisic", "Taleshi")
    lib.Add_book("Shimi", "Gholami")
    
    lib.show_books()
    
    lib.search_book("fisic")
    
    lib.remove_book("shimi")
    
    lib.show_books()