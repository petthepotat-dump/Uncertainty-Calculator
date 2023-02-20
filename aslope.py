import uncertainty
from uncertainty import Uncertainty

import math

# ------------------------------ #

R = 8.314

slope = Uncertainty(5674.139, abs_unc=985.2770)
print(slope)

ea = slope * R
print(ea)
