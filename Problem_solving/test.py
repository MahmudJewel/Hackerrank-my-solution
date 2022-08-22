def revercify(num):
    st=''
    while num:
        rem=num%10
        num=int(num/10)
        st=st+str(rem)
    result=int(st)
    return result

print(revercify(120))