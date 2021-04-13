class ElementFIFO:
    def __init__(self, r, w, x):
        self.r = r
        self.w = w
        self.x = x


class FIFO :
    'Это класс Rectangle'
    # Способ создания объекта (конструктор)
    def __init__(clas,x):         
        clas.x = x
    def show(clas):#демонстрация FIFO r-столбец индексов чтения
        print("r w x")
        for y in x:
            print(y.r,y.w,y.x)
    def add1(clas,i):#добавление нового элемента в конец
        e = ElementFIFO(0,0,i)
        x.append(e)
    def reset(clas):#указатель на чтение и редактирование встают в начало FIFO
        for y in x:
            y.r=0
            y.w=0

        clas.x[0].r =1;
        clas.x[0].w =1
    def Read(clas): #чтение элемента
        flag = 0
        for y in x:
            if flag !=0:
                y.r=1;
                return flag.x
            if y.r==1:
                y.r=0
                flag = y
        if flag !=0:
            x[0].r = 1
            y.r=0
            return flag.x
        x[0].r = 1;
        return x[0].x 

    def Write(clas,z):#запись элемента
        flag = 0
        for y in x:
            if flag !=0:
                y.w=1;
                return 0
            if y.w==1:
                y.w=0
                y.x = z
                flag = y
        if flag !=0:
            x[0].w = 1
            y.w=0
            y.x=z
            return flag.x
        x[0].w = 1;
        return x[0].x
             

x=[]
fifo = FIFO(x)
i=0
while(i<4):
    fifo.add1(i)
    i+=1
e1 = ElementFIFO(0,0,1)
e2 = ElementFIFO(0,0,1)

fifo.reset()
fifo.show()
print();
print("Read x=",fifo.Read()) #пример чтения
fifo.Write(9) #пример записи
print();
fifo.show()
