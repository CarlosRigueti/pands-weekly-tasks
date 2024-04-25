def readText(fileName):
    try:
        with open(fileName, 'rt') as f:
            read = f.read()
            count = read.count("e")
            print(count)
    except Exception as e:
        print(f"An error occurred: {e}")

readText("moby-dick.txt")
    
    