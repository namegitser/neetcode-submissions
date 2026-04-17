class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)
        for s in strs:
            new = [0]*26
            for c in s:
                new[ord(c)-ord('a')]+=1
            mapper[tuple(new)].append(s) #convert to tuple as list can't be used as key

        return list(mapper.values()) #convert back to list and only return values


            