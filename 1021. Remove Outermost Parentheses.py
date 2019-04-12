# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:17:47 2019

@author: Xiang
"""

class Solution:
    def removeOuterParentheses(self, S: str) -> str:


        
        group = [0]
        
        
        S_parentheses= {}
        S_parentheses['('] = 0
        S_parentheses[')'] = 0
        
        for i in range(len(S)):
            s = S[i]
            S_parentheses[s] += 1
            if S_parentheses['('] == S_parentheses[')']:
                group.append(i+1)
                S_parentheses['('] = 0
                S_parentheses[')'] = 0
            
        
        output = ''
        for j in range(len(group)-1):
            start_index = group[j] + 1
            end_index = group[j+1] - 1
            output += S[start_index:end_index]
            
        
        
        
        return output
        