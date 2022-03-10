from typing import List

class Twitter:

    def __init__(self):
        self.user_post_table = {}
        self.user_follow_table = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_post_table.setdefault(userId, []).append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for i in self.user_follow_table.get(userId, []) + [userId]:
            res += self.user_post_table.get(i, [])
        return sorted(res, reverse=True)


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follow_table.setdefault(followerId, []).append(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        follow_list = self.user_follow_table.get(followerId)
        follow_list = follow_list.remove(followeeId)
        self.user_follow_table[followerId] = follow_list