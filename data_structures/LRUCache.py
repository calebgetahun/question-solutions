class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    #eviction at tail node, insertion/recently used at head node
    
    def insertNodeAtHead(self, node):
        after = self.head.next
        after.prev = node
        node.next = after
        self.head.next = node
        node.prev = self.head
        return
    
    def removeNodeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.removeNodeFromList(node)
        self.insertNodeAtHead(node)

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNodeFromList(node)
            self.insertNodeAtHead(node)
        else:
            if len(self.cache) == self.capacity:
                #evict
                node = self.tail.prev
                self.removeNodeFromList(node)
                del self.cache[node.key]
            
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insertNodeAtHead(new_node)
    
    def printList(self):
        curr = self.head.next
        print("most recent")
        while curr.next:
            print(curr.key, curr.val)
            curr = curr.next
        
        print(f"least recent: to be evicted when capacity of {self.capacity}")

if __name__ == "__main__":
    lru = LRUCache(3)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    lru.printList()
    print(lru.get(5))
    lru.put(3, 3)
    lru.get(2)
    lru.put(4, 4)
    lru.printList()

# TC: O(1) for get and put operations 
# SC: O(N) for the number of key, value pairs

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
