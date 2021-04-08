def print_circle(radius):
    circle = ""
    for i in range(-radius, radius):
        for i in range(-radius, radius):
            if i**2 + j**2 > radius**2:
                circle += " "
            else:
                circle += "x"
        circle += "\n"
    print(circle)

print_circle(10)
