import math
def immediateGreater(arr,x):
    #return required ans
    
    #code here
    # ig = -1
    # min_ = arr[0]
    # for i in arr[1:]:
    #     if min_ < i and i > x:
    #         ig = i
    # return ig
    ans = -1
    diff = math.inf
    for e in arr:
        if e>x and e-x < diff:
            ans = e
            diff = e-x
            
            
    return ans

print(immediateGreater([1, 2, 3, 4, 5], 1))