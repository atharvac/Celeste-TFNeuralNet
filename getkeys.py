import win32api as wapi
import win32con
import time

convDict = {"C":"C", "X":"X", "Z":"Z", "%":"L", "'":"R", "&":"U", "(":"D"}
keyList = []

for char in "CXZ %'&(":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(convDict[key])
    return keys
