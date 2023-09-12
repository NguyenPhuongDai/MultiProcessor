from prettytable import PrettyTable

class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.wait_time = 0 
        self.start_time = 0
        self.finish_time = 0
    
    def __repr__(self):
        return f"{self.name}\t{self.arrival_time}\t{self.burst_time}\t{self.wait_time}\t{self.start_time}\t{self.finish_time}"
    
def fcfs_scheduling(processes):
    processes.sort(key=lambda process: process.arrival_time)
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.wait_time = current_time - process.arrival_time
        #process.turnaround_time = process.finish_time - process.arrival_time
        process.start_time = current_time
        current_time += process.burst_time
        process.finish_time = current_time
        process.turnaround_time = process.finish_time - process.arrival_time
        
    #time =0
    #for process in processes:
      #  process.wait_time = time
      #  for t in range(process.burst_time):
       #     print(f'{time} : {process.name}')
      #      time += 1
    
    avg_wait_time = sum([process.wait_time for process in processes]) / len(processes)
    avg_turnaround_time = sum([process.turnaround_time for process in processes])/ len(processes)
    #processes.sort(key=lambda process: process.name)
    return processes, avg_wait_time, avg_turnaround_time

def detail(processes):
    processes.sort(key=lambda process: process.arrival_time)
    time =0
    for process in processes:
        process.wait_time = time
        for t in range(process.burst_time):
            print(f'{time} : {process.name}')
            time += 1
    
    table_details = PrettyTable()
    table_details.field_names = ["Time","Process Name"]
    for process in processes:
        table.add_row([time, process.name])
    print(table_details)

#def sort_by_name(processes):
#    processes.sort(key=lambda process: process.name)
#    return processes
#def sort_by_AT(processes):
#    processes.sort(key=lambda process:process.arrival_time)
#    return processes
    
if __name__ == "__main__":
    print("")
    print("TRUONG DAI HOC SU PHAM THANH PHO HO CHI MINH")
    print("         KHOA CONG NGHE THONG TIN           ")
    print("")
    print("    BAI TIEU LUAN HOC PHAN HE DIEU HANH     ")
    print("")
    print("----------------------------------------------")
    print("Members:")
    print("1.        Nguyen Phuong Dai      47.01.104.057")
    print("2.       Doan Ngoc Nha Triet     47.01.104.218")
    print("3.         Nguyen Ngoc Tran      47.01.104.214")
    print("4.          Tran Minh Duc        47.01.104.070")
    print("5.           Vu Hong Son         47.01.104.183")
    print("----------------------------------------------")

    num_processes = int(input("Enter the number of processes: "))
    processes = []
    for i in range(num_processes):
        print("--------------------------------")
        name = input(f"Enter the name of process {i+1}: ")
        arrival_time = int(input(f"Enter the arrival time of process {i+1}: "))
        burst_time = int(input(f"Enter the burst time of process {i+1}: "))
        processes.append(Process(name, arrival_time, burst_time))
        
    
    processes, avg_wait_time, avg_turnaround_time = fcfs_scheduling(processes)
    
    print("Sort by")
    print("1. Name ")
    print("2. Arrival time ")
    decision = int(input(f"Enter the decision: "))
    if decision == 1:
        #processes= sort_by_name(processes)
        processes.sort(key=lambda process: process.name)
    elif decision ==2:
        #processes= sort_by_AT(processes)
        processes.sort(key=lambda process: process.arrival_time)
    
    
    table = PrettyTable()
    table.field_names = ["Process", "Arrival Time", "Burst Time", "Wait Time", "Start Time", "Finish Time"]
    for process in processes:
        table.add_row([process.name, process.arrival_time, process.burst_time, process.wait_time, process.start_time, process.finish_time])
    
    print(table)
    print(f"Average wait time: {avg_wait_time}")
    print(f"Average turn around time: {avg_turnaround_time}")


    print ("See details?")
    print("1. Yes")
    print("2. No")
    decs= int(input(f"Enter your decision: "))
    if decs ==1:
        processes.sort(key=lambda process: process.arrival_time)
        time =0
        table1 = PrettyTable()
        table1.field_names = ["Time","Process"]
        for process in processes:
            process.wait_time = time
            for t in range(process.burst_time):
                #print(f'{time} : {process.name}')
                table1.add_row([time, process.name])
                time += 1
        print(table1)
    else:
        print ("End!!!")
        
