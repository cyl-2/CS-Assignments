# Name: Chen Yu Lin
import time # using time for delays - simulating execution time of processes
import random

# Queue class
class Queue(object):
    queues = []
    blocked_queue = []

    def __init__(self):
        for i in range(8):
            self.queues.append([])

# Process class
class Process(object):
    def __init__(self, pid, quantum, priority, io_block):
        self._pid = pid
        self._quantum = quantum
        self._priority = priority
        self._io_block = io_block
        self._status = "Ready"
        
    def __str__(self):
        return "Process id: " + str(self._pid) + ", quantum: " + str(self._quantum) + ", priority: " + str(self._priority) + ", i/o: " + str(self._io_block) + ", status: " + self._status

def execute(process):

    '''
    Executing processes
    Check for I/O interruption: If there's an I/O interrupt, update process status to 'blocked'
    If the process quantum is 0, then process is finished and status is updated to 'complete'
    Otherwise, process status remains at 'ready'
    '''

    timeslice = 2**process._priority * 10
    print("Executing process: ", str(process), ", time slice: ", timeslice)
    time.sleep(timeslice)

    new_quantum = 0
    if process._quantum > timeslice:
        new_quantum = process._quantum - timeslice
    
    for block in process._io_block: # Checking for interruptions           
        if new_quantum <= block or process._quantum == block:
            process._quantum = block
            process._status = "Blocked"
            return process._status
    
    process._quantum = new_quantum
    if process._quantum == 0:
        process._status = "Complete"
    
    return process._status

def unblock_process(process):

    '''
    Process becomes ready once the I/O is executed
    '''

    time.sleep(list(process._io_block.values())[0])
    process._io_block.pop(max(process._io_block.keys()))
    process._status = "Ready"
    return process._status

def terminate(level, process):

    '''
    Terminating finished process from queue
    '''

    print("\n!! Process", q.queues[level][process]._pid, "terminated !!\n")
    q.queues[level].pop(process)

def idle_process():

    ''' If there are no processes in queue or blocked queue, OS goes into idle state '''

    print("There are no more processes in the queue to execute. Idle process will start soon")
    time.sleep(10)
    print("\n\nIdling...")

def run_system():

    ''' OS system runs if not in idle process
    For each queue level, each process within those queues are executed.
    If not terminated and there are no I/O interrupts, process priority +1 (priority decreases)
    If interrupted by I/O, process get moved into block queue and priority -1 (priority increases)
    '''

    queue_index = 0
    while queue_index < len(q.queues):
        level = q.queues[queue_index]
        process_index = 0
        while process_index < len(level): 
            process = q.queues[queue_index][process_index]
            status = execute(process)
            if status == "Ready":
                if queue_index < len(q.queues)-1:
                    process._priority += 1  # unfinished process is moved down a level
                    q.queues[queue_index+1][:0] = [level.pop(process_index)] # unfinished process is moved to the front of the next queue
            elif status == "Blocked":
                print("\nProcess has been blocked! Process ID:", process._pid, "will be added to the blocked queue.\n")
                if process._priority != 0: 
                    process._priority -= 1 # blocked process is moved up a level
                q.blocked_queue.append(level.pop(process_index))
            else:
                terminate(queue_index, process_index)
        queue_index += 1
   
    if not any(q.queues) and not any(q.blocked_queue):
        idle_process()

def blocked_processes():

    '''
    Execute blocked processes
    When the process is ready again, it is moved back into where it belongs in the multilevel queue 
    '''

    print("Blocked queue contains: ")
    for process in q.blocked_queue:
        print(str(process))
        unblock_process(process)        
    
    while len(q.blocked_queue) != 0:
        for index, process in enumerate(q.blocked_queue):
            q.queues[process._priority].append(q.blocked_queue.pop(index))
    
    run_system()

if __name__ == "__main__":
    # Hardcoding the processes within the queues
    q = Queue()

    for level, queue in enumerate(q.queues):
        process = Process(random.randint(1000, 9999), random.randint(100,999), level, {})
        if level == 2 or level == 6:
            process._io_block[random.randint(1, process._quantum)] = random.randint(1, 3) # when the interruption will happen : its' duration
        queue.append(process)

    for level, queue in enumerate(q.queues):
        for process in queue:
            print("Queue", level, ":", str(process))

    run_system()
    print("-" * 80)
    blocked_processes()