# coding=utf-8
import sys
import json

print('Hello,World!')


def testListRound(listToCheck):
    checkedList = []
    for dict in listToCheck:
        if dict.get("next") in checkedList:
            return True
        else:
            checkedList.append(dict)
    else:
        return False


dict1 = {"value": "fdsfsa", "next": None}
dict2 = {"value": "fdsfsa", "next": dict1}
dict3 = {"value": "dfsfsa", "next": dict2}
dict4 = {"value": "fdsafdsaf", "next": dict3}
dict2["next"] = dict4
listToCheck = [dict4, dict3, dict2, dict1]
print(testListRound(listToCheck))
