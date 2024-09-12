import typer

def main(x: int, y: int):
    for _ in range(y):
        print('*' * x)
        print('')

if __name__ == "__main__":
    typer.run(main)
