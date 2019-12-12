#Jenny Gonzales, CIS 103, Lab13

#Create the functions...list.. define rainy
def largestRainFall(arr, n):
    maxRainFall = arr[0]
    max = 0
    
    for i in range(1, n):
        if arr[i] > maxRainFall:
            maxRainFall = arr[i]
            max = i
    return max

#define dry
def smallest(arr, n):
    minRainFall = arr[0]
    min = 0

    for i in range(1, n):
        if arr[i] < minRainFall:
            minRainFaill = arr[i]
            min = i
    return min

#define average #initialize accumulation
def averageRainFall(arr, n):
    sum=0
    for i in range(n):
        sum = sum + arr[i] #accumulate with index i
    return sum/12
 #12months 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

#Classify and Display
def ClassifyAndDisplayRainFall(arr,n):
    avg=averageRainFall(arr,n)
    print ("Month\t", "                  RainFall(mm)", "            Classification")
    for i in range(n):
        if arr[i] > (avg * 0.2 + avg):
            print (months[i],"\t\t",arr[i],"\t\t", "rainy")
        elif arr[i] < (avg - avg * 0.25):
            print(months[i],"\t\t",arr[i],"\t\t", "dry")
        else:
            print (months[i],"\t\t",arr[i],"\t\t", "average")
#import the file                  
def main():
    listRainFall = []
    f = open("rainfall.txt", "r")
    for line in f:
        listRainFall.append(int(line))
    average = averageRainFall(listRainFall,12)
    print ("The year's average monthly rainfall was (", average, "mm)")
    Ans = largestRainFall(listRainFall,12)
    print (months[Ans], " has the highest rainfall (",listRainFall[Ans],"mm)")
    Ans = smallest(listRainFall, 12)
    print (months[Ans], "has the lowest rainfall  (",listRainFall[Ans],"mm)")

    ClassifyAndDisplayRainFall(listRainFall, 12)

main()
