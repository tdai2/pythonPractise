# coding=utf-8
import sys
import json
import random
import copy

print('Hello,World!')


class SingleListNode(object):
    "single node"
    def __init__(self,_item,_next=None):
        self.item = _item
        self.next = _next

# class SingleLinkedList(object):
#     def __init__(self):
#         self.head = None
#
#     def is_empty(self):
#         return self.head is None


def checkLoopInLinkedList(linkedListToCheck):
    if linkedListToCheck:

    else:
        return None








def testListRound(listToCheck):
    checkedList = []
    for dict in listToCheck:
        if dict.get("next") in checkedList:
            return True
        else:
            checkedList.append(dict)
    else:
        return False


# dict1 = {"value": "fdsfsa", "next": None}
# dict2 = {"value": "fdsfsa", "next": dict1}
# dict3 = {"value": "dfsfsa", "next": dict2}
# dict4 = {"value": "fdsafdsaf", "next": dict3}
# dict2["next"] = dict4
# listToCheck = [dict4, dict3, dict2, dict1]
listToCheck = []
previousNode = None
for index in range(0,4):
    value = random.randint(1,10000000)
    # next = previousNode
    # node = {}
    node = {"value":value,"next":next}
    previousNode = copy.deepcopy(node)
    next = previousNode
    listToCheck.insert(0,node)

listToCheck[1]["next"] = listToCheck[3]

print(testListRound(listToCheck))


# 环入口查找
# https://blog.csdn.net/yangruxi/article/details/80333000