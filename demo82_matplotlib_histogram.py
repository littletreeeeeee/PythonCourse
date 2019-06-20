import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

mu = 80
sigma = 8
X = mu+sigma*np.random.randn(10000)
print len(X)
num_bins = 1000
plt.figure(1)
plt.subplot(311)
plt.hist(X, num_bins, density=1, facecolor='black')



# using scipy.stats
# import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

mu = 80
sigma = 8
X = mu + sigma * np.random.randn(10000)
print len(X)
num_bins = 50
n, bins, patches = plt.hist(X, num_bins, density=1, facecolor='blue')
y = norm.pdf(bins, mu, sigma)
plt.subplot(312)

plt.plot(bins, y, 'r--')
plt.xlabel('sample data')
plt.ylabel('frequency')
plt.title('demo1')
plt.show()



# import matplotlib.mlab as mlab
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.stats import norm
#
# mu = 80
# sigma = 8
# X = mu + sigma * np.random.randn(10000)
# print len(X)
# num_bins = 50
# n, bins, patches = plt.hist(X, num_bins, density=1, facecolor='blue')
# y = norm.pdf(bins, mu, sigma)
# plt.plot(bins, y, 'r--')
# plt.xlabel('sample data')
# plt.ylabel('frequency')
# plt.title('demo1')
# plt.show()