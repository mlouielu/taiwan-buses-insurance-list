import json
import re
import sys

from collections import defaultdict


INSURS = ['乘客責任險', '強制汽車責任險', '其他保險']


def main(ptype, total):
    j = json.load(open('result.json'))

    results = defaultdict(list)
    for d in j:
        for insu in INSURS:
            v = sorted(map(lambda x: int(x[1:-1]) if not x[0].isdigit() and x[1].isdigit() else
                           int(x[2:-1]) if not x[0].isdigit() or not x[1].isdigit() else
                           int(x[:-1]), filter(
                               lambda x: '事故' not in x and '總額' not in x,
                               re.findall(r'..\d+萬', d[insu]))))
            if v and d['營業種類'] in ptype:
                while v[-1] > 2999:
                    v.pop()
                results[insu].append(
                    (v[-1], d['公司名稱'], d[insu], f"[查看]({d['url']})"))

    for insu in INSURS:
        print(f'#類型: {insu}\n')

        print('| 金額 | 公司名稱 | 全文 | 連結 |')
        print('| --- | --- | --- | --- |')
        for i in sorted(results[insu])[-total:][::-1]:
            print('| ' + ' | '.join(map(str, i)) + ' |')
        print()


if __name__ == '__main__':
    ptype = ['公路汽車客運業']
    total = 0
    if len(sys.argv) > 1:
        if sys.argv[1].startswith('tour'):
            ptype = ['遊覽車客運業']
        elif sys.argv[1].startswith('all'):
            ptype.append('遊覽車客運業')
    if len(sys.argv) > 2:
        total = int(sys.argv[2])

    main(ptype, total)
