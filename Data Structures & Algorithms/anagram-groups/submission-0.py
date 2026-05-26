class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index_store = {}
        # O(n) ; n = #strings
        for string in strs: # O(m log(m) + m + 1) = # O(m log (m)) = O(nm log (m))
            # m = #avg_len_strings
            s_string = "".join( # O(m)
                sorted(string) # O(m log m)
                )
            store = index_store.get(s_string, None) # O(1)
            if store is None:
                index_store[s_string] = [string]
            else:
                store.append(string)
        # O(n)
        return list(index_store.values())

# O(nm log (m))