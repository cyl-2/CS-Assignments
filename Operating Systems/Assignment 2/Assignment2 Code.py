#Name: Chen Yu Lin
#ID: 120377796

import random

# Data structures
# Memory Space : Doubly Linked List
# Memory Requests : queue

class Process:

    ''' Process Class - defines a process object, once a process object is instantiated, it is appended to the "requests" queue '''

    def __init__(self, pid, pages):
        self._pid = pid
        self._pages = 2**pages

    # prints out a string representation of the process  
    def __str__(self):
        return "process id: " + str(self._pid) + ", size: " + str(self._pages) + " pages"

class Block:

    ''' Block Class - defines the block object in the memory space (which has the structure of doubly-linked list).
        So each block is a node in the DLL. '''

    def __init__(self, pages):
        self._process = None        # data - process request
        self._previous = None       # prev pointer
        self._next = None           # next pointer
        self._pages = pages         # number of pages within the block
        self._accessed = 0          # data - access bit

    # prints out a string representation of the block    
    def __str__(self):
        memory = "Block Info [" + "pages in block: " + str(self._pages) + " | access bit: " + str(self._accessed) + " | process details - " + str(self._process)  +  "]"
        return memory
   
class Memory:
    ''' Memory Class - defines the doubly-linked list object, which represents the "memory space" in this assignment '''
    
    requests = [] # a queue holding all incoming processes    

    def __init__(self):    
        self._head = None           # head of the DLL
        self._tail = None           # tail of the DLL
        self._current = None        # current node being pointed to
        self._allocated_list = []   # the blocks currently occupied by a process
        self._size = 0              # number of blocks in the DLL

    # building the doubly-linked list object with the creation of blocks and their link pointers in the DLL        
    def addBlock(self, data):
        newBlock = Block(data)
        self._size = self._size + 1
             
        if(self._head == None):
            self._head = self._tail = newBlock
            self._head._previous = None
            self._tail._next = None
        else:       
            self._tail._next = newBlock
            newBlock._previous = self._tail
            self._tail = newBlock   
            self._tail._next = None
    
    # returns the list that keeps track of the blocks that are currently occupied by a process
    def getAllocated(self):
        return self._allocated_list

    # prints out a string representation of the memory space    
    def __str__(self):
        used = {2:"2-U", 4:"4-U", 8:"8-U", 16:"16-U", 32:"32-U"}
        free = {2:"2-F", 4:"4-F", 8:"8-F", 16:"16-F", 32:"32-F"}

        current = self._head    
        if(self._head == None):    
            print("Error! Memory doesn't exist.")    
            return
        print("Current Memory: \nPages \tAvailability")
        memory = ""
        memory += str(current._pages) + "\t"
        while(current != None):
            if current._process:
                memory += used[current._pages] + "(" + str(current._accessed) + ")" + " "
            else:
                memory += free[current._pages] + " "
            if current._next != None:
                if current._next._pages != current._pages:
                    memory += "\n" + str(current._next._pages) + "\t"
            current = current._next
        return memory

    # memory allocation is handled by the Next Fit algorithm
    def allocate(self, process):
        if self._current == None:
            self._current = self._head

        counter = 0  
        while self._current != None:
            if self._current._process == None and self._current._pages >= process._pages:
                self._current._process = process
                self._allocated_list.append(self._current)
                self._current = self._current._next
                return True
                break
            
            # when the end of the DLL is reached, reset current node to head 
            # and traverse through list one more time to check for free blocks
            if self._current._next == None:
                self._current = self._head
                counter +=1
            
            # If there are still no free blocks even after the second full search,
            # then call the page replacement function
            if counter == 2:
                return self.page_replace(process)
                counter = 0     # reset counter to 0

            self._current = self._current._next
    
    # page replacement is handled by the Second Chance algorithm
    def page_replace(self, process):
        for index, block in enumerate(self._allocated_list):
            if block._pages >= process._pages:
                if block._accessed == 0:        # if access bit is 0, then the page is swapped out and the new page is swapped in
                    print("\nPAGE REPLACING\n->", str(block), "->", process)
                    block._process = process
                    self._allocated_list.append(self._allocated_list.pop(index))
                    return True     # return True - page replacement happened successfully. 
                else:
                    # if the access bit is 1, then it is set to 0 and the block is moved to the end of the list
                    print("Setting bit to 0 in this block --- ",str(block))
                    block._accessed = 0
                    self._allocated_list.append(self._allocated_list.pop(index))
        # return False - something went wrong, page could not be replaced and process was not inserted.
        return False

    # Manages the memory requests queue
    def memory_request(self):
        if len(self.requests) == 0:
            return True

        process = self.requests[0]
        print("\nAllocating <<", str(process), ">> to memory")
        if len(self.requests) > 1:
            self.requests = self.requests[1::]
        else:
            self.requests = []
        
        success = self.allocate(process)
        if not success:
            print("ERROR! Process %s could not be allocated to memory!" % process)
    
    # randomly sets the access bits of some blocks to 1
    def accessed_bit(self):
        block = self._allocated_list[random.randint(0, len(self._allocated_list)-1)]
        print(str(block), "has just been accessed! Setting its' access bit to 1")
        block._accessed = 1

    # randomly deallocates some pages as they have "finished" execution
    def deallocate(self):
        deallocate = random.randint(0, len(self._allocated_list)-1)
        print("The process in the block << " + str(self._allocated_list[deallocate]) + " >> has finished executing! Page will be deallocated now!")
        self._allocated_list[deallocate]._process = None
        self._allocated_list.pop(deallocate)

# creating many blocks to be passed into the doubly-linked list (memory space)
def create_block(num, size):
    for i in range(num):
        space.addBlock(size)

if __name__ == "__main__":
    space = Memory()
    
    create_block(4, 2)
    create_block(2, 4)
    create_block(2, 8)
    create_block(2, 16)
    create_block(2, 32)

    num_requests = 20

    # generating random processes to be added to the request queue
    print(num_requests, "processes added to request queue...")
    for i in range(num_requests):
        process = Process(random.randint(1000, 99999), random.randint(1, 5))
        space.requests.append(process)

    print("Memory Request Queue: ")
    for process in space.requests:
        print(str(process))

    # while there are processes in the request queue, allocate those processes to blocks in memory
    while True:
        finished = space.memory_request()
        if finished:
            print("No more requests left...")
            print("\n\nMemory in it's final state\n", space)
            break
        
        list1 = space.getAllocated()
        print("In allocated list: ")
        for i in list1:
            print(i)

        print("\n", space, "\n", "-"*30)

        if random.randint(0, 2) == 0:
            space.accessed_bit()

        if random.randint(0, 3) == 0:
            space.deallocate()