class TimeMap:

    def __init__(self):
        self.timeMap = dict()
        self.queryTimes = dict()
        # dictionary of dictionaries, key = key, value = (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key][timestamp] = value
            self.queryTimes[key].append(timestamp)

        else:
            self.timeMap[key] = {timestamp: value}
            self.queryTimes[key] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        curr = self.queryTimes[key]

        low, high = 0, len(curr) - 1
        while low < high:
            mid = low + (((high - low) // 2) + 1)
            if timestamp < curr[mid]:
                high = mid - 1
            else:
                low = mid

        if timestamp < curr[low]:
            return ""
        ind = curr[low]    
        return self.timeMap[key][ind]

if __name__ == "__main__":
    obj = TimeMap()
    obj.set("foo", "bar", 1)
    print(obj.get("foo", 3))
    obj.set("foo", "bar2", 5)
    print(obj.get("foo", 7))
    print(obj.get("foo", 3))

# TC: set: O(1), get: O(logN) where N is the number of entries any specific key has
# SC: O(N), one dictionary to store the keys and values and another to store the keys to timestamps