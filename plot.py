#hsowing the relationship btw the days and cases with the help of a graph
import matplotlib.pyplot as plt

days = [1,2,3,4,5]
cases = [100,150,200,260,300]

plt.plot(days, cases)
plt.xlabel("Days")
plt.ylabel("Cases")
plt.title("Disease Spread Trend")
plt.show()
