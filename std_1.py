
def selection_sort(n):                                   
    for i in range(len(n)-1):                 #a for loop to iterate through the list           
        mini = i                              #setting the first to minimum
        for j in range(i+1,len(n)):           #iterate through the rest of the list
            if n[j] < n[mini]:                #if the element is smaller
                mini = j                      #set the minimum index to the current index     
        n[i], n[mini] = n[mini], n[i]         #swap the first element with the minimum

    print("Sorted List",n)                                  #we print the sorted list
print("Unsorted list: ", [11,22,14,67,2,9])
selection_sort([11,22,14,67,2,9])  #we call the function to sort the list

def selection_sor2(n):
    for i in range(len(n)):
        min_idx = i + min(range(i, len(n)-1), key=lambda j: n[j])
        n[i], n[min_idx] = n[min_idx], n[i]
    print("Sorted List",n)

print("Unsorted list: ", [11,22,14,67,2,9])
selection_sor2([11,22,14,67,2,9])