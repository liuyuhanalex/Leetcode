from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        exit_num_hash = {}
        end_seq_hash = {}
        for i in nums:
            exit_num_hash[i] = exit_num_hash.get(i, 0) + 1
        for i in nums:
            if exit_num_hash.get(i, 0) >= 1:
                if end_seq_hash.get(i-1, 0) >= 1:
                    end_seq_hash[i-1] = end_seq_hash[i-1] - 1
                    end_seq_hash[i] = end_seq_hash.get(i, 0) + 1
                    exit_num_hash[i] = exit_num_hash[i] - 1
                else:
                    if exit_num_hash.get(i+1, 0) >= 1 and exit_num_hash.get(i+2, 0) >=1:
                        end_seq_hash[i+2] = end_seq_hash.get(i+2, 0) + 1
                        exit_num_hash[i+1] = exit_num_hash[i+1] - 1
                        exit_num_hash[i+2] = exit_num_hash[i+2] - 1
                        exit_num_hash[i] = exit_num_hash[i] - 1
                    else:
                        return False
        return True






if __name__ == '__main__':
    print(Solution().isPossible([1, 2, 3, 3, 4, 5]))

