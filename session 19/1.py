import random as r

p1_s = 7
p1_e = 15
mu_p1 = (p1_s + p1_e) / 2

p2_s = 20
p2_e = 48
mu_p2 = (p2_s + p2_e) / 2

p3_s = 23
p3_e = 60
mu_p3 = (p3_s + p3_e) / 2

n = 1000
p1_m = 0
p2_m = 0
p3_m = 0

for i in range(n):
    x1 = r.uniform(p1_s, p1_e)
    p1_sigma = abs(mu_p1 - x1)
    y1 = r.gauss(mu_p1, p1_sigma)
    p1_m += y1

    x2 = r.uniform(p2_s, p2_e)
    p2_sigma = abs(mu_p2 - x2)
    y2 = r.gauss(mu_p2, p2_sigma)
    p2_m += y2

    x3 = r.uniform(p3_s, p3_e)
    p3_sigma = abs(mu_p3 - x3)
    y3 = r.gauss(mu_p3, p3_sigma)
    p3_m += y3

mean_p1 = p1_m / n
print('mean of phase 1:', mean_p1)

mean_p2 = p2_m / n
print('mean of phase 2:', mean_p2)

mean_p3 = p3_m / n
print('mean of phase 3:', mean_p3)

print('===============================')

total_mean = mean_p1 + mean_p2 + mean_p3
print('total mean is:',total_mean)