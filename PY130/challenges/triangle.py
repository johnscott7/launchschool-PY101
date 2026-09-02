class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        if not self.validate_triangle():
            raise ValueError

    def validate_triangle(self):
        return (
            self.side1 > 0
            and self.side2 > 0
            and self.side3 > 0
            and self.side1 + self.side2 > self.side3
            and self.side2 + self.side3 > self.side1
            and self.side1 + self.side3 > self.side2
        )

    def is_equilateral(self):
        return self.side1 == self.side2 == self.side3

    def is_isosceles(self):
        return (
            self.side1 == self.side2
            or self.side2 == self.side3
            or self.side1 == self.side3
        )

    def is_scalene(self):
        return (
            self.side1 != self.side2
            and self.side2 != self.side3
            and self.side1 != self.side3
        )

    def categorize_triangle(self):
        if self.is_equilateral():
            return "equilateral"
        if self.is_isosceles():
            return "isosceles"
        return "scalene"

    @property
    def kind(self):
        return self.categorize_triangle()

