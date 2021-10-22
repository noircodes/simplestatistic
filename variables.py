import numpy as np

# variables
class variables :
    x = [26, 12, 23, 17, 22, 16, 12, 16, 18, 18, 18, 21, 25, 16, 15, 13, 16, 19]
    np_x = np.array(x)
    mean = np.mean(np_x)
    median = np.round(np.median(np_x))
    n = len(np_x)
    sigma = np.sum(((np_x - median) ** 2))
    vs = sigma / (n - 1)

