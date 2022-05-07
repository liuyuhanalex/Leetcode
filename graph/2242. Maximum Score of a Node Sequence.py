from typing import List


class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        node_dict = {}
        for i in edges:
            node_dict.setdefault(i[0], []).append((i[1], scores[i[1]]))
            node_dict.setdefault(i[1], []).append((i[0], scores[i[0]]))
        for k, v in node_dict.items():
            node_dict[k] = sorted(v, key=lambda x: x[1], reverse=True)
        final = []
        for edge in edges:
            total = scores[edge[0]] + scores[edge[1]]
            edge_0 = [i for i in node_dict.get(edge[0]) if i[0] != edge[1]]
            edge_1 = [i for i in node_dict.get(edge[1]) if i[0] != edge[0]]
            if len(edge_0) > 0 and len(edge_1) > 0:
                if edge_0[0] != edge_1[0]:
                    total += edge_1[0][1] + edge_0[0][1]
                else:
                    num = edge_0.pop(0)[1]
                    edge_1.pop(0)
                    if len(edge_0) > 0 and len(edge_1) >0:
                        total += num + max(edge_0[0][1], edge_1[0][1])
                    else:
                        if len(edge_0) > 0:
                            total += num + edge_0[0][1]
                        elif len(edge_1) > 0:
                            total += num + edge_1[0][1]
                        else:
                            total = -1
            else:
                total = -1
            final.append(total)
        if len(final) == 0:
            return -1
        return max(final)



if __name__ == '__main__':
    #Solution().maximumScore(scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])
    #Solution().maximumScore([9,20,6,4,11,12], [[0,3],[5,3],[2,4],[1,3]])
    #print(Solution().maximumScore([5,2,9,8,4], [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
    print(Solution().maximumScore([9,20,6,4,11,12], [[0,3],[5,3],[2,4],[1,3]]))
    #print(Solution().maximumScore([6,17,3,22,27,18,10,26,30,22,16,18], [[0,1],[6,7],[0,2],[6,8],[0,3],[6,9],[0,4],[6,10],[0,5],[6,11],[1,2],[7,8],[1,3],[7,9],[1,4],[7,10],[1,5],[7,11],[2,3],[8,9],[2,4],[8,10],[2,5],[8,11],[3,4],[9,10],[3,5],[9,11],[4,5],[10,11]]))