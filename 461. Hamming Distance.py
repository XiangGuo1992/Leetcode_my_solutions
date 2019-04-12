# -*- coding: utf-8 -*-


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]

        if len(x_bin) > len(y_bin):
            y_bin = '0'*(len(x_bin) - len(y_bin)) + y_bin
        else:
            x_bin = '0'*(len(y_bin) - len(x_bin)) + x_bin

        return len([i for i in range(len(x_bin)) if x_bin[i]!=y_bin[i]])
    
    
        # better way
        # return bin(x^y).count('1')