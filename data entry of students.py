def student_details():
    print("Enter the operation to perform:")
    y = input("Choose: write, read, delete: ")
    if y == 'write':
        name=input("enter student name")
        age=input("enter student age")
        grade=input("enter student grade")
        a=(name  + age  + grade )
        f = open(name, "w")
        f.write(a)
        f.close()

    elif y=='read':
        import os
        b=input("enter the file name to open")
        if os.path.exists(b):
          f = open(b,"r")
          print(f.read())
        else:
            print("file does not exists")

    elif y=='delete':
       c= input("Enter the file name to delete: ")
       import os
       if os.path.exists(c):
           os.remove(c)
           print(f"'{c}'deleted")
       else:
         print(f"'{c}'does not exists")
student_details()