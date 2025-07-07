def main():
    a=input("enter an string =")
    let=0
    digi=0
    space=0

    for ch in a:
        if ch.isalpha():
            let+=1
        elif ch.isdigit():
            digi+=1
        elif ch.isspace():
            space+=1

    print(a)
    print("number of letters",let)
    print("number of digits",digi)
    print("number of spaces",space)
if __name__=="__main__":
  main()