#Import
import pandas as pd
import matplotlib.pyplot as plt

#Read
df = pd.read_csv('Space_Corrected.csv')

# Part 1
def split_sts(sts):
    return sts.split(', ')

df['Status Mission'] = df['Status Mission'].apply(split_sts)
itr = 0
itr2 = 0

def count_success(row):
    global itr
    if 'Success' in row['Status Mission']:
        itr += 1
    return False

def count_failure(row):
    global itr2
    if 'Failure' in row['Status Mission']:
        itr2 += 1
    return False

def count_prefailure(row):
    global itr2
    if 'Prelaunch Failure' in row['Status Mission']:
        itr2 += 1
    return False

def count_parfailure(row):
    global itr2
    if 'Partial Failure' in row['Status Mission']:
        itr2 += 1
    return False

#Part 2
def split_com(com):
    return com.split(', ')

df['Company Name'] = df['Company Name'].apply(split_com)
com1 = 0
com2 = 0
com3 = 0
com4 = 0

def count_com1(row):
    global com1
    if 'RVSN USSR' in row['Company Name']:
        com1 += 1
    return False

def count_com2(row):
    global com2
    if 'Arianespace' in row['Company Name']:
        com2 += 1
    return False
    
def count_com3(row):
    global com3
    if 'ULA' in row['Company Name']:
        com3 += 1
    return False

def count_com4(row):
    global com4
    if 'NASA' in row['Company Name']:
        com4 += 1
    return False

#Apply
df.apply(count_success, axis = 1)
df.apply(count_failure, axis = 1)
df.apply(count_prefailure, axis = 1)
df.apply(count_parfailure, axis = 1)
df.apply(count_com1, axis = 1)
df.apply(count_com2, axis = 1)
df.apply(count_com3, axis = 1)
df.apply(count_com4, axis = 1)

#Output
print('CHART INFO 1')
print('Number of successful missions:', itr)
print('Number of failed missions:', itr2)
print('CHART INFO 2')
print('Number of RVSN USSR rockets:', com1)
print('Number of Arianespace rockets:', com2)
print('Number of ULA rockets:', com3)
print('Number of NASA rockets:', com4)
print('TIP: Close chart before proceeding')

#Input and Plot for CHART 1
tc1 = input('Enter type for CHART 1 (Recommended: pie. Other types: hist, box, scatter, bar, barh, line):')
if (tc1 != 'hist' and tc1 != 'box' and tc1 != 'scatter' and tc1 != 'bar' and tc1 != 'barh' and tc1 != 'line' and tc1 != 'pie'):
    tc1 = 'pie'

col1 = ''
if (tc1 != 'pie' and tc1 != 'scatter'):
    col1 = input('Please select colour of CHART 1:')
    c1 = pd.Series(data = [itr, itr2], index = ['Success', 'Failure'])
    c1.plot(kind = tc1, figsize = (6, 5), color = col1)
    plt.title('Status')
    plt.xlabel(None)
    plt.ylabel(None)
    plt.show()
else:
    print('Colours are unavailable for types pie and scatter.')
    c1 = pd.Series(data = [itr, itr2], index = ['Success', 'Failure'])
    c1.plot(kind = tc1, figsize = (6, 5))
    plt.title('Status')
    plt.xlabel(None)
    plt.ylabel(None)
    plt.show()

#Input and Plot for CHART 2
tc2 = input('Enter type for CHART 2 (Recommended: barh. Other types: hist, box, scatter, bar, pie, line):')
if (tc2 != 'hist' and tc2 != 'box' and tc2 != 'scatter' and tc2 != 'bar' and tc2 != 'barh' and tc2 != 'line' and tc2 != 'pie'):
    tc2 = 'barh'

col2 = ''
if (tc2 != 'pie' and tc2 != 'scatter'):
    col2 = input('Please select colour of CHART 2:')
    c2 = pd.Series(data = [com1, com2, com3, com4], index = ['RVSN USSR', 'Arianespace', 'ULA', 'NASA'])
    c2.plot(kind = tc2, subplots = True, grid = True, figsize = (9, 6), color = col2)
    plt.title('Rockets Launched')
    plt.xlabel(None)
    plt.ylabel(None)
    plt.show()

else:
    print('Colours are unavailable for types pie and scatter.')
    c2 = pd.Series(data = [com1, com2, com3, com4], index = ['RVSN USSR', 'Arianespace', 'ULA', 'NASA'])
    c2.plot(kind = tc2, subplots = True, grid = True, figsize = (9, 6))
    plt.title('Rockets Launched')
    plt.xlabel(None)
    plt.ylabel(None)
    plt.show()
