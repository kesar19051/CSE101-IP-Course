#string_functions_2019051.py

def get_every_fourth(s):
    r=s.strip()
    p=r[::-1]
    return p[::4]




def get_every_kth(s,k,i):
	r=s.strip()
	p=r[i::-k]
	return p[::-1]



def decode_string(s):
	r=s[::-1]
	x=r.index('_')
	p=r[x+1::]
	y=p.index('_')
	h=p[0:y]
	return h[::-1]

# hello

