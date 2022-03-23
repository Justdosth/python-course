class convert_L:
    def __init__(self,L):
        self.l=L
    def m_cm(self):
        m=self.l
        cm=m*100
        return cm
    def m_mm(self):
        m=self.l
        mm=m*1000
        return mm
    def cm_m(self):
        cm=self.l
        m=cm/100
        return m
    def cm_mm(self):
        cm=self.l
        mm=cm*10
        return mm
    def mm_cm(self):
        mm=self.l
        cm=mm/10
        return cm
    def mm_m(self):
        mm=self.l
        m=mm/1000
        return m
    #inch
    def inch_cm(self):
        inch = self.l
        cm = inch * 2.54
        return cm
    def cm_inch(self):
        cm = self.l
        inch = cm / 2.54
        return inch
    #micron
    def micron_m(self):
        micron = self.l
        m = micron * 10**6
        return m
    def m_micron(self):
        m = self.l
        micron = m / 10**6
        return micron
