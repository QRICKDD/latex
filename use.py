import os
import re

def remove_n_t(x:str):
    while x.find('\n')!=-1:
        x=x.replace('\n','')
    while x.find('\t')!=-1:
        x=x.replace('\t','')
    return x

def remove_dollor(x:str):
    newx=''
    flag=False
    for item in x:
        if item=='$' and flag==False:
            flag=True
        elif item!='$' and flag==True:
            continue
        elif item=='$' and flag==True:
            flag=False
        elif item!='$' and flag==False:
            newx+=item
    return newx

def remove_redundant_blank(x:str):
    x=x.strip()
    while x.find('  ')!=-1:
        x=x.replace('  ',' ')
    while x.find(' .')!=-1:
        x=x.replace(' .','.')
    return x

def remove_item(x:str):
    while x.find('\item')!=-1:
        x=x.replace(r'\item','')
    return x

def remove_ref_cite_textbf_textit(x:str):
    pattern="ref\{.*?\}"
    pattern = re.compile(pattern)
    while pattern.search(x)!=None:
        (s,e)=pattern.search(x).regs[0]
        x=x.replace(x[s-1:e],'')

    #删掉cite
    pattern="cite\{.*?\}"
    pattern = re.compile(pattern)
    while pattern.search(x)!=None:
        (s,e)=pattern.search(x).regs[0]
        x=x.replace(x[s-1:e],'')

    #删掉textbf 保留内容
    pattern="textbf\{.*?\}"
    pattern = re.compile(pattern)
    while pattern.search(x)!=None:
        (s,e)=pattern.search(x).regs[0]
        x=x.replace(x[s-1:e],x[s+7:e-1])


    #删掉textit 保留内容
    pattern="textit\{.*?\}"
    pattern = re.compile(pattern)
    while pattern.search(x)!=None:
        (s,e)=pattern.search(x).regs[0]
        x=x.replace(x[s-1:e],x[s+7:e-1])
    return x


def remove_and_percent(x:str):
    x=x.replace(r'\&','&')
    x = x.replace(r'\%', '%')
    return x



# pattern="ref\{.*\}"
# pattern=re.compile(pattern)
# a=r'adaasdd \ref{asdaasdasaa,asdad} asd a'
# print(re.match(pattern,a))
# print(pattern.search(a))