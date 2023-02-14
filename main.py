

class Uncertainty:
    def __init__(self, value: float, abs_unc: float = None, rel_unc: float = None, percent_unc: float = None):
        # abs = % (x / 100)
        # rel = actual
        self.value = value
        if abs_unc or percent_unc:
            self.absu = abs_unc if abs_unc else percent_unc / 100
            self.relu = self.value * self.absu
        elif rel_unc:
            self.relu = rel_unc
            self.absu = self.relu / self.value
    
    def __add__(self, other) -> "Uncertainty":
        """Add values"""
        return Uncertainty(self.value + other.value, rel_unc = self.relu + other.relu)

    def __sub__(self, other) -> "Uncertainty":
        """Sub values"""
        return Uncertainty(self.value - other.value, rel_unc = self.rlu + other.relu)
    
    def __mul__(self, other) -> "Uncertainty":
        """Multiply values"""
        return Uncertainty(self.value * other.value, abs_unc = self.absu + other.absu)
    
    def __truediv__(self, other) -> "Uncertainty":
        """Dividing values"""
        return Uncertainty(self.value / other.value, abs_unc = self.absu + other.absu)
    
    def __repr__(self) -> str:
        """Represent"""
        return f"Value: {self.value:.10f} | Rel: {abs(self.relu):.10f} | Abs: {abs(self.absu*100):.10f}%"


conc = Uncertainty(-0.04028577723, percent_unc=1317.629888)
t = Uncertainty(373.4, rel_unc=0.1)

print(conc / t)


    

