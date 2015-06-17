from time import sleep
def get_list():
    res = []
    for i in range(10):
        sleep(1)
        print("get data....")
        yield i


def read_file_data(filename, all_string = True):
    inf = open(filename)
    inf.readline()
    data=[]
    for i in inf:
        line = i.strip().split(',')
        date = line[0]
        oil_98 = line[1] if all_string else float(line[1])
        oil_95 = line[1] if all_string else float(line[2])
        oil_92 = line[1] if all_string else float(line[3])
        oil    = line[1] if all_string else float(line[4])
        data.append( (date, oil_98,oil_95,oil_92,oil))
    inf.close()
    return data

def my_hello_world():
    print("hello world!" + " Jhon~~~~~")

