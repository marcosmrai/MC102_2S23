#Funciona em python >= 3.10

argument = "Jão"

match argument:
    case 0:
        print("This is Case Zero");
    case 1:
        print(" This is Case One");
    case 2:
        print(" This is Case Two ");
    case "Jão":
        print("This is Jão")
    case _:
        print("nothing");