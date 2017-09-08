p=" ---"
q="|   "
heightinp= int(input("Enter the height of the board: "))
widthinp= int(input("Enter the width of the board: "))
def gameboard(a,b):
    total=a*2+1
    for i in range(total):
        if(i%2==0):
                print(p*widthinp)
        else:
                print(q*(widthinp+1))

gameboard(heightinp,widthinp)