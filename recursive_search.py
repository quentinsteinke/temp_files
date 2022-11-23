class Folder:
    def __init__(self, name, contense: list) -> None:
        self.name = name
    
class File:
    def __init__(self, name) -> None:
        self.name = name

fi1 = File("File1")
fi2 = File("File2")
fi3 = File("File3")

fo1 = Folder("Folder1", [])
fo2 = Folder("Folder2", [])
fo3 = Folder("Folder3", [])

fo1.contense = [fo2,fi2,fi3]
fo2.contense = [fi1,fi2,fi3]
fo3.contense = [fo1,fi2,fi3]

database = [fo1, fo2, fo3]


def search(obj):

    for i in obj:

        print(f"## Object {i.name} ##")
        if type(i) == Folder:
            print(f"###### Searching, {i.name} ######")

            search(i.contense)
        
        elif type(i) == File:
            print(i.name)


############ Calling Main Loop ############
def main():
    search(database)


if __name__ == "__main__":
    main()