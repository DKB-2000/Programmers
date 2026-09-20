def solution(a, b, c, d):
    answer = 0

    mdic = dict()
    mm,mn = 0,0
    for i in [a,b,c,d]:
        if i not in mdic.keys():
            mdic[i] = 1
        else:
            mdic[i] += 1

    tmp = list(mdic.keys())

    tmp_item = list(mdic.items())
    
    if len(tmp) == 1:
        answer = tmp[0] * 1111
        
    if len(tmp) == 2:
        for i,v in tmp_item:
            if v == 3:
                mm = i
            if v == 1:
                mn = i
        answer = (10*mm + mn) ** 2
        
        if mm == 0 and mn == 0:
            answer = (tmp[0] + tmp[1]) * abs(tmp[0]-tmp[1])
            
            
    if len(tmp) == 3:
        candidate = []
        for i,v in tmp_item:
            if v == 2:
                continue
            else:
                candidate.append(i)
                
        answer = candidate[0] * candidate[1]

    if len(tmp) == 4:
        answer = min(tmp)

        
    return answer