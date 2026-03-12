class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.a
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented
    def __add__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.b + other.a * self.b
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented
    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.b - other.a * self.b
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b == other.a * self.b
        return False
    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > other.a * self.b
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < other.a * self.b
        return NotImplemented
    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"



f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

print(f"f_a = {f_a}")  # 2/3
print(f"f_b = {f_b}")  # 3/6

f_c = f_b + f_a
print(f"\nf_c = f_b + f_a = {f_c}")
assert str(f_c) == 'Fraction: 21, 18', 'Test1'
print("✓ Test1: Додавання")

f_d = f_b * f_a
print(f"f_d = f_b * f_a = {f_d}")
assert str(f_d) == 'Fraction: 6, 18', 'Test2'
print("✓ Test2: Множення")

f_e = f_a - f_b
print(f"f_e = f_a - f_b = {f_e}")
assert str(f_e) == 'Fraction: 3, 18', 'Test3'
print("✓ Test3: Віднімання")

assert f_d < f_c, 'Test4'
print("✓ Test4: f_d < f_c")

assert f_d > f_e, 'Test5'
print("✓ Test5: f_d > f_e")

assert f_a != f_b, 'Test6'
print("✓ Test6: f_a != f_b")

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2, 'Test7'
print("✓ Test7: 2/4 == 3/6")

print('\nOK')