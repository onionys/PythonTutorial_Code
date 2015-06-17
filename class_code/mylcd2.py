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

    ## new function !
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
        list(msg)
        if len(msg) < 16:
            for i in range(len(msg)):
                self.line1[i]=msg[i]
        else:
            for i in range(16):
                self.line1[i]=msg[i]

    def print_2(self,msg):
        list(msg)
        if len(msg) < 16:
            for i in range(len(msg)):
                self.line2[i]=msg[i]
        else:
            for i in range(16):
                self.line2[i]=msg[i]

    # not so new function !
    def show(self):
        print("------------------")
        print("=" + "".join(self.line1) + "=")
        print("=" + "".join(self.line2) + "=")
        print("------------------")
