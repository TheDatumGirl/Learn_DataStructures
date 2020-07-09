class STACK():
    def __init__ (self):
        self.stack_array=[]
    
    def push(self,element):
        self.stack_array.append(element)
    
    def pop(self):
        if self.isEmpty() == 1 :
            print("Stack is empty")
            return None
        else:
            len_arr=len(self.stack_array)
            ele= self.stack_array[len_arr -1 ]
            print(ele)
            return self.stack_array.pop()
    
    def peek(self):
        if self.isEmpty() == 1 :
            print("Stack is empty")
            return None
        else:
            print(self.stack_array[len(self.stack_array)-1])
    
    def isEmpty(self):
        len_arr=len(self.stack_array)
        if len_arr == 0:
            return 1
        else:
            return 0

if __name__ == '__main__' :
    mystack=STACK()
    mystack.push("Ajit")
    mystack.push("Shashi")
    mystack.push("Deepa")
    mystack.push("Megha")
    mystack.pop()
    mystack.peek()
    mystack.push("naresh")
    mystack.peek()
    mystack.push("megha")
    mystack.peek()
