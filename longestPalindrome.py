class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_inverse = s[::-1]
        max = 0
        maxStr = ""
        if len(s) < 2:
            return s
        for start in range(len(s)):
            for end in range(start+1, len(s)+1):
                # python count()方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置
                # 统计s的逆序输出字符串的数量
                if s.count(s_inverse[start:end]) > 0:
                    print("s_inverse[start:end]: ", s_inverse[start:end])
                    print("s.count(s_inverse[start:end]):", s.count(s_inverse[start:end]))
                    # 索引
                    index = s.index(s_inverse[start:end])
                    print("s.index(s_inverse[start:end])", s.index(s_inverse[start:end]))
                    print("s_inverse is:", s_inverse)
                    # print("s")
                    print("s_inverse[start:end] is:", s_inverse[start:end])
                    print("start is: end is", start, end)
                    start_inverse = len(s) -end
                    print("start_inverse is:", start_inverse) 
                    print('\n')
                    if (end - start > max) and (index == start_inverse):
                        max = end - start
                        maxStr = s_inverse[start:end] 
        print("maxStr:", maxStr) 
        return maxStr              
    # def longestPalindrome(self, s: str) -> str:
        # python切片,分片就是从一整个字符串中分离提取出一部分内容(即子字符串),从而获取所需的部分数据
        # s = 'abcdefg'
        # print(s[0]) a
        # print(s[-2]) 从后往前倒数2个 f
        # print(s[1:4]) bcd
        # print(s[1:-1]) bcdef
        # 这个是python的slice notation的特殊用法。
        # a = [0,1,2,3,4,5,6,7,8,9] b = a[i:j] 表示复制a[i]到a[j-1]，以生成新的list对象 b =  
        # a[1:3] 那么，b的内容是 [1,2] 当i缺省时，默认为0，即 a[:3]相当于 a[0:3] 当j缺省时，默认为  
        # len(alist), 即a[1:]相当于a[1:10] 当 i,j都缺省时，a[:]就相当于完整复制一份a了
        # b = a[i:j:s]这种格式呢，i,j与上面的一样，但s表示步进，缺省为1. 所以a[i:j:1]相当于a[i:j] 当s<0时，i缺省时，默认为-1. j缺省时，
        # 默认 为-len(a)-1 所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍。所以你看到一个倒序的东东。
        # 如果还不理解，把我说的东西测试一遍，你就明白了
        # 初始化 s逆序字符串s'
        ## s_inverse = s[::-1]
        # 初始化 最长回文串长度
        ## max = 0
        # 初始化 最长回文串maxStr = ""
        ## maxStr = ""
        # 只有一个字符,返回本身
        ## if len(s) < 2:
            ## return s
        # for 循环遍历s 
        ## for start in range(len(s)):
            ## print("外循环,字符", s[start])
            ## for end in range(start+1, len(s)+1):
                ## print("start+1;",start+1)
                ## print("内循环,字符;",end)
         
        ## return maxStr
       


