class Solution:

    delim = "@"

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            l = len(s)
            out += f"{l}{self.delim}{s}"
        #print(out)
        return out


    def decode(self, s: str) -> List[str]:
        out = []

        i = 0
        while i < len(s):
            #print(out)
            s_len = 0
            j = i + 1
            while j < len(s):
                #print(s[j])
                if s[j] is self.delim:
                    s_len = int(s[i:j])
                    #print(f"len: {s_len}, str: {s[j + 1:j + s_len + 1]}")
                    out.append(s[j + 1:j + s_len + 1])
                    break
                j += 1
            #print(f"changing 'i' to {j} + {s_len}")
            i = j + s_len + 1

        return out
