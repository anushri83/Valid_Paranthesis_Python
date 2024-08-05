class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dict_of_bracket={"(":")","[":"]","{":"}"}
        for char in s:
            if char in dict_of_bracket.keys():
                stack.append(char)
            elif char in dict_of_bracket.values():
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    if dict_of_bracket[top] != char:
                        return False
                
        if not stack:
            return True
        else:
            return False
               


        
