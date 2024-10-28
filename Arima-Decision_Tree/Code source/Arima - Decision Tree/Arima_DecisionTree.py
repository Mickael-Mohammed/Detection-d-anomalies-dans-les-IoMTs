import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc


def Prediction(file,file2, file3):


    f = open(file, "r")
    f2 = open(file2,"w")
    f3 = open(file3,"w")

    # Création des listes de valeurs

    # Liste des valeurs de SP02 extraites à partir du fichier contenant le jeu de données
    SP02_values = []

    # Liste de valeurs de Heart rate extraites
    HR_values = []

    # Liste de valeurs de Blood Pressure
    BP_values = []

    #Liste des valeurs de la classe
    Classe_Reel=[]



    # Lecture du fichier et stockage de chacune des lignes du jeu de données dans le tableau lines
    # Chaque valeur du tableau lines correpond à une ligne du fichier
    lines = f.readlines()

    # La somme des résidus
    Sum_error_rate=0

    # Affichage des deux premières lignes du dataset contenant les noms des paramètres de santé ainsi que leurs unités
    print(lines[0])
    print(lines[1])

    line0=lines[0]
    line1=lines[1]

    f2.write(line0)
    f2.write((line1))
    f3.write(line0)
    f3.write((line1))
    lines.remove(lines[0])
    lines.remove(lines[0])
    tmp=[]
    for l in lines:

        newLine1 = l.replace("\n", "")
        newLine2 = newLine1.split(',')

        # Conversion des valeurs de str à float
        newLine2[2]=float(newLine2[2])
        newLine2[4]=float(newLine2[4])
        newLine2[7]=float(newLine2[7])


        # Ajout des valeurs de chaque paramètre à une liste
        HR_values.append(newLine2[4])
        BP_values.append((newLine2[2]))
        SP02_values.append((newLine2[7]))
        tmp.append(newLine2[8])

    for val in tmp:
        chaine = val.replace("'","")
        chaine2 = chaine.replace("]","")
        chaine3= chaine2.replace(" ","")
        Classe_Reel.append(chaine3)


    # taille de la fenetre des sous-listes de valeurs utilisées pour la prédiction
    n=12

    # Indice dans la liste des valeurs de Heart Rate
    i=0


    HR_list=[]
    HR_subset=[]
    SP02_list=[]
    SP02_subset=[]



    for valeur in HR_values:
        if i<n:

            if(i!=0):
                if(HR_values[i]+10<HR_values[i-1] or HR_values[i]-10>HR_values[i-1]):
                    HR_subset.append(HR_values[i])


                    i=i+1


                else:
                    HR_subset.append(HR_values[i])
                    i = i + 1
            else:
                HR_subset.append(HR_values[0])
                i=i+1


        else:

            HR_list.append(HR_subset)
            n=n+12

            HR_subset=[]
            if (HR_values[i]+10 < HR_values[i-1] or HR_values[i]-10 > HR_values[i-1]):
                HR_subset.append(HR_values[i])
                i = i + 1
            else:
                HR_subset.append(HR_values[i])
                i = i + 1

    i = 0
    n = 12

    for valeur in SP02_values:
        if i<n:

            if(i!=0):
                if(SP02_values[i]+10<SP02_values[i-1] or SP02_values[i]-10>SP02_values[i-1]):
                    HR_subset.append(HR_values[i])


                    i=i+1


                else:
                    SP02_subset.append(SP02_values[i])
                    i = i + 1
            else:
                SP02_subset.append(SP02_values[0])
                i=i+1


        else:

            SP02_list.append(SP02_subset)
            n=n+12

            SP02_subset=[]
            if (SP02_values[i]+10 < SP02_values[i-1] or SP02_values[i]-10 > SP02_values[i-1]):
                SP02_subset.append(SP02_values[i])
                i = i + 1
            else:
                SP02_subset.append(SP02_values[i])
                i = i + 1


    List_len=[]
    for val in SP02_list:
        x= len(val)
        List_len.append(x)

    print(List_len)




    BP_list = []
    BP_subset = []
    i=0
    n=12

    for valeur in BP_values:
        if i<n:

            if(i!=0):
                if(BP_values[i]+10<BP_values[i-1] or BP_values[i]-10>BP_values[i-1]):
                    BP_subset.append(BP_values[i])
                    i=i+1


                else:
                    BP_subset.append(BP_values[i])
                    i = i + 1
            else:
                BP_subset.append(BP_values[0])
                i=i+1


        else:

            # On ajoute la sous liste de 12 valeurs de BP à la liste contenant toutes les sous listes de BP
            BP_list.append(BP_subset)

            n=n+12

            BP_subset=[]
            if (BP_values[i]+10 < BP_values[i-1] or BP_values[i]-10 > BP_values[i-1]):
                BP_subset.append(BP_values[i])
                i = i + 1
            else:
                BP_subset.append(BP_values[i])
                i = i + 1

    print(BP_list)

    List_len = []
    for val in BP_list:
        x = len(val)
        List_len.append(x)












    # Liste contenant des sous listes de valeurs de prédictions
    Forecast_list=[]


    # Listes contenant toutes les valeurs de prédictions
    Forecast_values=[]


    # Listes contenant toutes les résidus temporelles
    Error_rate_list=[]



    # Arima
    # Prédictions d'une sous liste de valeur d'un paramètre de santé avec Arima





    def Arima(param):

        index = 0
        List_values=[]
        if(param=="HR_list"):
            List_values=HR_list
        if(param=="BP_list"):
            List_values=BP_list
        if(param=="SP02_list"):
            List_values=SP02_list

        print(List_values)
        Sum_error_rate=0

        # Pour chaque sous-liste de la liste composé de sous listes de valeurs d'un paramètre de santé
        for l in List_values:



            model = sm.tsa.ARIMA(l, order=(2, 1, 1))

            # Ajuster le modèle aux données
            result = model.fit()

            # Prédire les 12 prochaines valeurs
            forecast = result.forecast(steps=12)

            for x in forecast:
                Forecast_values.append(x)

            forecast1=[]
            for x in forecast:
                forecast1.append(x)




            Forecast_list.append(forecast1)


            #Indice dans la liste forecast
            i = 0

            # Index sert à ne pas prendre en compte la première sous-liste de valeurs réelles car il n'y a pas de valeurs de prédictions à comparer avec la 1ère sous liste puisque ces prédictions ont été émises à partir de la 1ère sous-liste
            Error_rate=0
            if (index != 0 and index!=List_values.__len__()-1):

                Next_index_real_list_values = index+1

                for val in List_values[Next_index_real_list_values]:
                    if(val==forecast1[i]):
                        i+=1
                        Error_rate_list.append(Error_rate)
                    else:
                        Error_rate_list.append(abs(forecast1[i] - val))
                        Sum_error_rate+=abs(forecast1[i]-val)
                        i+=1
            else:
                #On vérifie qu'on va pas comparer la dernière liste de HR_list avec une liste q
                if(index!=List_values.__len__()-1):
                    # On va comparer chaque valeur prédite avec chaque valeur réelles de la prochaine liste de HR
                    for val in List_values[1]:
                        if(forecast1[i]==val):
                            i=i+1
                            Error_rate_list.append(Error_rate)
                        else:
                            Error_rate_list.append(abs(forecast1[i]-val))
                            Sum_error_rate+=abs(forecast1[i]-val)
                            i=i+1
                index=index+1

        return(Forecast_list, Error_rate_list, Sum_error_rate, Forecast_values)



    # A partir de la 1ère sous-liste de valeurs réelles d'une taille de 12 d'un paramètre de santé on va prédire les 12 prochaines valeurs et on va comparer ces valeurs prédites avec les valeurs réelles.
    # Pour la n-ième valeur prédite on va la comparer avec la n-ième valeur réelle de la sous liste de valeurs réelles d'un seul paramètre de santé
    # On va effectuer le calcul :
    #  Pour tous les valeurs prédites d'une liste de taille 12 avec toutes les valeurs réelles d'une sous liste on va calculer les résidus et effectuer un calcul de la moyenne des résidus
    #  Résidus n = valeur absolue( valeur réelle - valeur prédite)
    #

    # Fonction pour calculer la précsion du modèle Arima appliquée sur un paramètre de santé donnée en argument de la fonction

    def precision(param):
        if(param=="SP02"):
            Arima_results=Arima("SP02_list")
            list=SP02_list
        if(param=="HR"):
            Arima_results = Arima("HR_list")
            list=HR_list
        if (param=="BP"):
            Arima_results = Arima("BP_list")
            list=BP_list



        Forecast_list=Arima_results[0]
        Error_rate_list=Arima_results[1]
        Sum_error_rate=Arima_results[2]
        Forecast_values=Arima_results[3]



        #On va retirer la dernière liste de prédiction car elle n'est comparable avec aucune liste de valeurs réelles


        Forecast_list.remove(Forecast_list[len(Forecast_list)-1])


        Precision= 100-(Sum_error_rate / (SP02_values.__len__() - 12))

        return(Forecast_values)







    # Fonction pour créer des figures décrivant une comparaison des deux courbes des valeurs réelles d'un paramètre de santé avec les valeurs prédites en fonction du temps




    list1=precision("BP")
    Forecast_values=[]
    list2=precision("HR")
    Forecast_values=[]
    list3=precision("SP02")

    x= len(list1)
    i=0

    Sum_True_Positifs=0
    True_Positifs=[]
    False_Positifs=[]

    while i<x:

        line=[]

        val=round(list1[i],1)
        line.append(val)

        val=round(list2[i],1)
        line.append(val)

        val = round(list3[i], 1)
        line.append(val)

        f3.write(str(line))
        f3.write("\n")
        # decision tree to forecast values
        Forecast_Classe = "Normal"
        HR = "Normal"
        SP02 = "Normal"
        BP = "Normal"

        if(list1[i]<=90 or list1[i]>=140):
            BP="Critical"
        if(list2[i]<=60 or list2[i]>=120):
            HR="Critical"
        if(list3[i]<=90):
            SP02="Critical"
        if (HR == "Critical" and SP02 == "Critical" and BP == "Critical"):
            Forecast_Classe = "Critical"
        if (HR == "Critical" and SP02 == "Critical" and BP == "Normal"):
            Forecast_Classe = "Critical"
        if (HR == "Critical" and SP02 == "Normal" and BP == "Critical"):
            Forecast_Classe = "Critical"
        if (HR == "Normal" and SP02 == "Critical" and BP == "Critical"):
            Forecast_Classe = "Critical"
        line.append(Forecast_Classe)
        if(Forecast_Classe==Classe_Reel[i]):
            Sum_True_Positifs+=1
            True_Positifs.append(Forecast_Classe)
        else:
            False_Positifs.append(Forecast_Classe)
        f2.write(str(line))
        f2.write("\n")
        i = i + 1
    


def moyenne(liste):
    somme=0
    for valeur in liste:
        somme+=valeur
    moyenne= somme / len(liste)
    return(moyenne)



file="C:\\Users\micka\OneDrive\Bureau\Arima\TrainDataset.csv"
file2="C:\\Users\micka\OneDrive\Bureau\Arima\\Forecast_Train.csv"
file3="C:\\Users\micka\OneDrive\Bureau\Arima\\Forecast_Tests.csv"

Prediction(file, file2, file3)
