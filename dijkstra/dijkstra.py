import heapq
class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        d = dict()
        dest = dict()
        dest[start] = 1.00000
        for i,tp in enumerate(edges):
            if tp[0] in d:
                d[tp[0]].append((tp[1],succProb[i]))
            else:
                d[tp[0]] = [(tp[1], succProb[i])]
                
            if tp[1] in d:        
                d[tp[1]].append((tp[0],succProb[i]))
            else:
                d[tp[1]] = [(tp[0], succProb[i])]

        if start not in d:
            return 0.00000

        
        
        visited = set()
        heap = []
        heap.append((-1.00000,start))
        cur = start
        while heap:
            # print heap
            tmp = heapq.heappop(heap)
            prob,cur =  tmp[0], tmp[1]
            if cur in visited:
                continue
            if cur == end:
                return -prob
            visited.add(cur)
            if cur not in d:
                return 0.00000
            for tp in d[cur]:
                if tp[1] not in visited:
                    heapq.heappush(heap,(tp[1]*prob,tp[0]))
        return 0.00000
