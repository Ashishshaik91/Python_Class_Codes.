with open("Test.txt", "r") as aplha:
    # aplha.write("Casio also introduced one of the first watches that could display the time in many differen time zones\n")
    # data1 = aplha.read()
    data = aplha.readlines()
    for i in range(5):
        print(data[0][i])


