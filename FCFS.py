# Syed Musaib Hussain
# 200901065
# Lab 5

def findWaitingTime(processes, n, bt, wt):
	wt[0] = 0
	# Waiting Time Formula
	for i in range(1, n ):
		wt[i] = bt[i - 1] + wt[i - 1]

def findTurnAroundTime(processes, n, bt, wt, tat):
	# Turn Around Time Formula
	for i in range(n):
		tat[i] = bt[i] + wt[i]

def findavgTime(processes, n, bt):
	wt = [0] * n
	tat = [0] * n
	total_wt = 0
	total_tat = 0

	findWaitingTime(processes, n, bt, wt)
	findTurnAroundTime(processes, n, bt, wt, tat)
	
	print("PID" + "     BT" + "   WT" + "      TAT")

	for i in range(n):
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" " + str(i + 1) + "\t\t" + str(bt[i]) + "\t " + str(wt[i]) + "\t\t " + str(tat[i]))

	print("\nAverage Waiting Time = " + str(total_wt / n))
	print("\nAverage Turn Around Time = " + str(total_tat / n))


if __name__ =="__main__":
	processes = [1, 2, 3]
	n = len(processes)
	burst_time = [10, 5, 8]
	
	findavgTime(processes, n, burst_time)
	
