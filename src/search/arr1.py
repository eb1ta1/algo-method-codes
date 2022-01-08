N, V = map(int, input().split())
A_list = list(map(int, input().split()))
value = ['Yes' if V in A_list else 'No']
print(value[0])