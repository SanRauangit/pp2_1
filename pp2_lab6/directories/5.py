list=['a','b','c']
with open('output.txt','w') as file:
    for item in list:
        file.write(str(item) + '\n')
print("Done")