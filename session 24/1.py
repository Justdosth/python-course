import statistics as st
Data1=[0,-1,3,4,3,4,0,5,8,9,-4,0,4,5]
Data2=[456.7,547.8,926.6,236.1,543,439]

print('mean for Data1=',st.mean(Data1))
print('Data1 does not have geometric or harmonic mean')
print('median for Data1=',st.median(Data1))
print('variance for Data1=',st.pvariance(Data1))
print('std for Data1=',st.pstdev(Data1))

print('mean for Data2=',st.mean(Data2))
print('geometric mean for Data2=',st.geometric_mean(Data2))
print('harmonic mean for Data2=',st.harmonic_mean(Data2))
print('median for Data2=',st.median(Data2))
print('variance for Data2=',st.pvariance(Data2))
print('std for Data2=',st.pstdev(Data2))