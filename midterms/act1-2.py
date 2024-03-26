class Solution:
    def majorityElement(self, A, N):
        candidate = A[0]
        count = 1

        for i in range(1, N):
            if A[i] == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = A[i]
                    count = 1
                    
        count = 0
        for i in range(N):
            if A[i] == candidate:
                count += 1
        
        if count > N // 2:
            return candidate
        else:
            return -1