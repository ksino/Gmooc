#_*_coding:utf-8_*_

import json


def write_html():
    header = '<!DOCTYPE html><html><head><title></title></head><body>'
    with open('sex_real.txt', 'r') as f:
        data = json.load(f)
    for d in data:
        model = '<div class="column"><a href="{video}" rel="bookmark" title="{title}">{title}</a></div>'.format(image=d['image'], title=d['title'], video=d['mp4'])
        header += model
    header += '</body> </html>'
    with open('link.html', 'w') as f:
        f.write(header)


# def real_url():
#     with open('sex_real.txt', 'r') as f:
#         data = json.load(f)
#     for d in data[0]:
#         print data[0]
#         r = requests.get(d['video'])
#         tree = etree.HTML(r.content)
#         results = tree.xpath(r'//video/a/@href')
#         print results

# real_url()
write_html()
