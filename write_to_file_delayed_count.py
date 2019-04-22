import time
filepath = '//fstpdata/Team/Quality_FAR/2019/Test/textchangetext.txt'
delay = 3
x = 0
for i in list(range(1000)): 
    with open(filepath, 'w') as f:
        print('Writing to file. iteration number:{}. \n({} seconds elapsed.)\n'.format(str(i),x))
        f.write('Iteration number:{}. \n({} seconds elapsed)\n.'.format(str(i),x))
    x += delay
    time.sleep(delay)
    f.close()