import math
n=int(input("The number of flips : "))
H_OR_T=input("Head or Tail :")
n_of_app=int(input(f"The number of {H_OR_T} apperance : ") )
p=float(input(f"The probaility of {H_OR_T} (< 1) : "))
if p>1:
    print("please enter number < 1 ")
else:
    r=math.comb(n,n_of_app) * math.pow(p,n_of_app) *math.pow((1-p),(n-n_of_app))
    print("the answer is :",r)