def Largest_Four(arr):
    arr.sort(reverse=True)
    Largest_Four = arr[:4]
    return Largest_Four, sum(Largest_Four)

arr = [6, 7, 8, 1, 10, 6, 7, 14, 17, 10]
print(Largest_Four(arr))