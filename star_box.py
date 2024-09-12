import typer

def main(x: int = typer.Option(..., help="Width of the rectangle"), y: int = typer.Option(..., help="Height of the rectangle")):
    for _ in range(y):
        print('*' * x, end=' ')

if __name__ == "__main__": 
    typer.run(main)
