def myrange(end,start= None,step =1):
    if step == 0: raise ValueError('Step size should not be zero')
    if start != None:
        temp = start
        start = end
        end = temp
    else:
        start = 0
    if start > end and step > 0 : raise ValueError('Invalid step size')
    if start < end and step < 0 : raise ValueError('Invalid step size')
    if start > end:
        while end < start:
            yield start
            start += step
    else:
        while start < end:
            yield start
            start += step
