from statistics import *
def mean_d(stt):
        return sum(stt)/len(stt)
def mod_d(stt):
        col = max(stt)
        if col == a1:
                return "green"
        elif col==a2:
                return "yellow"
        elif col == a3:
                return "brown"
        elif col == a4:
                return "blue"
        elif col == a5:
                return "pink"
        elif col == a6:
                return "orange"
        elif col == a7:
                return "cream"
        elif col == a8:
                return "red"
        elif col == a9:
                return "white"
        elif col == a10:
                return "arch"
        elif col == a11:
                return "black"
def varian(stt):
        return variance(stt)

def median_d(stt):
        col = median(stt)
        if col == a1:
                return "green"
        elif col==a2:
                return "yellow"
        elif col == a3:
                return "brown"
        elif col == a4:
                return "blue"
        elif col == a5:
                return "pink"
        elif col == a6:
                return "orange"
        elif col == a7:
                return "cream"
        elif col == a8:
                return "red"
        elif col == a9:
                return "white"
        elif col == a10:
                return "arch"
        elif col == a11:
                return "black"
mon =['green','yellow','green','brown','blue','pink','blue','yellow','orange','cream','orange','red','white','blue','white','blue','blue','blue','green']
tues = ['arch','brown','green','brown','blue','blue','blue','pink','pink','orange','orange','red','white','blue','white','white','blue','blue','blue']
wed = ['green','yellow','green','brown','blue','pink','red','yellow','orange','red','orange','red','blue','blue','white','blue','blue','white','white']
thur = ['blue','blue','green','white','blue','brown','pink','yellow','orange','cream','orange','red','white','blue','white','blue','blue','blue','green']
fri = ['green','white','green','brown','blue','blue','black','white','orange','red','red','red','white','blue','white','blue','blue','blue','white']
lst = []
for i in mon:
	lst.append(i)
for j in tues:
	lst.append(j)
for k in wed:
	lst.append(k)
for m in thur:
	lst.append(m)
for n in fri:
	lst.append(n)
a1 = lst.count('green')
a2 = lst.count('yellow')
a3 = lst.count('brown')
a4 = lst.count('blue')
a5 = lst.count('pink')
a6 = lst.count('orange')
a7 = lst.count('cream')
a8 = lst.count('red')
a9 = lst.count('white')
a10 = lst.count('arch')
a11= lst.count('black')
stt = []
stt.append(a1)
stt.append(a2)
stt.append(a3)
stt.append(a4)
stt.append(a5)
stt.append(a6)
stt.append(a7)
stt.append(a8)
stt.append(a9)
stt.append(a10)
stt.append(a11)
print("The mean of the data is: ", mean_d(stt))
print("The most occuring colour is: ", mod_d(stt))
print("The variance of data is: ", varian(stt))
print("The median colour is: ", median_d(stt))

