import uncertainty as u


# ------------------------------ #
one_mag = u.Uncertainty(0.27218, abs_unc=0.0002) / 1000

solenoid_radius = u.Uncertainty(0.40, abs_unc=0.05) / 100
current = u.Uncertainty(10.00, abs_unc=0.01)
permittivity_air = 4 * u.pi * 10**-7
length_of_solenoid = u.Uncertainty(6.0, abs_unc=0.05) / 100

# tbd
turns = 100

# ------------------------------ #


def output_magnet_mass():
    for i in range(4, 10):
        v = one_mag * i
        print(f"{v.value:.4f}±{v.get_unc():.4f}")


# ------------------------------ #
print(permittivity_air)
print(length_of_solenoid)
print(one_mag)
mag_force = (current * permittivity_air) / (solenoid_radius * 2)
print(mag_force)
