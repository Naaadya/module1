X=input()
Xf=float(X)
Y=input()
Yf=float(Y)
max1=(Xf>Yf)*Xf+(Yf>=Xf)*Yf
print('Max: ',max1)