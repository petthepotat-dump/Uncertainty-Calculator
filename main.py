

class Unc:
    def __init__(self, unc: str):
        self.abs = self.unc.endswith("%")
        self.unc = unc
    
    @property
    def is_abs(self):
        """Check if absolute uncertainty"""
        return self.abs
    
    @property
    def abs_val(self):
        """Find absolute value of uncertainty"""
        if self.abs: return self.abs


class UncObject:
    def __init__(self, value: str, unc: str):
        self.value = value
        self.unc = Unc(unc)
    
    @property
    def percent_uncertainty(self):
        """Find percent uncertainty"""
        return

