
nsList = []
for line in open('NSList.txt','r').readlines():
    nsList.append(line.strip())


print (nsList)           
           

NSname = input("Please enter the NS Record ")



HP = input ("Is the project using a Nu-Heat Heat Pump?, Yes or No ")
if HP == 'Yes':
    print ("This is a Repeater project")
    if HP == 'Yes':
        raise SystemExit    
      
Size = input ("Is the project over 200 SQM? ")
if Size == 'Yes':
    print ("This is a Repeater project")
    if Size == 'Yes':
        raise SystemExit   

LPM = input ("Is this project over 120 SQM of Lo-Pro Max? ")
if LPM == 'Yes':
    print ("This is a Repeater project")
    if LPM == 'Yes':
        raise SystemExit

LP = input ("Is this project over 60 SQM of Lo-Pro10? ")
if LP == 'Yes':
    print ("This is a Repeater project")
    if LPM == 'Yes':
        raise SystemExit

    
else:
    print ("This is a runner")



