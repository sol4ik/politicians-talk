import re


read_fie = open('stenograms.list', 'r')
write_files = []
for i in range(8):
    path = 'stenograms_skl' + str(i + 1) + '.list'
    write_files.append(open(path, 'w'))

for line in read_fie.readlines():
    link_pattern = r'http://data.rada.gov.ua/ogd/zal/agenda/skl\d/sten/\d+-?\d?.htm'
    skl_pattern = r'skl\d'
    link = re.search(link_pattern, line)
    skl = re.search(skl_pattern, line)
    skl_num = 0
    if skl:
        skl_num = int(skl.group(0)[-1])
    if link:
        write_files[skl_num - 1].write(link.group(0) + '\n')

read_fie.close()
for file in write_files:
    file.close()
