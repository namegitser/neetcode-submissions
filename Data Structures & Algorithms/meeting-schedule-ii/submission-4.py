"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        # MinHeap Approach we maintain minHeap using endTime and will keep adding in the heap the new meetings and as soon as i have a meeting start > end time of previous i vacat the room
        intervals.sort(key = lambda x: x.start)
        minHeap = []

        heapq.heappush(minHeap, intervals[0].end)

        for meeting in intervals[1:]:
            if meeting.start >= minHeap[0]:
                heapq.heappop(minHeap)

            heapq.heappush(minHeap, meeting.end)


        return len(minHeap) #Treat the nodes in minHeap like rooms where meeting endTime is pasted as value since it is minHeap i'll have room that's meeting is about to end on top. So i'll keep on checking if my new meeting start time is greater that the endTime of top of minHeap if yes, i'll give that room to new meeting if no, i'll have to assign a new room. This push will automatically find its place in minHeap



        