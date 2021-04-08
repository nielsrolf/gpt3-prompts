from glob2 import glob

def count_code_lines(src_dir):
    lines = 0
    for filepath in glob(f"{src_dir}/**/*.py"):
        with open(filepath, "r") as f:
            lines +=  len(f.readlines())
    return lines

print(count_code_lines("."))
