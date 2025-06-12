
try:
    with open("testData.txt", 'r') as file:
        data=file.read()
        print(data)
except Exception as e:
    print(e)
finally:
    print("test data loaded")