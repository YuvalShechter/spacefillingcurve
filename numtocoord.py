from sklearn import datasets
from coordtonum import coord_to_num
import numpy as np
from decimal import Decimal
from graph3d import plot1D, todf3D, plot3D, todf2D, plot2D

def nuzzles_you(nums, d):
    nd_coords = []
    max_num = np.max(nums)
    maxnum_len = len('{0:b}'.format(max_num))
    maxnum_len += d - (maxnum_len % d) if (maxnum_len % d) != 0 else 0
    maxnum_len = maxnum_len if maxnum_len > d else d
    for _, num in enumerate(nums):
        strnum = '{0:b}'.format(num)
        strnum = ''.join(['0']*(maxnum_len - len(strnum)))+strnum
        assert len(strnum) == maxnum_len, "String padding failed"
        nd_coord = [[] for _ in range(d)]
        for j in range(maxnum_len):
            nd_coord[j % d].append(strnum[j])
        for k in range(d):
            nd_coord[k] = ''.join(nd_coord[k])
        nd_coords.append(nd_coord)

    return nd_coords, maxnum_len

def nuzzles_you_float(nums, cap):
    n_dec = 0
    for i, num in enumerate(nums):
        if int(num) == num:
            continue
        n_dec_i = len(str(num).split(".")[-1])
        if n_dec_i <= cap:
            n_dec = n_dec if n_dec >= n_dec_i else n_dec_i
        else:
            n_dec = cap
            break

    for j in range(len(nums)):
        nums[j] = int(nums[j] * (10**n_dec))
    return nums

def convert_to_uwu(coords):
    for i, coord in enumerate(coords):
        for j, loc in enumerate(coord):
            halves = [2**(-k) for k in range(1, len(loc)+1)]
            int_vec = [int(loc_i) for loc_i in loc]
            coord[j] = np.dot(int_vec, halves)
    return coords

# iris = datasets.load_iris()
# X = iris.data[:, :2].tolist()  # we only take the first two features.
# y = iris.target

random_state = 170
X, y = datasets.make_blobs(n_samples=15000, random_state=random_state)
X = abs(X)
X = X.tolist()
plot1D(X, y)

# coords, max_pad = nuzzles_you(list(range(0, 2**13)), 3)
# coords = np.array(convert_to_uwu(coords))
# plot3D(todf3D(coords[:, 0], coords[:, 1], coords[:, 2], range(len(coords))))

# coords, max_pad = nuzzles_you(list(range(0, 2**13)), 2)
# coords = np.array(convert_to_uwu(coords))
# X, _ = coord_to_num(coords.tolist(), 10)
# plot1D(X, list(range(0, len(X))))

# coords, max_pad = nuzzles_you(list(range(0, 1024)), 2)
# coords = np.array(convert_to_uwu(coords))
# plot2D(todf2D(coords[:, 0], coords[:, 1], range(len(coords))), line=True)