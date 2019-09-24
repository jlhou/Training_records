import time
t= time.time()
print("{}{:02}".format(time.localtime(t).tm_year,time.localtime(t).tm_mon))#利用{}和format来给予数值