class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x : x[0])
        merged = [intervals[0]]

        for curr_interval in intervals[1:]:
            prev_start, prev_end = merged[-1]
            curr_start, curr_end = curr_interval

            if prev_end >= curr_start:
                merged[-1][1] = max(curr_end, prev_end)

            else:
                merged.append(curr_interval)

        return merged



        