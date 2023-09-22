test = [1, 5, -3, 0, 66]
alias0fTest = test
copyOfTest = []
for element in test:
    copyOfTest.append(element)


print(test, alias0fTest, copyOfTest)
test[0] = 100
print(test, alias0fTest, copyOfTest)


