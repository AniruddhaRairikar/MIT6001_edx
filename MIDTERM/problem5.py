# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:53:54 2020

@author: aniru
"""

#testCase:
aDict = {'a': 1,'x': 22, 'b': 2, 'c': 3, 'd': 1, 'e': 3, 'z': 4}

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here

    keylist = [] #List containing keys with non-unique/repeating values.
    akeys = aDict.keys()

    for key, value in aDict.items():
        for key2, val2 in aDict.items():
            if key != key2 and value == val2:
                keylist.append(key) if key not in keylist else keylist
    
    uniqueKeys = sorted(list(akeys - keylist))
    
    return(uniqueKeys)
    
uniqueValues(aDict)
