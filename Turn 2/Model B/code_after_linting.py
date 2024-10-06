def calculate_area(shape, length, width=None):
    if shape == 'rectangle':
        area = length * width
    elif shape == 'square':
        area = length * length
    else:
        raise ValueError('Invalid shape entered!')
    return area

result = calculate_area('rectangle', 4, 6)
print(result)
