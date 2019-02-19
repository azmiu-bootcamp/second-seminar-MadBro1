print('0=Sunday, 1=Monday, 2=Tuesday, 3=Wednesday, 4=Thursday, 5=Friday, 6=Saturday')
day=int(input('0-dan 6-ya qədər rəqəm daxil edin: '))
print('True= Tətildir, False= Tətil deyil')
vocation=input('True və ya False daxil edin: ')
if 1<=day<=5 and vocation=='False':
    print('Zəngli saat işə düşdü: 07:00')
elif day in (0,6) and vocation=='False':
    print('Zəngli saat işə düşdü: 10:00')
elif 1<=day<=5 and vocation=='True':    
     print('Zəngli saat işə düşdü: 10:00')
elif day in (0,6) and vocation=='True':
    print('Zəngli saat söndürülmüşdür')
else:
    print('Əməliyyat mümkün olmadı')     
