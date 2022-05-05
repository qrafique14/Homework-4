import math


num_calls = 0


def partition(user_ids, i, k):
    # start and end point of partition
    start = i
    end = k


    pivot = user_ids[math.floor((i + k) / 2)]

    # find the position of the pivot in the given array by iterating throuh below loop
    while start <= end:
        # start is incremented until we found the value greater than pivot
        while user_ids[start] < pivot:
            start = start + 1
        # end is decremented until we found the value less than pivot
        while user_ids[end] > pivot:
            end = end - 1
        # swap start and end position values and then continue the loop until start<end
        if start <= end:
            tmp = user_ids[start]
            user_ids[start] = user_ids[end]
            user_ids[end] = tmp
            start = start + 1
            end = end - 1

    return start


def quicksort(user_ids, i, k):
    global num_calls
    num_calls = num_calls + 1
    if i < k:
        mid = partition(user_ids, i, k)
        quicksort(user_ids, i, mid - 1)
        quicksort(user_ids, mid, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while (user_id != "-1"):
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)

    print(num_calls)

    for x in user_ids:
        print(x)