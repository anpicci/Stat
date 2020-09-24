#! /usr/bin/env python
import sys
import os
import commands
import string
import optparse
from Stat.Limits.settings import *

#points = [vec1, vec2, vec3, vec4, vec5, vec6, vec7, vec8, vec9, vec10, vec11, vec12, vec13, vec14, vec15, vec16, vec17, vec18, vec19, vec20, vec21,vec22, vec23, vec24, vec25]
def getLimits(optdir, post):
   i = 0;
   sigmodelpoints=0
   for item in sigpoints:
      mass=item[0]
      width=item[1]
      chir = item[2]
      postfix=""
   
      sigmodelpoints+=1
      filename = "%s/WP_M%sW%s_%s/asymptotic_WP_M%sW%s_%s%s.log" %(optdir, mass, width, chir, mass, width, chir, post)
      os.system(("grep \"r < \" %s| awk '/Observed Limit/{f=1}f'") % (filename))
      os.system(("grep \"r < \" %s| awk '{print $5}' >> a%s") % (filename, i))
      
      print ("grep \"r < \" %s| awk '{print $5}' >> a%i") % (filename, i)  
    
      count=0
      with open (('a%i' % i), 'rb') as f:
         for line in f:
            count += 1
            
      if(count < 2):
         os.system("echo '0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n' >> a%i" % i)
      i = 1 + i
 
#   if(len(sigpoints)):sigmodelpoints+=1

   os.system("echo 'y_observed" + post + "        '>> left")
   os.system("echo 'y_down_points2" + post + "    '>> left")
   os.system("echo 'y_down_points1" + post + "    '>> left")
   os.system("echo 'y_vals" + post + "            '>> left")
   os.system("echo 'y_up_points1" + post + "      '>> left")
   os.system("echo 'y_up_points2" + post + "      '>> left")
   
   for i in xrange(sigmodelpoints):
         os.system("echo ' '>>commas")
         os.system("echo ' '>>right")
         
   os.system("rm data/limit"+post +".txt")
   print "rm data/limit"+post +".txt"
   #os.system("paste left a0 commas a1 commas a2 commas a3 commas a4 commas a5 commas a6 commas a7 commas a8 commas a9 commas a10 commas a11 commas a12 commas a13 commas a14 commas a15 commas a16 commas a17 commas a18 commas a19 commas a20 commas a21 commas a22 commas a23 commas a24 commas a25 commas a26 commas a27 commas a28 commas a29 commas a30 commas a31 commas a32 commas a33 commas a34 commas a35 commas a36 commas a37 commas a38 commas a39 commas a40 right  > data/limit" + post + ".txt")

   stringpaste="paste left "
 #  npaste=0
   for npaste in xrange(0,sigmodelpoints):
      stringpaste = stringpaste + "a"+str(npaste)
      if(npaste<sigmodelpoints-1):stringpaste = stringpaste+" commas "
      if(npaste==sigmodelpoints-1):stringpaste = stringpaste+" right "
      
  #    npaste=npaste+1
      
   print stringpaste   
   stringpaste=stringpaste+" > data/limit"+post+".txt"
   os.system(stringpaste)
#   os.system("paste left a0 commas a1 commas a2 commas a3 commas a4 commas a5 commas a6 commas a7 right  > data/limit" + post + ".txt")
#   os.system("paste left a0 commas a1 commas a2 commas a3 commas a4 commas a5 commas a6 commas a7 right  > data/limit" + post + ".txt")

   #os.system("paste left commas a6 commas a7 commas a8 commas a9 commas a10 commas a11 commas a12 commas a13 commas a14 commas a15 commas a16 commas a17 commas a18 commas a19 commas a20 commas a21 commas a22 commas a23 commas a24 commas a25 commas a26 commas a27 commas a28 commas a29 commas a30 commas a31 commas a32 commas a33 commas a34 commas a35 commas a36 commas a37 commas a38 commas a39 commas a40 right  > data/limit" + post + ".txt")
   #os.system("paste left a0 commas a1 commas a2 commas a3 commas a4 commas a5 commas a6 commas a7 commas a8 commas a9 commas a10 commas a11 commas a12 commas a13 commas a14 commas a15 commas a16 commas a17 commas a18 commas a19 commas a20 commas a21 commas a22 commas a23 commas a24 right  > data/limit" + post + ".txt")
   #os.system("paste left a0 commas a1 commas a2 right  > data/limit" + post + ".txt")
   #os.system("paste left a0 right  > data/limit" + post + ".txt")
   #print "paste left a0 commas a1 commas a2 commas a3 commas a4 commas a5 commas a6 commas a7 commas a8 commas a9 commas a10 commas a11 commas a12 commas a13 commas a14 commas a15 commas a16 commas a17 commas a18 commas a19 commas a20 commas a21 commas a22 commas a23 commas a24 commas a25 commas a26 commas a27 commas a28 commas a29 commas a30 commas a31 commas a32 commas a33 commas a34 commas a35 commas a36 commas a37 commas a38 commas a39 commas a40 right > data/limit" + post + ".txt"
   #print "paste left a0 commas a1 commas a2 commas a3 commas a4 commas a5 commas a6 commas a7 commas a8 commas a9 commas a10 commas a11 commas a12 commas a13 commas a14 commas a15 commas a16 commas a17 commas a18 commas a19 commas a20 commas a21 commas a22 commas a23 commas a24 commas a24 right > data/limit" + post + ".txt"
   #xprint "paste left a0 commas a1 commas a2 right > data/limit" + post + ".txt"
   
   #   print "paste left a0 right > data/limit" + post + ".txt"
   os.system("more data/limit"+post +".txt")

   os.system("rm -rf left right commas a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12 a13 a14 a15 a16 a17 a18 a19 a20 a21 a22 a23 a24 a25 a26 a27 a28 a29 a30 a31 a32 a33 a34 a35 a36 a37 a38 a39 a40")
      
