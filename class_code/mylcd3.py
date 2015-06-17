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
