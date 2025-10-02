x = input("Do you want to shut down the system?\nEnter yes/no: ")
def shutdown():
    if x == "yes" or x == "YES":
        print("Shutting down...")
    elif x == "no" or x == "NO":
        print("About to shut down...")
    else:
        print("Sorry...")
shutdown()