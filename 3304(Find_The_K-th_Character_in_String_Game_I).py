"""class Solution:
  def kthCharacter(self, k: int) -> str:
    return string.ascii_lowercase[(k - 1).bit_count()]

"""
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = [0]  # represent 'a' as 0
        while len(word) < k:
            word.extend([(x + 1) % 26 for x in word])
        return chr(ord('a') + word[k - 1])

