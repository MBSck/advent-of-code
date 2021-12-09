import numpy as np

#sea floor depth as in example (??)
#depth = np.array([199,200,208,210,200,207,240,269,260,263])

#sea floor depth with randomly generated values similar to example
depth = np.random.randint(low=180, high=300, size=10, dtype=int)

#change of depth to the next measurement
#no measurement before the first measurement
depth_change = np.zeros(depth.size-1, dtype=int)

#compute difference between two consecutive measurements
for i in range(depth_change.size):
    depth_change[i] = depth[i+1] - depth[i]

#number of measurements larger than the previous measurement
nr_increase = depth_change[np.where(depth_change > 0)].size

print('depth measurements:', depth)
print('depth changes:', depth_change)
print(nr_increase, 'measurements are larger than the previous measurement')
