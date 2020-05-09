import copy
set_name = ""
best_length = 0 #the answer for the shortest length
best_path = [] #the answer for the order of points
points = [] #all the points
my_path = [] # path of numbers
my_points_path = [] #path of point objects
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
    global set_name
    for i in range (len(lines)):
        elements = lines[i].split (",")
        if elements[0] == points_set:
            set_name = elements[0]
            best_length = elements[1]
            x_cors = lines[i + 1].split (",")
            y_cors = lines[i + 2].split (",")
            answer_path = lines[i + 3].split (",")
            for num in range (len (x_cors)):
                best_path.append (int (answer_path[num]))
                adding = point (num, int (x_cors[num]), int (y_cors[num]))
                points.append (adding)
    o.close()

def other_solve (point_now, position):
    global other_length
    if None not in other_path:
        return
    else:
        if position == 0:
            other_path[0] = 0
            other_path[-1] = 0
            other_pointspath.append (point_now)
        else:
            if other_path[position] != None:
                other_path[len(other_path) - position] = point_now.num
                other_pointspath.append (point_now)
            else:
                other_path[position] = point_now.num
                other_pointspath.append (point_now)
        closest_point = None
        smallest_distance = float ('inf')
        for point in points:
            if point.num not in other_path:
                d = point_now.distance (point)
                if d < smallest_distance and d != 0:
                    closest_point = point
                    smallest_distance = d
        if closest_point != None:
            other_length += smallest_distance
            other_solve (closest_point, position + 1)
        else: #reached the end
            dist = point_now.distance (other_pointspath[0])
            other_path.pop()
            other_length += dist

def solve (point_now):
    global my_length
    if len (my_path) == len (best_path):
        return
    else:
        my_path.append (point_now.num)
        my_points_path.append (point_now)
        closest_point = None
        smallest_distance = float ('inf')
        for point in points:
            if point.num not in my_path:
                d = point_now.distance (point)
                if d < smallest_distance and d != 0:
                    closest_point = point
                    smallest_distance = d
        # print ("smallest distance: ", smallest_distance)
        #my_path.append (closest_point.num)
        # print ("path now: ", my_path)
        # print ()
        if closest_point != None:
            my_length += smallest_distance
            solve (closest_point)
        else: #reached the end
            dist = point_now.distance (my_points_path[0])
            my_length += dist


parser ("points.csv", "A30")

##### TO TEST OTHER SOLVER #####
other_path = [None for i in range (len (points) + 1)]
other_length = 0
other_pointspath = []
other_solve (points[0], 0)
# output = open ("firstsolve.txt", "w")
# s = set_name + "\n"
# for i in range (len (my_path)):
#     if i + 1 >= len (my_path):
#         s += (str (my_path[i]))
#     else:
#         s += (str (my_path[i]) + ",")
# output.write (s)
# output.close ()
print ("Second Solve Results\nMy Length\t", other_length)
print ("Answer    \n", best_length)
print ("My Path\t", other_path)
print ("Answer    \n\n", best_path)
##### TO TEST OTHER SOLVER #####

##### TO TEST FIRST SOLVER #####
solve (points[0])
# output = open ("firstsolve.txt", "w")
# s = set_name + "\n"
# for i in range (len (my_path)):
#     if i + 1 >= len (my_path):
#         s += (str (my_path[i]))
#     else:
#         s += (str (my_path[i]) + ",")
# output.write (s)
# output.close ()
print ("First Solve Results\nMy Length\t", my_length)
print ("Answer    \n", best_length)
print ("My Path\t", my_path)
print ("Answer    ", best_path)
##### TO TEST FIRST SOLVER #####
