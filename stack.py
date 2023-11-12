# stack using arrays

class ArrayStack:
    def __init__(self):
        self.data = []
    def isEmpty(self):
        return len(self.data) == 0
    def len(self):
        return len(self.data)
    def push(self, ele):
        self.data.append(ele)
        print("element pushed")
    def top(self):
        if self.isEmpty == False:
            self.data[-1]
        else:
            print("Stack empty")
    def pop(self):
        if self.isEmpty == False:
            self.data.pop()
        else:
            print("Stack empty")
    

my_stack = ArrayStack()
my_stack.push("orange")
my_stack.push("500")
my_stack.push("armour")

my_stack.pop()
my_stack.pop()