from collections import List

class Solution:

  def is_palindrome(self, s: str, i: int, j: int) -> bool:
    while i < j:
      if str[i] != str[j]:
        return False
      i += 1
      j -= 1
    return True

  def create_partition(self, tmp, res, indx: int, s: str):
    if indx == len(s):
      res.append(tmp)
      return
    for j in range(indx, len(s)):
      if self.is_palindrome(s, indx, j):
        tmp.append(s[indx:j])
        self.create_palindrome(tmp, res, j+1, s)
        tmp.pop()

  def partition(self, s: str) -> List[List[str]]:
    res = []
    tmp = []
    self.create_partition(tmp, res, 0, s)
    return res