import re


def format_anchor(s):
    s = re.sub(r"[^\w\s-]", '', s.lower())
    s = re.sub(r"\s", '-', s.lstrip().rstrip('\r\n'))
    return s


if __name__ == '__main__':
    s = input()
    print(format_anchor(s))
