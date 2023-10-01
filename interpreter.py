import sys


class FuzzError(Exception):
    pass


if not sys.argv[1].endswith(".fuzz"):
    raise FuzzError()

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

for line in lines:
    if line.startswith("echo "):
        if line.endswith(";"):
            line = line[::-1].replace(";", "", 1)[
                ::-1
            ]  # overcomplicated way of saying "remove last semicolon"
            print(line.replace("echo ", "", 1))
        else:
            raise FuzzError()
    else:
        if line.startswith("//"):
            continue  # AT LEAST I ADDED COMMENTS (although you can't put them at the end of lines)
        raise FuzzError()
