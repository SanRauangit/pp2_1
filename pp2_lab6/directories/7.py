source=input("Enter source filename: ").strip()
destination=input("Enter destination filename: ").strip()
with open(source,'r') as source_file:
    with open(destination,'w') as destination_file:
        destination_file.write(source_file.read())
print("Done")