my_list1 =[]
my_list2 =[]

n = 1
while n < 6:
    my_list1.append(n)
    my_list2.append(n)
    n = n + 1
print(my_list1)

print(1 in  my_list1)
print(6 in  my_list1)
print(6 not in  my_list1)

my_number_1 = 1
my_number_2 = 2
print(my_number_1 == my_number_2)
print(my_number_1 is my_number_2)


print(my_list1 == my_list2)
print(my_list1 is my_list2)


car ={'hello':2000}
print(car.items())

my_dict = {}
print(any(my_dict))

my_dict2 = {"key_1": 1, "key_2": 2}
print(any(my_dict2))

class cylinder():
    def __init__(self,height,radius=1):
        self.height = height
        self.radius = radius
        self.surface_area = None
        self.volume = None

    def get_surface_area(self):
        return round(2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius**2, 2)

    def get_volume(self):
        return round(math.pi * self.radius**2 * self.height, 2)
