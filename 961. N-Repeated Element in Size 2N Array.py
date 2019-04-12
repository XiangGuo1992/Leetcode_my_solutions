# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 20:58:26 2019

@author: Xiang
"""



class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        import collections
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k