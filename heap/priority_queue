        for n in range(lo,hi+1):
            t = (n+1,n*n)
            heapq.heappush(stack,t)
        while k > 1:
            heapq.heappop(stack)
            k -= 1
        return stack[0][1]
