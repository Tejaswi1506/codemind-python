m1,m2,m3,m4,m5=map(int,input().split())
p=((m1+m2+m3+m4+m5)/500)*100
if p>=90:
    print("Grade A")
elif p>=80:
    print("Grade B")
elif p>=70:
    print("Grade C")
elif p>=60:
    print("Grade D")
elif p>=40:
    print("Grade E")
else:
    print("Grade F")

