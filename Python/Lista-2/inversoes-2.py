
def merge_sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort_and_count(arr[:mid])
    right, inv_right = merge_sort_and_count(arr[mid:])
    merged, inv_split = merge_and_count(left, right)

    return merged, inv_left + inv_right + inv_split

def merge_and_count(left, right):
    merged = []
    count = 0
    i = j = 0

    # Mesclando os dois arrays e contando inversões
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i  # Todos os elementos restantes em 'left' são maiores
            j += 1

    # Adiciona os elementos restantes
    merged += left[i:]
    merged += right[j:]
    return merged, count

# Exemplo
A = [2, 4, 1, 3, 5]
_, inversions = merge_sort_and_count(A)
print(inversions)  # Saída esperada: 3