from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    n_prices = len(prices)
    
    for i in range(n_prices-1):
        n = prices.popleft()
        answer.append(n_prices-i-1)
        for idx,j in enumerate(prices):
            if n > j:
                answer.pop()
                answer.append(idx+1)
                break
        
    answer.append(0)   
    return answer
