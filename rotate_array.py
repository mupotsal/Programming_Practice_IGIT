from collections import deque as dq

def rotate_array(nums,times):
    deq = dq()
    deq.extend(nums)

    for i in range(times):
        p = deq.pop()
        deq.appendleft(p)
        deq.
    print(deq)



def main():
    nums = [2,3,4,6,7]
    rotate_array(nums,3)

main()