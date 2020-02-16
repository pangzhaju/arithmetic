[TOC]

# 无重复字符的最长子串2

## 1 python版

1.0)流程图

```flow
st=>start: 开始
io=>inputoutput: 输入字符串s
e=>end: 结束
op_forin1=>operation: 1层for循环遍历字符串inputString
op_addnum1=>operation: 初始化字典dic
op_forin2=>operation: 取本次遍历得到的字母currentCharacter
op_addnum2=>operation: dic[currentCharacter]取值
cond_same=>condition: dic[currentCharacter]没有值？
op_none_value=>operation: dic[currentCharacter] = i
op_same=>operation: 不做操作
op_output_result=>operation: 输出最长子串
st->io->op_forin1->op_addnum1->op_forin2->op_addnum2->cond_same(yes,right)->op_none_value->op_forin1
st->io->op_forin1->op_addnum1->op_forin2->op_addnum2->cond_same(no,down)->op_output_result->e
```



1.0.1）python遍历数组

*  for循环    c-style for statement has been removed in Swift 3

*  for in

* 索引－值方式enumerate（）

1.0.2) 代码_version01   

```py
class solution:
	

```

   

| 执行用时 | 内存消耗 | 疑问🤔️ 去掉空格 预编译？编译？                          |
| -------- | -------- | ------------------------------------------------------ |
| 1184ms   | 18.9MB   | 空格会影响时间==  加几行空格->1284ms->再加空格->1456ms |

1.1)swift改进版流程图

```flow
st=>start: 开始
op_forin=>operation: 遍历数组 值记为nums[i]
op_findvalueindex=>operation: nums[i+1]开始遍历数组
op=>operation: target-nums[i]相等
op_equal=>condition: 是否相等
op_outout=>inputoutput: 输出下标
op_diff=>operation: 继续
e=>end: 结束
st->op_forin->op_findvalueindex->op->op_equal(yes)->op_outout->e
st->op_forin->op_findvalueindex->op->op_equal(no)->op_forin
```

1.1.2代码

```swift
class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        for i in 0 ..< nums.count {
            for j in (i+1) ..< nums.count{
                if (nums[j] == target - nums[i]){
                    return [i ,j]
                }
            }
        }
    return [0]
    }
}
```



---------

| 执行用时 | 内存消耗 |      |
| :------- | -------- | ---- |
| 693ms    | 18.9MB   |      |
|          |          |      |

1.2.0swift版本hash表格

```flow
st=>start: 开始
io_parameters=>inputoutput: 输入数组nums,和targets
op_forin=>operation: index,value方式遍历数组
op_savedic=>operation: 将数组index做value,value做key存入字典dic
op_forinagain=>operation: 再次遍历数组
op_caculate_add=>operation: 计算出被加数addednum=target-nums[i]
cond_iscontain=>condition: 字典的keys是否
                           包含被加数addednum,
                           且i != dic[addednum]
io_contain=>inputoutput: 输出i,dic[nums[i]]
e=>end: 结束
st->io_parameters->op_forin->op_savedic->op_forinagain->op_caculate_add->cond_iscontain(yes)->io_contain->e
st->io_parameters->op_forin->op_savedic->op_forinagain->op_caculate_add->cond_iscontain(no)->op_forinagain
```

1.2.1代码

```swift
class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var arrayDic = [Int: Int] ()
        for (index,value) in nums.enumerated(){
            let dicKey = value
            arrayDic.updateValue(index, forKey:dicKey)
        }
        for i in 0..<nums.count {
            let addedValue = target - nums[i]
            if arrayDic.keys.contains(addedValue){
                if(i != arrayDic[addedValue]) {
                    return [i, arrayDic[addedValue]!]
                }else{
                    
                }
            }
        }
        return [0]
    }
}
```

| 执行用时 | 内存消耗 |      |
| :------- | -------- | ---- |
| 68ms     | 19MB     |      |
|          |          |      |

1.3.0极限改进

```swift
class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var arrayDic = [Int: Int] ()
        for (index,value) in nums.enumerated(){
            arrayDic.updateValue(index, forKey:value)
        }
        for i in 0..<nums.count {
            if arrayDic.keys.contains(target - nums[i]){
                if(i != arrayDic[target - nums[i]]) {
                    return [i, arrayDic[target - nums[i]]!]
                }else{
                    
                }
            }
        }
        return [0]
    }
}
```

| 执行耗时 | 内存消耗 |      |
| -------- | -------- | ---- |
| 60ms     | 19.2MB   |      |
|          |          |      |

1.4.0改进一次遍历

```flow
st=>start: 开始
op_initarray=>operation: 创建存结果下标的数组
op_initdic=>operation: 创建存下标和值的字典
op_enumerarray=>operation: 枚举遍历数组
op_addednum=>operation: 计算被加数addednum
cond_containkeys=>condition: 字典keys是否
                             包含addednum
io_contain=>inputoutput: 输出index,dic[addednum]
op_continue=>operation: dic添加值为index,key为num
e=>end: 结束
st->op_initarray->op_initdic->op_enumerarray->op_addednum->cond_containkeys(yes)->io_contain->e
st->op_initarray->op_initdic->op_enumerarray->op_addednum->cond_containkeys(no)->op_continue->op_enumerarray

```

1.5.0一遍hash表

```flow
st=>start: 开始
op_inithash=>operation: 创建hash表
op_forin=>operation: index,vallue枚举
                     遍历数组
op_addednum=>operation: 计算被加数
                        target-value
cond_findaddednum=>condition: 是否hsash找到
                              第二数的下标
io_found=>inputoutput: 输出addednum  
                       下标,index下标
op_failfind=>operation: table[num] = index
e=>end: 结束
st->op_inithash->op_forin->op_addednum->cond_findaddednum(yes)->io_found->e
st->op_inithash->op_forin->op_addednum->cond_findaddednum(no)->op_failfind->op_forin
```

```swift
  var arrDic = [Int: Int]()
        var arr = [Int]()
        for (index , value) in nums.enumerated() {
            if (arrDic.keys.contains(target - value)){
                arr = [arrDic[target - value]!,index]
                break
            }else{
                arrDic[value] = index
            }
        }
        return arr
    }
```









