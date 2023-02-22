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


def find_mean_unc(values: list[Uncertainty]):
    """Find uncertainty of values"""
    # use sqrt or smth
    mean = find_mean(values)
    return math.sqrt(sum([(i.value - mean) ** 2 for i in values]) / (len(values) - 1))


def find_rate(mass_of_copper: Uncertainty, time: Uncertainty):
    """Find rate of reaction"""
    return (m / CU_MOLAR) * -4 / (VOLUME * t)


finput = [
    """0.052 324.3
0.049 281.2
0.048 275.3
0.051 288.6
0.052 286.7 """,
    """0.052 149.3
0.051 142.8
0.048 145.6
0.053 151.9
0.051 146.7""",
    """0.052 58.1
0.048 54.3
0.051 59.7
0.053 60.3
0.049 58.9 """,
    """0.052 43.9
0.051 46.8
0.049 48.3
0.047 43.2
0.052 44.4""",
    """0.052 39.8
0.050 35.2
0.052 43.3
0.048 39.5
0.050 40.1""",
]

print("Data for Mean Rate + Uncertainty")
mean_data = []
temp = 273.15 + 40
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

    unc = find_mean_unc(res)
    # print(unc)
    mm = Uncertainty(mean, abs_unc=unc)
    mm *= -1

    print(f"{mm.value:7f}    {mm.get_unc():.7f}")
    mean_data.append((mm, temp))
    temp += 10

print("ln(k)  k%  ln(k)%  1/T")
# find the values corresponding to temp and mean k[Cu]
for val, temp in mean_data:
    # find ln(val) and 1/T
    lnk = uncertainty.ln(val)
    invT = 1 / temp
    print(f"{lnk.value:7f}  {lnk.get_unc():.7f}    {invT:7f}")

# print(f"{-mm.value:7f}    {mm.relu:.7f}")
