'''import sys,traceback
try:
	d=1+'l'
except :
	k=traceback.format_exc()
'''


l=[]
def fun():
	global l
	l.append(1)

print l

