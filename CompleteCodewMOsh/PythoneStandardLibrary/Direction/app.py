from pathlib import Path

path = Path('Direction')

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("Newname")

# directions = path.iterdir()
# print(directions)

# for p in path.iterdir():
#     print(p)

# paths = [p for p in path.iterdir()]
# print(paths)

# paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths)
# pyfiles = [p for p in path.glob("*.py")]
pyfiles = [p for p in path.rglob("*.py")]
print(pyfiles)
