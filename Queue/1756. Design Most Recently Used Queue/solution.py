class MRUQueue:

    def __init__(self, n: int):
        self.nums = list(range(1, n+1))
        
    def fetch(self, k: int) -> int:

        p = self.nums.pop(k-1)
        self.nums.append(p)

        return p
