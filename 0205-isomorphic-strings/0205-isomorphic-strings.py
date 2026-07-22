class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        map_s_t = {}
        map_t_s = {}

        for chars, chart in zip(s, t):
            
            if chars in map_s_t:
                if map_s_t[chars] != chart:
                    return False

            else:
                map_s_t[chars] = chart


            if chart in map_t_s:
                if map_t_s[chart] != chars:
                    return False

            else:
                map_t_s[chart] = chars

        return True
