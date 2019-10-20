# coding:utf-8
import os
import sys
import re
import pdfkit

infile=sys.argv[1]
outfile=sys.argv[2]
sep=sys.argv[3]
pat=re.compile(r'[\s\n\r]')
lines=[]
outs=[]
size=5
size1=4
idx=0
template=''

options={
    'page-size':'Letter',
    'margin-top':'0.75in',
    'margin-right':'0.75in',
    'margin-bottom':'0.75in',
    'margin-left':'0.75in',
    'encoding':"UTF-8",
    'no-outline':None
}

# with open('compareTemplate.html') as sample:
#     template=sample.read()
#     print(template)

with open(infile) as inn:
    lines=inn.readlines()


for line in lines:
    line=pat.sub('',line)
    outs.extend(line.split(sep))

# with open(outfile,mode='w') as savefile:
#     savefile.write(template)
str=""
for one in outs:
    if idx%size==0:
        str+='<tr>'
    str+='<td><div>'
    for e in one:
        str+=e+'<br />'
    str+='</div></td>'
    if idx%size==size1:
        str+='</tr>'
    idx+=1
        #savefile.write(str)
    # savefile.write(str)
    # savefile.write('</table></body></html>')
#print(str)
pdfkit.from_string('<table width="100%">'+str+"</table></body></html>",outfile,css="c.css",options=options)