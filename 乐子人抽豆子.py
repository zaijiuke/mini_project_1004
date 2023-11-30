import random
nmb={'A':0,'B':0, 'C':0, 'D':0, 'E':0}
time=0
n=0
class Game:
    def __init__(self):
        global time,n,A,B,C,D,E,total,another,a,b,c,d,e
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        A=0
        B=0
        C=0
        E=0
        D=0
        total=[]
        another=[]
        time=0
        while A+B+C+D+E!=100:
            self.select_n_true()
            if time%5==0:
                A=0
                self.sum_a()
                time+=1
            elif time%5==1:
                B=0
                self.sum_b()
                time+=1
            elif time % 5 ==2:
                C=0
                self.sum_c()
                time+=1
            elif time%5==3:
                D=0
                self.sum_d()
                time+=1
            elif time%5==4:
                E=0
                self.sum_e()
                time+=1
        total.sort()
        total.append(A)
        total.append(B)
        total.append(C)
        total.append(D)
        total.append(E)
        total.sort()
        for cnm in range(5):
            another.append(total[cnm])
        global ta,tb,tc,td,te,nmb
        ta=0
        tb=0
        tc=0
        td=0
        te=0
        for md in range(5):
            if total[md]==A and ta==0:
                total[md]='A'
                ta+=1
            elif total[md]==B and tb==0:
                total[md]='B'
                tb+=1
            elif total[md]==C and tc==0:
                total[md]='C'
                tc+=1
            elif total[md]==D and td==0:
                total[md]='D'
                td+=1
            elif total[md]==E and te==0:
                total[md]='E'
                te+=1
            else:
                print('sb')
        if another[0]==another[1]:
            if another[1]==another[2]:
                if another[2]==another[3]:
                    nmb[total[1]]+=1
                    nmb[total[0]]+=1
                    nmb[total[2]]+=1
                    nmb[total[3]]+=1
                    nmb[total[4]]+=1
                else:
                    nmb[total[0]]+=1
                    nmb[total[1]]+=1
                    nmb[total[2]]+=1
                    self.judge_max()
            else:
                nmb[total[0]]+=1
                nmb[total[1]]+=1
                self.judge_max()
        else:
            nmb[total[0]]+=1
            self.judge_max()

    def select_n(self):
        global n
        n=random.randint(1,10)#这一行是调整选东西的范围，可以自己调着玩

    def sum_a(self):
        a.append(n)
        for i in range(len(a)):
            global A
            A+=a[i]
    
    def sum_b(self):
        b.append(n)
        for f in range(len(b)):
            global B
            B+=b[f]

    def sum_c(self):
        c.append(n)
        for pq in range(len(c)):
            global C
            C+=c[pq]
    
    def sum_d(self):
        d.append(n)
        for q in range(len(d)):
            global D
            D+=d[q]

    def sum_e(self):
        e.append(n)
        for p in range(len(e)):
            global E
            E+=e[p]

    def select_n_true(self):
            global n
            self.select_n()
            if 100-(A+B+C+D+E)<n:
                n=100-(A+B+C+D+E)
            else:
                n=n
    
    def judge_max(self):
        if another[-1]==another[-2]:
            if another[-2]==another[-3]:
                if another[-3]==another[-4]:
                    nmb[total[1]]+=1
                    nmb[total[0]]+=1
                    nmb[total[2]]+=1
                    nmb[total[3]]+=1
                    nmb[total[4]]+=1
                else:
                    nmb[total[-1]]+=1
                    nmb[total[-2]]+=1
                    nmb[total[-3]]+=1
            else:
                nmb[total[-1]]+=1
                nmb[total[-2]]+=1
        else:
            nmb[total[-1]]+=1

for ccgf in range(100000):#这一行是运行的次数
    Game()
print(nmb)