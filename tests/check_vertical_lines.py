from collections import defaultdict
# Note i solved vertical instead of horizontal oops

X_IN_ROW_TO_WIN = 3

def is_vertical(points : list[tuple[int,int]]) :
    # Group points so easier to work with
    grouped_points = defaultdict(list)
    for point in points:
        grouped_points[point[0]].append(point[1])

    print(grouped_points)

    # Check for horizontal lines now    
    for x_coords , y_points in grouped_points.items() :
        # Skip
        if len(y_points) < X_IN_ROW_TO_WIN : continue

        # Now in poinst check for increase numbers so that nums[i] + 1 = nums[i + 1] and the sequences continues for a len of X_IN_ROW_TO_WIN
        start = 1

        # Max is X_IN_ROW_TO_WIN - 1 then return true
        iter_index = 0 
        #is_increasing = True
        while start + X_IN_ROW_TO_WIN <= len(y_points) + 1 :
            print(f"{y_points[start - 1 + iter_index]} and {y_points[start + iter_index]}")
            if y_points[start + iter_index - 1] + 1 == y_points[start + iter_index] :
                iter_index += 1
            else :
                # Note : Don't change to 0 as that creates infinte loop
                iter_index = 1 

            if iter_index == 1 : 
                start += 1

            if iter_index == X_IN_ROW_TO_WIN - 1 :
                return True        
    return False

def handler(points,shouldbe) :
    print(f"{points} should be {shouldbe}, but is {is_vertical(points)}")

handler([(1, 1), (1, 2),(1,5),(2,0),(2,4),(2,5),(2,7),(2,8),(2,9)],True)

"""from collections import defaultdict

X_IN_ROW_TO_WIN = 3

def group_by_x_coords(points : list[tuple[int,int]]) :
    # Group points so easier to work with
    grouped_points = defaultdict(list)
    for point in points:
        grouped_points[point[0]].append(point[1])
    
    return grouped_points

def group_by_y_coords(points : list[tuple[int,int]]) :
    # Group points so easier to work with
    grouped_points = defaultdict(list)
    for point in points:
        grouped_points[point[1]].append(point[0])
    
    return grouped_points

def is_vertical_or_horizontal(points : list[tuple[int,int]]) :
    pass

# Generate a list of points
points = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1)]

# Group the points
grouped_points = group_by_x_coords(points)
print(grouped_points)

# Check the grouped points
expected_grouped_points = {
    1: [1, 2, 3, 4, 5, 6, 7, 8, 9],
}

assert grouped_points == expected_grouped_points"""

