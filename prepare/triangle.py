def is_valid(f):
    def inner(sides):
        return sum(sides) > 2 * max(sides) and f(sides)
    return inner
    
@is_valid
def equilateral(sides):
    return len(set(sides)) == 1
    
@is_valid
def isosceles(sides):
    return len(set(sides)) < 3

@is_valid
def scalene(sides):
    return len(set(sides)) == 3