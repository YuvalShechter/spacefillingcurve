import numpy as np

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

    return nd_coords

# coords = nuzzles_you(list(range(0, 11)), 3)
# print(coords[-10:])