from pathlib import Path

base = Path("data")
file_path = base/"user.txt"

print(file_path)
print(file_path.name)
print(file_path.parent) # directory
print(file_path.suffix) # file extension