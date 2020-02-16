[TOC]

# Swift 两数之和

### 1前提Swift定义链表

值val![img](file:///Users/v_liuxiaoju/Library/Caches/BaiduMacHi/Share/images/7a86d98aa8293fbd24f05b385aae118c.jpg)

下一个节点的引用(地址)next

初始化方法

* 头文件引用
  * Swift引用oc
    * 引用自定义oc头文件:要建立桥接文件
    * 引用cocopod第三方库/系统类库
      * 有桥接文件，需要配置
      * 无桥接文件，需要创建桥接文件，并配置
  * Swift引用Swift
    * 引用自定义swift头文件:无需导入
    * 引用coopod第三方库/系统库

``` swift
class ListNode {
    var val: Int
    var next: ListNode ?
    init(_ val: Int) {
        self.val = val
        self.next = nil
    }
}
```

* ``` swift
  func addTwoNums(_ ListNode:l1, _ ListNode:l2)->ListNode{
     var p = l1
     var q = l2
     
  }
  ```

* 数组链表区别

  https://www.cnblogs.com/jiqing9006/p/7615467.html

* 引入头文件处理:https://www.jianshu.com/p/8589dd2e11ed

* 函数调用https://www.jianshu.com/p/b254e84d2624

* 参数标签https://blog.csdn.net/gang544043963/article/details/83865236

* 链表https://www.jianshu.com/p/cf962aeff643

* 打印链表？

* swift var let ?  !

  * 不需要修改变量，用let声明。 需要修改变量用var声明。

  * !?

    在实际用Swift写CocoaTouch时，发现下面这样写才可以通过编译

    ``` swift
    
    
    var amiteLbl :UILabel?
    
    self.amiteLbl = UILabel(frame:CGRectMake(50,100,200,40))
    
    self.amiteLbl!.text = “I love mixbox”
    
    self.view?.addSubview(self.amiteLbl)
    ```

    解释：

    由于amiteLbl是可选变量，所以可能有值，也可能为nil。

    使用self.amiteLbl!是明确声明此时self.amiteLbl里一定有值，无论什么情况都调用后面的.text赋值方法。

    而使用self.view?是声明此时并不确定self.view里是否有值，所以只在view有值时调用后面.addSubview方法。

    这样做的目的一是让代码更明确， 二是给编译器提供更多线索，在编译时发现更多潜在错误。

    Swift显然是一门非常明确，需要开发者先想清楚再编程的语言。

  * let

    * let声明的变量通常为不可变的变量

    * let 变量名:  类型  = 值

    * let声明的变量，**不能**再**赋值**，**修改**。

  * var

    * var生命的变量，统统为可变变量

    * 声明可变变量没有被修改

      * 会提示：Variable 'a' was never mutated; consider changing to 'let' constant

      * 提示你声明的是可变变量，而你没有修改它,建议用let修饰

      * swift是**类型安全**语言，对类型的要求比较严格

        * 

        * 类型安全语言

          * 什么是类型安全

            * 类型安全很大程度可以等价于内存安全

            * 类型安全的代码不会试图访问自己没被授权的内存区域

            * 类型安全的语言鼓励程序员在编写代码时,提前预设好变量及常量的类型,防止在传递及赋值时传给不同类型的值

            * Swift在编译时就会做类型检测,并且以错误的方式标明所有不匹配的类型

            * Swift增加的类型推断,会自动对常量与变量进行类型推断,声明合适的类型

            * 如果代码中使用一个字符串String，那么你不能错误的传递一个整型Int给它。因为Swift是类型安全的，它会在代码**编译的时候**做类型检查，并且把所有不匹配的类型作为一个错误标记出来。这样使得程序员在开发中尽可能早地发现和修正错误。

            * 如果你没有给一个值指定你所需要的类型，Swift会使用**类型推断**来推算出一个合适的类型。类型推断使得编译器在代码**编译**的时候，通过简单的检测提供的值，能够自动推断出类型。

            * **类型别名**

              类型别名是使用typealias关键字为一个已经存在的类型定义了一个可替换的名字。

              typealiasAudioSample=UInt16

              一旦你定义了一个类型别名，你可以在任何使用原名的地方使用这个别名。

              varmaxAmplitudeFound=AudioSample.min

              这里AudioSample被定义为UInt16的一个别名。因为它是别名，所以AudioSample.min实际上是调用UInt16.min。

            * 类似，如果你没有为一个浮点值指定类型，Swift会推断你想生成一个Double 类型：

              letpi=3.14159

              Swift总是会选择Double（而不是Float）作为浮点数的推断类型。如果在一个表达式中把整数和浮点数相加，那么Double将会是作为一个推断类型：

              letanotherPi=3+0.14159

              

  ​    

    

### 2流程图

  ```flow
st=>start: 开始
e=>end: 结束
st->e
  ```

  

  
