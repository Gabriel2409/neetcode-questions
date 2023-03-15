def search_matrix(matrix: list[list[int]], target: int) -> bool:


    l = 0 
    r = len(matrix[0])-1
    u = 0
    d = len(matrix)-1

    while u < d - 1:
        mid = u + (d - u) // 2

        if target < matrix[mid][0]:
            d = mid - 1
        else:
            u = mid
    if target < matrix[d][0]:
        vert = u
    else:
        vert = d


    if target == matrix[u][l]:
        return True
    elif target == matrix[u][r]:
        return True

    while l <= r :
        midh =   l + ((r - l) // 2) # avoid overflow

        if matrix[vert][midh] > target:
            r = midh -1
        elif matrix[vert][midh] < target:
            l = midh +1
        else:
            return True

    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(search_matrix(matrix, target))