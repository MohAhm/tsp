

res = [
    (565.0, 575.0), (25.0, 185.0),
    (345.0, 750.0), (945.0, 685.0),
    (845.0, 655.0), (880.0, 660.0),
    (25.0, 230.0), (525.0, 1000.0),
    (580.0, 1175.0), (650.0, 1130.0)
]

data = []


# file_object = open('Assignment 3 berlin52.tsp')
# all_the_text = file_object.read()
# print(all_the_text)


# list_of_all_the_lines = file_object.readlines()
# print(list_of_all_the_lines)


# file_object.close()


# for line in open('thefile.txt'):
#     do_something_with(line)


file_object = open('Assignment 3 berlin52.tsp')
while True:
    line = file_object.readline()

    if not line:
        break

    elif line[0].isdigit():
        xy = tuple(line.strip().split())
        data.append((float(xy[1]), float(xy[2])))

file_object.close()

for d in data:
    print(d)

print(data)
print(len(data))

# def load_cities(filename):
#     path = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

#     ab_distance = []
#     with open(path) as file:
#         for line in file:
#             if 'A B' in line:
#                 break

#         for line in file:
#             if 'Straight' in line:
#                 break

#             ab = tuple(line.strip().split())
#             if ab:
#                 ab_distance.append((ab[0], ab[1], int(ab[2])))

#     return ab_distance
