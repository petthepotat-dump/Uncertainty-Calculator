import uncertainty
from uncertainty import Uncertainty

import math


data = """0.000146 0.000007
0.000291 0.000008
0.00073 0.00002
0.00093 0.00006
0.0010 0.0001"""

# first item is rate, second index is rel_unc, create a rate uncertainty object, divide the value by 4.0**2.6
for data in data.split("\n"):
    d = data.split()
    rate = Uncertainty(float(d[0]), rel_unc=float(d[1]))
    rate.value /= 4.0**2.6
    # print(rate.value, rate.relu)
    print(f"{rate.value:6f}    {rate.relu:.6f}")
