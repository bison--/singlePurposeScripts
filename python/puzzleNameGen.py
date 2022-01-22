format_string = 'Assets/_{0}_{1}x{1}.png'
sizes = [4, 6, 10, 15, 20, 25]

image_name = input('enter name:')

for size in sizes:
    print(format_string.format(image_name, size))
