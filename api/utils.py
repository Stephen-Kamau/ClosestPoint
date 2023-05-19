# THIS PROCESS INPUTS AND GET THE CLOSEST BETWEEN THEM...
def find_all_distance(point_list):
    #we split by semicolon and get the values as (x,y) into a list
    points = [tuple(map(int, point.split(','))) for point in point_list]
    #we then need to iterate all points, get the distance between them and all other points..
    # Later we will get the one with the shortest distance
    all_distance = []
    smallest_distance = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = calculate_distance(points[i], points[j])
            if distance < smallest_distance:
                smallest_distance = distance
                all_distance = [points[i], points[j]]

    #get back the closest point as a x,y tuple..
    return  ';'.join([','.join(map(str, point)) for point in all_distance])


# CALCULATING THE DISTANCE..
# WE TAKE sqrt(Dx^2 + Dy^2)
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance
