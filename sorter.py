def get_input():
    n=int(input("Enter the number of inputs: "))
    data=[]
    for item in range(0,n):
        data.append(int(input()))

    return data

print(get_input())
