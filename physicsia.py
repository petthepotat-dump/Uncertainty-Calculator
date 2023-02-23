import uncertainty as u


# ------------------------------ #
one_mag = u.Uncertainty(0.27218, abs_unc=0.0002) / 1000

solenoid_radius = u.Uncertainty(0.40, abs_unc=0.05) / 100
current = u.Uncertainty(10.00, abs_unc=0.01)
permittivity_air = u.Uncertainty(1.256637*(10**-6))
length_of_solenoid = u.Uncertainty(6.0, abs_unc=0.05) / 100

solenoid_strength_constant =  (current*permittivity_air) / (solenoid_radius * 2)

# tbd
turns = 300

# ------------------------------ #


def output_magnet_mass():
    for i in range(4, 10):
        v = one_mag * i
        print(f"{v.value:.4f}±{v.get_unc():.4f}")


# ------------------------------ #
# print(permittivity_air)
# print(length_of_solenoid)
# print(one_mag)
# mag_force = (current * permittivity_air) / (solenoid_radius * 2)
# print(mag_force)

# new section
def calc_rep_force(magnet1:float, magnet2:float, distance: float):
    return permittivity_air*3/(4*u.pi) * (magnet1*magnet2)/(u.pow(distance, 4))

def calc_solenoid_strength(turns: int):
    return solenoid_strength_constant * turns

data = {
    "mass+strength": """3 1408.36
4 1765.56
5 1924.42
6 2125.23
7 2275.76
8 2512.90""",
    "m+s+l": """3 1408.36 1.08872
4 1765.56 1.36090
5 1924.42 1.63308
6 2125.23 1.90526
7 2275.76 2.17744
8 2512.90 2.44962""",

}


# ------------------------------ #

def rep_for_each_turn_and_mass():
    magnet1 = u.Uncertainty(2512.90*10**-6, abs_unc=0.01)

    # find repulsive strength for each num of magnets at each of the following turns: [100, 200, 300, 400... 900]
    print('-'*20)
    for n, s, l in [map(float, line.split()) for line in data["m+s+l"].splitlines()]:
        n = int(n)
        solenoid = calc_solenoid_strength(turns)
        value = calc_rep_force(magnet1*n, solenoid, solenoid_radius)
        weight = one_mag*n / 1000 * 9.81
        # print(f"{n} | Turns: {i} | Repulsion: {value.value:.8f} ± {value.get_per_unc():.7f}% | Weight: {weight.value:.7f} ± {weight.get_per_unc():.7f}%")
        m = one_mag*n
        print(f"{m.value:.6f}±{m.get_per_unc():.2f}%")
        # print(f"{n} | {value.value:.4f}±{value.get_unc():.4f} | {weight.value:.8f}±{weight.get_per_unc():.2f}%")
        # print(value, weight)
    print('-'*20)
rep_for_each_turn_and_mass()


exit()

# ------------------------------ #

mag8s = u.Uncertainty(2512.90, abs_unc=0.01) / 1000000
mag8m = u.Uncertainty(2.4496, abs_unc=0.018) / 1000
# weight
mag8w = mag8m * 9.81
# calculate repulsion force
mag8r = calc_rep_force(mag8s, solenoid, solenoid_radius)

print(f"Weight: {mag8w.value:.7f} ± {mag8w.get_per_unc():.7f}%")
print(f"Replusion: {mag8r.value:.8f} ± {mag8r.get_per_unc():.7f}%")


exit()

for i in range(100, 901, 100):
    solenoid = calc_solenoid_strength(i)
    value = calc_rep_force(magnet1, solenoid, solenoid_radius)
    print(f"Replusion: {value.value:.7f} ± {value.get_per_unc():.7f}% | {i} turns")

