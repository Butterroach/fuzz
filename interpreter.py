import sys

VERSION = "1.0.0"


class FuzzError(Exception):
    pass


def interpret(line: str):
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
            return  # AT LEAST I ADDED COMMENTS (although you can't put them at the end of lines)
        raise FuzzError()


if len(sys.argv) > 1:
    if not sys.argv[1].endswith(".fuzz"):
        raise FuzzError()

    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    for line in lines:
        interpret(line)
else:
    print(f"fuzz v{VERSION} shell. press ctrl+c to close.")
    while True:
        try:
            line = input("fuzz> ")
            interpret(line)
        except FuzzError:
            print("FuzzError occurred")
            print("you messed up and i wont tell you!!!!")
            continue
        except (KeyboardInterrupt, EOFError):
            break

print("\nfinished executing!")
sys.exit(0)
