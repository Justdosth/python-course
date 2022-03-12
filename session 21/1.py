class names():
    def __init__(self,n):
        self.n = n
        names = []
        for i in range(self.n):
            name = input('name=')
            names.append(name)
        self.names = names
    def max_name(self):
        nmax = self.names[0]
        for i in self.names:
            if len(nmax) < len(i):
                nmax = i
        return nmax
    def min_name(self):
        nmin = self.names[0]
        for i in self.names:
            if len(nmin) > len(i):
                nmin = i
        return nmin

n = int(input('n='))
p1 = names(n)
print(f'max name is {p1.max_name()}')
print(f'min name is {p1.min_name()}')