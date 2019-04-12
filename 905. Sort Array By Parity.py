# -*- coding: utf-8 -*-


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_li = [i for i in A if i%2 != 0]
        odd_li = [i for i in A if i%2 == 0]
        return odd_li + even_li 
        