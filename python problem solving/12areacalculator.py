while True:
    n = int(input("""
Choose a number :
          1 for square,
          2 for rectangle
          3 for triangle
          0 to exit
"""))
    if(n==0):
        print("thanks for using my program Byyyy!!")
        break
    elif(n==1):
        l= int(input("Enter the side of square :"))
        print("the area of square is ", l*l)
    elif(n==2):
        l= int(input("Enter the length of rectangle :"))
        b= int(input("Enter the breadth of rectangle :"))
        print("the area of rectangle is ", l*b)
    elif(n==3):
        b= int(input("Enter the base of triangle :"))
        h= int(input("Enter the height of triangle :"))
        print("the area of triangle is ", 0.5*b*h)
    else:
        print("choose a valid option")