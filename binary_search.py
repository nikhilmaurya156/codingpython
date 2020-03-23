a = [11, 12, 13, 14, 15, 17, 19]
try:
    b = int(input('Enter a number you wanted to search'))
except ValueError:
    print('IS NOT NUMBER PLEASE ENTER A NUMBER')
mid_index = int(len(a)/2)
for i in range(mid_index+1):
    if a[mid_index] == b:
        print('Number found at position ' + str(mid_index+1))
        break
    elif a[mid_index] < b:
        start = mid_index
        last = len(a)
        mid_index = int((start + last)/2)
    elif a[mid_index] > b:
        last = mid_index
        start = 0
        mid_index = int((start + last) / 2)
