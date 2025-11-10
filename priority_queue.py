from typing import Any, List, Optional
from dataclasses import dataclass, field
@dataclass(order=True)
class Task:
    priority:int
    arrival_time:int
    id:str=field(compare=False, default="")
    deadline: Optional[int]=field(compare=False, default=None)
    payload: Any=field(compare=False, default=None)
class BinaryHeapPQ:
    def __init__(self): self.a: List[Task]=[]
    def __len__(self): return len(self.a)
    def is_empty(self)->bool: return not self.a
    def _p(self,i): return (i-1)//2
    def _l(self,i): return 2*i+1
    def _r(self,i): return 2*i+2
    def _swap(self,i,j): self.a[i],self.a[j]=self.a[j],self.a[i]
    def insert(self,t:Task)->None:
        self.a.append(t); self._up(len(self.a)-1)
    def _up(self,i:int)->None:
        while i>0 and self.a[self._p(i)]<self.a[i]:
            self._swap(i,self._p(i)); i=self._p(i)
    def extract_max(self)->Task:
        if not self.a: raise IndexError("extract_max from empty")
        self._swap(0,len(self.a)-1); out=self.a.pop()
        if self.a: self._down(0)
        return out
    def _down(self,i:int)->None:
        n=len(self.a)
        while True:
            largest=i; l=self._l(i); r=self._r(i)
            if l<n and self.a[l]>self.a[largest]: largest=l
            if r<n and self.a[r]>self.a[largest]: largest=r
            if largest==i: break
            self._swap(i,largest); i=largest
    def increase_key(self,index:int,new_p:int)->None:
        if new_p<self.a[index].priority: raise ValueError("use decrease_key")
        self.a[index].priority=new_p; self._up(index)
    def decrease_key(self,index:int,new_p:int)->None:
        if new_p>self.a[index].priority: raise ValueError("use increase_key")
        self.a[index].priority=new_p; self._down(index)
if __name__=="__main__":
    pq=BinaryHeapPQ()
    pq.insert(Task(priority=3, arrival_time=0, id="A"))
    pq.insert(Task(priority=5, arrival_time=1, id="B"))
    pq.insert(Task(priority=1, arrival_time=2, id="C"))
    out=[]
    while not pq.is_empty(): out.append(pq.extract_max().id)
    print(out)
