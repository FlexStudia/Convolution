# coding: utf-8

import math


def list_compare(list1, list2, accuracy):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if math.fabs(list1[i] - list2[i]) > accuracy:
            return False
    return True
