n=int(input())
tt=0
fh=0
th=0
oh=0
ft=0
ty=0
tn=0
fv=0
tw=0
on=0
while(n>=2000):
 tt=tt+1
 n=n-2000
while(n>=500):
 fh=fh+1
 n=n-500
while(n>=200):
 th=th+1
 n=n-200
while(n>=100):
 oh=oh+1
 n=n-100
while(n>=50):
 ft=ft+1
 n=n-50
while(n>=20):
 ty=ty+1
 n=n-20
while(n>=10):
 tn=tn+1
 n=n-10
while(n>=5):
 fv=fv+1
 n=n-5
while(n>=2):
 tw=tw+1
 n=n-2
while(n>=1):
 on=on+1
 n=n-1
if tt>0:
 print("2000:"+str(tt))
if fh>0:
 print("500:"+str(fh))
if th>0:
 print("200:"+str(th))
if oh>0:
 print("100:"+str(oh))
if ft>0:
 print("50:"+str(ft))
if ty>0:
 print("20:"+str(ty))
if tn>0:
 print("10:"+str(tn))
if fv>0:
 print("5:"+str(fv))
if tw>0:
 print("2:"+str(tw))
if on>0:
 print("1:"+str(on))
