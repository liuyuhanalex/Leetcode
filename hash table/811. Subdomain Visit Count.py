from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash_table = {}
        for i in cpdomains:
            nums, all_com = i.split(' ')
            all_list = all_com.split('.')
            for j in range(0, len(all_list)):
                name = '.'.join(all_list[j:])
                hash_table[name] = hash_table.get(name, 0) + int(nums)
        res = []
        for k, v in hash_table.items():
            res.append(str(v) + ' ' + k)
        return res





if __name__ == '__main__':
    print(Solution().subdomainVisits(cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))