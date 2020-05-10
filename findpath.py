import copy
import random
set_name = ""

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

def parser (file, points_set, b_len, b_path, pnts):
    o = open (file, "r")
    lines = o.readlines ()
    for i in range (len(lines)):
        elements = lines[i].split (",")
        if elements[0] == points_set:
            b_len = elements[1]
            x_cors = lines[i + 1].split (",")
            y_cors = lines[i + 2].split (",")
            answer_path = lines[i + 3].split (",")
            for num in range (len (x_cors)):
                b_path.append (int (answer_path[num]))
                adding = point (num, int (x_cors[num]), int (y_cors[num]))
                points.append (adding)
    o.close()

def random_gen (points, num_lists): #produces num_lists lists with random ordering of the points
    ans = []
    for i in range (num_lists):
        adding = []
        nums = []
        while len (nums) < len (points):
            r = random.randint (0,len (points) - 1)
            if r not in nums:
                nums.append (r)
                adding.append (points[r])
        ans.append (adding)
        #print (nums)
    #print ()
    return ans


def solve (point_now, my_length, my_path, my_points_path, all_points):
    if len (my_path) == len (all_points):
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
        if closest_point != None:
            my_length += smallest_distance
            solve (closest_point, my_length, my_path, my_points_path, all_points)
        else: #reached the end
            dist = point_now.distance (my_points_path[0])
            my_length += dist

all_sets = ["A4", "A8", "A9", "A9-2", "A10", "A11", "A12", "A12-2", "A13", "A13-2", "A30", "A50"]
output = open ("out.txt", "w")
for name in all_sets:
    best_length = 0 #the answer for the shortest length
    best_path = [] #the answer for the order of points
    points = [] #all the points
    parser ("points.csv", name, best_length, best_path, points)
    a = random_gen (points, 3)
    # my_path = [] # path of numbers
    # my_points_path = [] #path of point objects
    # my_length = 0
    # solve (points[0], my_length, my_path, my_points_path, points)
    # s = name + "\n"
    # for i in range (len (my_path)):
    #     if i + 1 >= len (my_path):
    #         s += (str (my_path[i]))
    #     else:
    #         s += (str (my_path[i]) + ",")
    # output.write (s + "\n\n")
output.close ()

##### TESTING ONE BY ONE #####
# parser ("points.csv", "A30")
# solve (points[0])
# output = open ("out.txt", "w")
# s = set_name + "\n"
# for i in range (len (my_path)):
#     if i + 1 >= len (my_path):
#         s += (str (my_path[i]))
#     else:
#         s += (str (my_path[i]) + ",")
# output.write (s + "\n")
# output.close ()
# print ("First Solve Results\nMy Length\t", my_lengthgth)
# print ("Answer    ", best_length)
# print ("My Path\t", my_path)
# print ("Answer    ", best_path)
##### TO TEST FIRST SOLVER #####
