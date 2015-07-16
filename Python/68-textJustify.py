from math import ceil
class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        length = len(words)
        if length == 0: return words
        res  = []; line = [words[0]]; line_len = len(words[0])
        word_len_sum = line_len
        for i in xrange(1, length):
            word_len = len(words[i])
            if line_len + 1 + word_len <= maxWidth:
               line.append(words[i])
               line_len += 1 + word_len
               word_len_sum += word_len
            else:
               res.append(self.lineJustify(line, word_len_sum, maxWidth))
               line     = [words[i]]
               line_len = word_len
               word_len_sum = word_len
        res.append(self.lineJustify(line, word_len_sum, maxWidth, True))
        return res
    
    def lineJustify(self, line, word_len_sum, maxWidth, last=False):
        length  = len(line); gap_num = length - 1; diff = maxWidth - word_len_sum
        if gap_num == 0:  
           return line[0] + ' ' * diff
        if last:
           return ' '.join(line) + ' ' * (diff - gap_num)
        res = line[0]
        idx = 1
        while diff:
              space_num = int(ceil(diff * 1.0 / gap_num))
              # space_num = (diff / gap_num) + 1
              gap_num -= 1
              diff    -= space_num
              res     += ' ' * space_num + line[idx]
              idx     += 1
        return res 

if __name__ == '__main__':
   s = Solution()
   print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
   print s.fullJustify(["justification."], 16)
   print s.fullJustify([""], 16)
   print s.fullJustify([], 16)
   print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 14)
   print s.fullJustify(["My","momma","always","said,","\"Life","was","like","a","box","of","chocolates.","You","never","know","what","you're","gonna","get."], 20)

