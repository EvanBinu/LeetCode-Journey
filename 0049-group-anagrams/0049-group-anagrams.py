class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for x in strs:
            c = "".join(sorted(x)) 
            if c in freq:
                freq[c].append(x)
            else:
                freq[c] = []
                freq[c].append(x)
        result=[]
        for key in freq:
            result.append(freq[key])
        return result
