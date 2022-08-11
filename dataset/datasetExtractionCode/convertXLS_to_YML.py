import pandas as pd

import yaml

#### functions
def deleteDuplicates(fname):
    resultantList = []
    for element in fname:
        if element not in resultantList:
            resultantList.append(element)
    return resultantList

def writeYML(yf, input, type):
    yf.write("- intent: " + type + "\n"  )
    yf.write("  example: | \n")
    for k in input:
        yf.write(f"    - {k} \n")
    yf.write(f"\n")

# read xls file
df = pd.read_excel('annotatedData_corrected.xls')

input1 = 'userSA'
inptu2 = 'user_utterance'
input3 = 'sysRepField'

example_provide = []
example_provide_field = []
example_provide_food = []
example_provide_localization = []
example_provide_price = []
example_provide_time = []
example_provide_date = []
example_provide_all = []

example_accept = []
example_neglect = []
example_else = []
example_accept_provide = []
example_affirm = []
example_affirm_provide = []
example_negate = []
example_provide_else = []

# lock for intents/user_fields and delete duplicates
intents = deleteDuplicates(df[input1])
user_fields = deleteDuplicates(df[input3])

# sort data by intent and write to an array
for i in range(2001):
    if df[input1][i] == intents[0]:
        if df[input3][i] == user_fields[1]: 
            example_provide_food.append(df[inptu2][i])
        elif df[input3][i] == user_fields[2]: 
            example_provide_time.append(df[inptu2][i])
        elif df[input3][i] == user_fields[8]: 
            example_provide_localization.append(df[inptu2][i])
        elif df[input3][i] == user_fields[6]: 
            example_provide_field.append(df[inptu2][i])      
        elif df[input3][i] == user_fields[6]: 
            example_provide_field.append(df[inptu2][i]) 
        elif df[input3][i] == user_fields[4]: 
            example_provide_price.append(df[inptu2][i])   
        elif df[input3][i] == user_fields[3]: 
            example_provide_date.append(df[inptu2][i])  
        elif df[input3][i] == user_fields[0]: 
            example_provide_all.append(df[inptu2][i])  
        else: 
            example_provide_else.append(df[inptu2][i])         
    #if df[input1][i] == intents[0]:
        #print(user_fields[6])
    #    example_provide.append(df[inptu2][i])  
    elif df[input1][i] == intents[1] :
        example_accept.append(df[inptu2][i])
    elif df[input1][i] == intents[2]  :
        example_neglect.append(df[inptu2][i])
    elif df[input1][i] == intents[3] :
        example_else.append(df[inptu2][i])
    elif df[input1][i] == intents[4] :
        example_accept_provide.append(df[inptu2][i])
    elif df[input1][i] == intents[5] :
        example_affirm.append(df[inptu2][i])
    elif df[input1][i] == intents[6] :
        example_affirm_provide.append(df[inptu2][i])
    elif df[input1][i] == intents[7] :
        example_negate.append(df[inptu2][i])
    else:
        example_else.append(df[inptu2][i])   

# create array with intent provide  
provided = []
for k in range(len(example_provide_food)):
    provided.append(example_provide_food[k])
for k in range(len(example_provide_time)):
    provided.append(example_provide_time[k])
for k in range(len(example_provide_localization)):
    provided.append(example_provide_localization[k])
for k in range(len(example_provide_field)):
    provided.append(example_provide_field[k])
for k in range(len(example_provide_price)):
    provided.append(example_provide_price[k])
for k in range(len(example_provide_date)):
    provided.append(example_provide_date[k]) 
for k in range(len(example_provide_all)):
    provided.append(example_provide_all[k])   
for k in range(len(example_provide_else)):
    provided.append(example_provide_else[k])  
#print(provided)

# delete duplicates
provide = deleteDuplicates(provided)
accept = deleteDuplicates(example_accept)
neglect = deleteDuplicates(example_neglect)
accept_provide = deleteDuplicates(example_accept_provide)
affirm = deleteDuplicates(example_affirm)
affirm_provide = deleteDuplicates(example_affirm_provide)
negate = deleteDuplicates(example_negate)
ex_else = deleteDuplicates(example_else)

# write data into yml file
with open(r'newGerNLU.yml', "w+") as yf :
    yf.write("nlu: \n", )
    writeYML(yf, provide, 'provide')
    writeYML(yf, accept, intents[1])
    writeYML(yf, neglect, intents[2])
    writeYML(yf, accept_provide, intents[4])
    writeYML(yf, affirm, intents[5])
    writeYML(yf, affirm_provide, intents[6])
    writeYML(yf, negate, intents[7])
    writeYML(yf, ex_else, "")

