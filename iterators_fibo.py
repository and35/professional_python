# we created a iterator which can generate all the fibonacci sequence 
class IterFibo():
    def __init__(self, max=None):
        self.max = max
    def __iter__(self): # in this method we define the varibales to use 
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self # don forget return self object
    def __next__(self): # here we define the logic to get a num in the fibo sequence
        if not self.max or self.counter <= self.max:
            if self.counter == 0:
                self.counter += 1
                return  self.n1 # we return the num of the sequence 
            elif self.counter == 1:
                self.counter += 1
                return  self.n2
            else:
                self.counter += 1
                self.aux = self.n1 + self.n2
                #self.n1 = self.n2
                #self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux # use a swap sintaxis 
                return self.n2
        else:
            raise StopIteration 

# what if we created a function to visualize the phi? lets try: i tried but it was dificult jaja 

fibonacci = IterFibo(100) # we can created the first 100 numbers of phi sequence

for n in fibonacci:
    print(n)