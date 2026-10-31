class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            # Find the delimiter '#'
            j = i
            while s[j] != "#":
                j += 1
            
            # Extract length and the string itself
            length = int(s[i:j])
            start_str = j + 1
            end_str = start_str + length
            
            res.append(s[start_str:end_str])
            
            # Move index to the start of the next prefix
            i = end_str

        return res