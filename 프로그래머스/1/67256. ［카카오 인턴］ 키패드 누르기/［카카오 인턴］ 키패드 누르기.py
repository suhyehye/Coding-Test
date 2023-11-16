def solution(numbers, hand):
    answer = ''
    phone = {1:[0,0], 2:[0,1], 3:[0,2],
            4:[1,0], 5:[1,1], 6:[1,2],
            7:[2,0], 8:[2,1], 9:[2,2],
            "*":[3,0], 0:[3,1], "#":[3,2]}
    
    l, r = "*", "#"
    for num in numbers:
        if num in [1,4,7]:
            answer += "L"
            l = num
        elif num in [3,6,9]:
            answer += "R"
            r = num
        else:
            l_tmp = abs(phone[l][0]-phone[num][0]) + abs(phone[l][1]-phone[num][1])
            r_tmp = abs(phone[r][0]-phone[num][0]) + abs(phone[r][1]-phone[num][1])
            if l_tmp == r_tmp:
                if hand == 'right':
                    r = num
                    answer += 'R'
                else:
                    l = num
                    answer += 'L'
            elif l_tmp > r_tmp:
                r = num
                answer += 'R'
            else:
                l = num
                answer += 'L'
    return answer