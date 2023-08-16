from tkinter import END, TRUE
import numpy as np
# matrix creating function
def m_0():
    # input for number of rows in matrix
    n=int(input("enter number of equations "))
    # input for number of columns
    l=int(input("Enter Columns"))
    col=[]
    # loop for rows
    for i in range(0,n):
        row=[]
        #  nested loop  of columns
        for j in range (0,l):
            print ("row",i,"Element",j)
            # input of column entry      
            e=float(input("enter:"))
            # append  column entry into row list
            row.append(e)
        # append all rows into single  list and create list of rows  
        col.append(row)
    #  converte list of rows into matrix 
    m=np.matrix(col)
    print  (m)
    return m,n,l
#  guass jordan implemantation
def process():
    # input of column&row for pivote element
    end_p=str(input("End program:"))
    if end_p=="yes" :
        return None
    row=int(input("enter roow:"))
    column=int(input("enter column:"))
    if end_p=="yes" :
        return None
    else:
        #   variables for making zero on upper&lower rows of pivote element on same column 
        r=1  
        z=-1
        h=-1
        #  variable for loop continuetion     
        idx=True
        # loop for  making pivote element into 1 making zero on upper&lower rows of pivote element on same column  
        while idx:
            # making pivote element into 1
            matrix[row, : ]=matrix[row, : ]/matrix[row,column]
            if row+1==eq: 
                h=0
                Condition=True
                while Condition:
                    if row-h!=row:
                        D=matrix[row-h,column]/matrix[row,column]
                        for k in range (0,method):
                                    matrix[row-h,k]=(matrix[row-h,k]-D*matrix[row,k])
                    if row-z==row:
                            D=matrix[row-z+1,column]/matrix[row,column]
                            for k in range (0,method):
                                    matrix[row-z+1,k]=(matrix[row-z+1,k]-D*matrix[row,k])
                    if row-h==0: break

                    h+=1
                break
            D=matrix[row+r,column]/matrix[row,column]
            for k in range (0,method):
                        matrix[row+r,k]=(matrix[row+r,k]-D*matrix[row,k])
            if row+r+1==eq:
                z=0
                Condition=True
                while Condition:
                    if row-z!=row:
                        D=matrix[row-z,column]/matrix[row,column]
                        for k in range (0,method):
                                    matrix[row-z,k]=(matrix[row-z,k]-D*matrix[row,k])
                    if row-z==row:
                            D=matrix[row-z+1,column]/matrix[row,column]
                            for k in range (0,method):
                                    matrix[row-z+1,k]=(matrix[row-z+1,k]-D*matrix[row,k])
                    if row-z==0: break

                    z+=1
            if row-z==0:
                break
            r+=1
        print(matrix)    
        process()


matrix,eq,method=m_0()
process()



