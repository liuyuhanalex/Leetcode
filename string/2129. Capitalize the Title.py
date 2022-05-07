class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join([i[0].upper() + i[1:].lower() if len(i)>3 else i.lower() for i in title.split(' ')])



if __name__ == '__main__':
    print(Solution().capitalizeTitle(title = "capiTalIze tHe titLe"))
