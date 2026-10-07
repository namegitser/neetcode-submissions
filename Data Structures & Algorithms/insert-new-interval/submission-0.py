class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        i = 0
        while i< len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1

        #loop ends means somewhere i have hit overlap newInterval[0] < interval[i][1] An overlap occurs as long as the current interval starts before or at the same time the new interval ends: intervals[i][0] <= newInterval[1].
        while i< len(intervals) and intervals[i][0] <= newInterval[1]:
            # res.append([min((interval[i][0]), (newInterval[0])), max(interval[i][1]), (newInterval[1])])
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i+=1
        res.append(newInterval) #append after catching the whole boundary

        
        while i < len(intervals):
            res.append(intervals[i])
            i+=1
        
        
        return res
        
        