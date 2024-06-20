try:
    with open("1.txt","r") as f:
        print(f.read())

        with open("2.txt","r") as f:
            print(f.read())

            with open("3.txt","r") as f:
                pritn(f.read())
except Exception as e:
    print("there is no such directory or file")
    print("thank you")