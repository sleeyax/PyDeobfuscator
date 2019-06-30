#!/usr/bin/env python
M=ImportError
T=print
R=False
I=object
try:
 import demiurgic
except M:
 T("Warning: You're not demiurgic. Actually, I think that's normal.")
try:
 import mystificate
except M:
 T("Warning: Dark voodoo may be unreliable.")
l=R 
class G(I):
 def __init__(self,*args,**kwargs):
  pass
 def D(self,dactyl):
  q=demiurgic.palpitation(dactyl)
  o=mystificate.dark_voodoo(q)
  return o
 def e(self,whatever):
  T(whatever)
if __name__=="__main__":
 T("Forming...")
 f=G("epicaricacy","perseverate")
 f.test("Codswallop")
# Created by pyminifier (https://github.com/liftoff/pyminifier)

