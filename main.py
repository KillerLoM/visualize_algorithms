import matplotlib.pyplot as plt
import os
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mp
import numpy as np
import random
import timeit 
import math
def mergesort(A, start, end):
	if end <= start:
		return
	mid = start + ((end - start + 1) // 2) - 1
	yield from mergesort(A, start, mid)
	yield from mergesort(A, mid + 1, end)
	yield from merge(A, start, mid, end)
def merge(A, start, mid, end):
	merged = []
	leftIdx = start
	rightIdx = mid + 1
	
	while leftIdx <= mid and rightIdx <= end:
		if A[leftIdx] < A[rightIdx]:
			merged.append(A[leftIdx])
			leftIdx += 1
		else:
			merged.append(A[rightIdx])
			rightIdx += 1

	while leftIdx <= mid:
		merged.append(A[leftIdx])
		leftIdx += 1

	while rightIdx <= end:
		merged.append(A[rightIdx])
		rightIdx += 1

	for i in range(len(merged)):
		A[start + i] = merged[i]
		yield A
def quicksort(a, l, r):
    if l >= r:
        return
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]
        yield a
    a[l], a[j]= a[j], a[l]
    yield a
    yield from quicksort(a, l, j-1)
    yield from quicksort(a, j + 1, r)
def heapify(arr, n, i):
    largest = i 
    left = 2 * i + 1    
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        yield arr
        yield from heapify(arr, n, largest)
def heapsort(arr):
    n = len(arr)
    frames = [] 
    for i in range(n//2 - 1, -1, -1):
        yield from heapify(arr,n,i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        yield arr
        yield from heapify(arr, i, 0)
def max_element(lst):
    max = lst[0]
    for x in lst:
        if x > max:
            max = x
    return max
def num_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count
def counting_sort(lst, pos):
    count = [0] * 10
    result = [0] * len(lst)
    for x in lst:
        digit = (x // 10**pos) % 10
        count[digit] += 1 
    for i in range(1, 10):
        count[i] += count[i-1]
    for i in range(len(lst)-1, -1, -1):
        digit = (lst[i] // 10**pos) % 10 
        result[count[digit]-1] = lst[i]
        count[digit] -= 1
    return result
def radix_sort(lst):
    from timeit import default_timer as timer
    start_time = timer()
    max = max_element(lst)
    digits = num_digits(max)
    steps = []
    for i in range(digits):
        lst = counting_sort(lst, i)
        steps.append(lst.copy())
    end_time = timer()
    time_run = round((end_time - start_time),5)
    plot_steps(a, steps, time_run)
    return lst,  steps
def plot_steps(lst, steps, end_time):
    plt.style.use('fivethirtyeight')
    fig, axes = plt.subplots(len(steps)+1, 1, figsize=(10, 10))
    sub = ["A[0]", "A[1]", "A[2]", "A[3]", "A[4]", "A[5]", "A[6]", "A[7]", "A[8]", "A[9]","A[10]","A[11]","A[12]","A[13]","A14]","A[15]","A[16]","A[17]","A[18]","A[19]","A[20]"]
    axes[0].bar(sub, lst)
    
    axes[0].set_title("Danh sách ban đầu \n" + str(lst) + "\nĐộ phức tạp của thuật toán là 0(2nm) = O(n)"+"= O(" + str(2*len(lst)*2) +")",fontdict={'fontsize': 12,'color' : 'purple'})      
    for i in range(len(steps)):
        axes[i+1].bar(sub, steps[i], label = "Xếp theo cơ số thứ " + (str(i+1)+":"+str(steps[i])), align ="edge")
        axes[i+1].legend(loc ="upper left")
        plt.xlabel("Thời gian chạy là: " + str(end_time) + "giây",color= "red")
    plt.show()
from timeit import default_timer as timer
def showGraph(a, algoName, check):
	n=len(a)
	sub = ["A[0]", "A[1]", "A[2]", "A[3]", "A[4]", "A[5]", "A[6]", "A[7]", "A[8]", "A[9]","A[10]","A[11]","A[12]","A[13]","A14]","A[15]","A[16]","A[17]","A[18]","A[19]","A[20]"]
	start_time = timer()
	if (check == 1): generator = mergesort(a, 0, len(a)-1)
	if (check == 2): generator = quicksort(a,0, len(a)-1)
	if (check == 3) :generator = heapsort(a)
	plt.style.use('fivethirtyeight')
	fig, ax = plt.subplots()
	bar_rects = ax.bar(sub, a, align ="center")
	ax.set_title("Thuật toán : "+algoName+"\n"+"Độ phức tạp là O(NlogN) = " +"O(" + str(len(a)*math.log(len(a),10)) + ")",fontdict={'fontsize': 11,'color' : 'purple'})
	text = ax.text(0.01, 1, "", transform=ax.transAxes,color="red")
	iteration = [0]
	def animate(A, rects, iteration):
		for rect, val in zip(rects, A):
			rect.set_height(val)
		iteration[0] += 1
		text.set_text("Số lần lặp : {}".format(iteration[0]))
	anim = FuncAnimation(fig, func=animate, fargs=(bar_rects, iteration), frames=generator, interval=120, repeat=False, cache_frame_data= False)
	end_time = timer()
	temp = round(end_time - start_time, 5)
	plt.xlabel("Thời gian chạy của thuật toán là: " + format(temp) + " giây",color= "red")
	plt.show()

def Nguyen_Minh_Tam(a):
    print("                        Xin hãy đưa ra sự lựa chọn cho sự mô phỏng các thuật toán sắp xếp")
    print("Phím 1 để chọn thuật toán Merge Sort\n")
    print("Phím 2 để chọn thuật toán Quick Sort\n")
    print("Phím 3 để chọn thuật toán Heap sort\n")
    print("Phím 4 để chọn thuật toán Radix sort\n")  
    mode = input("Bấm phím từ 1->4 để lựa chọn các thuật toán sắp xếp tương ứng   ")
    match mode:
        case '1':
            check = 1
            os.system('cls')
            algoName='Merge Sort'
            print("Thuật toán đã chọn là  ", algoName)
            print("Mảng cần sắp xếp là: ")
            for i in range (len(a)):
                print(a[i], end =" ")
            print("\n")  
            showGraph(a, algoName, check)
            print("Mảng sau sắp xếp là: ")
            for i in range (len(a)):
                print(a[i], end =" ")  
            return 1
        case '2':
            check = 2
            os.system('cls')
            algoName='Quick Sort'
            print("Thuật toán đã chọn là  ", algoName)
            print("Mảng cần sắp xếp là: ")
            for i in range (len(a)):
                print(a[i], end =" ")
            print("\n")  
            showGraph(a, algoName, check)
            print("Mảng sau sắp xếp là: ")
            for i in range (len(a)):
                print(a[i], end =" ")  
            return 2
        case '3':
            check = 3
            os.system('cls')
            algoName='Heap Sort'
            print("Thuật toán đã chọn là  ", algoName)
            print("Mảng cần sắp xếp là: ")
            for i in range (len(a)):
                print(a[i], end =" ")
            print("\n")  
            showGraph(a, algoName, check)
            print("Mảng sau sắp xếp là: ")
            for i in range (len(a)):
                print(a[i], end =" ")  
            return 3
        case '4':
            check = 3
            os.system('cls')
            algoName='Radix Sort'
            print("Thuật toán đã chọn là  ", algoName)
            print("Mảng cần sắp xếp là: ")
            for i in range (len(a)):
                print(a[i], end =" ")
            print("\n")
            a, steps = radix_sort(a)    
            print("Mảng sau sắp xếp là: ")
            for i in range (len(a)):
                print(a[i], end =" ") 
            return 4 
a= [9,12,4,16,1,20,17,8,10,15,11,19,18,7,2,13,14,3,5,6,20]
print("       Nguyễn Minh Tâm - 20200333\n")
print("          Chương trình mô phỏng trực quan các thuật toán sắp xếp \n")                                      
mode = Nguyen_Minh_Tam(a)



