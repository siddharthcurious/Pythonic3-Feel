class SegmentTree:

    def __init__(self, nums):

        def createSegmentTree(nums, last_index):


            if last_index % 2 == 1:
                parent_index = (last_index-1)/2
            else:
                parent_index = last_index/2

            nums[parent_index] = nums[parent_index] + nums[last_index]

            


if __name__ == "__main__":
    pass

