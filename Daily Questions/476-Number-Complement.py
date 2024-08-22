class Solution(object):
    def findComplement(self, num):
      
        bin_num = bin(num)[2:] # to ignore prefix note that type of bin_ num is string
        complement = ''.join('1' if n == '0' else '0' for n in bin_num )
        return int(complement,2)
        


