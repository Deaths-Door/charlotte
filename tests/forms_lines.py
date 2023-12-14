
import math

X = 3  # Desired length of the line

def is_horizontal(points) :
    pass

def is_line(points):
    if len(points) < 2:
        return False 
"""
    is_horizontal = all(a[0] == b[0] for a, b in zip(points[:-1], points[1:]))
    is_vertical = all(a[1] == b[1] for a, b in zip(points[:-1], points[1:]))
    is_diagonal = all(math.fabs(a[0] - b[0]) == math.fabs(a[1] - b[1]) for a, b in zip(points[:-1], points[1:]))

    if not is_horizontal and not is_vertical and not is_diagonal:
        return False
    elif is_horizontal:
        # Check if all points have the same x-coordinate
        for point in points:
            if point[0] != points[0][0]:
                return False
    elif is_vertical:
        # Check if all points have the same y-coordinate
        for point in points:
            if point[1] != points[0][1]:
                return False
    elif is_diagonal:
         # Check if all points have the same slope (rise/run)
        slope = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
        for i in range(1, len(points) - 1):
          if (points[i + 1][1] - points[i][1]) / (points[i + 1][0] - points[i][0]) != slope:
            return False
        """# Check if all points have the same slope (rise/run)
        slope = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
        for i in range(1, len(points) - 1):
            if (points[i + 1][1] - points[i][1]) / (points[i + 1][0] - points[i][0]) != slope:
                return False

        # Check if the points form a line of length X
        line_length = 0
        for i in range(1, len(points)):
            line_length += math.sqrt((points[i][0] - points[i - 1][0])**2 + (points[i][1] - points[i - 1][1])**2)

        if line_length != X:
            return False"""          
"""
    return is_horizontal(points) or False

def handler(points,showbe) :
    print(f"{points} should be {showbe}, but is {is_line(points)}")

handler([(1, 1), (1, 2), (1, 3)],True)

handler([(1, 1), (2, 2), (3, 3)],True)

handler([(1, 0), (1, 1), (1, 2)],True)

handler([(1, 0), (1, 1), (1, 3)],False)

handler([(1, 1), (2, 3), (3, 5)],False)
