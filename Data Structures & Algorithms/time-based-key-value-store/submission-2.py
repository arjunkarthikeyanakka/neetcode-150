class TimeMap:

    def __init__(self):
        self.d=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key]=[]
        self.d[key].append((timestamp,value))

    def get(self, key: str, ts: int) -> str:
        nums=self.d.get(key,None)
        if not nums or nums[0][0]>ts:
            return ""
        # print(nums)
        left,right=0,len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            if nums[mid][0]==ts:
                return nums[mid][1]
            elif nums[mid][0]<ts:
                left=mid+1
            else:
                right=mid
        # print('end',left,right)
        if nums[left][0]>ts:
            left=max(0,left-1)
        return nums[left][1]