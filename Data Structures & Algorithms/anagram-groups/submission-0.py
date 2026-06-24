class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create empty dict {key: [values]}
        #iterate strs
            #sort current str chars and if str is in dict then add word to values
            #if not then create new element in dict and add value
        #get all values and return

        str_dict = {}
        for s in strs:
            ss = "".join(sorted(s))
            str_dict.setdefault(ss, []).append(s)
        
        matrix = [v for v in str_dict.values()]
        return matrix
        