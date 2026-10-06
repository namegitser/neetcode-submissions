class MedianFinder:
    #initialize 2 heaps - [large]minHeap(to store large values) -                          [small]maxHeap(to store small values)
    #think like we are dividing our sorted list so that each i have max from left side, min from right to easily get median

    #since, python don't have maxHeap we push -1*element
    def __init__(self):
        self.small, self.large = [], [] 

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)
        if self.small and self.large and (self.small[0] > self.large[0]):
            val = self.small[0]
            heapq.heappop_max(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = self.small[0]
            heapq.heappop_max(self.small)
            heapq.heappush(self.large, val)

        elif len(self.large) > len(self.small) + 1:
            val = self.large[0]
            heapq.heappop(self.large)
            heapq.heappush_max(self.small, val)

        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(self.small[0])

        elif len(self.small) < len(self.large):
            return float(self.large[0])

        return (self.small[0] + self.large[0])/2.0

        
        