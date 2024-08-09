class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dy = [False for _ in range(len(s) + 1)]
        dy[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dy[i] = dy[i + len(w)]
                if dy[i]:
                    break
        
        return dy[0]