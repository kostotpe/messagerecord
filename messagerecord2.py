# line對話紀錄轉換練習
# 清單分割介紹 n[開始值:結尾值] 包含開始值 不包含結尾值
# n = [2, 6, 6, 8, 4]
# n[:3] # 前三個數字
# n[2:4] # 可以一個
# n[-2:] # 取最後兩個數字 結尾值不寫表示到底
# print(n[:3])
# print(n[2:4])
# print(n[-2:])

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: # utf-8-sig去掉奇怪讀取編碼
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    person = None
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)

    print('Allen說了', allen_word_count, '個字', '傳了', allen_sticker_count, '個貼圖')
    print('Allen傳了', allen_image_count, '個圖片')
    print('Viki說了', viki_word_count, '個字', '傳了', viki_sticker_count, '個貼圖')
    print('Viki傳了', viki_image_count, '個圖片')


def output_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    # output_file('output_line.txt', lines)

if __name__ == '__main__':
    main()

