from uncertainty import *
from uncertainty import Uncertainty as u

# ------------------------------------------------------------
# constnats
# ------------------------------------------------------------
MASS_UNC = 0.0

TURNS = 200
CURRENT = u(10.00, abs_unc=0.01)
AIR_PERMITTIVITY = u(1.256637*(10**-6))

SOLENOID_RADIUS = u(0.40, abs_unc=0.05) / 100
SOLENOID_LENGTH = u(6.0, abs_unc=0.05) / 100
SOLENOID_STRENGTH_CONSTANT =  (CURRENT*AIR_PERMITTIVITY) / (SOLENOID_RADIUS * 2)

SOLENOID_300 = SOLENOID_STRENGTH_CONSTANT * TURNS

# data
data = {
    "m": """1.0887±0.0008
1.3609±0.0010
1.6331±0.0012
1.9053±0.0014
2.1774±0.0016
2.4496±0.0018""",
    "s-microT": """1408.36±0.01
1765.56±0.01
1924.42±0.01
2125.23±0.01
2275.76±0.01
2512.90±0.01""",
}

# parse data
masses = []
strengths = []
for line in data["m"].splitlines():
    _v, _u = line.split("±")
    masses.append(u(float(_v), abs_unc=float(_u)))

for line in data["s-microT"].splitlines():
    _v, _u = line.split("±")
    strengths.append(u(float(_v)*10**-6, abs_unc=float(_u)))


# ------------------------------------------------------------
# 1. Exit velocity
# ------------------------------------------------------------

def find_exit_velocity(net_accel: u, distance: u, initial_velocity: u):
    """Find the exit velocity of a projectile."""
    return sqrt(net_accel * 2 / distance + pow(initial_velocity, 2))

def calc_rep_force(magnet1:float, magnet2:float, distance: float):
    return AIR_PERMITTIVITY*3/(4*pi) * (magnet1*magnet2)/(pow(distance, 4))


# ------------------------------------------------------------

# sapmle test with 3 mag projectile
# 0 = 3 magnets
mass = masses[0]
strength = strengths[0]

print("Mass:", mass.value, "Strength", strength.value)

net_force = calc_rep_force(strength, SOLENOID_300, SOLENOID_RADIUS)
net_accel = net_force / mass
print(find_exit_velocity(net_accel, SOLENOID_LENGTH, 0))


