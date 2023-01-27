from typing import List

'''
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
#
'''


class Solution:

  def find(self, st: set, wrd: str, match: int) -> bool:
    if wrd == "":
      if match > 1:
        return True
      else:
        return False
    i = 0
    flg = False
    for j in range(1, len(wrd) + 1):
      nw_wrd = wrd[i: j]
      if nw_wrd in st and j <= len(wrd):
        flg = True
        flg = flg and self.find(st, wrd[j:len(wrd)], match + 1)
      if flg == True:
        break
    return flg

  def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    st = set()
    for i in words:
      st.add(i)
    res = []
    for i in words:
      if self.find(st, i, 0):
        res.append(i)
    return res


if __name__ == '__main__':
  s = Solution()
  s.findAllConcatenatedWordsInADict(
    ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"])
