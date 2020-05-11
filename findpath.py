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
            #print ("Best Length: ", b_len)
            x_cors = lines[i + 1].split (",")
            y_cors = lines[i + 2].split (",")
            answer_path = lines[i + 3].split (",")
            for num in range (len (x_cors)):
                b_path.append (int (answer_path[num]))
                adding = point (num, int (x_cors[num]), int (y_cors[num]))
                points.append (adding)
    o.close()

def random_gen (points, num_lists): #produces a dictionary with num_lists items; key = distance || val = path
    #ans = {}
    ans = []
    for i in range (num_lists):
        adding = []
        nums = []
        dist = 0
        while len (nums) < len (points):
            r = random.randint (0,len (points) - 1)
            if r not in nums:
                nums.append (r)
                if len (adding) != 0:
                    dist += points[r].distance (adding[-1])
                adding.append (points[r])
        dist += adding[-1].distance (adding[0])
        ans.append (adding)
        #ans[ 1 / dist] = adding
    # print (ans)
    # print ()
    return ans

def cross_over (lists): #creates one child
    #keys = list (lists.keys ())
    r1, r2  = 0, 0
    while r1 == r2: #makes sure they dont produce the same number
        r1 = random.randint (0, len (lists) - 1)
        r2 = random.randint (0, len (lists) - 1)
    path1 = lists[r1]
    path2 = lists[r2]

    new_points = [None for i in range (len (path1))] #path of point objects
    new_path = [None for i in range (len (path1))] #list of the points' numbers
    r3 = random.randint (0, len (path1) - 1)
    if r3 != len(path1) - 1:
        r4 = r3 + 1
    else:
        r4 = 0

    new_points[r3] = path1[r3]
    new_points[r4] = path1[r4]
    new_path[r3] = path1[r3].num
    new_path[r4] = path1[r4].num

    i = max (r4, r3) + 1
    if i > len (path1) - 1:
        i = 0
    #print("before: ", new_path)
    while None in new_points:
        adding = path2[i]
        if adding.num not in new_path:
            new_points[i] = adding
            new_path[i] = adding.num
            if i == len (path1) - 1:
                i = 0
            else:
                i += 1
        else:
            if i == len (path1) - 1:
                i = 0
            else:
                i += 1
    return new_points

def mutate (path):
    r = random.randint (1, 100)
    if r < 5:
        r1, r2 = 0, 0
        while r1 == r2: #makes sure they dont produce the same number
            r1 = random.randint (0, len (path) - 1)
            r2 = random.randint (0, len (path) - 1)
        one = path[r1]
        another = path[r2]
        path[r1] = another
        path[r2] = one
        #print ("mutated!")
    # ans = []
    # for point in path:
    #     ans.append (point.num)
    # print (ans)
def find_length (path):
    dist = 0
    for i in range (len(path)):
        if i == len (path) - 1:
            dist += path[i].distance (path[0])
        else:
            dist += path[i].distance (path[i + 1])
    return dist

def genetic_solve (points, num_generation):
    gen_now = random_gen (points, 100) #makes 100 different random paths
    for i in range (num_generation):
        new_gen = []
        for j in range (len (gen_now)): #makes a new generation
            g = cross_over (gen_now) #makes one child
            mutate (g)
            #score = 1 / find_length (g)
            new_gen.append (g)
        gen_now = new_gen

    best_length = float ("inf")
    best_path = None
    for path in gen_now:
        l = find_length (path)
        if l < best_length:
            best_length = l
            best_path = path
    print ("My Length: ", best_length)
    print ()
    print ()
    return best_path


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
            my_points_path.append (my_points_path[0])
            my_path.append (my_points_path[0].num)
            my_length += dist

all_sets = ["A4", "A8", "A9", "A9-2", "A10", "A11", "A12", "A12-2", "A13", "A13-2", "A30", "A50"]
output = open ("out.txt", "w")
for name in all_sets:
    best_length = 0 #the answer for the shortest length
    best_path = [] #the answer for the order of points
    points = [] #all the points
    parser ("points.csv", name, best_length, best_path, points)

    ##### TESTING GENETIC SOLVE #####
    # ans = genetic_solve (points, 200)
    # s = name + "\n"
    # for i in range (len (ans)):
    #     p = ans[i]
    #     if i == len (ans) - 1:
    #         s += str (p.num)
    #     else:
    #         s += str (p.num) + ","
    # output.write (s + "\n\n")
    ##### TESTING GENETIC SOLVE #####

    ans_len = float ('inf')
    ans_path = None
    for p in points:
        my_path = [] # path of numbers
        my_points_path = [] #path of point objects
        my_length = 0
        solve (p, my_length, my_path, my_points_path, points)
        l = find_length (my_points_path)
        if l < ans_len:
            ans_len = l
            ans_path = my_path
    print (ans_len)
    s = name + "\n"
    for i in range (len (ans_path)):
        if i + 1 >= len (ans_path):
            s += (str (ans_path[i]))
        else:
            s += (str (ans_path[i]) + ",")
    output.write (s + "\n\n")
output.close ()
