import time
def clockfn(fnptr):
    def clockwraper(*args,**kwargs):
        print('Start Time:',time.asctime())
        start = time.time()
        i = fnptr(*args, **kwargs)
        print('RunTime: ', time.time()-start,'sec','\nEnd Time:',time.asctime(),'\n')
        return i
    return clockwraper


        
        
