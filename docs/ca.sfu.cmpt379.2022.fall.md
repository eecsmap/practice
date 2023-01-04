## 项目基本结构
课程项目框架按照功能阶段组织如下：

1. logging
    1. 这个被用来报错，感觉还是有点不对劲
2. inputHandler
    1. 引入接口Locator
    2. 将输入文件封装成可定位的可回退的字符流，方便lexicalAnalyzer提取token
3. lexicalAnalyzer
    1. 本质上是一个token iterator
    2. lextant: 词法单元中的标点符号以及关键字
4. tokens
    1. 基本抽象token：可定位，可获取词素
       1. 词素
       2. 定位
       3. 是否属于lextant set
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
            1.  这个间接寻址等价于通过寄存器寻址，用一个预先分配的固定内存位置充当寄存器。
        2.  design pattern: template method, Java enum singleton
        3.  public void generateAddress(ASMCodeFragment code, String baseAddress, int offset, String comment)
            1.  往code里加入变量的地址，并加以标注
            2.  基地址，offset，以及标注（名字）来自绑定的memoryLocation
            3.  这个类其实应该放在code generator里
    3.  基本抽象Scope
        1.   每个scope有一个内存分配器MemoryAllocator（subscope继承这个分配器）
             1.   MemoryAllocator（管理寻址方式，基址，分配方向）
                  1.   接受给定大小的分配请求，返回MemoryLocation
                       1.   MemoryLocation提供生成压栈地址的指令序列
        2.  每个Scope维护自己的符号表SymbolTable(String -> Binding)
        3.  nullInstance()这个其实没有存在的必要。唯一用到的地方其实是死代码
        4.  getAllocatedSize()
        5.  每次创建scope时，对应的分配器做一次标记，离开这个scope的时候，分配器弹出上一个记录
    4.  SymbolTable本质上就是标识符到绑定的映射
    5.  Binding: 标识符名称，类型，源文件位置，内存位置，等相关的信息。每个分配了内存地址的binding，都应该有一个memoryLocation，并且可以根据这个内存地址来生成代码将此代码压栈。binding.memoryLocation.getAddressCode()，或者CodeGenerator.generateAddressCode(binding.memoryLocation)。哪种设计更好？为什么？
12. asmCodeGenerator
    1.  产生线性的代码结构
13. asmCodeGenerator.codeStorage
    1.  指令，指令块
14. asmCodeGenerator.operators
15. asmCodeGenerator.runtime
    1.  运行时支持
        1.  内存分配器
        2.  运行时函数

## 一些笔记，以免遗忘
1. Binding是在哪里构造的
   1. 语义分析时，遇到声明语句时，因为已经处理过标识符节点，以及表达式节点。可以在退出访问声明语句节点时构建绑定。
      1. SemanticAnalyzer
      2. IdentifierNode
      3. Scope
      4. CreateBinding
   2. 语义分析时，获取了类型信息就直接分配内存并生成绑定并传递给IdentifierNode
2. Binding核心功能就是提供类型和内存地址
3. IdentifierNode是叶子结点，所以使用visit。语义分析访问属于DeclarationNode的此结点时生成Binding，代码生成器访问时此结点时生成地址。
4. MemoryManager.java是一个堆的分配器，这里的函数都使用全局变量，因此不能递归调用。其实与其叫它们函数，不如叫routine/procedure更合适，因为它们没有自己的局部变量。
1. 函数调用应该生成一个值，即使这个函数是void，代码生成也是一个ValueCode
2. AtomicExpression等同于C里的PrimaryExpression，即最高优先级的表达式，表达式最高优先级总是会收敛到此。
3. 错误处理，语法，返回一个ErrorNode，语义赋值一个ErrorTYpe，代码生成拒绝。
4. Bilby只有全局（静态）作用域，函数作用域，变量寻址就相当容易。
5. 所有的string字面量都可以放在global下。
6. 左值以地址的形式出现在赋值操作左侧，其他地方都转成所包含的数值。
7. 算符的类型是所支持的signature的集合。
8. 如果函数支持重载，那么它的类型也是signature的集合，（匹配参数的时候，只关心参数类型，所以不同的返回类型不能作为不同signature的判断依据）
9. 

## 任务分解
1. 堆分配器的运行时逻辑


## 关于动态作用域跟静态作用域
```
a = 1
foo():
    return a + 3

main():
    a = 2
    b = foo()
    if (b == 5) dynamic else if (b == 4) static
```

## Design Patterns
1. parseTree.PathToRootIterable


## size of the skeleton project
```
engineer@mac bilby-S % find . -name '*.java' | grep 'tests' -v | xargs wc -l | sort -hr
    5876 total
     785 ./src/asmCodeGenerator/runtime/MemoryManager.java
     404 ./src/parser/Parser.java
     319 ./src/asmCodeGenerator/ASMCodeGenerator.java
     188 ./src/asmCodeGenerator/codeStorage/ASMCodeFragment.java
     171 ./src/semanticAnalyzer/SemanticAnalysisVisitor.java
     170 ./src/asmCodeGenerator/codeStorage/ASMOpcode.java
     167 ./src/lexicalAnalyzer/LexicalAnalyzer.java
     166 ./src/parseTree/ParseNode.java
     158 ./src/asmCodeGenerator/codeStorage/ASMInstruction.java
     124 ./src/symbolTable/Scope.java
     121 ./src/parseTree/ParseTreePrinter.java
     118 ./src/parseTree/ParseNodeVisitor.java
     109 ./src/semanticAnalyzer/signatures/FunctionSignature.java
     108 ./src/lexicalAnalyzer/PunctuatorScanningAids.java
     105 ./src/asmCodeGenerator/Macros.java
      96 ./src/semanticAnalyzer/signatures/FunctionSignatures.java
      92 ./src/asmCodeGenerator/runtime/RunTime.java
      91 ./src/applications/BilbyApplication.java
      88 ./src/inputHandler/InputHandler.java
      87 ./src/applications/BilbyCompiler.java
      86 ./src/applications/BilbyCodeGenerator.java
      85 ./src/inputHandler/LocatedCharStream.java
      78 ./src/asmCodeGenerator/PrintStatementGenerator.java
      77 ./src/parseTree/nodeTypes/IdentifierNode.java
      77 ./src/inputHandler/LineBasedReader.java
      68 ./src/symbolTable/SymbolTable.java
      66 ./src/symbolTable/Binding.java
      65 ./src/logging/BilbyLogger.java
      62 ./src/inputHandler/LocatedChar.java
      61 ./src/lexicalAnalyzer/PunctuatorScanner.java
      61 ./src/inputHandler/TextLocation.java
      59 ./src/symbolTable/MemoryLocation.java
      58 ./src/symbolTable/NegativeMemoryAllocator.java
      58 ./src/asmCodeGenerator/codeStorage/ASMCodeChunk.java
      57 ./src/symbolTable/PositiveMemoryAllocator.java
      56 ./src/lexicalAnalyzer/Punctuator.java
      52 ./src/parseTree/nodeTypes/DeclarationNode.java
      51 ./src/tokens/TokenImp.java
      50 ./src/parseTree/nodeTypes/OperatorNode.java
      49 ./src/lexicalAnalyzer/Keyword.java
      49 ./src/inputHandler/PushbackCharStream.java
      46 ./src/inputHandler/LocatedCharString.java
      43 ./src/symbolTable/MemoryAccessMethod.java
      43 ./src/applications/BilbyTokenPrinter.java
      42 ./src/applications/BilbySemanticChecker.java
      39 ./src/parseTree/PathToRootIterable.java
      38 ./src/applications/BilbyAbstractSyntaxTree.java
      36 ./src/parseTree/nodeTypes/BooleanConstantNode.java
      36 ./src/applications/NumberedFileLister.java
      35 ./src/parseTree/nodeTypes/IntegerConstantNode.java
      35 ./src/lexicalAnalyzer/ScannerImp.java
      33 ./src/tokens/LextantToken.java
      33 ./src/parseTree/nodeTypes/PrintStatementNode.java
      32 ./src/lexicalAnalyzer/PartiallyScannedPunctuator.java
      31 ./src/tokens/Tokens.java
      28 ./src/tokens/NumberToken.java
      28 ./src/parseTree/nodeTypes/ProgramNode.java
      28 ./src/parseTree/nodeTypes/MainBlockNode.java
      27 ./src/semanticAnalyzer/types/PrimitiveType.java
      25 ./src/lexicalAnalyzer/LexemeMap.java
      23 ./src/parseTree/nodeTypes/SpaceNode.java
      23 ./src/parseTree/nodeTypes/NewlineNode.java
      23 ./src/parseTree/nodeTypes/ErrorNode.java
      22 ./src/semanticAnalyzer/SemanticAnalyzer.java
      21 ./src/asmCodeGenerator/Labeller.java
      20 ./src/tokens/NullToken.java
      20 ./src/tokens/IdentifierToken.java
      17 ./src/semanticAnalyzer/types/Type.java
      13 ./src/tokens/Token.java
      11 ./src/symbolTable/MemoryAllocator.java
      11 ./src/asmCodeGenerator/operators/SimpleCodeGenerator.java
       9 ./src/lexicalAnalyzer/Scanner.java
       8 ./src/lexicalAnalyzer/Lextant.java
       5 ./src/inputHandler/Locator.java
```
