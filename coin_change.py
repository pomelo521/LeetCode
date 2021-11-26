# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    
        que = deque()
        seen = set()
        
        que.append(amount)
        seen.add(amount)
        count = 0
        
        while que:
            count += 1
            for _ in range(len(que)):
                amountLeft = que.popleft()
                print(amountLeft, count)
                
                if amountLeft == 0:
                    return count - 1
                
                for coin in coins:
                    if coin <= amountLeft and amountLeft - coin not in seen:
                        que.append(amountLeft - coin)
                        seen.add(amountLeft - coin)
        
        return -1
