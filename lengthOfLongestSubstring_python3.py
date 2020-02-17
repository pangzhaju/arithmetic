#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Solution:
     # IndentationError: unindent does not match any outer indentation level
     # def sliding_window(self, s:str) -> int:
    def sliding_window(self, s:str) -> int:
        # 初始化定义窗口起始位置
        start = 0 
        # 初始化定义窗口滑动结束位置
        # end = 0
        # 初始化定义结果
        answer = 0
        # 初始化定义储存窗口结束位置的字典map
        map = {}
        # for循环遍历输入字符串s
        #  for j, ch range(s):
        #  SyntaxError: invalid syntax      ^ 
        # NameError: name 'length' is not definedfor j in range(length(s)):
        for end in range(len(s)):
            # 判断当前字符是否在map中
            if s[end] in map:
                # 在map中需要更新start的值
                # eg: pwwkew 窗口结束位置滑倒第二个w start需要更新为map[s[end]]
                #            窗口结束位置滑倒第三个w start需要更新为
            # NameError: name 'Max' is not defined  i = Max(i,map[s[end]])
                start = max(start,map[s[end]])
            # map[s[j]] = end + 1
            # answer = max(answer, end-start+1)
            answer = max(answer, end-start+1)
            map[s[end]] = end + 1
            # print('当前字符是', s[j])
            # print('当前索引是', j) 
        print('answer is:', answer)
        return answer
    #def force(self, s:str) -> int:
        # max = 0
        # if s != ""
        #    max =1
        # for i in range(len(s)):
            # for j in range(i+1, len(s)):
                # if s[i] !+ s[j]:
                    
    def lengthOfLongestSubstring(self, s: str) -> int:
        # for character in str: TypeError: 'type' object is not iterable
        # python中可以迭代的对象包括：字符串，列表，元组，字典，文件
        # print(type(str))
        # print(character)
        # print(str)
        # print(s)
        # print(type(s))
        # print(type(str))
        character_dict = dict()
        start = 0
        end = 0
        max = 0
        currentCount = 0
        i = 0
        for character in s:
        # TabError: inconsistent use of tabs and spaces in indentation 空格和tab键混用/缩进
	#    print(character)
            print(character)
            current_character = character
            # 判断字典是否包含键值
            if current_character in character_dict:
                #character_dict = dict()
                start = end
                print('已存在')
                currentCount =0 
                # IndexError: string index out of range 数组越界
                # if character[i-1] == current_character:
                # if (i>0) && character[i-1] == current_character: 
                # SyntaxError: invalid syntax &&
                # if (i>0) and character[i-1] == current_character:  
                # IndexError: string index out of range
                # if (i>0):
                    # if s[i-1] == current_character:
                        # return i
                        # print('和前一个相同')
                        # j = i
                    # else:
                        # print('和前一个不同')
                        # max = max + 1
                    
            else:
                print('不存在,添加')
                character_dict[current_character] = str(i)
                end = end + 1
                max = max + 1
                print('max是:',max)
                currentCount = currentCount + 1
                if currentCount > max:
                    max = currentCount
            # i++ SyntaxError: invalid syntax,编译器不认识++
            i = i + 1
            # print('max是是是:', max)
            
                 

 
            
           
    
            
   
