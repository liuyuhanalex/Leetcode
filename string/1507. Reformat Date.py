

class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split(' ')
        day = day.replace('th', '').replace('rd', '').replace('st', '')
        month_dict = {"Jan": '01',
                      "Feb": '02',
                      "Mar": '03',
                      "Apr": '04',
                      "May": '05',
                      "Jun": '06',
                      "Jul": '07',
                      "Aug": '08',
                      "Sep": '09',
                      "Oct": '10',
                      "Nov": '11',
                      "Dec": '12'}
        month = month_dict.get(month)
        if len(day) == 1:
            day = '0' + day
        return year + '-' + month + '-' + day





if __name__ == '__main__':
    # "1960-05-26"
    print(Solution().reformatDate(date="26th May 1960"))