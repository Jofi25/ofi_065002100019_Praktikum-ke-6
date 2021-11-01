# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:44:33 2021

@author: jofin
"""


def nilai(n= "0", t = 0, j = 0 ):
    while (n != "") :
        n = str(input("Masukkan nilai :"))
        j = j + 1
        if (n == ''):
            return t/(j - 1)
        elif (n== 'A'):
            print ("Nilai = 4.00")
            t += 4.00
        elif (n == 'A-'):
            print ("Nilai = 3.75")
            t += 3.75
        elif (n == 'B+'):
            print ("Nilai = 3.50")
            t += 3.50
        elif (n == 'B'):
            print ("Nilai = 3.00")
            t += 3.00
        elif (n == 'B-'):
            print ("Nilai = 2.75")
            t += 2.75
        elif (n == 'C+'):
            print("Nilai = 2.50")
            t += 2.50
        elif (n == 'C'):
            print("Nilai = 2.00")
            t += 2.00
        elif (n == 'C-'):
            print("Nilai == 1.75")
            t += 1.75
        elif (n == "D"):
            print("Nilai = 1.5")
            t += 1.75
        elif (n == 'E'):
            print("NIlai = 1.25")
            t += 1.25
        else :
            print ("Tolong Masukkan Nilai Yang Benar! ")
            
rata = nilai ()
print("Rata-ratanya adalah",rata)
        