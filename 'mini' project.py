while 1==1:
    size=int(input("choose your board size:  15 or 19"))
    if size==15 or size==19:
        break
    else:
        print("error,try again")
# piece=[["十"for i in range(size)] for j in range(size)]
piece=["十"*size for j in range(size)]
for row in piece:
    # print(' '.join(row))
    print(row)
    print(type(row))
n=0
while 2==2:
    if n%2==0:
        player="x"
    else:
        player="o"
    a,b = input(f"Player {player}, enter your move (row column): ").split(',')
    