import copy
best_length = 0 #the answer for the shortest length
best_path = [] #the answer for the order of points
points = [] #all the points
points_left = []
my_path = []
my_length = 0

class point:
    def __init__ (self, num, x, y):
        self.num = num
        self.x = x
        self.y = y

    def distance (self, another_point):
        delta_x = self.x - another_point.x
        delta_y = self.y - another_point.y
        return ((delta_x ** 2) + (delta_y ** 2)) ** 0.5

    def print_me (self):
        print ("Num ", self.num)
        print ("X   ", self.x)
        print ("Y   ", self.y)

def parser (file, points_set):
    o = open (file, "r")
    lines = o.readlines ()
    global best_length
    for i in range (len(lines)):
        elements = lines[i].split (",")
        if elements[0] == points_set:
            best_length = elements[1]
            x_cors = lines[i + 1].split (",")
            y_cors = lines[i + 2].split (",")
            answer_path = lines[i + 3].split (",")
            for num in range (len (x_cors)):
                best_path.append (int (answer_path[num]))
                adding = point (num, int (x_cors[num]), int (y_cors[num]))
                points.append (adding)
    o.close()

def solve (point_now):
    global my_length
    if len (my_path) == len (best_path):
        return
    else:
        my_path.append (point_now.num)
        closest_point = None
        smallest_distance = float ('inf')
        for point in points:
            if point.num != my_path:
                d = point_now.distance (point)
                if d < smallest_distance and d != 0:
                    closest_point = point
                    smallest_distance = d
        print ("Point now: ", point_now.num, "\tClosest: ", closest_point.num)
        my_path.append (closest_point.num)
        print ("path now: ", my_path)
        my_length += smallest_distance
        solve (closest_point)

parser ("points.csv", "A4")
points_left = copy.deepcopy (points)
print (len (points_left))
solve (points[0])
print (my_length)
print (my_path)
