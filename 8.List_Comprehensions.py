def check(x,y,z,n):
    
    my_list=[ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ]
                
                    
    print(my_list)



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    check(x,y,z,n) 
   

                    

