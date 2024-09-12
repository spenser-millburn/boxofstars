def generate_star_box(width, height):
    if width < 1 or height < 1:
        return []
    
    if height == 1:
        return ['*' * width]
    
    star_box = []
    for _ in range(height):
        star_box.append('*' * width)
    
    return star_box
