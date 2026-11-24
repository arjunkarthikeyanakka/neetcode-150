class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(speed)
        d={}
        for i in range(n):
            d[position[i]]=speed[i]
        d=dict(sorted(d.items(),reverse=1))
        # print(d)
        ans=1
        time=[]
        for i in d:
            time.append((target-i)/d[i])
        # print(time)
        for i in range(1,n):
            if time[i]<=time[i-1]:
                time[i]=time[i-1]
                # print(i,time[i],time[i-1])
                continue
            ans+=1
        return ans