import uncertainty
from uncertainty import Uncertainty


data = """2	0.048	373.4	0.133
2	0.05	377.8	0.133
2	0.048	385.9	0.133
3	0.049	84.2	0.15
3	0.048	82.9	0.15
3	0.049	79.2	0.15
4	0.051	52.5	0.166
4	0.052	42.6	0.166
4	0.05	45.8	0.166
5	0.052	38.7	0.183
5	0.05	39.3	0.183
5	0.049	36.7	0.183
6	0.051	17.2	0.2
6	0.05	18.1	0.2
6	0.051	16.9	0.2"""

VOLUME = Uncertainty(0.075, rel_unc=0.005)
CU_MOLAR = 63.546


def find_rate(
    mass_of_copper: Uncertainty, conc_of_acid: Uncertainty, time: Uncertainty
):
    """Find rate of reaction"""
    # find moles of Cu consumed
    moles_of_cu = mass_of_copper / CU_MOLAR
    # print("Moles of Copper:", moles_of_cu)
    # find moles of HNO3 acid consumed
    moles_of_acid_consumed = moles_of_cu * 4
    # print("Moles of acid consumed:", moles_of_acid_consumed)
    # find final moles in solution
    final_moles = VOLUME * conc_of_acid - moles_of_acid_consumed
    # print("Final moles:", final_moles)
    # find final concentration
    final_conc = final_moles / VOLUME
    # print("Final concentration:", final_conc)
    # find change in concentration
    change_in_conc = final_conc - conc_of_acid
    # print("Change in concentration:", change_in_conc)
    # find rate of reaction
    rate = change_in_conc / time
    # print("Rate of reaction:", rate)
    return rate


for blob in data.split("\n"):
    conc, mass, time, conc_unc = map(float, blob.split("\t"))
    c = Uncertainty(conc, rel_unc=conc_unc)
    m = Uncertainty(mass, rel_unc=0.001)
    t = Uncertainty(time, rel_unc=0.1)
    result = find_rate(m, c, t)
    # print(f"{result.value:.6f}      {result.get_abs_unc():.2f}%")
    print(f"{result.get_abs_unc():.2f}%")
