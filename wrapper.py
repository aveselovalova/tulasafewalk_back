import pandas as pd
import sys, getopt

def main(argv):
    districts = set(['Привокзальный район', 'Зареченский район', 'Пролетарский район', 'Советский район', 'Центральный район'])
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except:
        pass
    
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            inputfile = arg
            train = pd.read_csv(inputfile)
            new_train = pd.DataFrame()
            new_train['Дата'] = train['Дата']
            new_train['Время'] = train['Время']
            new_train['Широта'] = train['Широта']
            new_train['Долгота'] = train['Долгота']
            new_train['Вид ДТП'] = train['Вид ДТП']
            new_train['Адрес'] = train['Адрес']
            new_train['Число погибших'] = train['Число погибших']
            new_train['Число раненых'] = train['Число раненых']
            new_train['Долгота'] = pd.to_numeric(new_train['Долгота'], errors='coerce')
            new_train['Широта'] = pd.to_numeric(new_train['Широта'], errors='coerce')
            final_train = new_train.drop(new_train[new_train['Широта'].isnull()].index, 0)
            final_train = final_train.drop(final_train[~final_train['Адрес'].isin(districts)].index, 0)
            final_train = final_train[::2]
        if opt in ("-o", "--ofile"):
            outputfile = arg
            final_train.to_csv(outputfile)
    print (inputfile, outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])