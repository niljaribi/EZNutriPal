import os
import sys

import nltk
from nltk.corpus import *
from nltk import *
import pylev
import time
from difflib import SequenceMatcher

def nutrient_calculator(Number, Food, Unit, DefaultVal,FrDictCode,FrDictCal,FrDictAsh,FrDictCarb,FrDictFiber,FrDictLipid,FrDictProtein,FrDictSugar,Csum, outFile=None):
    string = []
    Calorie = []
    Ash = []
    Carb = []
    Fiber = []
    Lipid = []
    Protein = []
    Sugar = []
    string = ""
    for c in range(0, len(Food)):
        Calorie.append(round(((float(Number[c])/float(Unit[c]))*float(FrDictCal[Food[c]])),2))
        Ash.append(round(((float(Number[c])/float(Unit[c]))*float(FrDictAsh[Food[c]])),2))
        Carb.append(round(((float(Number[c])/float(Unit[c]))*float(FrDictCarb[Food[c]])),2))
        Fiber.append(round(((float(Number[c])/float(Unit[c]))*float(FrDictFiber[Food[c]])),2))
        Lipid.append(round(((float(Number[c])/float(Unit[c]))*float(FrDictLipid[Food[c]])),2))
        Protein.append(round(((float(Number[c])/float(Unit[c]))*float(FrDictProtein[Food[c]])),2))
        Sugar.append(round(((float(Number[c])/float(Unit[c]))*float(FrDictSugar[Food[c]])),2))        
        line = str(Number[c])+ ","+str(Unit[c])+ "," + Food[c] + "," + str(Calorie[c]) + "," + str(Ash[c]) + "," + str(Carb[c]) + "," + str(Fiber[c]) + "," + str(Lipid[c]) + "," + str(Protein[c]) + "," + str(Sugar[c]) + "," + str(FrDictCode[Food[c]]) + ","
        string += line
        if outFile is not None:
            outFile.write(line)
    
    return string
def string_matching(FN, Size, Unit, Threshold, raw):

    cup_file = "cupFile.txt"
    tbsp_file = "tbspFile.txt"
    tsp_file = "tspFile.txt"
    package_file = "packageFile.txt"
    oz_file = "ozFile.txt"
    inch_file = "inchFile.txt"
    lb_file = "lbFile.txt"
    scoop_file = "scoopFile.txt"
    size_file = "sizeFile.txt"
    default_file = "defaultFile.txt"
    gram_file = "gramFile.txt"
    code_file = "codesRev.txt"
    name_file = "NamesRev.txt"
    ash_file = "ash.txt"
    carb_file = "carb.txt"
    cube_file = "cube.txt"
    fiber_file = "fiber.txt"
    lipid_file = "lipid.txt"
    ml_file = "ml.txt"
    quantity_file = "quantity.txt"
    protein_file = "protein.txt"
    sugar_file = "sugar.txt"
    calorie_file = "caloriesRev.txt"
    data_dir = "data"
    parent_dir = os.path.dirname(os.path.abspath(__file__)) + "/" + data_dir + "/"


    f1= open(parent_dir + cup_file,'r')
    f2= open(parent_dir + cube_file,'r')
    f3= open(parent_dir + tbsp_file,'r')
    f4= open(parent_dir + tsp_file,'r')
    f5= open(parent_dir + ml_file,'r')
    f6= open(parent_dir + package_file,'r')
    f7= open(parent_dir + oz_file,'r')
    f8= open(parent_dir + inch_file,'r')
    f9= open(parent_dir + lb_file,'r')
    f10= open(parent_dir + quantity_file,'r')
    f11= open(parent_dir + scoop_file,'r')
    f12= open(parent_dir + size_file,'r')
    f14= open(parent_dir + default_file,'r')
    f15= open(parent_dir + gram_file,'r')
    f16= open(parent_dir + code_file,'r')
    f17= open(parent_dir + name_file,'r')
    f18= open(parent_dir + calorie_file,'r')

    f19= open(parent_dir + ash_file,'r')
    f20= open(parent_dir + carb_file,'r')
    f21= open(parent_dir + fiber_file,'r')
    f22= open(parent_dir + lipid_file,'r')
    f23= open(parent_dir + protein_file,'r')
    f24= open(parent_dir + sugar_file,'r')

    i=0
    Fcup = []
    Fcube = []
    Ftbsp = []
    Ftsp = []
    Fml = []
    Fpackage = []
    Foz = []
    Finch = []
    Flb = []
    Fquantity = []
    Fscoop = []
    Fsize = []
    Fdefault = []
    Fgram = []
    Fcode = []
    Fname = []
    Fcalorie = []
    Fash = []
    Fcarb = []
    Ffiber = []
    Flipid = []
    Fprotein = []
    Fsugar = []

    Fcup = f1.readlines()
    Fcube = f2.readlines()
    Ftbsp = f3.readlines()
    Ftsp = f4.readlines()
    Fml = f5.readlines()
    Fpackage = f6.readlines()
    Foz = f7.readlines()
    Finch = f8.readlines()
    Flb = f9.readlines()
    Fquantity = f10.readlines()
    Fscoop = f11.readlines()
    Fsize = f12.readlines()
    Fdefault = f14.readlines()
    Fgram = f15.readlines()
    Fcode = f16.readlines()
    Fname = f17.readlines()
    Fcalorie = f18.readlines()
    Fash = f19.readlines()
    Fcarb = f20.readlines()
    Ffiber = f21.readlines()
    Flipid = f22.readlines()
    Fprotein = f23.readlines()
    Fsugar = f24.readlines()
    
    List =[]
    for row in range(len(Fname)):
        List +=[[row]*24]
        

    FDictCal={}
    FDictAsh={}
    FDictCarb={}
    FDictFiber={}
    FDictLipid={}
    FDictProtein={}
    FDictSugar={}

    FDictCup={}
    FDictCube={}
    FDictTbsp={}
    FDictTsp={}
    FDictMl={}
    FDictPack={}
    FDictOz={}
    FDictInch={}
    FDictLb={}
    FDictQuantity={}
    FDictScoop={}
    FDictSize={}
    FDictDef={}
    FDictGram={}
    FDictCode={}
##
##    #############building the dictionaries#######################
    for i in range(0, len(Fname)-1):
        #print(i)
        Fcup[i] = Fcup[i].strip()
        Fcube[i] = Fcube[i].strip()
        Ftbsp[i] = Ftbsp[i].strip()
        Ftsp[i] = Ftsp[i].strip()
        Fml[i] = Fml[i].strip()
        Fpackage[i] = Fpackage[i].strip()
        Foz[i] = Foz[i].strip()
        Finch[i] = Finch[i].strip()
        Flb[i] = Flb[i].strip()
        Fquantity[i] = Fquantity[i].strip()
        Fscoop[i] = Fscoop[i].strip()
        Fsize[i] = Fsize[i].strip()
        Fdefault[i] = Fdefault[i].strip()
        Fgram[i] = Fgram[i].strip()
        Fcode[i] = Fcode[i].strip()
        Fname[i] = Fname[i].strip()
        Fcalorie[i] = Fcalorie[i].strip()
        Fash[i] = Fash[i].strip()
        Fcarb[i] = Fcarb[i].strip()
        Ffiber[i] = Ffiber[i].strip()
        Flipid[i] = Flipid[i].strip()
        Fprotein[i] = Fprotein[i].strip()
        Fsugar[i] = Fsugar[i].strip()

        List[i][0] = Fcup[i]
        List[i][1] = Fcube[i]
        List[i][2] = Ftbsp[i]
        List[i][3] = Ftsp[i]
        List[i][4] = Fml[i]
        List[i][5] = Fpackage[i]
        List[i][6] = Foz[i]
        List[i][7] = Finch[i]
        List[i][8] = Flb[i]
        List[i][9] = Fquantity[i]
        List[i][10] = Fscoop[i]
        List[i][11] = Fsize[i]
        List[i][13] = Fdefault[i]
        List[i][14] = Fgram[i]
        List[i][15] = Fcode[i]
        List[i][16] = Fname[i]
        List[i][17] = Fcalorie[i]
        List[i][18] = Fash[i]
        List[i][19] = Fcarb[i]
        List[i][20] = Ffiber[i]
        List[i][21] = Flipid[i]
        List[i][22] = Fprotein[i]
        List[i][23] = Fsugar[i]

        FDictCup[Fname[i]]=Fcup[i]
        FDictCube[Fname[i]]=Fcube[i]
        FDictTbsp[Fname[i]]=Ftbsp[i]
        FDictTsp[Fname[i]]=Ftsp[i]
        FDictMl[Fname[i]]=Fml[i]
        FDictPack[Fname[i]]=Fpackage[i]
        FDictOz[Fname[i]]=Foz[i]
        FDictInch[Fname[i]]=Finch[i]
        FDictLb[Fname[i]]=Flb[i]
        FDictQuantity[Fname[i]]=Fquantity[i]
        FDictScoop[Fname[i]]=Fscoop[i]
        FDictSize[Fname[i]]=Fsize[i]
        FDictDef[Fname[i]]=Fdefault[i]
        FDictGram[Fname[i]]=Fgram[i]
        FDictCal[Fname[i]] = Fcalorie[i]
        FDictAsh[Fname[i]] = Fash[i]
        FDictCarb[Fname[i]] = Fcarb[i]
        FDictFiber[Fname[i]] = Ffiber[i]
        FDictLipid[Fname[i]] = Flipid[i]
        FDictProtein[Fname[i]] = Fprotein[i]
        FDictSugar[Fname[i]] = Fsugar[i]
        FDictCode[Fname[i]] = Fcode[i]

    DictNum = {'a':1, 'an':1, 'half':0.5, 'quarter':0.75,'some':1, 'bit':1}

    tokens = word_tokenize(raw) # tokenizing the sentence
##    #########initializing##########
    Food = []
    Calorie = []
    SizeL = []
    UnitL = []
    UnitL1 = []
    Fcnt = -1;
    cnt = -1;
    Tcnt = -1;
    Ucnt = -1;
    count = 0;
    j=0

    minDist1 = 100000;
    minDist2 = 100000;
    minDist3 = 100000;

    minDistInd1=0;
    minDistInd2=0;
    minDistInd3=0;

    flagDist1 = False;
    flagDist2 = False;
    prevInd=-1;
    NumFlag = False
    Flag1=False
    Flag2=False
    Flag1prime = False
    Flag1prime1 = False
    flag3=False
    Flag2prime = False
    Namefound = False
    TimeFlag = False
    DefaultVal = 1;
    Csum =0;
    start_time = time.time()
    i=0
    tokens = word_tokenize(raw) # tokenizing the sentence
    flagNN = False
    flagDT = False

    print(str(tokens))
    ###### for all the tags######
    while i <= len(FN)-1:
        print(FN[i])
        #####everytime till we reach period########
        if FN[i] in FDictCal.keys():
            print("Foodname is:"+FN[i])
            Fcnt += 1
            Food.append(FN[i])
            Flag1 = True
            Flag1prime=True
            Flag1prime1 = True
            Namefound = True
            i=i+1
        else:
            ######String Matching##########
            for FrCounter in range(0,len(Fname)):
                distance = pylev.levenshtein(Fname[FrCounter],FN[i])
                simProb = SequenceMatcher(None,Fname[FrCounter],FN[i]).ratio()
                if (distance <= minDist1) and simProb >=Threshold:
                    minDist1 = distance
                    minDistInd1 = FrCounter
            FrCounter = 0
            if minDist1<10:
                Food.append(Fname[minDistInd1])
                Fcnt += 1;
                Flag1 = True
                Flag1prime = True
                Flag1prime1 = True
                i += 1
                prevInd = minDistInd1;
                flagDist1 = True;
                minDist1 = 10000;
                Namefound = True
                continue
        Namefound = False
        NumFlag = False
        TimeFlag = False
        dis = 0
        mindis = 10000
        mindisind=-1
    dis = 0
    mindis = 10000
    mindisind=-1
   
############simple matching##############
    
    if len(FN) == len(Size):
        for Scounter in range(0,len(Size)):
            SizeL.append(Size[Scounter])
    elif len(Size) < len(FN):
        for i in range(0,len(Size)):
            for j in range(0,len(FN)):
                FNTokens = word_tokenize(FN[j])
                dis = tokens.index(FNTokens[0])- tokens.index(Size[i])
                if(dis<mindis and dis>0):
                    mindis = dis
                    mindisind = j           
            for k in range(i,mindisind):        
                SizeL.insert(k,1)
            SizeL.insert(mindisind,Size[i])
            mindisind = -1
            mindis = 1000
            dis=0
    mindis = 10000
    mindisind=-1
    dis=0
    i=0
    j=0
    if len(Unit)== len(FN):
        for Ucounter in range(0,len(FN)):
            UnitL.append(Unit[Ucounter])
    else:
        for i in range(0,len(Unit)):
            for j in range(0,len(FN)):
                
                FNTokens = word_tokenize(FN[j])
                dis = tokens.index(FNTokens[0]) - tokens.index(Unit[i])
                if(dis<mindis and dis > 0):
                    mindis = dis
                    mindisind = j
            for k in range(i,mindisind):        
                UnitL.insert(k,"default")
            UnitL.insert(mindisind,Unit[i])
            mindisind = -1
            mindis = 1000
            dis=0



#######################################Unit Matching#######################################
    i=0;
    for i in range(0,len(UnitL)):
        if UnitL[i] == "cup" or UnitL[i] == "glass":
            if(FDictCup[Food[i]] != "null"):
                UnitL1.append(FDictCup[Food[i]])
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "piece":
            if(FDictQuantity[Food[i]] != "null"):
                UnitL1.append(FDictQuantity[Food[i]])
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "cube":
            if(FDictCube[Food[i]] != "null"):
                UnitL1.append(FDictCube[Food[i]])
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "ml":
            if(FDictMl[Food[i]] != "null"):
                UnitL1.append(FDictMl[Food[i]])
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i].strip() == "tbsp" or UnitL[i].strip() == "tablespoon":
            if(FDictTbsp[Food[i]] != "null"):
                UnitL1.append(FDictTbsp[Food[i]])
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "tsp" or UnitL[i] == "teaspoon":
            if(FDictTbsp[Food[i]] != "null"):
                UnitL1.append(FDictTbsp[Food[i]])
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "slice":
            if(FDictPiece[Food[i]] != "null"):
                UnitL1.append(FDictQuantity[Food[i]])
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "package":
            if(FDictPack[Food[i]] != "null"):
                UnitL1.append(FDictPack[Food[i]])
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "oz":
            if(FDictOz[Food[i]] != "null"):
                UnitL1.append(FDictOz[Food[i]])
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "inch":
            if(FDictInch[Food[i]] != "null"):
                UnitL1.append(FDictInch[Food[i]])
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "leaf":
            if(FDictQuantity[Food[i]] != "null"):
                UnitL1.append(FDictQuantity[Food[i]])
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "lb":
            if(FDictLb[Food[i]] != "null"):
                UnitL1.append(FDictLb[Food[i]])
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "scoop":
            if(FDictScoop[Food[i]] != "null"):
                UnitL1.append(FDictScoop[Food[i]])
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "small":
            if(FDictSize[Food[i]] != "small"):
                UnitL1.append(1)
            elif(FDictSize[Food[i]] != "large"):
                UnitL1.append(2)
            elif(FDictSize[Food[i]] != "medium"):
                UnitL1.append(1.5)            
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "large":
            if(FDictSize[Food[i]] != "small"):
                UnitL1.append(0.25)
            elif(FDictSize[Food[i]] != "large"):
                UnitL1.append(1)
            elif(FDictSize[Food[i]] != "medium"):
                UnitL1.append(0.5)            
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "medium":
            if(FDictSize[Food[i]] != "small"):
                UnitL1.append(0.5)
            elif(FDictSize[Food[i]] != "large"):
                UnitL1.append(1.5)
            elif(FDictSize[Food[i]] != "medium"):
                UnitL1.append(1)            
            else:
                UnitL1.append(FDictDef[Food[i]])

        elif UnitL[i] == "tall":
            if(FDictSize[Food[i]] != "tall"):
                UnitL1.append(1)
            elif(FDictSize[Food[i]] != "grande"):
                UnitL1.append(1.5)
            elif(FDictSize[Food[i]] != "venti"):
                UnitL1.append(2)            
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "grande":
            if(FDictSize[Food[i]] != "tall"):
                UnitL1.append(0.5)
            elif(FDictSize[Food[i]] != "grande"):
                UnitL1.append(1)
            elif(FDictSize[Food[i]] != "venti"):
                UnitL1.append(1.5)            
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "venti":
            if(FDictSize[Food[i]] != "tall"):
                UnitL1.append(0.25)
            elif(FDictSize[Food[i]] != "grande"):
                UnitL1.append(0.5)
            elif(FDictSize[Food[i]] != "venti"):
                UnitL1.append(1)            
            else:
                UnitL1.append(FDictDef[Food[i]])

        elif UnitL[i] == "footlong":
            if(FDictSize[Food[i]] != "6 inch"):
                UnitL1.append(2)
            elif(FDictSize[Food[i]] != "footlong"):
                UnitL1.append(1)            
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "6 inch":
            if(FDictSize[Food[i]] != "6 inch"):
                UnitL1.append(1)
            elif(FDictSize[Food[i]] != "footlong"):
                UnitL1.append(0.5)            
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "strip":
            if(FDictQuantity[Food[i]] != "null"):
                UnitL1.append(FDictQuantity[Food[i]])
            else:
                UnitL1.append(FDictDef[Food[i]])
        elif UnitL[i] == "gr" or UnitL[i] == "gram":
            if(FDictGram[Food[i]] != "null"):
                UnitL1.append(FDictGram[Food[i]])
            else:
                UnitL1.append(FDictDef[Food[i]])
        else:
            UnitL1.append(FDictDef[Food[i]])
        Ucnt += 1
        
    #################Calorie Calculator unit #######################   

    numLen=len(SizeL)
    foodLen = len(Food)
    unitLen = len(UnitL1)
    
    outStr = nutrient_calculator(SizeL, Food, UnitL1, DefaultVal,FDictCode, FDictCal,FDictAsh,FDictCarb,FDictFiber,FDictLipid,FDictProtein,FDictSugar,Csum)
    i+=1
    del SizeL
    del Food
    del UnitL1
    Food = []
    Calorie = []
    SizeL = []
    UnitL1 = []
    Fcnt = -1
    cnt=-1
    Tcnt = -1
    Ucnt = -1

    return outStr
                

