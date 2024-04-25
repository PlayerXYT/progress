import os, sys

def progress_one(percent: int, number: bool = True, width: int = None) -> None:
    if width is None:
        width, _ = os.get_terminal_size()
    if number:
        width -= 5

    finished = width*percent//100
    unfinished = width-finished
    sys.stdout.write("\b\033[0;40;97m" + "━"*finished + "─"*unfinished + "\033[0m")

    if number:
        spaces = len(str(percent))
        sys.stdout.write(" "*spaces + str(percent) + "%")
    sys.stdout.flush()

def progress_two(percent_a: int, percent_b: int, number: bool = True, width: int = None) -> None:
    if width is None:
        width, _ = os.get_terminal_size()
    if number:
        width -= 5

    finished_a = width*percent_a//100
    finished_b = (width*percent_b//100) - finished_a
    unfinished = width-finished_a-finished_b
    sys.stdout.write("\b\033[0;40;97m" + "━"*finished_a + "\033[37m" + "━"*finished_b + "\033[97m" + "─"*unfinished + "\033[0m")

    if number:
        spaces = len(str(percent_a))
        sys.stdout.write(" "*spaces + str(percent_a) + "%")
    sys.stdout.flush()
