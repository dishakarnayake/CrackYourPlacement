class Solution(object):
    def reorganizeString(self, s):
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0)+1     
        max_key = None
        max_value = None

        for key, value in dic.items():
            if max_value is None or value > max_value:
                max_value = value
                max_key = key
        if max_value > ((len(s)+1)//2):
            return ""

        res = (len(s)) * ['']
        idx = 0
        while(max_value):
            res[idx] = max_key
            idx+=2
            max_value-=1

        for key, value in dic.items():
            if key not in res:
                val = value
                while(value):
                    if idx >= len(s):
                        idx=1
                    res[idx] = key
                    idx+=2
                    value-=1
        return "".join(res)
        