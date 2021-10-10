def valid(mat,row,col):
    for j in range(9):
        i=1
        while(i<10):
        
            if mat[j][col]==i:
                i+=1
        mat[row][col]=i
        sudoku(mat,row+1,col,)        





def sudoku(mat,row,col):
    for j in range(9):
        if mat[j][col]==0:
            if valid(mat,j,col) is False:
                return False
        else:
            sudoku(mat,row,col+1)        
    return True            
