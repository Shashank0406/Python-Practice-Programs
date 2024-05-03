

def histogram(num):


    for i in num:
        
        count = i
        output = ""
        while count >0:

            output +="*"
            count = count-1
        
        #print("\t"+output)
        print(output)

histogram([1,3,5,6])