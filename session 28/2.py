import numpy_financial as nf
nper = 10 * 12
pmt = -100
fv = 15692.93
rate = 0.05 / 12
pv = nf.pv(rate,nper,pmt,fv)
print(pv*-1,'$ is needed cause pv is',pv)