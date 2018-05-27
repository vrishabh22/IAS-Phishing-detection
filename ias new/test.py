import numpy as np
import cv2 
from PIL import Image
from random import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
from collections import deque

#dna encoding
msg_str = raw_input('Enter message: ')
key =int(raw_input('Enter shift key: '))

msg=list(msg_str)
print msg
enc=[]
bin1=[]
j=0
dna=""
for i in msg:
	print i
	yy=(ord(i)-97+key)%26
	enc.append(chr(yy+97))
	
	xx='{0:08b}'.format(yy+97)
	bin1.append(xx)
print enc
print bin1
a=[]
a=np.array(a)
str_comp=""
matrix = [[0 for i in range(3)] for j in range(3)]
for b in bin1:
	#b -> string
	#complement
	str_comp=""
	for b1 in b:
		if(b1=='0'):
			str_comp=str_comp+'1'
		else:
			str_comp=str_comp+'0'

	print type(str_comp)
	matrix[0][0]=str_comp[0]
	matrix[1][0]=str_comp[1]
	matrix[2][0]=str_comp[2]
	matrix[0][1]=str_comp[3]
	matrix[1][1]=-1
	matrix[2][1]=str_comp[4]
	matrix[0][2]=str_comp[5]
	matrix[1][2]=str_comp[6]
	matrix[2][2]=str_comp[7]

	print matrix
	new_str=""
	for i in range(3):
		for j in range(3):
			if(matrix[i][j]!=-1):
				new_str=new_str+matrix[i][j]
	print new_str

	for i in range(4):
		if(new_str[i]+new_str[7-i]=='00'):
			dna=dna+'A'
		elif(new_str[i]+new_str[7-i]=='01'):
			dna=dna+'C'
		elif(new_str[i]+new_str[7-i]=='10'):
			dna=dna+'G'
		else:
			dna=dna+'T'

print "Encoded format is ",dna

img = cv2.imread("enc.png")

print "The image size is:", img.size
print "Image shape is:",img.shape
#for blue
b = img[:,:,0]
#for green
g = img[:,:,1]
#for red
r= img[:,:,2]

#for encoding algorithm mentioned in nit rourkela paper lsb technique
rs=r.copy()
bs=b.copy()
gs=g.copy()

print
print

ascii=[]



#ASCII -> bin

binary=[] #contains list of binary values for message

for i in range(len(dna)):
	v=ord(dna[i])
	ascii.append(v)
	v1 = '{0:08b}'.format(v)
	binary.append(v1)

print "binary of message",bin


#getting image dimsensions
shape=img.shape
rows = shape[0]
col = shape[1]



#For embedding data into image
count = 0
#for red
for i in range(rows):
	for j in range(col):
		rval = r[i][j]
		gval = g[i][j]
		bval = b[i][j]
		if count==len(binary):
			break
		bin_2bits = binary[count][6:]
		count=count+1

		red_bin =  '{0:08b}'.format(rv)
		green_bin =  '{0:08b}'.format(gv)
		blue_bin =  '{0:08b}'.format(bv)

		#print "red_bin value", red_bin

		red_2bits = red_bin[6:]
		#print "Last two bits of red pixel for pixel ",count," is ",red_2bits

		input_a0 = int(bin_2bits[0],2)
		input_b0 = int(red_2bits[0],2)
		xor_res0 = bin(input_a0^input_b0)
		xor_res0= xor_res0[2:] #after removing 0b
		input_a1 = int(bin_2bits[1],2)
		input_b1 = int(red_2bits[1],2)
		xor_res1 = bin(input_a1^input_b1)
		xor_res1 = xor_res1[2:]


		#print "result of xor is: ",xor_res0,xor_res1
		stego = red_bin[0:6]+xor_res0+xor_res1
		#print "stego 8 bit binary value is ",stego, " for pixel ", count
		int_red=int(stego,2)
		red_stego[i][j] = int_red
	if count==len(binary):
			break

print red
print red_stego

print "green"
count = 0
for i in range(rows):
	if i%2 == 0:
		for j in range(col):
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																					
	
			green_val = g[i][j]
			
			#print "count is",count
			if count==len(binary):
				break
			bin_2bits = binary[count][4:6]																																																																																																						     
			#print "The 5th and 6th of message is: ",bin_2bits, " for pixel ", count
			 
			count=count+1
			green_bin =  '{0:08b}'.format(green_val)
			green_2bits = green_bin[6:]
			#print "last 2 bits of green pixel is: ",green_2bits, " for pixel ", count

			
			input_a0 = int(bin_2bits[0],2)
			
			input_b0 = int(green_2bits[0],2)
			
			xor_res0 = bin(input_a0^input_b0)
			xor_res0= xor_res0[2:] 

			input_a1 = int(bin_2bits[1],2)
			
			input_b1 = int(green_2bits[1],2)
			
			xor_res1 = bin(input_a1^input_b1)
			xor_res1 = xor_res1[2:] 


			#print "result of xor for green pixel is: ",xor_res0,xor_res1
			stego = green_bin[0:6]+xor_res0+xor_res1
			#print "stego 8 bit binary value for green pixel is: ",stego
			int_green=int(stego,2)
			green_stego[i][j] = int_green
	
	else:

		j = col-1
		while j>=0: 
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																		
	
			green_val = green[i][j]
			
			#print "count is",count
			if count==len(binary):
				break
			bin_2bits = binary[count][4:6]																																																																																																						     
			#print "5th and 6th bit of message is: ",bin_2bits
			
			count=count+1

			green_bin =  '{0:08b}'.format(green_val)

			green_2bits = green_bin[6:]
			#print "last two bits of green pixel is: ",green_2bits, " for pixel ", count 
			
			input_a0 = int(bin_2bits[0],2)
			
			input_b0 = int(green_2bits[0],2)
			
			xor_res0 = bin(input_a0^input_b0)
			xor_res0= xor_res0[2:] 
			input_a1 = int(bin_2bits[1],2)
			
			input_b1 = int(green_2bits[1],2)
			
			xor_res1 = bin(input_a1^input_b1)
			xor_res1 = xor_res1[2:] 

			#print "result of xor for green pixel is: ",xor_res0,xor_res1, " for pixel ",count
			stego = green_bin[0:6]+xor_res0+xor_res1
			#print "stego 8 bit binary value for green pixel is: ",stego, " for pixel ", count
			int_green=int(stego,2)
			green_stego[i][j] = int_green
			j=j-1
	
	if count==len(binary):
			break

print green
print green_stego




print "blue"
count = 0
#for blue
for j in range(col):
	#print "blue"
	if j%2 == 0:
		for i in range(rows):
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																					
	
			blue_val = b[i][j]
			if count==len(binary):
				break
			bin_4bits = binary[count][0:4]																																																																																																						     
			#print "the first 4 bits of the message are: ",bin_4bits," for pixel ",count
			
			count=count+1
		
			blue_bin =  '{0:08b}'.format(blue_val)
			

			#print "blue_bin value", blue_bin

			blue_4bits = blue_bin[4:]
			#print "last four bits of blue pixel are: ",blue_4bits, " for pixel ",count
			input_a0 = int(bin_4bits[0],2)
			input_b0 = int(blue_4bits[0],2)
			xor_res0 = bin(input_a0^input_b0)
			xor_res0= xor_res0[2:] 
			input_a1 = int(bin_4bits[1],2)
			input_b1 = int(blue_4bits[1],2)
			xor_res1 = bin(input_a1^input_b1)
			xor_res1 = xor_res1[2:] 
			input_a2 = int(bin_4bits[2],2)
			
			input_b2 = int(blue_4bits[2],2)
			
			xor_res2 = bin(input_a2^input_b2)
			xor_res2 = xor_res2[2:] 
			
			input_a3 = int(bin_4bits[3],2)
			


			input_b3 = int(blue_4bits[3],2)
			
			xor_res3 = bin(input_a3^input_b3)
			xor_res3 = xor_res3[2:] 



			#print "result of xor for blue pixel",xor_res0,xor_res1, " for pixel ", count
			
			stego = blue_bin[0:4]+xor_res0+xor_res1+xor_res2+xor_res3
			#print "stego 8 bit binary value of blue pixel is: ",stego, "for pixel", count
			int_blue=int(stego,2)
			blue_stego[i][j] = int_blue
	
	else:

		i = rows-1
		while i>=0: 
			blue_val = blue[i][j]
			if count==len(binary):
				break
			bin_4bits = binary[count][0:4]																																																																																																						     
			print "first four bits of the message are: ",bin_4bits, " for pixel ",count
			
			count=count+1

			
			blue_bin =  '{0:08b}'.format(blue_val)
			

			
			blue_4bits = blue_bin[4:]
			print "last four bits of blue pixel is: ",blue_4bits, " for pixel ", count

			
			
			input_a0 = int(bin_4bits[0],2)
			
			input_b0 = int(blue_4bits[0],2)
			
			xor_res0 = bin(input_a0^input_b0)
			xor_res0= xor_res0[2:] 

			input_a1 = int(bin_4bits[1],2)
			print "input_a1",input_a1,type(input_a1)
			input_b1 = int(blue_4bits[1],2)
			print "input_b1",input_b1,type(input_b1)
			xor_res1 = bin(input_a1^input_b1)
			xor_res1 = xor_res1[2:] 

			input_a2 = int(bin_4bits[2],2)
			
			input_b2 = int(blue_4bits[2],2)
			xor_res2 = bin(input_a2^input_b2)
			xor_res2 = xor_res2[2:] 
			input_a3 = int(bin_4bits[3],2)
			input_b3 = int(blue_4bits[3],2)
			xor_res3 = bin(input_a3^input_b3)
			xor_res3 = xor_res3[2:]

			#print "result of xor for blue pixel ",xor_res0,xor_res1,xor_res2,xor_res3," for pixel ", count
			
			stego = blue_bin[0:4]+xor_res0+xor_res1+xor_res2+xor_res3
			#print "stego 8 bit binary value for blue pixel is: ",stego, " for pixel ",count
			int_blue=int(stego,2)
			blue_stego[i][j] = int_blue
			i=i-1

	if count==len(binary):
			break

print blue
print blue_stego

# merging 
merge_img =  cv2.merge((blue_stego,green_stego,red_stego))








#
#
#
#
#
#



####################################################################

print "OUTPUT IMAGE"

###########################################################################################33


cv2.imwrite('stego.png',merge_img)

#Decryption part


bit_xor = merge_img^img
print "The original image is", img
print "The merge image is", merge_img
print "The bit_xor imge is: ",bit_xor
#print "bit_xor[0][0]", bit_xor[0][0]
print "SHape of xor matrix",bit_xor.shape

l_encr_words_red=[]
l_encr_words_green=[]
l_encr_words_blue=[]
l_encr_words=[]
l_encr_words_int=[]


#For red
for i in range(rows):
	for j in range(col):
		








		r_bin = '{0:02b}'.format(bit_xor[i][j][2])

		
		###########################################################??
		l_encr_words_red.append(r_bin)

#For green
for i in range(rows):
	if i%2==0:
		for j in range(col):
			g_bin = '{0:02b}'.format(bit_xor[i][j][1])
			l_encr_words_green.append(g_bin)
	else:
		j=col-1
		while j>=0:
			g_bin = '{0:02b}'.format(bit_xor[i][j][1])
			l_encr_words_green.append(g_bin)
			j=j-1

#For blue
for j in range(col):
	if j%2==0:
		for i in range(rows):
	
			print "b value before ",bit_xor[i][j][0]
			b_bin = '{0:04b}'.format(bit_xor[i][j][0])
			print "b value 4 bits ",b_bin
		
			l_encr_words_blue.append(b_bin)
	else:
		i=rows-1
		while i>=0:
			print "b value before ",bit_xor[i][j][0]
			b_bin = '{0:04b}'.format(bit_xor[i][j][0])
			print "b value 4 bits ",b_bin
			l_encr_words_blue.append(b_bin)
			i=i-1
print "Length of list for b is ",len(l_encr_words_blue)
print "List is "
print "Size is ", bit_xor.size

for i in range(bit_xor.size/3):
	#print "blue value ", l_encr_words_blue[i]
	#print "green value ", l_encr_words_green[i]
	#print "red value ", l_encr_words_red[i]

	k = l_encr_words_blue[i] + l_encr_words_green[i] + l_encr_words_red[i]
	#print k
	l_encr_words.append(k)
	l_encr_words_int.append(int(k,2))


print l_encr_words_int

l_encr_words_bin=[]

for i in range(len(l_encr_words_int)):
	v2 = '{0:08b}'.format(l_encr_words_int[i])
	l_encr_words_bin.append(v2)

print "Binary form is ",l_encr_words_bin
#print '{0:04b}'.format(bit_xor[1][0][0]),'{0:02b}'.format(bit_xor[0][1][1]),'{0:02b}'.format(bit_xor[0][1][0])
l_encr_words_final=[]
for i in range(len(l_encr_words_int)):
	if(l_encr_words_int[i]<>0):
		l_encr_words_final.append(l_encr_words_int[i])
	else:
		break



print l_encr_words_final
enc_msg=""
for i in range(len(l_encr_words_final)):
	c=(chr)(l_encr_words_final[i])
	enc_msg=enc_msg+c

print enc_msg



dna1=enc_msg
# Decoding
dec_string=""

i=0
while(i<len(dna1)):
	j=0
	print "i is ",i
	binfromdna=[0]*8
	new_str=dna1[i:i+4]
	i=i+4
	print "new_str is ",new_str
	for k in range(4):	
		if(new_str[k]=='A'):
			binfromdna[j]='0'
			binfromdna[7-j]='0'	
		elif(new_str[k]=='C'):
			binfromdna[j]='0'
			binfromdna[7-j]='1'
		elif(new_str[k]=='G'):
			binfromdna[j]='1'
			binfromdna[7-j]='0'
		else:
			binfromdna[j]='1'
			binfromdna[7-j]='1'
		j=j+1
	print binfromdna

	matrix[0][0]=binfromdna[0]
	matrix[1][0]=binfromdna[1]
	matrix[2][0]=binfromdna[2]
	matrix[0][1]=binfromdna[3]
	matrix[1][1]=-1
	matrix[2][1]=binfromdna[4]
	matrix[0][2]=binfromdna[5]
	matrix[1][2]=binfromdna[6]
	matrix[2][2]=binfromdna[7]
	new_str1=""
	for m in range(3):
		for n in range(3):
			if(matrix[m][n]!=-1):
				new_str1=new_str1+matrix[m][n]
	print "new_str1 is ",new_str1
	str_comp1=""
	for n1 in new_str1:
		if(n1=='0'):
			str_comp1=str_comp1+'1'
		else:
			str_comp1=str_comp1+'0'
	print "complemented value is ",str_comp1
	print "int value is ",int(str_comp1,2)
	enc_char=chr(int(str_comp1,2))
	print enc_char

	yy1=(ord(enc_char)-97-key)%26
	dec_string=dec_string+(chr(yy1+97))

print dec_string