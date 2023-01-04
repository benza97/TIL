
num = int(input('홀수인가? 짝수인가? >'))
if (num%2==1):
    print('홀수입니다.')
else:
    print('짝수입니다.')



dust = int(input('미세먼지 농도'))

if(dust < 30):
    print('좋음')
elif(dust < 80):
    print('보통')
elif(dust < 150):
    print('나쁨')
elif(dust > 151):
    print('매우나쁨')