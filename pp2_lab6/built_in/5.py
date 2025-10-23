def all_true(data):
    return all(data)
test=(1,2,3)
test2=(1,0,3)
test3=()
print(all_true(test))
print(all_true(test2))
print(all_true(test3))