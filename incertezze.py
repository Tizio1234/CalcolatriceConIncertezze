class Number:
    def __init__(self, value, absolute_error=0, relative_error=0) -> None:
        absolute_error = abs(absolute_error)
        relative_error = abs(relative_error)
        self.value = value
        if absolute_error:
            self.absolute_error = absolute_error
            self.relative_error = self.absolute_error / self.value
        elif relative_error:
            self.relative_error = relative_error
            self.absolute_error = self.relative_error * self.value
        else:
            self.relative_error = 0
            self.absolute_error = 0
    
    def str_absolute(self):
        return f"({self.value}±{self.absolute_error:.3f})"
    
    def str_relative(self):
        return f"({self.value}±{self.relative_error*100:.2f}%)"
    
    def __add__(self, other):
        return Number(self.value + other.value, self.absolute_error + other.absolute_error)
    
    def __sub__(self, other):
        return Number(self.value - other.value, self.absolute_error + other.absolute_error)
    
    def __mul__(self, other):
        result = self.value*other.value
        return Number(result, relative_error=self.relative_error + other.relative_error)
    
    def __truediv__(self, other):
        result = self.value/other.value
        return Number(result, relative_error=self.relative_error + other.relative_error)
    
    def __float__(self):
        return float(self.value)
    
    def __int__(self):
        return int(self.value)
    
    def __pow__(self, other):
        power = float(other)
        result = self.value**power
        return Number(result, relative_error=self.relative_error*abs(power))
