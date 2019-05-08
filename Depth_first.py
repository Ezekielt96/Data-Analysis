#Depth first Search
import queue

#put --add an element to the end of th queue
#get-- return and removes an element from the head of the queue

graph = [[1,2,3,5],[2,1,3],[6.5.1],[4,2,5],[5,1,2,3,4]]
#add the head elemnt onot the queue
#while the queue is empty
    #pop an eleemnt out of the queue
    #queue the popped element's neigbors
myQueue = queue.Queue()
myQueue.put(graph[0][0])

print (myQueue)
