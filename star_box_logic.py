def generate_star_box(width, height):
    if width < 1 or height < 1:
        return []

    star_box = []
    for i in range(height):
        if i == 0 or i == height - 1:
            star_box.append('*' * width)
        else:
            star_box.append('*' + ' ' * (width - 2) + '*')

    return star_box
