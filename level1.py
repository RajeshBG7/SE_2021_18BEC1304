l=[]
for i in range (5):
    l.append(["-","-","-","-","-"])
print(l)

playerA=list(map(str,input().split(", ")))
for i in range(5):
    l[-1][i]="A-"+playerA[i]
print(l)

playerB=list(map(str,input().split(", ")))
for i in range(5):
    l[0][i]="B-"+playerB[i]
print(l)

players=["A","B"]
currentplayer=players[0]
k=0
while(True):
    check=-1
    move=input()
    movedirection=move[-1]
    for i in range(5):
        for j in range(5):
            if((currentplayer+"-"+move[0:2])==l[i][j]):
                if(currentplayer=="A"):
                    q=-1
                else:
                    q=1
                check=0
                temp=l[i][j]
                if(movedirection=="F"):
                    if(i+q<0 or l[i+q][j][0]==currentplayer):
                        print("Invalid Move")
                        check=-1
                    else:
                        l[i+q][j]=temp
                        l[i][j]="-"
                
                if(movedirection=="B"):
                    if(i-q>=5 or l[i-q][j][0]==currentplayer):
                        print("Invalid Move")
                        check=-1
                    else:
                        l[i-q][j]=temp
                        l[i][j]="-"
                
                if(movedirection=="R"):
                    if(j-q>4 or l[i][j-q][0]==currentplayer):
                        print("Invalid Move")
                        check=-1
                    else:
                        l[i][j-q]=temp
                        l[i][j]="-"
                
                if(movedirection=="L"):
                    if(j+q<0 or l[i][j+q][0]==currentplayer):
                        print("Invalid Move")
                        check=-1
                    else:
                        l[i][j+q]=temp
                        l[i][j]="-"
    if(check==0):
        k=k+1
        currentplayer=players[k%2]
    print(l)
    print(currentplayer)
    a_remaining=0
    b_remaining=0
    for i in l:
        for j in i:
            if j[0]=="B":
                b_remaining+=1
            if j[0]=="A":
                a_remaining+=1
    if(a_remaining==0):
        print("B Won")
        break
    if(b_remaining==0):
        print("A Won")
        break

