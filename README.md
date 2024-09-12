# Star Box

This project contains two Python scripts to generate and display a box of stars (`*`).

## Files

- `star_box.py`: A command-line interface (CLI) script using Typer to print a box of stars.
- `star_box_logic.py`: A module with a function to generate a box of stars as a list of strings.

## Usage

### star_box.py

Run the script with the required arguments `--x` and `--y` to specify the width and height of the star box:

```
python3 star_box.py --x <width> --y <height>
```

### star_box_logic.py

Import the `generate_star_box` function to use it in your own scripts:

```python
from star_box_logic import generate_star_box

box = generate_star_box(width, height)
for line in box:
    print(line)
```

## Requirements

- Python 3.6+
- Typer

Install Typer using pip:

```
pip install typer

