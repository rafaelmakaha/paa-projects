def merge(esq, dire):
    esq_i = 0
    dire_i = 0
    result = []
    while esq_i < len(esq) and dire_i < len(dire):
        if esq[esq_i] < dire[dire_i]:
            result.append(esq[esq_i])
            esq_i += 1
        else:
            result.append(dire[dire_i])
            dire_i += 1
    
    result += esq[esq_i:]
    result += dire[dire_i:]
    return result

def merge_sort(lista):
    if len(lista) <=1:
        return lista
    metade = len(lista)//2
    esq = merge_sort(lista[:metade])
    dire = merge_sort(lista[metade:])
    
    return merge(esq, dire)

merge_sort([int(x) for x in input().split()])