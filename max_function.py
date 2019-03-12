
#import math



def maxnums(*args):
    argslist = list(args)
    result = filter(lambda item: isinstance(item, int), argslist)

    resultlist = list(result)
    resultlist.sort(reverse=True)
    return resultlist[0]
   # return max(args)

print(maxnums(1,3,4,16,'john',2,7,4,3))
