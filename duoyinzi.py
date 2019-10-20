import sys
import os
import pdfkit
import re

path=os.path.split(os.path.realpath(__file__))[0]
pat=re.compile(r'[\s\n\r]')
infile=sys.argv[1]
outfile=sys.argv[2]

lines=[]
outs=[]
with open(os.path.join(path,infile)) as inputfile:
    lines=inputfile.readlines()

for line in lines:
    line=pat.sub('',line)
    outs.extend(line)
str=""
size=5
size1=size-1
idx=0
for one in outs:
    for e in one:
        if idx%size==0:
            str+='<tr>'
        str+='<td>'+e+'</td>'
        if idx%size==size1:
            str+='</tr>'
        idx+=1

if idx%size<size1:
    str+='</tr>'

options={
    'page-size':'Letter',
    'margin-top':'0.75in',
    'margin-right':'0.75in',
    'margin-bottom':'0.75in',
    'margin-left':'0.75in',
    'encoding':"UTF-8",
    'no-outline':None
}

str='<html><body><table width="100%">'+str+"</table></body></html>"
print(str)
pdfkit.from_string(str,os.path.join(path,outfile),css="c.css",options=options)