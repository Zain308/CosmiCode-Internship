class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)
    
    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        if denominator == 0:
            raise ValueError("Division by zero is not allowed")
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real, imag)
    
    def __str__(self):
        return f"{self.real:.2f} + {self.imag:.2f}i"

if __name__ == "__main__":
    # Example usage
    c1 = ComplexNumber(3, 2)
    c2 = ComplexNumber(1, 7)
    
    print(f"c1 = {c1}")
    print(f"c2 = {c2}")
    print(f"Addition: {c1 + c2}")
    print(f"Subtraction: {c1 - c2}")
    print(f"Multiplication: {c1 * c2}")
    print(f"Division: {c1 / c2}")