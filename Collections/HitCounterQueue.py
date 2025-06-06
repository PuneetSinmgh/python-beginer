from collections import deque

class HitCounter(object):

    def __init__(self):
        self.queue = deque();   

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        self.queue.append(timestamp)
        

    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        
        while len(self.queue) > 0 and timestamp - self.queue[0] >= 300:
            self.queue.popleft()
        
        
        return len(self.queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)