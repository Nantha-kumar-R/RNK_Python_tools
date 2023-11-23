filename = input('Enter Log file name: ')
def infofn(fn):
    def infoinner(*args,**kwds):
        with open(filename,'a') as txtfile:
            txtfile.write(fn.__name__ + ' Begings.\n')
        i = fn(*args,**kwds)
        with open(filename,'a') as txtfile:
            txtfile.write(fn.__name__ + ' Ends.\n')
        return i
    return infoinner
import time
def timestamp(fn):
    def timeinner(*args,**kwds):
        start = time.time()
        with open(filename,'a') as txtfile:
            txtfile.write('Start Time: ' + str(time.asctime()) + '\n')
        i = fn(*args,**kwds)
        with open(filename,'a') as txtfile:
            txtfile.write('Duration: ' + str(time.time()-start) + ' sec\n' +'End Time: ' + str(time.asctime()) + '\n')
        return i
    timeinner.__name__ = fn.__name__
    return timeinner
