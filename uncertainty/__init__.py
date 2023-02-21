import math

# ------------------------------ #
pi = math.pi


class Uncertainty:
    def __init__(
        self,
        value: float,
        abs_unc: float = None,
        rel_unc: float = None,
        percent_unc: float = None,
    ):
        # abs = val
        # rel = % (rel / 100)
        self.value = value
        if abs_unc:
            self.absu = abs_unc
            self.relu = abs_unc / value
        elif percent_unc:
            self.absu = value * percent_unc / 100
            self.relu = percent_unc / 100
        elif rel_unc:
            self.relu = rel_unc
            self.absu = rel_unc * value

    def __add__(self, other) -> "Uncertainty":
        """Add values"""
        if type(other) == Uncertainty:
            return Uncertainty(self.value + other.value, abs_unc=self.absu + other.absu)
        return Uncertainty(self.value + other, abs_unc=self.absu)

    def __sub__(self, other) -> "Uncertainty":
        """Sub values"""
        if type(other) == Uncertainty:
            return Uncertainty(self.value - other.value, abs_unc=self.absu + other.absu)
        return Uncertainty(self.value - other, abs_unc=self.absu)

    def __mul__(self, other) -> "Uncertainty":
        """Multiply values"""
        if type(other) == Uncertainty:
            return Uncertainty(self.value * other.value, rel_unc=self.relu + other.relu)
        return Uncertainty(self.value * other, rel_unc=self.relu)

    def __truediv__(self, other) -> "Uncertainty":
        """Dividing values"""
        if type(other) == Uncertainty:
            return Uncertainty(self.value / other.value, rel_unc=self.relu + other.relu)
        return Uncertainty(self.value / other, rel_unc=self.relu)

    def __repr__(self) -> str:
        """Represent"""
        return f"Value: {self.value:.10f} | abs: {self.get_unc():.10f} | %: {self.get_per_unc():.10f}%"

    def get_unc(self) -> float:
        """Get uncertainty"""
        return abs(self.absu)

    def get_per_unc(self) -> float:
        """Get absolute uncertainty"""
        return abs(self.relu) * 100


# ------------------------------ #
# adding mathematical functions


def ln(x: Uncertainty) -> Uncertainty:
    """Natural log"""
    return Uncertainty(math.log(x.value), abs_unc=x.absu / x.value)


def log(x: Uncertainty, base: float = 10) -> Uncertainty:
    """Log"""
    return Uncertainty(
        math.log(x.value, base), abs_unc=x.absu / (x.value * math.log(base))
    )


def exp(x: Uncertainty) -> Uncertainty:
    """Exponential"""
    return Uncertainty(math.exp(x.value), abs_unc=x.absu * math.exp(x.value))


def sqrt(x: Uncertainty) -> Uncertainty:
    """Square root"""
    return Uncertainty(math.sqrt(x.value), abs_unc=x.absu / (2 * math.sqrt(x.value)))


def sin(x: Uncertainty) -> Uncertainty:
    """Sine"""
    return Uncertainty(math.sin(x.value), abs_unc=x.absu * math.cos(x.value))


def cos(x: Uncertainty) -> Uncertainty:
    """Cosine"""
    return Uncertainty(math.cos(x.value), abs_unc=x.absu * math.sin(x.value))


def tan(x: Uncertainty) -> Uncertainty:
    """Tangent"""
    return Uncertainty(math.tan(x.value), abs_unc=x.absu / math.cos(x.value) ** 2)


def asin(x: Uncertainty) -> Uncertainty:
    """Arc Sine"""
    return Uncertainty(math.asin(x.value), abs_unc=x.absu / math.sqrt(1 - x.value**2))


def acos(x: Uncertainty) -> Uncertainty:
    """Arc Cosine"""
    return Uncertainty(math.acos(x.value), abs_unc=x.absu / math.sqrt(1 - x.value**2))


def atan(x: Uncertainty) -> Uncertainty:
    """Arc Tangent"""
    return Uncertainty(math.atan(x.value), abs_unc=x.absu / (1 + x.value**2))


def sinh(x: Uncertainty) -> Uncertainty:
    """Hyperbolic Sine"""
    return Uncertainty(math.sinh(x.value), abs_unc=x.absu * math.cosh(x.value))


def cosh(x: Uncertainty) -> Uncertainty:
    """Hyperbolic Cosine"""
    return Uncertainty(math.cosh(x.value), abs_unc=x.absu * math.sinh(x.value))


def tanh(x: Uncertainty) -> Uncertainty:
    """Hyperbolic Tangent"""
    return Uncertainty(math.tanh(x.value), abs_unc=x.absu / math.cosh(x.value) ** 2)


def asinh(x: Uncertainty) -> Uncertainty:
    """Arc Hyperbolic Sine"""
    return Uncertainty(
        math.asinh(x.value), abs_unc=x.absu / math.sqrt(1 + x.value**2)
    )


def acosh(x: Uncertainty) -> Uncertainty:
    """Arc Hyperbolic Cosine"""
    return Uncertainty(
        math.acosh(x.value), abs_unc=x.absu / math.sqrt(x.value**2 - 1)
    )


def atanh(x: Uncertainty) -> Uncertainty:
    """Arc Hyperbolic Tangent"""
    return Uncertainty(math.atanh(x.value), abs_unc=x.absu / (1 - x.value**2))
