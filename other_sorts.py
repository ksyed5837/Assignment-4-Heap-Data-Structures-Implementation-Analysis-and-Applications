from typing import List
import random
def randomized_quicksort(a: List[int]) -> List[int]:
    if len(a) <= 1: return a
    p = random.choice(a)
    L=[x for x in a if x<p]; M=[x for x in a if x==p]; R=[x for x in a if x>p]
    return randomized_quicksort(L)+M+randomized_quicksort(R)
def mergesort(a: List[int]) -> List[int]:
    n=len(a)
    if n<=1: return a
    mid=n//2
    L=mergesort(a[:mid]); R=mergesort(a[mid:])
    i=j=0; out=[]
    while i<len(L) and j<len(R):
        if L[i]<=R[j]: out.append(L[i]); i+=1
        else: out.append(R[j]); j+=1
    out.extend(L[i:]); out.extend(R[j:]); return out
def is_sorted(a: List[int]) -> bool:
    return all(a[i]<=a[i+1] for i in range(len(a)-1))
