
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Created on Tue Aug 11 14:48:00 2020

@author: ln.starmark@gmail.com
         ln.starmark@ekatra.io
"""
import os
import time
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

import codecs
#sys.stdout = codecs.getwriter('utf-8')(sys.stdout,'replace')
import locale
import argparse

'''
import math
import random
import re

#import numpy
import scipy
import matplotlib
import timeit
import tkinter
'''

MULT1 = 20
MULT2 = 22

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def nextwork(mult = MULT1):
    print('\n')
    print('----'*mult)
    input('NEXT: Input Enter key...')
    print('----'*mult)

def nextworkname(n,nm, mult = MULT1):
    s='Work %d: %s' % (n,nm)
    print('\n')
    print('----'*mult)
    print(s)
    print('----'*mult)

def planwork(sps, mult = MULT1):
    print()
    print('----'*mult)
    print('--- Plan')
    i=1
    for s in sps: 
        print(i,'\t'+s)
        i+=1;
    print('----'*mult)    

def nextpunct(title, mult = MULT1):
    lns = len(title)
    addstr = ' '*(4*mult-lns-4-2)
    print('\n')
    print('----'*mult)
    print('|   %s %s|' % (title,addstr))
    print('----'*mult)
    s = '    '*(mult-3)+'NEXT: --> _/'
    input(s)

def titleprogram(target,title,author, mult = MULT1):
    print('----'*mult)
    print('Platform used: ', sys.platform)
    print('Begin program: ', sys.argv[0])
    print('System time:   ', time.asctime())
    print('Author:        ', author)
    print('Target:        ', target)
    print('Title:         ', title)
    print('----'*mult)
    syscode = sys.getdefaultencoding()
    print("syscode = " + syscode)
    localecode = locale.getpreferredencoding()	
    print("localecode = " + localecode)
    print("sys.stdout.encoding = " + sys.stdout.encoding)    
    print('----'*mult)    

def titl(stroka, mult = MULT2):
    print("----"*mult)
    print("--- Python module( %s )" % stroka)
    print("----"*mult)

def zagolovok(txt):
    '''Function output headers and titles
    '''
    lenstr = len(txt)
    s = '=' * (64 - lenstr)
    if(lenstr == 0):
        print("\n=============={}{}\n".format(txt,s))
    else:    
        print("\n=== Section: {} {}\n".format(txt,s)) 

def underline(char, n):
    '''Function output char underline "_"
    '''
    print(char*n)

def print_list_column(lst, n, delim, title=''):
    '''Function output list in N columns 
    '''
    print()
    print(title)
    cnt = 0
    for it in lst:
        print('%6s' % it, end=delim)
        cnt += 1
        if cnt == n:
            print()
            cnt = 0
    print()

def print_list(lst, title=''):
    '''Function output list in N columns 
    '''
    print()
    print(title)
    for it in lst:
        print(it)
    print()

#--- lst: [list, tuple], columns: int, len: int <- {max lenght string}
def Print_table(lst, columns, len):
    frm_t = "%"+str(len)+"s\t"
    frm_n = "%"+str(len)+"s\n"
    cnt = 1
    for el in lst:
        if (cnt % columns == 0):
             print(frm_n % el)
        else:
            print(frm_t % el, end="")
        cnt += 1
    print("\n")

def paramout(obj, clmn, name):
    titl(name)
    quant = 0
    cnt = 0
    cnt_ = 0
    cnt__ = 0
    par = []
    par_ = []
    par__ = []
    for it in dir(obj):
        if not it.startswith('_'):
            par.append(it)
            cnt += 1
            if cnt == clmn:
                cnt = 0
        if it.startswith('_') and not it.startswith('__'):
            par_.append(it)
            cnt_ += 1
            if cnt_ == clmn:
                cnt_ = 0
        if it.startswith('__'):
            par__.append(it)
            cnt__ += 1    
            if cnt__ == clmn:
                cnt__ = 0

        param = []
        param.append(par)
        param.append(par_)
        param.append(par__)

    for par in param:
        cn = 0
        cnt = 0
        for it in par:
            print('%40s ' % it, end=' ')
            cn += 1
            cnt += 1
            if cn == clmn:
                cn = 0
                print()
        print()
        print("Quant param = %4d" % (cnt), end='\n\n')
        quant += cnt

    print()        
    print("Quantity parameters in %s = %4d" % (name,quant), end='\n\n')
    return quant

    
def selfdoc():
    print(
    ''' 
       === Any function Python ===============================================
               
       In modules:

       - os, sys, time, codecs, locale,argparse,  main modules
       - math, random, re                         add modules
       - numpy, scipy, matplotlib, timeit, tkinter
       - clear()                                  cls
       - nextwork(mult = MULT1)                   prompt continue
       - nextpunct(title, mult = MULT1)           prompt continue by punct
       - titleprogram(target,title, mult = MULT1) common title program
       - titl(stroka, mult = MULT2)               kurtz title
       - paramout(obj, clmn, name)                printing parameters
       - zagolovok(txt)                           title in text
       - underline(char, n)                       output char '_'
       - print_list_column(lst,n,delim,title='')  output list in N columns
        
       =======================================================================
    '''        
    )

def main():
    print(os.name)
    pass

if __name__ == "__main__":
    main()

    titleprogram("Python","STR Common Modules", "ln.starmark@gmail.com")
 
    selfdoc()

    '''
    nextpunct("Sqare values")
    ls = [x**2 for x in range(1,101)]
    print_list_column(ls, 9, '\t', title='List square values')
    

    nextpunct("Printing parameters module (by numb)")

    err = 0
    while err == 0:
        print(
        """
        Gen numb for printing Python Module 
        
        os              - 1
        sys             - 2
        time            - 3
        codecs          - 4
        locale          - 5
        argparse        - 6 
        math            - 7
        random          - 8
        re              - 9
        numpy           - 10
        scipy           - 11
        matplotlib      - 12
        timeit          - 13
	tkinter         - 14 
        """
        )
        al = 0
        sn = input("Numb module -> ")
        if sn.isdigit() and (int(sn) in range(15)):
            n = int(sn)
            if n == 1: 
                al = paramout(os, 2, "os")
            elif n == 2:    
                al = paramout(sys, 2, "sys")
            elif n == 3:    
                al = paramout(time, 2, "time")
            elif n == 4:    
                al = paramout(codecs, 2, "codecs")
            elif n == 5:    
                al = paramout(locale, 2, "locale")
            elif n == 6:    
                al = paramout(argparse, 2, "argparse")    
            elif n == 7:    
                al = paramout(math, 2, "math")
            elif n == 8:    
                al = paramout(random, 2, "random")
            elif n == 9:    
                al = paramout(re, 2, "re")
            elif n == 10:    
                al = paramout(numpy, 2, "numpy")    
            elif n == 11:    
                al = paramout(scipy, 2, "scipy")
            elif n == 12:    
                al = paramout(matplotlib, 2, "matplotlib")
            elif n == 13:    
                al = paramout(timeit, 2, "timeit")
            elif n == 14:    
                al = paramout(tkinter , 2, "tkinter")
        else:
            err = 1
            print("Err: Bad number module")

        if err == 0: 
            print()

    '''
