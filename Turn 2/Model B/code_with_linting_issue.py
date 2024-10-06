def calculate_area(shape, length, width=None):
    if shape == 'rectangle':
        area = length * width
    elif shape == 'square':
        area = length * length
    else:
        print('Invalid shape entered!')
        return
    return area

result = calculate_area('rectangle', 4, 6)
print(resul)  # Typo in 'print' statement
