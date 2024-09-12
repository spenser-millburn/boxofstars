import typer

def generate_star_box(x: int, y: int):
    if x < 2 or y < 2:
        for _ in range(y):
            print('*' * x)
    else:
        print('*' * x)
        for _ in range(y - 2):
            print('*' + ' ' * (x - 2) + '*')
        print('*' * x)

def main(x: int = typer.Option(..., help="Width of the rectangle"), y: int = typer.Option(..., help="Height of the rectangle")):
    generate_star_box(x, y)

if __name__ == "__main__": 
    typer.run(main)
