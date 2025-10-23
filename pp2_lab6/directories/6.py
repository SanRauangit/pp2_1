for i in range(65,91):
    letter=chr(i)
    filename=f"{letter}.txt"
    with open(filename,'w') as file:
        file.write(f"File content for {letter}.txt")
    print(f"Created {filename}")
print("Done")