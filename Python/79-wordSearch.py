class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def __init__(self):
        self.wordLen = 0
        self.length  = 0
        self.width   = 0 
    
    # Chris:TODO:: change it to the following version, replace the word matching with index

    def exist(self, board, word):
        self.wordLen = len(word)
        self.length  = len(board[0][0])
        self.width   = len(board)
        res          = False
        for i in xrange(self.width):
            board[i] = list(board[i][0])
        
        for i in xrange(self.width):
            for j in xrange(self.length):
                if board[i][j] == word[0]:
                   res |= self.dfs(board, i, j, "", word)
        return res
    
    def dfs(self, board, i, j, pastword, word):
        currLen = len(pastword) + 1
        if self.width > i > -1 and self.length > j > -1:  
           visitword = board[i][j]
           
           if currLen == self.wordLen:
              # print pastword + board[i][j]
              if pastword + visitword == word:
                 # print pastword + board[i][0][j]
                 return True
              else:
                 return False
           elif currLen < self.wordLen:
                # print pastword + board[i][0][j]
                board[i][j] = '#'
                result =                                                     \
                (self.dfs(board, i + 1, j, pastword + visitword, word) or    \
                 self.dfs(board, i, j + 1, pastword + visitword, word) or    \
                 self.dfs(board, i - 1, j, pastword + visitword, word) or    \
                 self.dfs(board, i, j - 1, pastword + visitword, word))
                board[i][j] = visitword
                return result
           else:
                return False
        return False

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        solution = False
        for i in range(0,len(board)):
            for j in range(0, len(board[0])):
                solution = solution or self.existRec(board, word, i, j, 0)
        return solution
        
    def existRec(self, board, word, row, col, index):
        if row < 0 or row>=len(board) or col<0 or col>=len(board[0]) or  board[row][col]!=word[index]:
            return False
        if index==len(word)-1:
            return True
        board[row][col] = "$"
        solution = self.existRec(board, word, row-1, col, index+1) or self.existRec(board, word, row+1, col, index+1) or self.existRec(board, word, row, col-1, index+1) or self.existRec(board, word, row, col+1, index+1)
        board[row][col] = word[index]
        return solution

# Chris:TODO:: rewrite the iterative version

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def dfs(x, y, word):
            if len(word)==0: return True
            #up
            if x>0 and board[x-1][y]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x-1,y,word[1:]):
                    return True
                board[x][y]=tmp
            #down
            if x<len(board)-1 and board[x+1][y]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x+1,y,word[1:]):
                    return True
                board[x][y]=tmp
            #left
            if y>0 and board[x][y-1]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x,y-1,word[1:]):
                    return True
                board[x][y]=tmp
            #right
            if y<len(board[0])-1 and board[x][y+1]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x,y+1,word[1:]):
                    return True
                board[x][y]=tmp
            return False
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if(dfs(i,j,word[1:])):
                        return True
        return False


if __name__ == '__main__':
   s = Solution()
   board =  [          \
              ["ABCE"],\
              ["SFCS"],\
              ["ADEE"] \
            ]
   # print s.exist(board, "ABCCED")
   # print s.exist(board, "SEE")
   print s.exist(board, "ABCB")

