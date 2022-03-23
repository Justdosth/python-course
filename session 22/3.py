class convert_P:
    def __init__(self,P):
        self.p = P
        self.a = 100000
        self.b = 101325
    
    def Pa_bar(self):
        Pa = self.p
        bar = Pa / self.a
        return bar
    def Pa_atm(self):
        Pa = self.p
        atm = Pa / self.b
        return atm
    def bar_Pa(self):
        bar = self.p
        Pa = bar * self.a
        return Pa
    def atm_Pa(self):
        atm = self.p
        Pa = atm * self.b
        return Pa
    def bar_atm(self):
        bar = self.p
        atm = bar * (self.b/self.a)
        return atm
    def atm_bar(self):
        atm = self.p
        bar = atm * (self.a/self.b)
        return bar

pre = convert_P(float(input('pressure=')))
print(pre.Pa_atm())