## 项目基本结构
课程项目框架按照功能阶段组织如下：

1. logging
    1. 这个被用来报错，感觉还是有点不对劲。
2. inputHandler
    1. 引入接口Locator
    2. 将输入文件封装成可定位的可回退的字符流，方便lexicalAnalyzer提取token
3. lexicalAnalyzer
    1. 本质上是一个token iterator
    2. lextant: 词法单元中的标点符号以及关键字
4. tokens
    1. 基本抽象token：可定位，可获取词素
    2. 字面量：整型，浮点，字符，布尔值，字符串
    3. 标识符
    4. 标点
    5. 关键字
5. parser
    1. 读取token流，通过BNF产生式构造AST
6. parseTree
    1. 提供基本类ParseNode
       1. getClass()
       2. getToken()
       3. getType()
       4. getScope()
    2. 提供基本类ParseNodeVisitor
7. parseTree.nodeTypes
    1. 非终结符对应的各种具体的Node
8.  sementicAnalyzer
    1.  对AST进行语义分析，检查推断类型，分配内存，构建绑定
9.  sementicAnalyzer.types
    1.  类型系统
10. sementicAnalyzer.signatures
    1.  根据输入的类型选择合法的操作
11. symbolTable
    1.  MemoryLocation
        1.  baseAddress:String; 内存定位总是基于某个基地址，可以是内存的某个段，或者通过“寄存器”间接寻址。这个机器里没有寄存器的概念，但是我们可以通过预留的全局空间来模拟。比如FP,SP的实现。
        2.  offset:int
        3.  因为分配内存的时候，并没有完全确定下来最后的位置。所以分配的内存信息包含了相对的偏移值。
    2.  MemoryAccessMethod
        1.  这个类以enum的形式提供了2个内存访问方法，分别是基于符号的直接偏移寻址，以及间接寻址。base[offset], base[0][offset]
        2.  design pattern: template method, Java enum singleton
        3.  public void generateAddress(ASMCodeFragment code, String baseAddress, int offset, String comment)
            1.  往code里加入变量的地址，并加以标注。
            2.  基地址，offset，以及标注（名字）来自绑定的memoryLocation。
            3.  这个类其实应该放在code generator里。
    3.  基本抽象Scope
        1.   每个scope有自己的内存分配器MemoryAllocator
             1.   MemoryAllocator
             2.   建立subscope的时候，理所当然MemoryAllocator应该向下传递。
        2.  getAllocatedSize()
        3.  nullInstance()这个其实没有存在的必要。唯一用到的地方其实是死代码。
    4.  每个Scope维护自己的符号表SymbolTable
    5.  SymbolTable本质上就是标识符到绑定的映射
    6.  绑定：标识符内存，类型，等相关的信息
12. asmCodeGenerator
    1.  产生线性的代码结构
13. asmCodeGenerator.codeStorage
    1.  指令，指令块
14. asmCodeGenerator.operators
15. asmCodeGenerator.runtime
    1.  运行时支持
        1.  内存分配器
        2.  运行时函数
