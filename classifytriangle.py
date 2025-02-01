def classify_triangle(side1, side2, side3):

    # Verify sides form a valid triangle
    if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
        return "Does not form a valid triangle"
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "Does not form a valid triangle"
    

    # Determine if the triangle is equilateral, isosceles, or scalene
    if side1 == side2 == side3:
        triangle_type = "Equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Check if it is a right triangle using the Pythagorean theorem
    sides = [side1, side2, side3]
    sides.sort()  # Sort sides to identify the hypotenuse (longest side)
    if abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 1e-6:
        triangle_type += " and Right"

    return triangle_type