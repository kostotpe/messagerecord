#對話紀錄練習

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: # utf-8-sig去掉奇怪讀取編碼
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ': ' + line)
    return new

def output_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    output_file('output.txt', lines)

main()

