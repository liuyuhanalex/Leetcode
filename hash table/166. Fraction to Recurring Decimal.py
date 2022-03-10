

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        remain = 1
        res_set = {}
        str_ans = '-' if numerator * denominator < 0 else ''
        numerator = 0-numerator if numerator < 0 else numerator
        denominator = 0-denominator if denominator < 0 else denominator
        while remain != 0:
            ans = int(numerator/denominator)
            str_ans += str(ans)
            remain = numerator - ans*denominator
            if not str_ans.__contains__('.') and remain < denominator:
                str_ans += '.'
            numerator = remain * 10
            if numerator in res_set:
                old_str_ans = res_set.get(numerator)
                recur_part = str_ans[len(old_str_ans):]
                return old_str_ans + '(' + recur_part + ')'
            res_set[numerator] = str_ans
        return str_ans.rstrip('.')


if __name__ == '__main__':
    # long division
    print("final_result", Solution().fractionToDecimal(-50, 8))