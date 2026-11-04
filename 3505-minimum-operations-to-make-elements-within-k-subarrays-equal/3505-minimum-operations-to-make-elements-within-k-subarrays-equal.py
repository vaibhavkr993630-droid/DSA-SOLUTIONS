class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        from sortedcontainers import SortedList
        n=len(nums)
        lo=SortedList()
        hi=SortedList()
        sl=0
        sh=0
        cst=[0]*(n-x+1)

        def fix():
            nonlocal sl,sh
            while len(lo)>len(hi)+1:
                v=lo.pop()
                sl-=v
                hi.add(v);sh+=v
            while len(hi)>len(lo):
                v=hi.pop(0)
                sh-=v
                lo.add(v); sl+=v

        for i in range(n):
            v=nums[i]
            if lo and v<=lo[-1]:
                lo.add(v);sl+=v
            else:
                hi.add(v);sh+=v
            if i>=x:
                old=nums[i-x]
                if old<=lo[-1]:
                    lo.remove(old);sl-=old
                else:
                    hi.remove(old);sh-=old
            fix()
            if i>=x-1:
                m=lo[-1]
                cst[i-x+1]=m*len(lo)-sl+sh-m*len(hi)

        INF=float('inf')
        prev=[0]*(n+1)
        for j in range(1,k+1):
            cur=[INF]*(n+1)
            for i in range(1,n+1):
                cur[i]=cur[i-1]
                if i>=x and prev[i-x]!=INF:
                    t=prev[i-x]+cst[i-x]
                    if t<cur[i]: cur[i]=t
            prev=cur
        return prev[n]