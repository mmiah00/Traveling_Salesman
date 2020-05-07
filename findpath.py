best_length = 0
best_path = []
points = []
class point:
    def __init__ (self, num, x, y):
        self.num = num
        self.x = x
        self.y = y

    def distance (self, another_point):
        delta_x = self.x - another_point.x
        delta_y = self.y - another_point.y
        return ((delta_x ** 2) + (delta_y ** 2)) ** 0.5

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

parser ("points.csv", "A12")
print (best_length)
print (best_path)
