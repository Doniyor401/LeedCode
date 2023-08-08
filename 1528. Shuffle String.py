class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        str_dict = {}
        string = ''
        
        count = 0
        for i in indices:
            str_dict[i] = s[count]
            count += 1
            
        for e in range(len(s)):
            string += str_dict[e]
            
        return string