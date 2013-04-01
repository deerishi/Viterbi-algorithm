import sys
taglist=['O','RARE','I-GENE','ALLCAPS','NUMERIC','LASTCAP']
pi_prob=[]
tag_nos=[0.0,0.0,0.0,0.0,0.0,0.0]

def main():
	f=open('unigram.txt','r')
	for line in f:
		i=0
		p=line.split()
		while(i<6):
			if(p[2]==taglist[i]):
				c=float(p[0])
				tag_nos[i]=tag_nos[i]+c
				break
			i=i+1
	f.close()
	print 'nos of each tags are=',tag_nos
	#sys.exit(0)
	f1=open('gene.test','r') #test file
	f2=open('gene_test.p3.out','w')#output file
	k=0
	w='*'
	u='*'
	prev=1
	nos=0
	for line2 in f1:
		p=line2.split()
		for ww in p:
			line=ww
			break
		if(line2=='\n'):
			k=0
			w='*'
			u='*'
			prev=1
			f2.write(line2)
		else:
			for v in taglist:
		 		q=trigram(w,u,v)
		 		e=emission(line,v)
		 		cur=prev*q*e
		 		pi_prob.append(cur)
		 		#print 'w=%s,u=%s,v=%s,x=%s,q=%f,e=%f'%(w,u,v,line,q,e)
		 	max_prob=max(pi_prob)
		 	if (max_prob!=0):
		 		index_v=pi_prob.index(max_prob)
		 		x=line+' '+taglist[index_v]+'\n'
		 		prev=max_prob
		 		del pi_prob[:]
		 		w=u
		 		u=taglist[index_v]
		 		f2.write(x)
		 		nos=nos+1
		 		print 'in line=',nos
		 	else:
		 		len1=len(line)
				i=0
				isnum=0
				while(i<len1):
					if(line[i].isdigit()):
						isnum=1
						rtag='NUMERIC'
					i=i+1
				if(isnum==1):
					rtag='NUMERIC'
				elif(line.isupper()):
					rtag='ALLCAPS'
				elif(line[len1-1].isupper() and line[:len1-1].islower()):
					rtag='LASTCAP'
				else:
					rtag='RARE'
		 		x=line+' '+rtag+'\n'
		 		#prev=1
		 		del pi_prob[:]
		 		w=u
		 		u=rtag
		 		f2.write(x)
		 		nos=nos+1
		 		print 'in line=',nos
		 	
		 	
def trigram(w,u,v):
	f3=open('trigram.txt','r+')
	f4=open('bigram.txt','r+')
	c2=0
	c1=0
	for line in f3:	
		p=line.split()
		if(p[2]==w and p[3]==u and p[4]==v):
			c1=float(p[0])
			break
	for line in f4:	
		p=line.split()
		if(p[2]==w and p[3]==u):
			c2=float(p[0])
			break
	if(c2!=0):
		x=float(c1)/float(c2)
		return x
	else:
		return 0
	f3.close()
	f4.close()
	
def emission(w,v):
	f5=open('unigram.txt','r+')
	c1=0
	#print 'w=%s v=%s'%(w,v)
	for line in f5:
		p=line.split()
		#if(w=="heart"):
			#print 'in heart'
		if(p[3]==w and p[2]==v):
			c1=float(p[0])
			#print '\tfound seq in emi c1=%f'%(c1)
	i=taglist.index(v)
	f5.close()
	if(c1==0):
		return 0.0
	else:
		x=float(c1)/tag_nos[i]		
		return x
	
if __name__=='__main__':
	main()	
		 	
		 
		 
