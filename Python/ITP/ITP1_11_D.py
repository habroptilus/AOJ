class Dice(object):
    def __init__(self,num):
        self.f=num[0]
        self.s=num[1]
        self.e=num[2]
        self.w=num[3]
        self.n=num[4]
        self.b=num[5]
    def create(self,order):
        if order=='N':
            return [self.s,self.b,self.e,self.w,self.f,self.n]
        elif order=='S':
            return [self.n,self.f,self.e,self.w,self.b,self.s]
        elif order=='E':
            return [self.w,self.s,self.f,self.b,self.n,self.e]
        else:
            return [self.e,self.s,self.b,self.f,self.n,self.w]
    def judge(self,dice_2):
        T={0:'N',1:'E',2:'S',3:'W'}
        m=[dice_2.s,dice_2.w,dice_2.n,dice_2.e,dice_2.f,dice_2.b]
        for i in range(6):
            if m[i]==self.f:#上面と一致しているものがある
                if i==4:temp=dice_2#上面どうし一致
                elif i==5:temp=Dice(Dice(dice_2.create('N')).create('N'))#下面と一致
                else:temp=Dice(dice_2.create(T[i]))#側面と一致

                if self.b==temp.b:
                        side_1=''.join(list(map(str,[self.s,self.w,self.n,self.e])))*2
                        side_2=''.join(list(map(str,[temp.s,temp.w,temp.n,temp.e])))
                        if side_2 in side_1:return 'accordance'
        return 'discordance'
    @staticmethod
    def isdifferent(dices):
        for i in range(len(dices)):
            for j in range(i+1,len(dices)):
                if dices[i].judge(dices[j])=='accordance':return 'No'
        return 'Yes'

n=eval(input())
dices=[]
for i in range(n):
    dices.append(Dice(list(map(int,input().split()))))
print(Dice.isdifferent(dices))
