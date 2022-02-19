f1 = open('input.txt','r')
f2 = open('out.txt','w')
def xuly(matkhau):
    mk=matkhau
    matkhau=int(matkhau)
    if matkhau-9*len(mk)>0:
        ketqua=matkhau-9*len(mk)
    else: 
        ketqua=0
    while ketqua != matkhau:
        kq=str(ketqua)
        test=ketqua
        giatri=ketqua
        for dem in range(0,len(kq)):
            test=test+int(kq[dem])
        if test==matkhau:
            ketqua=test
        else:
            ketqua=ketqua+1
    giatri=str(giatri)
    f2.writelines(giatri)
kt=False
while kt==False:
    a=f1.readline()
    a=a.rstrip()
    if a!='':
        xuly(a)
    else: kt=True
f1.close()
f2.close()

    
    
