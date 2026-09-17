class MyHashMap:

    def __init__(self):
        self.storage = [[] for _ in range(1000001)]
        

    def put(self, key: int, value: int) -> None:
        lis = self.storage[key]
        if len(lis)==0:
            self.storage[key].append((key,value))
        else:
            for l in lis:
                if l[0]==key:
                    lis.remove(l)
                    lis.append((key,value))
                    return
            lis.append((key,value))
        

    def get(self, key: int) -> int:
        lis= self.storage[key]
        if len(lis) == 0:
            return -1
        else:
            for l in lis:
                if l[0]==key:
                    return l[1]
        return -1
        

    def remove(self, key: int) -> None:
        lis= self.storage[key]
        if len(lis) == 0:
            return
        else:
            for l in lis:
                if l[0]==key:
                    lis.remove(l)
        return 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)