
import numpy as np

for index in range(0, 1000):
    if (np.random.rand() >= 0.5):
        gender = 1 # male
    else:
        gender = 0 # female

    height = 7 * np.random.randn() + (172 if (gender == 1) else 163)
    standand_weight = (height - 105) if (gender == 1) else (height - 110)
    weight = 5 * np.random.randn() + standand_weight

    print "%d,%d,%d"%(gender, height, weight)

