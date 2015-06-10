
# 數值運算

#----------------------------------
a = True
b = 10
c = 100000000000000000000000000000000000000000000000000000000
d = 10.0
e = 1.0 + 5.0j  ## 注意: 虛數符號“j” 和數字之間不能有空格

#----------------------------------
nums = [a,b,c,d,e]
for i in nums:
    print(type(i))

#----------------------------------
print(10 / 3)  ## 整數無法整除，計算結果會自動轉換成浮點數
print(10 // 3) ## 防止自動整除的方法，要使用整除運算子 "//"


# 字串

#----------------------------------
a = "ABCD"
b = "EFGH"
c = a + b
print(c)

#----------------------------------
print(c[0])
print(c[5])
print(c[2:5])
print(c[::-1])
print(c[1:7:2])

#----------------------------------
my_str = "int: %d , float: %f , hex: %X" % (10, 3 , 250 )
print(my_str)

#----------------------------------
a = "This is an apple,\t and that is a book."
b = a.split()    # 沒有特別指定分裂節點符號，預設以空格、換行、tab 為準
print("原始字串: " + a)
print("分裂字串: " , b)
c = "*".join(b)
print("聚合(組合)字串: ", c)

#----------------------------------
print('apple' in a) # 可使用 'in' 來判斷原始字串 a 內是否含有指定字串 "apple"
print("apple".upper())   ## 使用字串自帶物件函式將所有英文字變大寫
print("APPLE".lower())   ## 使用字串自帶物件函式將所有英文字變小寫
print("apple".zfill(10)) ## 使用字串自帶物件函式將其成指定個數的字串，多出來的空格填"0"

#----------------------------------
msg = "John,25,168,78"
data   = msg.split(',')
name   = data[0]
age    = int(data[1])
tall   = float(data[2])
weight = float(data[3])
bmi = weight / ( (tall / 100.0) **2 )
print("NAME:%s AGE:%d HEIGHT:%1f WEIGHT:%1f BMI:%2f", name, age, tall, weight, bmi)

#----------------------------------
print( "String" * 5 )

# List 練習

#----------------------------------
a = [1,2,3,4,5,6]
b = list('abcdefg')
a.append(100)
print(a)
a.extend(b)
print(a)
#a.extend(1000)   ## !! 該行程式碼錯誤
a.append(b)
print(a)
a = [5,3,1,2,7,8,9]
a.sort()      ## 利用list 物件內建函式對自身進行排序
print(a)

# Dictionary 練習

#----------------------------------
a = {1:'a', 2:'b', 3:'c'}
b = {1:'a', 2:'B', 5:'E'}
a.update(b)
print(a)

#----------------------------------
## dict --> list <--> tupel <--> set
print( list({1:'a', 2:'b', 3:'c'}) )   # Dictionary 轉型為其他容器時，只會留下 key 值
print( set({1:'a', 2:'b', 3:'c'}) )
## 其他容器無法直接轉型為 Dictionary 容器
## list, tuple, set 之間可以互相轉換，但是其他容器轉型為 Set 時重覆的元素會被去掉
print( tuple([1,2,3,4,5]) )      # Tuple 和 List 之間可任意轉型
print( set([1,2,3,4,5,5,5,5,5]) )

#----------------------------------
a = 1
b = 1
print(a is b)
a = "String"
b = "S"
print(b is a[0])
a = "ABCD EFGH"
d = "ABCD"
b,c = a.split()
print( b is d)
a = "ABCDA"
print( a[0] is a[-1] )

#----------------------------------
select = input()
if select == '1':
    print("Condition: 1")
elif select == '2':
    print("Condition: 2")
elif select == '3':
    print("Condition: 3")
elif select == '4':
    print("Condition: 4")
else:
    print("Other Condition.")

#----------------------------------
## 請注意此區段的兩組if elif else 判斷式在輸入 2 的時候會產生不同的結果

select = int(input())
if select < 3:
    print("selection < 3")
elif select > 1:
    print("selection > 1")
else:
    print("other condition")

print("Attention ....")
if select < 3:
    print("selection < 3")
if select > 1:
    print("selection > 1")
else:
    print("other condition")


#----------------------------------
a = bool(int(input()))
print("YES" if a else "No")  ## 

#----------------------------------
print(list(range(5)))
print("for loop one")
for i in range(5):
    print(i)
    
print("for loop two")
for i in [1,3,5,7,9]:
    print(i)
    
print("for loop three")
for i in ["abc",'def','ghi','jkl']:
    print(i)


#----------------------------------
print("making list with 'for ... loop ... if' ")
a = [i for i in range(10) if i % 2 == 0]
print(a)

a = [ i*1000 for i in range(10) if i % 2 == 0]
print(a)

#----------------------------------
## 注意這邊 for loop 的用法
a = [1,2,3,4,5]
for i in a:
    i = 10
    print(i)
print(a)


a = [[1,2,3],[4,5,6],[7,8,9]]
for i in a:
    i[0] = 1000
print (a)

#----------------------------------
a = { i:chr(i+65) for i in range(10)}
print(a)
a = { chr(i+65):i for i in range(10)}
print(a)

# 練習 for loop

#----------------------------------
print(  [i for i in range(10) if i % 2 == 1]  )
a = list(range(10))
print(  [i**2 for i in a]  )

a = list('abcdefghijklmnop')
b  = []
for i in range(len(a)):
    b.append((i,a[i]))
print(b)

#----------------------------------
system_run = True
while(system_run):
    print("Input selection:")
    selection = input()
    if(selection == 'END'):
        system_run = False
    elif(selection == '1'):
        print("Run selection 1")
    elif(selection == '2'):
        print("Run selection 2")
    else:
        print("Unknown Selection")

# File Write

#----------------------------------
outf = open("test.txt","w")
outf.write("ABCDEF")
outf.write("GHIJKL")
outf.close()

#----------------------------------
with open("test2.txt",'w') as outf:
    outf.write("ABCDEF")
    outf.write("GHIJKL")

# File read 

#----------------------------------
filename = 'oil2.csv'
inf = open(filename)
data = inf.read()
inf.close()
print(data)

#----------------------------------
inf = open(filename)
data = inf.readlines()
inf.close()
print(data)

#----------------------------------
inf = open(filename)
for i in inf:
    print(i.strip())
inf.close()

#----------------------------------
with open(filename) as inf:
    line = True
    while(line):
        line = inf.readline()
        print(line.strip())

#----------------------------------
data = []
with open(filename) as inf:
    data = [i for i in inf]
print(data)

#----------------------------------
data = [i.strip() for i in open(filename)]
print(data)

# 讀取 big5 編碼的檔案

#----------------------------------
## 注意該檔案中的價錢數值會多加一個"元"字 
filename = "oil_big5.csv"
lines = [line.strip() for line in open(filename, encoding="big5")]
data = []
for i in lines[1:]:
    a = i.strip().split(',')
    date = a[0]
    oil_98 = float(a[1][:-1])
    oil_95 = float(a[2][:-1])
    oil_92 = float(a[3][:-1])
    diesel = float(a[4][:-1])
    data.append((date, oil_98, oil_95, oil_92, diesel))
print(data)

# 函式練習

#----------------------------------
## 注意 func1() , func2(), func3() 的差異
## func3() 會有錯誤出現
msg = 'TEST'
def func1():
    print("func1 : " + msg)
func1()

def func2():
    global msg
    print("func2 : " + msg)
    msg = "ABC"
func2()
print(msg)

def func3():
    print("func3 : " + msg)
    msg = "DEF"
func3()

#----------------------------------
def say_my_name(name="Heisenberg", more_msg = False):
    msg = "You are %s!" % name
    print(msg)
    if(more_msg):
        print ( "You are goddamn right!!" )
    else:
        print ( "..." )
print("TEST 1")
say_my_name()
print("TEST2")
say_my_name(name="John")
print("TEST3")
say_my_name(more_msg=True)
print("TEST4")
say_my_name("John",True)
print("TEST5")
say_my_name(True)
print("TEST6")
say_my_name(True,True)

# 用 Dictionary 和 function 實作 switch case 的做法

#----------------------------------
def do1():
    print("Do something 1...")
    
def do2():
    print("Do something 2...")
    
def do3():
    global system_run
    print("Do something 3...")
    system_run = False
    print("system_run: " + str(system_run))

def default_func():
    print("default handle....")

switch_case = {
    "1" : do1,
    "2" : do2,
    "END" : do3,
}

system_run = True
while(system_run):
    selection = input() 
    switch_case.get(selection, default_func)()

# Generator : yield

#----------------------------------
from time import sleep
def ffunc_yield():
    for i in range(10):
        sleep(1)
        print("data generator.")
        yield i

def ffunc_return():
    data = []
    for i in range(10):
        sleep(1)
        print("data generator.")
        data.append(i)
    return data

 
for i in ffunc_yield():
    print(i)
    
for i in ffunc_return():
    print(i)

# class 制作練習

#----------------------------------
class LCD:
    def __init__(self):
        self.line1=[' ' for i in range(16)]
        self.line2=[' ' for i in range(16)]
        self.x = 0
        self.y = 0
        
    def move(self,x=0,y=0):
        if x >=0 and x < 16:
            self.x = x
        if y in [0,1]:
            self.y = y
    
    def put_str(self,msg):
        for i in msg:
            self.put_c(i)
            
    def put_str_at(self, msg,x,y):
        self.move(x,y)
        self.put_str(msg)
    
    def put_c(self,ch):
        if self.y == 0:
            self.line1[self.x] = ch
            self.x += 1
            if(self.x > 15):
                self.x = 0
        elif self.y == 1:
            self.line2[self.x] = ch
            self.x += 1
            if(self.x > 15):
                self.x = 0

    def print_1(self,msg):
        self.put_str_at(msg,0,0)

    def print_2(self,msg):
        self.put_str_at(msg,0,1)

    def show(self):
        print("------------------")
        print("=" + "".join(self.line1) + "=")
        print("=" + "".join(self.line2) + "=")
        print("------------------")

#----------------------------------
lcd1 = LCD()
lcd1.put_str("LCD1:")
lcd1.put_str("Hello World")
lcd1.move(0,1)
lcd1.put_str("Show Line 2")
lcd1.show()

lcd2 = LCD()
lcd2.put_str("LCD2")
lcd2.put_str_at("TEST LCD Class",1,1)
lcd2.show()

# enmerate 練習

#----------------------------------
a = list("abcdefghijklmnopqrstuvwxyz")

print("enumerate test 1")
for i in enumerate(a):
    print(i)

print("enumerate test 2")
for i,j in enumerate(a):
    print(" %d : %s" % (i,j))

#----------------------------------
filename = "oil2.csv"

print("TEST 1")
with open(filename) as inf:
    lines = inf.readlines()
    for i in enumerate(lines):
        print(i)

print("TEST 2")
with open(filename) as inf:
    for line in enumerate(inf):
        print(line)


# zip 練習

#----------------------------------
a = [1,2,3,4,5]
b = list('abcde')
c = [10,20,30,40,50]

print("zip test 0")
for i in zip(a,b,c):
    print (i)
    
print("zip test 1")
data = list( zip(a,b,c) )
print(data)

print("zip test 2")
for x,y,z in zip(a,b,c):
    print("x: %d , y: %s , z: %d" % (x,y,z))

print("zip test 3")
a = zip(a,b,c)
for i in a:
    print(i)

for i in a:

print(i)

#----------------------------------
oil_98 = []
oil_95 = []
oil_92 = []
diesel = []

with open("oil2.csv") as inf:
    for i in inf:
        line = i.strip().split(',')
        oil_98.append(line[1].strip())
        oil_95.append(line[2].strip())
        oil_92.append(line[3].strip())
        diesel.append(line[4].strip())

result = list(zip(diesel,oil_98,oil_95,oil_92))
print(result)


# map 練習

#----------------------------------
def do_something(x):
    return x ** 2

a = list(range(10))

b = list(map(do_something, a))
print(b)

c = list(map(str,a))
print(c)

d = [do_something(i) for i in a]
print(d)

for i in map(do_something, a):
    print(i)


#----------------------------------
def get_price(x):
    return x * 2.5
data = []
with open('oil2.csv') as inf:
    inf.readline()
    for i in inf:
        oil_98 = i.strip().split(',')[2]
        data.append(float(oil_98) )

for i in map(get_price,data):
    print(i)

# fileter 練習

#----------------------------------
def my_choice(x):
    return True if x > 10 else False

a = list(range(20))
print(a)
print("TEST filter 1")
print(list(filter(my_choice, a)))
print("TEST fiilter 2")
for i in filter(my_choice,a):
    print(i)

#----------------------------------
def choice_data(x):
    line = x.strip().split(',')
    oil_92 = float(line[3])
    if oil_92 < 30 :
        return False
    else:
        return True

with open('oil2.csv') as inf:
    print(inf.readline())
    for i in filter(choice_data,inf):
        print(i.strip())


