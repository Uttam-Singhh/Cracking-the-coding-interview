def main(a,b,c,n):
    if n==1:
        print(a,c)
        return
    main(a,c,b,n-1)
    main(a,b,c,1)
    main(b,a,c,n-1)    
print(main('a','b','c',3))   
