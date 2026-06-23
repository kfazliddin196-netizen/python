t=8
for i in range(1,11):
  print(t,'x',i,'=?')
  p=input()
  r=t*i
  if p=='keyingi':
    print('keyingi savol')
    continue
  if p=='bilmayman':
    break
  if int(p)==r:
    print("Barakala")
  else:
    print('Noto\'g\'ri kara jadvalni bilmas ekansiz',r)