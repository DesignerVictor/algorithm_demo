import json

filename = 'rectangle_divide_solution.json'
solution = {}


def rectangle_divide(length, width):
    """分治法处理矩形分割"""
    key = str(length)+','+str(width)

    if key in solution:
        return solution[key]
    else:
        if length == width:
            solution[key] = 1
            return 1
        if length == 1:
            solution[key] = width
            return width
        if width == 1:
            solution[key] = length
            return length
        min1 = rectangle_divide(1, width) + rectangle_divide(length-1, width)
        for i in range(2,int(length/2+1)):
            tmp = rectangle_divide(i, width) + rectangle_divide(length-i, width)
            if tmp < min1:
                min1 = tmp
        min2 = rectangle_divide(length, 1) + rectangle_divide(length, width-1)
        for i in range(2, int(width/2+1)):
            tmp = rectangle_divide(length, i) + rectangle_divide(length, width-i)
            if tmp < min2:
                min2 = tmp
        if min1 < min2:
            solution[key] = min1
            return min1
        else:
            solution[key] = min2
            return min2
