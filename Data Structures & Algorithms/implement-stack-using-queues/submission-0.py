class MyStack:

    def __init__(self):
        self.q = None # Empty queue

    def push(self, x: int) -> None:
        self.q = deque([x, self.q]) # new queue-node with x as first element and q as second assign this to self.q so that q point to this new structure

    def pop(self) -> int:
        top = self.q.popleft() #pop the first element 
        self.q = self.q.popleft() #update q to point to rest of the stack(queue)
        return top
        

    def top(self) -> int:
        return self.q[0] #just return the top element without changing anything
        

    def empty(self) -> bool:
        return not self.q #Return True if q is null/empty
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()