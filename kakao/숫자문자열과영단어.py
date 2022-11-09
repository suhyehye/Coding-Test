def solution(s):
    answer = ""
    dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    st = ""
    
    for i in s:
        try : 
            int(i)
            answer = answer + i
        except : 
            st = st +i
            if st in dict.keys():
                answer = answer + str(dict[st])
                print(dict[st])
                st = ""
            
            
    answer = int(answer)
    return answer
