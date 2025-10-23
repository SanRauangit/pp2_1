filename=input("Enter the filename: ").strip()
line_count=0
with open(filename,'r') as file:
    for line in file:
        line_count+=1
print(f"Number of lines: {line_count}")