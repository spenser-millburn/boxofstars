import typer

def main(x: int, y: int):
    for _ in range(y):
        print('*' * x)

if __name__ == "__main__":
    typer.run(main)
