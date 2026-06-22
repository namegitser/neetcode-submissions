class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        freq_mapper = {}
        max_freq = 0
        
        for r in range(len(s)):
            freq_mapper[s[r]] = 1 + freq_mapper.get(s[r], 0)
            max_freq = max(max_freq, freq_mapper[s[r]])

            #Need to update the window
            while (r-l+1) - max_freq > k:
                
                freq_mapper[s[l]]-=1
                l+=1

            max_len = max(max_len, r-l+1)

        return max_len
                

