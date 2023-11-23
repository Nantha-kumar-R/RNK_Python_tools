from random import random
def vectNormalizedcros(a,b):
    res = [(a[(i+1)%3]*b[(i+2)%3])- (b[(i+1)%3]*a[(i+2)%3]) for i in range(3)]
    mag = sum([i**2 for i in res])**0.5
    return [i/mag for i in res]
def RandPtTri(*pts):
    while True:
        w = [random() for i in range(3)]
        weight = [i/sum(w) for i in w]
        yield [sum([a*b for a,b in zip(weight,pts_col)]) for pts_col in zip(*pts)]
def RandPtRect(*pts):
    p1,p2,p3,p4 = pts
    tri1 = RandPtTri(p1,p2,p3)
    tri2 = RandPtTri(p1,p3,p4)
    c = True
    while True:
        if c:
            c = False
            yield next(tri1)
        else:
            c = True
            yield next(tri2)
def RandptQuad(*pts):
    side = []
    normal = []
    for i in range(len(pts)):
        side.append([a-b for a,b in zip(pts[i],pts[(i+1)%len(pts)])])
    for i in range(len(side)):
        normal.append(vectNormalizedcros(side[i],side[(i+1)%len(side)]))
    dot = [int(sum([a*b for a,b in zip(normal[0],i)])) for i in normal]
    if sum(dot) < -3.5 or sum(dot) > 3.5:
        oddindex = 0
    elif sum(dot) < 0:
        oddindex = dot.index(1)
    else: oddindex = dot.index(-1)
    a = RandPtRect(*[pts[(oddindex+i)% len(pts)] for i in range(1,len(pts)+1)])
    while True: yield next(a)
