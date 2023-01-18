from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for city in cities:
        city = city.lower()
        if city not in cache and len(cache) < cacheSize:
            cache.append(city)
            answer += 5
        elif city not in cache and len(cache) == cacheSize:
            cache.append(city)
            cache.popleft()
            answer += 5
        else:
            cache.remove(city)
            answer += 1
            cache.append(city)
        
    return answer
