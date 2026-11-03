"""abbrev.py

Scan a file for known "abbreviations" and replace those with the full word. May also be used for correcting common typos.

"""


def load_abbrevs(filename: str) -> dict[str, str]:
    """Load a Tab Separated Values file containing substrings for replacement"""
    abbrevs = {}
    with open(filename, "rt") as file:
        for line in file.readlines():
            split_line = line.split('\t')
            abbrevs[split_line[0]] = split_line[1]
    return abbrevs


def read_textfile(filename:str) -> list[str]:
    """Read a text file for substring replacement"""
    with open(filename, "rt") as file:
        text = file.readlines()
    return text


def write_textfile(lines: list[str], filename: str) -> None:
    """Write out the corrected text"""
    text = []
    for line in lines:
        temp = []
        words = line.split()
        for word in words:
            if word in abbrevs:
                temp.append(abbrevs[word])
            else:
                temp.append(word)
        new_temp = ' '.join(temp)
        text.append(new_temp)
    with open(filename, "wt") as file:
        file.writelines(text)
    return


if __name__ == '__main__':
    abbrevs = load_abbrevs('abbrev.tsv')
    lines = read_textfile('typos.txt')
    # Use abbrevs to correct the text in lines here
    write_textfile(lines, 'corrected.txt')
