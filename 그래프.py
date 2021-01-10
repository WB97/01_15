import matplotlib.pyplot as plt
plt.plot([10,20,30,40], 'r', label='asc')
plt.plot([40,30,20,10], '^', label='desc')
plt.title('plotting')
plt.legend(loc=7)
plt.show()