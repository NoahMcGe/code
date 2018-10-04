# binarystring.py noah m
def print_menu():
	print('1. Decimal to Binary')
	print('2. Decimal to hex')

if __name__ == '__main__':
	print_menu()
	choice = input('which conversion would you like?: ')
	if choice == '1':
		bincon(decimal)
		
	if choice == '2':
		cal(a)

a=input("enter number in decimal :")
def cal(a):
    if a<10:
        b=str(a)
    elif a==10:
        b="A"
    elif a==11:
        b="B"
    elif a==12:
        b="C"
    elif a==13:
        b="D"
    elif a==14:
        b="E"
    else:
        b="F"
    return b
b=a
L1=""
while True:
    c=b%16
    if b<16:
        L1=L1+cal(c)
        break
    else:
        L1=L1+cal(c)
    b=b/16
c=""
for i in reversed(L1):
    c=c+i
print c


def bincon(decimal):
	print("BINARY\n")
	print (decimal)
	binstr=""
	for i in range(8):
		bin = decimal % 2
		binstr = binstr + str(bin)
		decimal = decimal // 2 
		print (bin)
	print(binstr)
	
def oof():
	print("INPUT -1 TO EXIT LOOP")
	print("INPUT AN INTEGER LESS THAN 256 AND GREATER THAN -1")
	done = 0;
	while (done >= 0):
		dec = input("INPUT AN INTEGER : ")
		bincon(dec)
oof()

