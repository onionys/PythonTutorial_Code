class LCD:
    def __init__(self):
        self.line1=[' ' for i in range(16)]
        self.line2=[' ' for i in range(16)]
        
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

