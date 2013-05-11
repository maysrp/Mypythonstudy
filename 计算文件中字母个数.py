#!/usr/bin/env python
def shu():
    k=raw_input('Please Enter your file directory:').strip()
    try:
        fk=open(k,'r')
    except Exception,e:
        print e
        print 'Please Try Again!!'
        shu()
    kk=[]
    kk=26*[0]
    for eachLine in fk:
        for ik in eachLine:
                if ik=='a'or ik=='A':
                    kk[0]+=1
                elif ik=='b'or ik=='B':
                    kk[1]+=1
                elif ik=='c'or ik=='C':
                    kk[2]+=1
                elif ik=='d'or ik=='D':
                    kk[3]+=1
                elif ik=='e'or ik=='E':
                    kk[4]+=1
                elif ik=='f'or ik=='F':
                    kk[5]+=1
                elif ik=='g'or ik=='G':
                    kk[6]+=1
                elif ik=='h'or ik=='H':
                    kk[7]+=1
                elif ik=='i'or ik=='I':
                    kk[8]+=1
                elif ik=='j'or ik=='J':
                    kk[9]+=1
                elif ik=='k'or ik=='K':
                    kk[10]+=1
                elif ik=='l'or ik=='L':
                    kk[11]+=1
                elif ik=='m'or ik=='M':
                    kk[12]+=1
                elif ik=='n'or ik=='N':
                    kk[13]+=1
                elif ik=='o'or ik=='O':
                    kk[14]+=1
                elif ik=='p'or ik=='P':
                    kk[15]+=1
                elif ik=='q'or ik=='Q':
                    kk[16]+=1
                elif ik=='r'or ik=='R':
                    kk[17]+=1
                elif ik=='s'or ik=='S':
                    kk[18]+=1
                elif ik=='t'or ik=='T':
                    kk[19]+=1
                elif ik=='u'or ik=='U':
                    kk[20]+=1
                elif ik=='v'or ik=='V':
                    kk[21]+=1
                elif ik=='w'or ik=='W':
                    kk[22]+=1
                elif ik=='x'or ik=='X':
                    kk[23]+=1
                elif ik=='y'or ik=='Y':
                    kk[24]+=1
                elif ik=='z'or ik=='Z':
                    kk[25]+=1
    b=list('abcdefghijklmnopqrstuvwxyz')
    for num in range(26):
            print b[num],'=',kk[num]
    fk.close()
    AG=raw_input('again? Y/N').strip()
    if AG=='Y'or AG=='y':
        shu()
    else:
        print 'Thanks!'
        return
shu()

