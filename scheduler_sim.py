from typing import List
from priority_queue import BinaryHeapPQ, Task
def simulate_schedule(tasks: List[Task]) -> List[Task]:
    pq=BinaryHeapPQ()
    time=0; i=0; res=[]
    tasks=sorted(tasks, key=lambda t:t.arrival_time)
    while i<len(tasks) or not pq.is_empty():
        while i<len(tasks) and tasks[i].arrival_time<=time:
            pq.insert(tasks[i]); i+=1
        if not pq.is_empty():
            res.append(pq.extract_max())
        time+=1
    return res
if __name__=="__main__":
    jobs=[Task(2,0,"T1"), Task(5,0,"T2"), Task(1,1,"T3"), Task(3,2,"T4")]
    order=simulate_schedule(jobs)
    print([t.id for t in order])
