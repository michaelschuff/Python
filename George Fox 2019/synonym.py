num=int(input())
synonyms=[]
synIn=input()
synonyms=synIn.split(",")
textBlock=[]
for i in range(num):
    textIn=input()
    newList=textIn.split(" ")
    textBlock.append(newList)
counter=0
punct=""
for i in range(len(textBlock)):
    for x in range(len(textBlock[i])):
        punct=textBlock[i][x][len(textBlock[i][x])-1]
        if(punct == "." or punct == "," or punct == ":" or punct == ";" or punct == "!" or punct == "?"):
            textBlock[i][x]=textBlock[i][x][:len(textBlock[i][x])-1:1]
        else:
            punct=""
        if(textBlock[i][x] == synonyms[0]):
            textBlock[i][x]=synonyms[counter]
            counter+=1
            if(counter == len(synonyms)):
                counter=0
        textBlock[i][x]+=punct
        if(x!=len(textBlock[i])-1):
            print(textBlock[i][x],end=" ")
        else:
            print(textBlock[i][x],end="")
    print()