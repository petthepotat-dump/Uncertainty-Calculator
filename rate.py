import uncertainty
from uncertainty import Uncertainty

import math


TIME_UNC = 0.01
MASS_UNC = 0.001

VOLUME = Uncertainty(0.075, rel_unc=0.005)
CU_MOLAR = 63.45


def find_mean(values: list[Uncertainty]):
    """Find mean of values"""
    total = 0
    for i in values:
        total += i.value
    return total / len(values)


def find_unc(values: list[Uncertainty]):
    """Find uncertainty of values"""
    # use sqrt or smth
    mean = find_mean(values)
    return math.sqrt(sum([(i.value - mean) ** 2 for i in values]) / (len(values) - 1))


def find_rate(mass_of_copper: Uncertainty, time: Uncertainty):
    """Find rate of reaction"""
    return (m / CU_MOLAR) * -4 / (VOLUME * t)


finput = [
    """0.048 373.42
0.050 377.83
0.048 385.92""",
    """0.049 84.24
0.048 82.92
0.049 79.24""",
    """0.051 52.53
0.052 42.65
0.050 45.83""",
    """0.052 38.76
0.050 39.37
0.049 36.77""",
    """0.051 17.22
0.050 18.13
0.051 16.92""",
]


for data in finput:
    res = []
    for blob in data.split("\n"):
        bblob = blob.split()
        m = Uncertainty(float(bblob[0]), abs_unc=MASS_UNC)
        t = Uncertainty(float(bblob[1]), abs_unc=TIME_UNC)
        # print(find_rate(m, t).value)
        res.append(find_rate(m, t))

    # for each conc find mean + unc
    mean = find_mean(res)
    # print("Mean", mean)
    unc = find_unc(res)
    mm = Uncertainty(mean, abs_unc=unc)
    print(f"{-mm.value:7f}    {mm.get_unc():.7f}")
