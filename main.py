from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int) -> None:
        """Магический метод"""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Магический метод"""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Магический метод"""
        return f"({self.x}, {self.y})"

    def __add__(self, another_point: Point) -> str:
        result_x = self.x + another_point.x
        result_y = self.y + another_point.y
        return f"({result_x}, {result_y})"

    def __sub__(self, another_point: Point) -> Point:
        result_x = self.x - another_point.x
        result_y = self.y - another_point.y
        return Point(result_x, result_y)

    def __eq__(self, another_point: Point) -> bool:
        return self.x == another_point.x and self.y == another_point.y


class ComplexNumber:
    def __init__(self, real: int, img: int) -> None:
        self.real = real
        self.img = img

    def __add__(self, cx: ComplexNumber) -> ComplexNumber:
        result_real = self.real + cx.real
        result_img = self.real + cx.img
        return f"{result_real} {'+' if result_img > 0 else '-'} {abs(result_img)}j"

    def __sub__(self, cx: ComplexNumber) -> ComplexNumber:
        result_real = self.real - cx.real
        result_img = self.real - cx.img
        return ComplexNumber(result_real, result_img)

    def __repr__(self) -> str:
        return f"{self.real} {'+' if self.img > 0 else '-'} {abs(self.img)}j"


# p1 = Point(5, 0)
# p2 = Point(10, 15)
# p4 = Point(5, 0)

# p3 = p1 - p2
# print(p3)

# print(p1 == p2)

a1 = ComplexNumber(4, 4)
a2 = ComplexNumber(-10, -3)
a3 = a1 + a2
print(a2)
