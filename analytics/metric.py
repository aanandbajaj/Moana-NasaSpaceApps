import numpy as np

def metric(distance, volume):
    return distance/volume



import matplotlib.pyplot as plt
im = plt.imread("SaltonSeaLandSat1999.TIF")
print(len(im))

factor = 4
im_small = im[0::factor, 0::factor]
print(im_small)
print(len(im_small))


out = np.zeros((len(im_small),len(im_small[0])))

lakes = [[3000//factor, 3333//factor],[5000//factor, 4141//factor]]
lakes_volume = [1800, 200]
out1 = np.zeros((len(lakes), len(im_small),len(im_small[0])))

for i in range(len(out)):
    for j in range(len(out[1])):

        m = 0
        lake_index = 0
        for lake in range(len(lakes)):

            m_tmp = metric(((lakes[lake][0]-i)**2 + (lakes[lake][1]-j)**2)**0.5, lakes_volume[lake])
            out1[lake][i][j] = m_tmp

            if lake == 0:
                m = m_tmp
                #print(i, j, lake, m)

            else:
                if m_tmp <= m:
                    lake_index = lake
                    m = m_tmp

        out[i][j] = lake_index
    print(i, j, lake_index)

import matplotlib.pylab as plt

plt.imshow(out)
for lake in range(len(lakes)):
    plt.plot(lakes[lake][0], lakes[lake][1], "o")
plt.show()


for lake in range(len(lakes)):
    for i in range(len(out1[lake])):
        for j in range(len(out1[lake][i])):
            if out1[lake][i][j] >= 0.4:
                out1[lake][i][j] = np.NaN




plt.imshow(im_small,zorder=1)
for lake in range(len(lakes)):
    plt.imshow(out1[lake], zorder=2, alpha=0.9)

plt.savefig("out0.png")
plt.show()