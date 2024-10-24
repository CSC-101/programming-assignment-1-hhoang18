import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(word:str)->int:
    vowels = "aeiouAEIOU"
    count = 0
    for i in word: #loop
        if i in vowels:
            count=count+1
    return count
#the function counts the number of vowels in a word
#the input is a string, the word
#the output is an integer, the number of vowels in the word
#parameter is type string, and an integer is returned

# Part 2
def short_lists(x: list[list[int]])->list[list[int]]:
    sublist=list[int]
    return [sublist for sublist in x if len(sublist)==2]
#the function finds elements in the input list that are of length 2
#the input is a nested list, the output is a nested list
#the parameter is a list[list[int]], and a list is returned

# Part 3
def ascending_pairs(x: [list[list[int]]])->list[list[int]]:
    sublist=list[int]
    result = []
    for sublist in x:
        if len(sublist)==2:
            result.append([min(sublist), max(sublist)])
        else:
            result.append(sublist)
    return result
#the function returns the elements of sublists with length 2 in ascending order
#sublists not equal to 2 remain in the same order
#the input is a nested list, the output is a nested list
#the parameter is type list[list[int]], and list[list[int]] is returned

# Part 4
class Price:
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents

def add_prices(price1: Price, price2: Price)->Price:
    total_cents = price1.dollars*100 + price2.dollars*100 + price1.cents+ price2.cents
    dollars = total_cents // 100
    cents = total_cents % 100
    return data.Price(dollars,cents)
#the function finds the sum of the input prices as cents, then changes it back
#into dollars and cents so that the number of cents is not above 99
#modulus makes sure that the cents are within 0-99
#input is price1, price2, integers
#output is Price; dollars and cents in integers
#parameters are price1, price2, which are two prices that are inputted
#Price is returned; Price uses integers

# Part 5
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right
def rectangle_area(rectangle1: Rectangle)->float:
    width=rectangle1.bottom_right.x-rectangle1.top_left.x
    height=rectangle1.top_left.y-rectangle1.bottom_right.y
    area = width*height
    return area
#the function's purpose is to compute and return the area of a provided rectangle
#input is coordinates for the top left and bottom right of the rectangle
#output is the area as a float
#the parameter is type Rectangle, integer coordinates
#a float area is returned

# Part 6
class Book:
    def __init__(self, authors: list[str], title: str):
        self.authors = authors
        self.title = title
def books_by_author(author_name:str, books: list[Book])->list[Book]:
    return [book for book in books if author_name in book.authors]
#the purpose of the function is to find books by a certain author and return them
#input is author name and list of books, output is a list of books
#parameters are type str and list[Book]
#list[Book] is returned

# Part 7
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius
class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

def circle_bound(rectangle1: Rectangle)->Circle:
    x_center = (rectangle1.top_left.x+rectangle1.bottom_right.x)/2
    y_center = (rectangle1.top_left.y+rectangle1.bottom_right.y)/2
    center = data.Point(x_center,y_center)
    #distance from center to corner (Pythagorean theorem)
    radius = ((rectangle1.top_left.x-x_center)**2+(rectangle1.top_left.y-y_center)**2)**0.5
    return Circle(center,radius)
#the function's purpose is to find the bounding circle for the rectangle
#the input is the points for the rectangle, output is Circle
#top_left and bottom_right are type Point
#Circle is returned; center is Point (which contains integers), radius is a float

# Part 8
class Employee:
    def __init__(self, name: str, pay_rate: int):
        self.name = name
        self.pay_rate = pay_rate

def below_pay_average(empl: list[Employee])->list[str]:
    total = 0
    for Employee in empl:
        total = total + Employee.pay_rate
    average = total/len(empl)
    return [Employee.name for Employee in empl if Employee.pay_rate < average]
#the function's purpose is to return a list of employees who are paid less
#than the average pay of all employees in the list
#input is the list of employee names and their pay rates
#output is a list (list[str]) of employee names who are paid less than average
#name is type string, pay_rate is type integer
#the parameter for the function is type list[Employee]
#a list[str] is returned containing employee names
