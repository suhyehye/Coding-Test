def solution(phone_book):
    phone_book.sort(key = lambda x:(x,len(x)))
    for num, i in enumerate(phone_book[:-1]):
        if phone_book[num+1].startswith(i):
            return False
    return True
