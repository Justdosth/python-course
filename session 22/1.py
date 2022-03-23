class convert_T:
    def __init__(self,T):
        self.t=T

    def F_C(self):
        F=self.t
        C=(F-32)*(5/9)
        return C
    def C_F(self):
        C=self.t
        F=(C*(9/5))+32
        return F
    def F_K(self):
        F=self.t
        K=(F+459.67)*(5/9)
        return K
    def K_F(self):
        K=self.t
        F=(K*(9/5))-459.67
        return F
    def K_C(self):
        K=self.t
        C=K-273.15
        return C
    def C_K(self):
        C=self.t
        K=C+273.15
        return K
    #Rankin
    def R_K(self):
        R=self.t
        K=R*(5/9)
        return K
    def K_R(self):
        K=self.t
        R=K*(9/5)
        return R