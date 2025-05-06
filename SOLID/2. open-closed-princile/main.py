from enum import Enum

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Product(object):
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

# Wrong way of implementing filter. This clas will grow like anything and will be modified forever
# class ProductFilter(object):
#     def filter_by_color(self, products, color):
#         result = []
#         for item in products:
#             if item.color == color:
#                 result.append(item)
#         return result
#
#     def filter_by_size(self, products, size):
#         result = []
#         for item in products:
#             if item.size == size:
#                 result.append(item)
#         return result
#
#     def filter_by_size_and_color(self, products, size, color):
#         result = []
#         for item in products:
#             if item.size == size and item.color == color:
#                 result.append(item)
#         return result

# Right way
class Filter:
    def filter(self, items, spec):
        pass

class Spec:
    def is_satisfied(self, item):
        pass

class ColorSpec(Spec):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        if item.color == self.color:
            return True
        return False

class SizeSpec(Spec):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        if item.size == self.size:
            return True
        return False

class BetterFilter(Filter):
    def filter(self, items, spec):
        result = []
        for item in items:
            if not spec.is_satisfied(item):
                continue
            result.append(item)
        return result

class AndSpec(Spec):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))

if __name__ == "__main__":
    p1 = Product("Apple", Color.GREEN, Size.SMALL)
    p2 = Product("Tree", Color.GREEN, Size.LARGE)
    p3 = Product("Apple", Color.BLUE, Size.LARGE)

    products = [p1, p2, p3]

    greenSpec = ColorSpec(Color.GREEN)
    smallSpec = SizeSpec(Size.SMALL)
    bf = BetterFilter()

    print("Color Spec: ")
    res = bf.filter(products, greenSpec)
    for item in res:
        print("{} is green".format(item.name))
    print()

    print("Size Spec: ")
    res = bf.filter(products, smallSpec)
    for item in res:
        print("{} is small".format(item.name))
    print()

    print("Color: Green and Size: Large -- Spec: ")
    res = bf.filter(products, AndSpec(greenSpec, SizeSpec(Size.LARGE)))
    for item in res:
        print("{} is Green and Large".format(item.name))