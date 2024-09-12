def generate_star_box(width, height):
    if width < 1 or height < 1:
        return []

    star_box = []
    for _ in range(height):
        star_box.append('*' * width + ' ')
        
    return star_box
