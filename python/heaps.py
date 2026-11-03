import heapq


def top_k(datos, k):
    if k < 0:
        raise ValueError("La k no puede ser negativa.")
    
    if k == 0:
        return []
        
    monticulo_final = []
    
    for dato in datos:
        if len(monticulo_final) < k:
            heapq.heappush(monticulo_final, dato)
            
        elif dato > monticulo_final[0]:
            heapq.heapreplace(monticulo_final, dato)
    
    
    monticulo_final.sort(reverse=True)
    
    return monticulo_final



