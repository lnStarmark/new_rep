# -*- coding: utf-8 -*-
"""
Program My Soft base

Created on Tue Apr 14 13:42:00 2023

@author: LN Starmark
@e-mail: ln.starmark@ekatra.io
@e-mail: ln.starmark@gmail.com
@tel:    +380 66 9805661
"""

import json
import str_common as strc

#--- path ------------------------------------------------------------------------------------
FULL_PATH_JSON = "docs\\soft.json"
FULL_PATH_JSON_SAVE = "docs\\soft_save.json"
FULL_PATH_STRING_SAVE = "docs\\soft_string_save.txt"
def selfdoc():
    print(
        ''' 
           === Any function with JSON on Python ==================================
    
           def pars_print(jsn)                      parser and print 
           def parser(jsn)                          parser in to string
           
           <Open 'data_file.json'>        
                with open(FULL_PATH_JSON, "r") as read_file:
                    data = json.load(read_file)
                print(data)
        
            <'data_file.json' to string>
                json_string = json.dumps(data)
                print(json_string)
        
            <'data_file.json' loads from string>
                dat = json.loads(json_string)
                print(dat)
        
            <'data' parser to string and print to console">
                st = parser(data)
                print(st)            
        
            <Save data>
                with open(FULL_PATH_JSON_SAVE, "w") as write_file:
                    json.dump(data, write_file)
        
            <Save after pars_print>
                with open(FULL_PATH_STRING_SAVE, "w") as write_file:
                    write_file.write(st)
    
           =======================================================================
        '''
    )

#--- intervals -------------------------------------------------------------------
tt = {"0":'',
      "1":'\t', "2":'\t\t', "3":'\t\t\t', "4":'\t\t\t\t',
      "5":'\t\t\t\t\t', "6":'\t\t\t\t\t\t', "7":'\t\t\t\t\t\t\t', "8":'\t\t\t\t\t\t\t\t'}
ENDSTR = '\n'

def set_tt(n):
    return tt[str(n)]

def Out_KEY(stroka: str, key, tab: int):
    stroka += set_tt(tab) + key + set_tt(1) + ENDSTR
    return stroka

def Out_KEY_VAL(stroka: str, key, val, tab: int, points2=0):
    if(points2 > 0):
        stroka += set_tt(tab) + key + ':' + set_tt(1) + str(val) + ENDSTR
    else:
        stroka += set_tt(tab) + key + set_tt(1) + str(val) + ENDSTR
    return stroka


def parser(jsn):
    stroka = ""

    for key1, val1 in jsn.items():
        stroka = Out_KEY(stroka, key1, 0)

        for key2, val2 in val1.items():
            stroka = Out_KEY(stroka, key2, 1)

            for key3, val3 in val2.items():
                stroka = Out_KEY(stroka, key3, 2)

                for key4, val4 in val3.items():
                    if (key4 == "name" or key4 == "vers" or key4 == "year"):
                        stroka = Out_KEY_VAL(stroka, key4, val4, 3, 1)

                    if (key4 == "prog" or key4 == "studio"):
                        stroka = Out_KEY(stroka, key4, 3)

                        for key5, val5 in val4.items():
                            stroka = Out_KEY_VAL(stroka, key5, val5, 5, 1) #####5

                    if (key4 == "parts"):
                        stroka = Out_KEY(stroka, key4, 3)

                        if (isinstance(val4, dict)):
                            for key5, val5 in val4.items():

                                if(isinstance(val5, dict)):
                                    stroka = Out_KEY(stroka, key5, 5) ######5

                                    for key6, val6 in val5.items():
                                        stroka = Out_KEY_VAL(stroka, key6, val6, 6, 1) ####6
                                else:
                                    stroka = Out_KEY_VAL(stroka, key5, val5, 5, 1) #####5
                        else:
                            stroka = Out_KEY_VAL(stroka, key4, val4, 5, 1)  #####5
    return stroka

def main():
    print()

    strc.titleprogram("Set of programs", "My small base programs for dev", "ln.starmark@gmail.com")

    selfdoc()

    strc.zagolovok("Open 'data_file.json'")

    with open(FULL_PATH_JSON, "r") as read_file:
        data = json.load(read_file)
    print(data)

    strc.zagolovok("'data_file.json' to string")
    json_string = json.dumps(data)
    print(json_string)

    strc.zagolovok("'data_file.json' loads from string")
    dat = json.loads(json_string)
    print(dat)

    strc.zagolovok("'data' parser to string and print to console")


    st = parser(data)
    print(st)



    strc.zagolovok("Save data")
    with open(FULL_PATH_JSON_SAVE, "w") as write_file:
        json.dump(data, write_file)

    strc.zagolovok("Save after pars_print")
    with open(FULL_PATH_STRING_SAVE, "w") as write_file:
        write_file.write(st)


if __name__ == "__main__":
    main()


