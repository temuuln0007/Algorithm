class MyStack:

    def __init__(self):
        self.queue1 = []  # Primary queue
        self.queue2 = []  # Auxiliary queue

    def push(self, x: int) -> None:
        # Push the element into queue1
        self.queue1.append(x)

    def pop(self) -> int:
        # Transfer all elements from queue1 to queue2 except the last one (top of the stack)
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        
        # The last element of queue1 is the top of the stack
        top_element = self.queue1.pop(0)
        
        # Swap the names of the queues to prepare for the next operation
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return top_element

    def top(self) -> int:
        # Return the front element of queue1 (the top of the stack)
        return self.queue1[0]

    def empty(self) -> bool:
        # The stack is empty if queue1 is empty
        return len(self.queue1) == 0


# Example usage:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())    # Output: 2
print(obj.pop())    # Output: 2
print(obj.empty())  # Output: False
