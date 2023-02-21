nabor = input("Введите набор скобочек: ")

n1=nabor.find('{')
m1=nabor.find('}')
if m1==-1:
    m1=len(nabor)
n2=nabor.find('(')
m2=nabor.find(')')
if m2==-1:
    m2=len(nabor)
n3=nabor.find('[')
m3=nabor.find(']')
if m3==-1:
    m3=len(nabor)
x=0

y='0'*len(nabor)



while nabor!=y:
    if n1>m1 or n2>m2 or n3>m3:
            break
    if (m1==len(nabor)) and (m2==len(nabor)) and (m3==len(nabor)):
        break
    if ((n1!=-1) and (m1==len(nabor))) or ((n1==-1) and (m1!=len(nabor))):
            break
    if ((n2!=-1) and (m2==len(nabor))) or ((n2==-1) and (m2!=len(nabor))):
            break
    if ((n3!=-1) and (m3==len(nabor))) or ((n3==-1) and (m3!=len(nabor))):
            break
    if (min(m1,m2,m3)==m1) and (m1>0):
        k=list(nabor)
        k[m1]='0'
        while (k[m1-x] != '{'):
            x=x+1
            if k[m1-x]=='(':
                k[m1-x]='1'
                break
            if k[m1-x]=='[':
                k[m1-x]='1'
                break
            if (m1-x)==-1:
                break
        if k[m1-x]!='1':
            k[m1-x]='0'
        nabor=''.join(k)
        n1=nabor.find('{')
        m1=nabor.find('}')
        if m1==-1:
            m1=len(nabor)
        n2=nabor.find('(')
        m2=nabor.find(')')
        if m2==-1:
            m2=len(nabor)
        n3=nabor.find('[')
        m3=nabor.find(']')
        if m3==-1:
            m3=len(nabor)
        x=1
        if nabor==y:
            break
        i=0
        if nabor.find('1')!=-1:
            break
    if (min(m1,m2,m3)==m2) and (m2>0):
        k=list(nabor)
        k[m2]='0'
        while (k[m2-x] != '('):
            x=x+1
            if k[m2-x]=='{':
                k[m2-x]='1'
                break
            if k[m2-x]=='[':
                k[m2-x]='1'
                break
            if (m2-x)==-1:
                break
        if k[m2-x]!='1':
            k[m2-x]='0'
        nabor=''.join(k)
        n1=nabor.find('{')
        m1=nabor.find('}')
        if m1==-1:
            m1=len(nabor)
        n2=nabor.find('(')
        m2=nabor.find(')')
        if m2==-1:
            m2=len(nabor)
        n3=nabor.find('[')
        m3=nabor.find(']')
        if m3==-1:
            m3=len(nabor)
        x=1
        if nabor==y:
            break
        if nabor.find('1')!=-1:
            break
    if (min(m1,m2,m3)==m3) and (m3>0):
        k=list(nabor)
        k[m3]='0'
        while (k[m3-x] != '['):
            x=x+1
            if k[m3-x]=='{':
                k[m3-x]='1'
                break
            if k[m3-x]=='(':
                k[m3-x]='1'
                break
            if (m3-x)==-1:
                break
        k[m3-x]='0'
        nabor=''.join(k)
        n1=nabor.find('{')
        m1=nabor.find('}')
        if m1==-1:
            m1=len(nabor)
        n2=nabor.find('(')
        m2=nabor.find(')')
        if m2==-1:
            m2=len(nabor)
        n3=nabor.find('[')
        m3=nabor.find(']')
        if m3==-1:
            m3=len(nabor)
        x=1
        if nabor==y:
            break
        if nabor.find('1')!=-1:
            break

if nabor==y:
    print('true')
else:
    print('false')






