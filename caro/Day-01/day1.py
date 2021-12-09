import numpy as np

def number_increased_measurements(depth):
    #total number of measurements that increased compared to the previous one

    #change of depth to the next measurement
    #no measurement before the first measurement
    depth_change = np.zeros(depth.size-1, dtype=int)

    #compute difference between two consecutive measurements
    for i in range(depth_change.size):
        depth_change[i] = depth[i+1] - depth[i]

    #number of measurements larger than the previous measurement
    nr_increase = depth_change[np.where(depth_change > 0)].size

    print(nr_increase, 'measurements are larger than the previous measurement')


def measurements_sum(depth,nr):
    #total number of measurements that increased within the sum of nr measurements (window) compared to the previous window

    depth_sum = np.zeros(depth.size-(nr-1), dtype=int)

    #compute sum
    for i in range(depth_sum.size):
        depth_sum[i] = np.sum(depth[i:i+nr])

    return depth_sum


#sea floor depth genereated by advent of code
depth = np.loadtxt('day1.dat',dtype=int)

#first half of the puzzle:
number_increased_measurements(depth)
#correct solution: 1301

#second half of the puzzle:
depth_sum = measurements_sum(depth,3)
number_increased_measurements(depth_sum)
#correct solution: 1346
