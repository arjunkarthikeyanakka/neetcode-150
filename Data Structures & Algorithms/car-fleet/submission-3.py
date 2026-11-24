class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        intuition: sorted cars in desc order by their position, then calculate time taken by each of those cars to reach target, and then in the sorted order, find if the car down the road is reaching the target quicker then it means its gonna end up in the same cluster as the car ahead of it, and change its value to the car ahead of it - the time taken that is. Now, you inc local var everytime you find a faster car with later position, you'll have the ans.
        Time = O(NlogN), space = O(N)
        '''
        n=len(speed)
        d={}
        for i in range(n):
            d[position[i]]=speed[i]
        d=dict(sorted(d.items(),reverse=1))
        ans=1
        time=[]
        for i in d:
            time.append((target-i)/d[i])
        for i in range(1,n):
            if time[i]<=time[i-1]:
                time[i]=time[i-1]
                continue
            ans+=1
        return ans