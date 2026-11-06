# 学习进度只读镜像

数据版本：43
网站最后保存：2026-11-06T07:51:46.948000Z
本次同步：2026-11-06T07:55:12.905808Z
最近学习：2026-11-05

每次使用请检查同步时间和 GitHub Actions 最近一次运行结果；文件可读取不代表同步服务始终正常。

## 当前 C++ 起点
第 35/48 节｜Debug 与 Release｜已讲解

## 已验证与记录边界
C++ 第32–34节结课，累计34/48（70.8%），剩余14节。11月5日新验收12项实验：第32节3项、第33节4项、第34节5项。第33节实验2已讲解，按用户要求跳过实操。第35节已讲解，实验1待实操。
11-05 结课。11-04 已通过配置查询。11-05 验收实验2–4：合法更新为512，类型不符、缺键、负数均拒绝。模拟异常保持256/0.95，成功提交后为512/0.85。错误get<int>触发bad_variant_access，原配置保持512/0.85。
多文件编译、CMake、静态库、增量构建四项通过。对齐声明和定义的参数类型后解决arm64链接报错，IntelliSense改为C++20后红线消失。实验2头文件保护已讲解，用户跳过实操。
五项通过：规范目录与PUBLIC使用要求。故意改PRIVATE复现config.h缺失。生成约110KB的dylib。otool -L显示@rpath/libconfig_lib.dylib。otool -l显示LC_RPATH指向build目录。
已讲解Debug/Release、-g、-O0/-O2/-O3、NDEBUG和CMAKE_BUILD_TYPE。实验1已布置，待确认目录和源码后进行两套构建，尚缺实际输出。

此前验证：
2026-11-04新增验证：2026-11-04：C++第29–31节编程实验通过，主线31/48（64.6%）；第32节进行中，实验1配置查询通过。今日20项实验有运行/编译证据（6+6+7+1），包含预期失败和修复验证。第30节2道、第31节1道概念小测未提交。实际时长未提供；Jetson/CUDA没有新增实机实验。
6/6编程实验通过。异常捕获后继续运行；栈展开按B→A析构（模拟资源日志）；直接修改后保留40，临时副本失败则原值10/20/30不变；本机vector扩容有noexcept时Move A、去掉后Copy A。非GPU实验。
6/6编程实验通过。constexpr与static_assert、int/const/constexpr、运行期输入10→100；constexpr常量表达式故意编译失败为验证成功；多文件缺实现链接失败后修复输出25；-c目标文件108K/1.9K，链接运行输出25。末尾2道概念小测未提交；未实现CMake。
7/7编程实验通过。optional/空值取值、variant三类型切换与get、visit、if constexpr/类型别名、any_cast/reset均有输出。末尾1道optional<double>概念小测未提交。MatMul38ms/GPU名称为模拟示例，非设备性能。
实验1配置查询已验收：在cpp_lesson32正确目录重新编译运行，block_size=256、threshold=0.95、device=GPU、unknown: Not found。旧day1目录any程序的输出不是本节证据；实验2–5尚未运行。

此前验证（保留原日期与证据）：
第1–13节主要练习沿用原进度。2026-10-31日报附有第14节移动赋值和自移动输出、第15节数组统计两组输出、第16节重载及引用增量输出、第17节作用域输出和引用语义问答。第17节随后由用户确认验收；生命周期回答指出局部对象离开作用域后消失、指针悬空，核心判断正确。

Linux 2026-11-01：惠普光影精灵7，Windows + WSL Ubuntu，目录[本地路径已省略]。已验证grep/管道/wc/find/重定向、日志检查三分支、chmod755、bash与直接执行、位置参数及跨目录path_demo.sh。仅有主目录启动的一组路径输出；command -v bash在脚本内已验证。

2026-11-01 C++：第18–21节已验收。string/view复制与观察、分词6/3→7/4；vector统计588/93/3/84与重分配检查；span三类容器求和与重建；STL排序/查找/求和、迭代器失效与erase安全删除均有日报实测依据。第1–17节沿用既有状态。

2026-11-02：第22节四组关联容器实验据教学记录已验收；第23节四项Lambda编程实验现已通过，专项复习仍保留。

2026-11-02续学：Lambda四个编程实验通过。基础25、1/0、3、3；阈值30→40时值捕获计数3→3、引用捕获3→1；mutable内部15→20而外部10，引用修改外部15；自定义sort得到MatMul38、Reduce25、Softmax25、Add12、ReLU8，慢算子数3，并正确解释return控制流。以上排序耗时为手工模拟数据，非GPU性能。泛型Lambda、transform、引用捕获悬空风险与两道概念题未专项验收。
2026-11-02：第24节实验1已验收，修正MaxMul为MatMul后，Add count2 avg0.16、MatMul count2 avg1.74、ReLU count1 avg0.09、Softmax count2 avg0.70 ms；这些是模拟延迟。实验2排行榜仅讲解/布置，预期输出不是实测；实验3未开始。

2026-11-03：C++主线28/48（58.3%），第26–28节课程实验完成，共11项：26节4项（实验1沿用此前确认），27节4项，28节3项。重点复习RAII/所有权、shared_ptr循环引用、值类别/引用折叠/forward；关联P1缓冲区与P2任务/回调的工程用途。下一节29尚未开始。Jetson待首次连接，未核验环境、未运行CUDA。
4个实验完成。vector独立元素存储的输出沿用此前确认；unique_ptr

## 疑问与薄弱点
复习 optional→variant→visit 的取值顺序、字符串字面量与const引用、类型检查和副本提交。对照声明与定义的函数签名、编译/链接/运行三个阶段、CMake的PUBLIC/PRIVATE/INTERFACE与增量依赖。第33节头文件保护已讲解并跳过实操，第35节实验1待运行。

此前复习记录：
当前复习与未完成项：优先巩固：编译期/运行期、局部变量与常量表达式、const/constexpr；声明/定义/编译/链接/-c/.o；Lambda与普通函数；using类型别名/class定义/template<class T>；optional/variant/any、visit运行期派发与if constexpr编译期分支；unordered_map的find与[]；void return;、nullopt与break；-Wall/-Wextra含义（用户选择不加做额外实验）。第30节末2道概念小测、第31节末1道小测尚未提交，不撤销编程通过状态。
第28节const move与转发路径仍需巩固；扩容/noexcept对照已由第29节覆盖。第32节实验2–5尚未运行。

既有专项复习与历史疑问（当前断点以上方为准）：
当前专项复习：第26节：按值传vector的复制→移动链与默认特殊成员条件；第27节：所有权图、lock临时拥有者、循环引用；第28节优先：实参值类别→T推导→引用折叠→传出表达式→最终构造。const move、扩容/noexcept仍未补验。第24、25节依据日报汇总确认完成，尚缺本次新增逐实验输出。第23节既有专项复习继续；Linux原待实操保留。

此前疑问留档（以下按日期追溯，当前状态以上方与课表为准）：
第14节：含 unique_ptr 成员且未自定义特殊成员函数的类，为何不能拷贝却可以移动？此自测题待复习。第17节生命周期题已验收，复习时注意 p 是指针，解引用悬空指针是未定义行为。

Linux 待实操：sed修正errror后复测计数为2（未展示输出）；不传参数调用check_log.sh，验证默认文件名（未展示输出）；报错信息补充文件名后重新验证（未展示输出）；查看PATH并运行command -v code（待实操）；对比source/bash/直接执行及$0/BASH_SOURCE[0]（待实操）；补做从脚本所在目录启动的对照输出（尚缺一组）；Git/CMake/GDB小型C++项目综合实践（今日未开展）。

第14节 unique_ptr/Rule of Zero题仍待复习；视图生命周期、扩容导致引用/span/迭代器失效、旧end失效及erase返回值需持续巩固。

2026-11-02更新：第22节已验收；第23节捕获对照现已通过。第14节unique_ptr/Rule of Zero和Linux原待实操清单继续保留。

泛型Lambda、std::transform、引用捕获生命周期/悬空风险仍待专项练习；两道概念测验未提交。四项编程实验已通过，不阻止继续第24节。 第24节现由11-03日报汇总确认完成，新增逐实验输出仍待补。

## 下一步
从第35节实验1「Debug/Release 双构建」继续。先确认 cpp_lesson35 工程和源码，分别构建 Debug 与 Release，对比编译 flags，运行两个版本并保存终端输出。之后再做 assert 与 NDEBUG 对照。

Linux：先用sed修正errror并复测，再验证无参数默认文件名和包含文件名的报错；随后补PATH、source和路径对照实验，再做Git/CMake/GDB小项目。C++现有接续点为第35节，每日Linux复习≤1小时。

CANN 入门可与 C++ 第 35–40 节并行。先读社区教程的 NPU 架构与 Add 示例，有匹配的 CANNLab 环境后记录版本并运行样例。

每日算法练习从 Hot 100 开始。下一道待记录题为 #1 两数之和（哈希）。

## Linux / CANN 主线
沿用 48 节 C++ 课表。每次先完成当前实验，再做一道 C++ Hot 100 题或复做一道错题，建议留 20–40 分钟。
Linux 复习融入实际构建和排错，每天最多 1 小时。C++ 第 35–40 节期间可开始 CANN 社区入门，随后按算子验收进入赛题。
Ascend C 实践顺序为社区教程 → Add / Reduce 基线 → 往届赛题复现 → 天梯赛。设备与工具版本按题面核对，正式赛程以官方公告为准。
Jetson 两个项目归入历史。长期优先级为 2027 CANN 算子竞赛 → 可复现系统研究 → AI Infra 实习，软挑按时间选做。

## 最近学习摘要

### 2026-11-05｜C++｜第32–34节结课，第35节实验1待实操
C++ 第32–34节结课，累计34/48（70.8%），剩余14节。11月5日新验收12项实验：第32节3项、第33节4项、第34节5项。第33节实验2已讲解，按用户要求跳过实操。第35节已讲解，实验1待实操。
实验结论：11-05 结课。11-04 已通过配置查询。11-05 验收实验2–4：合法更新为512，类型不符、缺键、负数均拒绝。模拟异常保持256/0.95，成功提交后为512/0.85。错误get<int>触发bad_variant_access，原配置保持512/0.85。
多文件编译、CMake、静态库、增量构建四项通过。对齐声明和定义的参数类型后解决arm64链接报错，IntelliSense改为C++20后红线消失。实验2头文件保护已讲解，用户跳过实操。
五项通过：规范目录与PUBLIC使用要求。故意改PRIVATE复现config.h缺失。生成约110KB的dylib。otool -L显示@rpath/libconfig_lib.dylib。otool -l显示LC_RPATH指向build目录。
已讲解Debug/Release、-g、-O0/-O2/-O3、NDEBUG和CMAKE_BUILD_TYPE。实验1已布置，待确认目录和源码后进行两套构建，尚缺实际输出。
掌握情况：C++ 第32–34节结课，累计34/48（70.8%），剩余14节。11月5日新验收12项实验：第32节3项、第33节4项、第34节5项。第33节实验2已讲解，按用户要求跳过实操。第35节已讲解，实验1待实操。
疑问：复习 optional→variant→visit 的取值顺序、字符串字面量与const引用、类型检查和副本提交。对照声明与定义的函数签名、编译/链接/运行三个阶段、CMake的PUBLIC/PRIVATE/INTERFACE与增量依赖。第33节头文件保护已讲解并跳过实操，第35节实验1待运行。
下一步：从第35节实验1「Debug/Release 双构建」继续。先确认 cpp_lesson35 工程和源码，分别构建 Debug 与 Release，对比编译 flags，运行两个版本并保存终端输出。之后再做 assert 与 NDEBUG 对照。

### 2026-11-04｜C++｜第29–31节编程通过，第32节实验1通过
2026-11-04：C++第29–31节编程实验通过，主线31/48（64.6%）；第32节进行中，实验1配置查询通过。今日20项实验有运行/编译证据（6+6+7+1），包含预期失败和修复验证。第30节2道、第31节1道概念小测未提交。实际时长未提供；Jetson/CUDA没有新增实机实验。
实验结论：6/6编程实验通过。异常捕获后继续运行；栈展开按B→A析构（模拟资源日志）；直接修改后保留40，临时副本失败则原值10/20/30不变；本机vector扩容有noexcept时Move A、去掉后Copy A。非GPU实验。
6/6编程实验通过。constexpr与static_assert、int/const/constexpr、运行期输入10→100；constexpr常量表达式故意编译失败为验证成功；多文件缺实现链接失败后修复输出25；-c目标文件108K/1.9K，链接运行输出25。末尾2道概念小测未提交；未实现CMake。
7/7编程实验通过。optional/空值取值、variant三类型切换与get、visit、if constexpr/类型别名、any_cast/reset均有输出。末尾1道optional<double>概念小测未提交。MatMul38ms/GPU名称为模拟示例，非设备性能。
实验1配置查询已验收：在cpp_lesson32正确目录重新编译运行，block_size=256、threshold=0.95、device=GPU、unknown: Not found。旧day1目录any程序的输出不是本节证据；实验2–5尚未运行。
掌握情况：第29节6/6、第30节6/6、第31节7/7编程实验通过；第32节仅实验1通过，2–5未运行。第30/31节共3道概念小测待补；31/48为编程实践口径。
疑问：优先巩固：编译期/运行期、局部变量与常量表达式、const/constexpr；声明/定义/编译/链接/-c/.o；Lambda与普通函数；using类型别名/class定义/template<class T>；optional/variant/any、visit运行期派发与if constexpr编译期分支；unordered_map的find与[]；void return;、nullopt与break；-Wall/-Wextra含义（用户选择不加做额外实验）。第30节末2道概念小测、第31节末1道小测尚未提交，不撤销编程通过状态。
下一步：第32节实验2「类型安全读取与错误处理」：先简短回顾find与return;，然后一次只布置一个实验；测试正常值、键不存在、类型不符，提交实际终端输出后验收。实验1已经通过，不重复。之后依次参数合法性验证、安全更新、多文件与最小测试；这些后续步骤尚未运行。

### 2026-11-03｜C++｜第26–28节完成｜RAII、智能指针与完美转发难点复盘
C++主线28/48（58.3%），第26–28节课程实验完成，共11项：26节4项（实验1沿用此前确认），27节4项，28节3项。重点复习RAII/所有权、shared_ptr循环引用、值类别/引用折叠/forward；关联P1缓冲区与P2任务/回调的工程用途。下一节29尚未开始。Jetson待首次连接，未核验环境、未运行CUDA。
实验结论：4个实验完成。vector独立元素存储的输出沿用此前确认；unique_ptr移动后源为空/新对象值100；故意复制DataOwner得到隐式删除拷贝构造的编译错误（预期失败即通过）；新建资源拷贝100→200，原值100，Same address=false。
4个实验有本次终端输出。shared_ptr count 1→2→1且共享值200；weak lock期间count2、之后1、作用域后expired=true；A/B循环保持存活，手动断环后Destroy A/Destroy B；weak previous版本无需手动断环，A expired=true。
3个实验有本次终端输出。reserve(4)后push/emplace：Copy count=1，Move count=2，size4；relay中命名形参直接传出总是左值，forward保留输入值类别；四次插入依次Copy A、Move B、Copy C、Move C，Size=4。已完成四路径讲解，但保留专项复习；没有实测性能收益。
掌握情况：第26–28节11项课程实验完成；第26节实验1沿用此前确认。保留专项复习，尤其第28节四路径与反例；28/48，总体完成确认不补造24/25逐实验输出。Jetson待首次连接。
疑问：第26节：按值传vector的复制→移动链与默认特殊成员条件；第27节：所有权图、lock临时拥有者、循环引用；第28节优先：实参值类别→T推导→引用折叠→传出表达式→最终构造。const move、扩容/noexcept仍未补验。第24、25节依据日报汇总确认完成，尚缺本次新增逐实验输出。第23节既有专项复习继续；Linux原待实操保留。
下一步：第29节「异常与资源安全」尚未开始：先复盘第26–28节的所有权和四条转发路径，再按原课表做异常/错误路径下的资源清理实验。复习不撤销已通过实践；未完成反例不得标为验收。

### 2026-11-02｜C++｜第23节四实验已实践，第24节实验1通过（保留第22节既有验收）
关联容器选择、词频、find与[]、set；Lambda基础与捕获。

2026-11-02：第23节Lambda四项编程实验已实践通过；第24节模拟算子平均耗时统计实验1已验收，实验2排行榜待运行，实验3未开始。当天设备为MacBook Air M5，未做Jetson上机，未补录时长。
实验结论：依据2026-11-02用户上传的教学记录摘要：①map词频CANN3/kernel2/operator1，size3；②find不插入，[]插入CUDA0、更新为5、erase后size3；③map/unordered_map词频相同、遍历顺序不同，contains为1/0；④set对实际数据{CANN,CUDA,operator,CANN,kernel,CANN,kernel}去重4、删除CUDA后3。综合选择题未逐一提交，教学记录已确认第22节验收；不补写Tensor项。
依据2026-11-02用户上传的教学记录摘要：Lambda第一个实验已验证，平方25，偶数判断1/0，偶数个数3，大于30个数3；[threshold]与[&threshold]的第二个对照实验仅布置，尚无运行输出，第23节不计完成。

2026-11-02续学：Lambda四个编程实验通过。基础25、1/0、3、3；阈值30→40时值捕获计数3→3、引用捕获3→1；mutable内部15→20而外部10，引用修改外部15；自定义sort得到MatMul38、Reduce25、Softmax25、Add12、ReLU8，慢算子数3，并正确解释return控制流。以上排序耗时为手工模拟数据，非GPU性能。泛型Lambda、transform、引用捕获悬空风险与两道概念题未专项验收。
2026-11-02：第24节实验1已验收，修正MaxMul为MatMul后，Add count2 avg0.16、MatMul count2 avg1.74、ReLU count1 avg0.09、Softmax count2 avg0.70 ms；这些是模拟延迟。实验2排行榜仅讲解/布置，预期输出不是实测；实验3未开始。
掌握情况：第22节沿用已验收；第23节四个编程实验已实践通过并保留专项复习；第24节学习中，实验1通过、实验2待运行、实验3未开始。
疑问：泛型Lambda、std::transform、引用捕获生命周期/悬空风险仍待专项练习；两道概念测验未提交。四项编程实验已通过，不阻止继续第24节。 第14节与Linux原待实操清单继续保留。
下一步：第24节实验2：运行已有map→vector→sort + Lambda排行榜代码，提交实际终端输出，核对MatMul→Softmax→Add→ReLU排序、元素数与平均值；该顺序目前只是预期，尚未实测。通过后再做实验3阈值筛选。第23节泛型Lambda、transform与引用捕获生命周期及第14节unique_ptr/Rule of Zero保留专项复习。

### 2026-11-01｜C++｜C++ 第18–21节学习日报｜四节已验收
string/string_view拥有关系与切片；vector的size/capacity/reserve与扩容失效；array/span统一连续容器接口；迭代器与STL算法、end安全和erase失效规则。
实验结论：第18节：实验A：s修改后FANN，copy仍CANN，view为FANN；实验B size=13、find=5，copy为operator、part为Operator；分词6词/CANN3次，追加后7词/4次；remove_prefix理解题通过。
第19节：引用遍历得15 25 35 45，sum120；reserve后size3/capacity8，追加至9后capacity16（本机结果）；地址变化验证扩容且未访问失效ref；统计size7/capacity16/sum588/max93/count3/average84/reallocated=false。
第20节：局部span修改array结果10 25 40 40；统一sumValues(span<const int>)结果array60/vector220/raw6，修改后vector230；追加后旧span长度仍3，扩容后重建span长度9、末项99；IntelliSense设c++20后诊断解决。
第21节：sort后15 27 42 60 83，find42索引2，sum227；修改元素后10 25 30 40 50，find100返回end不解引用；扩容后重建迭代器；erase返回40，安全删除20倍数后10 50。四项实验通过验收。
掌握情况：第18、19、20、21节已验收；第22节未开始／实验待运行；学习时长未实测。
疑问：第14节 unique_ptr/Rule of Zero题仍待复习；第22节仅布置map词频实验，未提交运行证据，不标记学习中或验收。视图生命周期、扩容导致引用/span/迭代器失效、旧end失效及erase返回值需持续巩固。
下一步：第22节「关联容器」仍未开始：先运行 std::map<std::string,int> 词频统计实验并提交实际输出，再核对 ++counts[word]、结构化绑定、find、it->first / it->second 与 map.size()。随后按48节主线推进；第14节 unique_ptr / Rule of Zero 自测题继续待复习。

## 48 节课程状态
- 第 1 节｜环境与编译运行｜已实践
- 第 2 节｜变量与基本类型｜已实践
- 第 3 节｜函数与值传递｜已实践
- 第 4 节｜引用与 const｜已实践
- 第 5 节｜指针与地址｜已实践
- 第 6 节｜数组与动态内存｜已实践
- 第 7 节｜类与成员函数｜已实践
- 第 8 节｜构造与析构｜已实践
- 第 9 节｜RAII 与资源管理｜已实践
- 第 10 节｜智能指针入门｜已实践
- 第 11 节｜拷贝构造｜已实践
- 第 12 节｜拷贝赋值｜已实践
- 第 13 节｜移动构造｜已实践
- 第 14 节｜移动赋值与 Rule of Five｜已实验通过｜复习：unique_ptr 与 Rule of Zero 自测题待复习
- 第 15 节｜基本类型与控制流程复核｜已实验通过
- 第 16 节｜函数与参数设计｜已实验通过
- 第 17 节｜作用域与 const 正确性｜已验收
- 第 18 节｜std::string 与 string_view｜已验收
- 第 19 节｜std::vector 动态数组｜已验收
- 第 20 节｜std::array 与 std::span｜已验收
- 第 21 节｜迭代器与 STL 算法｜已验收
- 第 22 节｜关联容器｜已验收
- 第 23 节｜Lambda 表达式｜已实践｜复习：泛型Lambda、std::transform、引用捕获生命周期/悬空风险仍待专项练习；两道概念测验未提交。四项编程实验已通过，不阻止继续第24节。
  - 基础Lambda与count_if｜已通过｜平方25；偶数判断1/0；偶数个数3；大于30个数3。
  - 值捕获与引用捕获｜已通过｜threshold从30变40；Value count仍3，Reference count从3变1。
  - mutable内部状态｜已通过｜内部副本15→20；外部值保持10，引用捕获后外部15。
  - sort比较器与慢算子统计｜已通过｜模拟延迟排序MatMul38、Reduce25、Softmax25、Add12、ReLU8，慢算子数3；return控制流问答正确。
- 第 24 节｜阶段项目：数据处理工具｜已实践｜复习：本次仅有日报总体完成确认；需补存对应章节的逐实验输出以便复核，完成状态不等于新输出已补交。
  - 模拟算子平均延迟聚合｜已验收｜修正MatMul拼写后：Add 2/0.16，MatMul 2/1.74，ReLU 1/0.09，Softmax 2/0.70（count/模拟ms）。
  - map→vector→sort+Lambda排行榜｜汇总确认完成·输出待补｜尚无实际编译运行输出。

2026-11-03日报确认整节完成，但未补本实验实际输出；历史待运行说明保留作追溯。｜仅预期、尚未实测：预测顺序MatMul→Softmax→Add→ReLU，不能当作实验结果。
  - 慢算子阈值筛选｜汇总确认完成·输出待补｜实验2通过后再实施；无输出。

2026-11-03日报确认整节完成，但未补本实验实际输出；历史待运行说明保留作追溯。
- 第 25 节｜函数模板与类模板｜已实践｜复习：本次仅有日报总体完成确认；需补存对应章节的逐实验输出以便复核，完成状态不等于新输出已补交。
- 第 26 节｜Rule of Zero 与 RAII｜已实验通过｜复习：画出 nums → 按值形参 values → 成员 data：左值传入哪里复制，哪里移动？
不用提示解释：含 unique_ptr 的类为何可能不可复制但可移动？用户声明析构函数后要重新检查移动能力。
写出“复制整数资源”和“移动独占所有权”的对照，并检查地址与源对象状态。
  - vector默认复制与独立存储｜已验证（此前记录）｜Original first=10；Copied after set first=99；两个size均3。来源为日报明确引用的此前确认。
  - unique_ptr移动所有权｜已验收｜Before move=100；Moved value=100；Original has data=false；Moved has data=true。
  - 验证unique_ptr禁止复制｜已验收（预期编译失败）｜call to implicitly-deleted copy constructor of DataOwner；1 error generated。该编译错误为本实验预期结果。
  - 复制资源值以获得独立所有权｜已验收｜Original=100；Copied=100；修改后Original=100、Copied=200；Same address=false。
  - 难点：类的默认拷贝/移动能力取决于成员；“不用手写特殊成员”不代表“能复制”。还要分清复制指针、复制资源的值和转移所有权。
    判断方法：先问谁拥有资源，再看成员支持什么操作。vector 的复制产生独立元素；unique_ptr 禁止复制、允许移动。按值形参先接收自己的对象，再决定如何初始化成员。
    实际用途：算子工程中的输入和结果缓冲区、文件和资源句柄需要明确释放责任；优先让标准容器与资源包装类自动清理，减少错误路径上的泄漏或重复释放。
    后续练习（未验收）：后续实践：为 CPU 数据缓冲区写 RAII 包装，再为实际使用的昇腾资源 API 配置释放器。智能指针不会自动等待异步 GPU 工作完成，释放前仍需保证设备不再使用资源。
    复习：画出 nums → 按值形参 values → 成员 data：左值传入哪里复制，哪里移动？；不用提示解释：含 unique_ptr 的类为何可能不可复制但可移动？用户声明析构函数后要重新检查移动能力。；写出“复制整数资源”和“移动独占所有权”的对照，并检查地址与源对象状态。
    验证边界：4个实验完成；实验1沿用此前确认，实验3的预期编译失败属于验证通过。GPU资源包装仍未实现。
- 第 27 节｜智能指针全景｜已实验通过｜复习：逐行预测 shared_ptr 复制、作用域结束、weak_ptr::lock 后的 use_count 和析构时机。
重新画 A/B 循环引用：外部拥有者消失后为什么还活着？把哪一条边改成弱观察？
不用 expired() 后直接访问；用 if (auto p = weak.lock()) 分支处理失效对象。
  - 共享所有权与计数｜已验收｜Initial count1；Shared count2；Value through a200；After scope count1；Final value200。
  - weak_ptr与lock｜已验收｜Expired false；Value100；Count during lock2；Count after lock1；Expired after scope true；Resource released。
  - 循环引用与手动断环｜已验收｜A count2；B count2；A expired false；Destroy A；Destroy B；After break expired true。
  - weak_ptr反向观察避免环｜已验收｜A count1；B count2；Previous node =A；Destroy A；Destroy B；A expired true。
  - 难点：shared_ptr 对象、它管理的 Node 对象与控制块不是同一个东西；局部指针销毁后，对象仍可能被环中的其他拥有者保留。
    判断方法：独占用 unique_ptr，确有共享寿命需求再用 shared_ptr；观察关系用 weak_ptr。访问弱观察对象时检查 lock() 返回值；一次成功 lock 会暂时增加共享拥有者。
    实际用途：推理系统中多个请求可能共享只读模型/结果；回调或父子节点的反向关系可用弱观察避免所有权环。只借用对象的同步函数不必一律传 shared_ptr。
    后续练习（未验收）：后续实践：画“请求 → 任务 → 回调 → 请求”的所有权图，选一条观察边改为 weak_ptr；同时处理对象已释放的分支。shared_ptr 的引用计数机制不等于所指向数据自动线程安全。
    复习：逐行预测 shared_ptr 复制、作用域结束、weak_ptr::lock 后的 use_count 和析构时机。；重新画 A/B 循环引用：外部拥有者消失后为什么还活着？把哪一条边改成弱观察？；不用 expired() 后直接访问；用 if (auto p = weak.lock()) 分支处理失效对象。
    验证边界：4个实验有终端验证；析构输出证明本实验对象释放，不等同于完成内存分析工具或并发安全测试。
- 第 28 节｜移动语义进阶｜已实验通过｜复习：脱离答案，按五步写出下方四种调用的 T、形参、传出表达式与最终构造。
解释为什么 std::string&& value 中的 value 仍是左值表达式；哪些 T&& 才是转发引用？
const对象move仍待补；vector扩容与noexcept对照已在2026-11-04第29节实验5/6通过，独立解释继续巩固。
  - push_back与emplace_back构造对照｜已验收｜Copy A；Move A；Construct B/Move B；Construct C；Copy count1，Move count2，Data size4。reserve(4)控制扩容变量。
  - relay保留实参值类别｜已验收｜左值CANN：Without/With forward均Lvalue；临时Ascend：Without为Lvalue，With为Rvalue。使用默认a.out输出名运行成功。
  - vector插入四种转发路径｜已验收｜Construct A/Copy A；Construct B/Move B；Construct C/Copy C；Move C；Size4。四路径已经讲解，独立复述仍需巩固。
  - 难点：需要同时追踪实参值类别、T 的推导、形参引用折叠和函数体表达式类别。T&& 是形参声明的一部分；有名字的 value 作为表达式仍是左值。
    判断方法：调用处 → 推导 T → 折叠 T&& → 判断传出的表达式 → 重载/构造函数。move/forward 是转换；是否真的移动，由最终选中的操作决定。
    实际用途：算子与推理工程中的容器插入、任务队列和通用工厂要表达“保留原对象”还是“交出资源”，避免包装一层后意外复制大缓冲区；完美转发用于保留调用者的传参方式。
    后续练习（未验收）：后续实践：构建任务/缓冲区工厂，比较复制/移动次数，再用真实 Benchmark 判断收益。移动不是 Host→Device 搬运，emplace_back 也不是无条件更快。
    复习：脱离答案，按五步写出下方四种调用的 T、形参、传出表达式与最终构造。；解释为什么 std::string&& value 中的 value 仍是左值表达式；哪些 T&& 才是转发引用？；补做 const 对象 move、vector 扩容和 noexcept 对照；这些反例尚未验收。
    验证边界：3个实验与四路径讲解完成；用户曾明确反馈理解混乱，保留专项复习。计数实验采用 reserve 避免扩容干扰，不是性能加速证明。
- 第 29 节｜异常与资源安全｜已实验通过｜复习：复述异常传播、B→A析构、外层catch的先后关系；区分资源清理与外部状态回滚。
解释本机29-5/6为什么分别出现 Move A 与 Copy A，不把构造顺序当作所有标准库的保证。
在第32节失败更新实验中检查原配置完全不变，并审查提交操作的异常条件。
  - try/throw/catch｜已验收｜Start process: 10
Result = 20
Start process: -5
Caught exception: Negative value
Program continues
  - 异常栈展开与RAII｜已验收｜Program start
Acquire A
Acquire B
Start processing
Release B
Release A
Caught: Processing failed
Program end
  - 直接修改外部vector后的异常状态｜已验收｜Before: 10 20 30
Inside process: 10 20 30 40
Caught: Processing failed
After: 10 20 30 40
  - 副本修改与swap提交的失败路径｜已验收｜Before: 10 20 30
Temp: 10 20 30 40
Caught: Processing failed
After: 10 20 30
  - noexcept移动构造与扩容｜已验收｜---First insert---
Construct :A
Size = 1
Capacity = 1
---Second insert---
Construct :B
Move A
Size = 2
Capacity = 2
  - 移除noexcept后的扩容对照｜已验收｜---First insert---
Construct :A
Size = 1
Capacity = 1
---Second insert---
Construct :B
Copy A
Size = 2
Capacity = 2
  - 难点：异常会跨函数改变控制流；局部对象按逆序析构，但已经修改的外部状态不会自动回滚。noexcept 还会影响本例 vector 扩容时的拷贝/移动选择。
    判断方法：分开检查资源清理和状态保证。直接修改、临时副本、提交点分别画清；为 noexcept 提供真实保证，不能只为减少一次复制就添加。
    实际用途：缓冲区、文件、任务和配置更新需要在失败路径保持有效状态；大对象放入容器时，需要同时考虑移动成本与异常保证。
    后续练习（未验收）：第32节安全更新将用“副本修改 → 验证 → 安全提交”复用本节方法。GPU异步生命周期与CUDA专用释放器尚未实现。
    复习：复述异常传播、B→A析构、外层catch的先后关系；区分资源清理与外部状态回滚。；解释本机29-5/6为什么分别出现 Move A 与 Copy A，不把构造顺序当作所有标准库的保证。；在第32节失败更新实验中检查原配置完全不变，并审查提交操作的异常条件。
    验证边界：6/6编程实验通过。Acquire/Release是模拟资源日志；noexcept对照是Mac标准库上的实际观察，非GPU性能测量。
- 第 30 节｜constexpr 与程序组织｜已实验通过｜复习：末尾2道概念小测尚未提交，保留可选复习。
解释constexpr函数为什么能运行期调用；const运行期输入为何不能用于constexpr初始化。
画出源码 → 目标文件 → 可执行文件；区分声明、定义和链接。用户选择不加做Wall/Wextra额外实验。
  - constexpr函数与static_assert｜已验收｜Compile-time a = 25
Runtime b = 100
Static assert passed
  - int/const/constexpr对照｜已验收｜Result 1 = 49
Result 2 = 100
Result 3 = 400
  - const接收运行时输入｜已验收｜Enter a number : 10
a = 10
Result = 100
  - 故意触发constexpr编译错误｜已验收｜main.cpp:19:19: error: constexpr variable 'b' must be initialized by a constant expression
main.cpp:19:30: note: initializer of 'a' is not a constant expression
main.cpp:13:15: note: declared here
1 error generated.
预期编译失败=验证通过；完整诊断见章节原文。
  - 多文件链接失败与修复｜已验收｜Undefined symbols for architecture arm64:
  "square(int)", referenced from:
      _main in main-7a7479.o
ld: symbol(s) not found for architecture arm64
clang++: error: linker command failed with exit code 1 (use -v to see invocation)
修复：把math_utils.cpp加入编译/链接；实际输出Result = 25。
  - 分离编译与链接｜已验收｜-c main.cpp -o main.o；ls显示108K
-c math_utils.cpp -o math_utils.o；ls显示1.9K
clang++ main.o math_utils.o -o main
./main输出Result = 25
以上大小来自本次记录，不推断性能。
  - 难点：作用域、const和常量表达式容易混淆；头文件声明不等于实现已经链接，编译错误与链接错误发生在不同环节。
    判断方法：先判断值何时可得，再判断语境是否要求常量表达式；遇到构建失败，先区分编译器诊断和链接器缺符号，再核对输入文件。
    实际用途：为静态参数做编译期检查；搭建多文件工程，定位C++与后续CUDA联合构建中的缺少定义或目标文件问题。
    后续练习（未验收）：本日已用-c生成main.o/math_utils.o并链接；CMake仍是后续里程碑。目标文件大小与程序运行性能分别判断。
    复习：末尾2道概念小测尚未提交，保留可选复习。；解释constexpr函数为什么能运行期调用；const运行期输入为何不能用于constexpr初始化。；画出源码 → 目标文件 → 可执行文件；区分声明、定义和链接。用户选择不加做Wall/Wextra额外实验。
    验证边界：6/6编程实验通过；constexpr故意编译失败、缺少math_utils.cpp的链接失败与修复均有证据。概念小测未验收，CMake未实现。
- 第 31 节｜现代标准库类型｜已实验通过｜复习：末尾1道optional<double>概念小测尚未提交，保留可选复习。
区分optional无值、variant类型不符、any_cast不符；避免对空optional解引用。
复述Lambda与普通函数、using T与class、visit与if constexpr的区别。
  - optional查询｜已验收｜MatMul latency = 38ms
Unknown operator not found
  - optional取值与空值｜已验收｜A value_or = 38
B value_or = -1
A dereference = 38
A has value : true
B has value : false
  - variant类型切换｜已验收｜Int value = 256
Double value = 0.95
String value = GPU
  - variant活动类型与get｜已验收｜Current type: int / Value = 256
double / 0.95
string / GPU
Is int? false
  - visit与泛型Lambda｜已验收｜Value = 256
Value = 0.95
Value = GPU
  - if constexpr与类型别名｜已验收｜Block size = 256
Threshold = 0.95
Device = GPU
  - any与any_cast/reset｜已验收｜Int value = 256
String value = GPU
Has value = true
After reset = false
  - 难点：无值、活动类型和类型擦除是三类问题；visit按当前variant类型运行期派发，if constexpr按编译期条件选分支。using别名、class定义与模板class T也不同。
    判断方法：先明确接口允许哪些类型、是否允许无值，再选optional/variant/any；访问前核对有值与类型。Lambda的捕获和就地传递服务于接口组织，不推定更快。
    实际用途：为算子配置与任务参数建立明确的类型边界；用optional表达查不到，用variant约束候选值，避免把不存在或类型错误混为正常值。
    后续练习（未验收）：第32节已把unordered_map、optional与variant组合为配置查询；下一步补缺失键和类型不符的不同错误路径。any不是无需类型检查的万能容器。
    复习：末尾1道optional<double>概念小测尚未提交，保留可选复习。；区分optional无值、variant类型不符、any_cast不符；避免对空optional解引用。；复述Lambda与普通函数、using T与class、visit与if constexpr的区别。
    验证边界：7/7编程实验通过。MatMul38ms、GPU名称和阈值是手工模拟示例；概念小测没有作答记录。
- 第 32 节｜阶段项目：安全数据模块｜已实验通过｜复习：复述 optional → variant → visit 的调用顺序。
比较模拟异常与 bad_variant_access 两次失败后原配置的值。
区分字符串字面量、临时 std::string 和 const 引用。
  - 配置查询模块｜已验收｜block_size = 256
threshold = 0.95
device = GPU
unknown: Not found
  - 类型检查及安全修改｜已验收｜----Before----
block_size = 256
----Result----
Result1 = true
Result2 = false
Result3 = false
Result4 = false
----After modified----
New value:
block_size = 512
threshold = 0.95
  - Copy-and-Swap 与强异常安全｜已验收｜----Before----
block_size = 256
threshold = 0.95
-----First try-----
Caught : Simulate failure
----After true----
block_size = 256
threshold = 0.95
-----Second try-----
block_size = 512
threshold = 0.85
  - bad_variant_access 与原配置保护｜已验收｜-----Wrong type test-----
Temp block_size value changed to 1024
Caught type error : bad_variant_access
-----After type error-----
block_size = 512
threshold = 0.85
  - 难点：optional、variant、visit 分别处理有无结果、候选类型和实际取值。直接更新前要检查键、类型与取值，批量更新还要选定提交点。
    判断方法：读取时先检查 optional，再取出 variant 交给 visit。更新时先验证，再在副本上操作，通过后一次提交。
    实际用途：为算子和推理任务配置提供类型检查与安全更新，防止失败时留下部分修改。
    后续练习（未验收）：第33节已把配置模块拆分为头文件、实现文件与调用端。
    复习：复述 optional → variant → visit 的调用顺序。；比较模拟异常与 bad_variant_access 两次失败后原配置的值。；区分字符串字面量、临时 std::string 和 const 引用。
    验证边界：4项实验均有通过记录。实验1在11月4日完成，实验2–4在11月5日通过。
- 第 33 节｜头文件与多文件工程｜已实践｜复习：对照 std::string 按值与 const std::string& 两种签名。
说明只改实现文件与改公共头文件时，为什么重编译范围不同。
  - 头文件、实现与调用拆分｜已验收｜arm64 链接报错涉及 getConfig 和 updateIntConfig。对齐声明与定义的参数类型后成功编译。日报所列结果：初始 block_size = 128、threshold = 0.95、device = GPU。Update success = true。修改后 block_size = 512。未知键未找到。
  - pragma once 与 Include Guard｜已讲解，跳过实操｜已讲解两种头文件保护写法。用户要求跳过本实验并继续。
  - CMake 自动构建｜已验收｜cmake -S . -B build 和 cmake --build build 成功。分别编译 main.cpp.o 和 config.cpp.o，链接后 config_app 正常运行。
  - CMake 静态库｜已验收｜生成 libconfig_lib.a。构建日志出现 Built target config_lib 和 Built target config_app，程序正常运行。
  - 增量构建与依赖｜已验收｜无修改时两个目标直接显示 Built target。touch config.cpp 后只重编 config.cpp.o 并重链接。touch config.h 后两个 .o 都重编，再链接。
  - 难点：声明与定义的签名差异会影响链接。编辑器的语言标准提示、实际编译诊断、链接器的缺符号各有判断依据。
    判断方法：缺符号时同时核对源文件是否参与链接、声明与定义的参数是否一致。依据构建输出判断哪些目标重新编译。
    实际用途：拆分 C++ 算子测试和 CANN 工程，复用静态库，定位构建失败并减少无关文件的重编译。
    后续练习（未验收）：本次观察了 config.cpp 与 config.h 各自变化后的重编译范围。
    复习：对照 std::string 按值与 const std::string& 两种签名。；说明只改实现文件与改公共头文件时，为什么重编译范围不同。
    验证边界：多文件编译、CMake、静态库、增量构建四项通过。头文件保护已讲解，按用户要求跳过实操。
- 第 34 节｜CMake 工程化｜已实验通过｜复习：解释库的 PUBLIC include 与应用 PRIVATE 链接如何同时成立。
把 otool -L 的 @rpath 依赖与 LC_RPATH 的目录对应起来。
  - 工程目录与 PUBLIC 使用要求｜已验收｜include/config.h、src/config.cpp、app/main.cpp 分离，PUBLIC include 路径传给 config_app。配置、编译、运行通过。
  - PUBLIC 改 PRIVATE 的错误对照｜已验收｜[ 50%] Built target config_lib
[ 75%] Building CXX object .../app/main.cpp.o
fatal error: 'config.h' file not found
故意触发的缺头文件错误验证通过。之后恢复 PUBLIC。
  - SHARED 动态库｜已验收｜build/libconfig_lib.dylib，约 110 KB。程序正常运行。
  - otool -L 查看动态链接依赖｜已验收｜./build/config_app:
    @rpath/libconfig_lib.dylib (compatibility version 0.0.0, current version 0.0.0)
    /usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2100.43.0)
    /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1356.0.0)
  - LC_RPATH 与运行时搜索路径｜已验收｜cmd LC_RPATH
cmdsize 48
path [本地路径已省略] (offset 12)
Load command 17
家目录在此写作 ~。
  - 难点：include 路径的传播、目标链接依赖和程序运行时查找动态库分属不同环节。
    判断方法：先判断错误出在编译、链接还是运行。核对 PUBLIC/PRIVATE/INTERFACE 使用要求，再用 otool 查看依赖与 LC_RPATH。
    实际用途：组织 CANN 算子和推理后端的多目录工程，复用库并排查部署时的头文件、链接或缺库问题。
    后续练习（未验收）：本次验证 macOS 的 .dylib、@rpath 与 LC_RPATH。迁移到 Linux 的 CANN 环境时按实际系统检查库和搜索路径。
    复习：解释库的 PUBLIC include 与应用 PRIVATE 链接如何同时成立。；把 otool -L 的 @rpath 依赖与 LC_RPATH 的目录对应起来。
    验证边界：5项实验通过，包含 PUBLIC 改 PRIVATE 的故意失败对照。
- 第 35 节｜Debug 与 Release｜已讲解｜复习：回顾 -g、优化级别、NDEBUG 与 CMAKE_BUILD_TYPE 的作用。
  - Debug/Release 双构建与编译参数对照｜待实操｜已讲解并布置。工程目录、双构建、编译 flags 和两份可执行程序的输出均待用户实际操作确认。
  - 难点：CMAKE_BUILD_TYPE 是配置选择，编译器实际收到的 flags 要从构建记录核对。调试信息、优化与断言是不同属性。
    判断方法：确认工程目录，用同一份源码分别构建 Debug 和 Release，对比 flags 后运行两份程序。
    实际用途：为故障定位和性能测量准备各自可复现的构建配置。
    后续练习（未验收）：按第35节笔记执行实验1，保存两套构建和运行输出，再开展 assert 与 NDEBUG 对照。
    复习：回顾 -g、优化级别、NDEBUG 与 CMAKE_BUILD_TYPE 的作用。
    验证边界：本节已讲解。实验1已布置，目录创建、构建与运行结果待实操确认。
- 第 36 节｜Sanitizer 与内存错误定位｜未开始
- 第 37 节｜LLDB 进阶调试｜未开始
- 第 38 节｜单元测试与 CTest｜未开始
- 第 39 节｜Git 与项目文档｜未开始
- 第 40 节｜阶段项目：模块化工程｜未开始
- 第 41 节｜内存布局与对齐｜未开始
- 第 42 节｜CPU Cache 与数据布局｜未开始
- 第 43 节｜Benchmark 方法｜未开始
- 第 44 节｜Profiling 入门｜未开始
- 第 45 节｜编译优化与向量化｜未开始
- 第 46 节｜线程基础｜未开始
- 第 47 节｜同步与原子操作｜未开始
- 第 48 节｜毕业项目：CPU 算子优化｜未开始

## AI Infra全体系学习路线
AI Infra 工程师 · 以 CANN / Ascend C 算子开发与竞赛为专业主线，连接推理系统、可复现研究与实习。
沿用 48 节 C++ 课表。每次先完成当前实验，再做一道 C++ Hot 100 题或复做一道错题，建议留 20–40 分钟。
Linux 复习融入实际构建和排错，每天最多 1 小时。C++ 第 35–40 节期间可开始 CANN 社区入门，随后按算子验收进入赛题。
Ascend C 实践顺序为社区教程 → Add / Reduce 基线 → 往届赛题复现 → 天梯赛。设备与工具版本按题面核对，正式赛程以官方公告为准。
Jetson 两个项目归入历史。长期优先级为 2027 CANN 算子竞赛 → 可复现系统研究 → AI Infra 实习，软挑按时间选做。
规划版本：2026-11-06-cann-hot100-v1

## 设备与竞赛锚点
本地 CPU 参考与匹配的昇腾 NPU 环境
环境状态：
目标赛事：
正式提交截止T：待核实；报名截止不作为T
首次连接：
准备窗口：

###  Ascend C 算子实验库｜构想

MVP：
可选增强：
下一步：获得 NPU 环境后，建立基线、Profiling、优化和跨形状验证
仓库：
实际执行记录数：0
准备窗口：
计划启动：
预计体量：
实际首次执行日期：尚未开始
流程规则：

###  算子自动调优研究｜构想

MVP：
可选增强：
下一步：文献矩阵 → 研究问题 → 公平基线 → 消融 → 可复现实验 → 投稿
仓库：
实际执行记录数：0
准备窗口：
计划启动：
预计体量：
实际首次执行日期：尚未开始
流程规则：

## 学习与实践时间轴
- 2026.10 · 已有记录｜Linux 起步与环境搭建
  学习：保留 Shell、权限、路径、Git 与构建记录。之后结合本地工程和 CANN 远程开发复习。
  实践：继续 sed、默认参数和 source 的待实操清单，记录实际命令和输出。
  门槛：按原 Linux 笔记核对实验和遗留项。
  建议投入：每天最多 1 小时
- C++ 第 23–24 节 · 已有记录｜Lambda 与数据处理
  学习：第 23 节四项实验有实践记录。第 24 节保留已有完成记录与证据边界。
  实践：复用数据处理练习，为算法练习准备 STL 容器、Lambda 和排序。
  门槛：检查第 23 节捕获与第 24 节边界用例。
  建议投入：已有学习时长以打卡为准
- C++ 第 25–32 节 · 已有记录｜现代 C++ 与类型安全
  学习：模板、智能指针、异常安全与安全数据模块。
  实践：第 32 节 4 项实验已通过，保留配置查询、类型检查、Copy-and-Swap 和异常对照。
  门槛：原实验记录可回看，第 30–31 节概念小测待复习。
  建议投入：按疑问补练
- 当前 · C++ 第 35–40 节｜工程化 + Hot 100 + CANN 入门
  学习：接续第 35 节 Debug / Release 双构建，再学调试、测试与工程交付。每日用 C++ 做一道 Hot 100 题或复做错题。
  实践：先本地完成构建实验。有余力时读社区 NPU 基础和 Add 示例，确认 CANNLab 环境后运行样例。
  门槛：第 40 节按原课表验收。CANN 入门单独记录编译与参考输出对照。
  建议投入：C++ 为主，算法建议 20–40 分钟，CANN 入门按余力
- C++ 第 41–48 节 · Add 样例跑通后｜CPU 性能与 Ascend C 算子基线
  学习：Cache、Benchmark、并发与 CPU 算子。随 CANN 实验补 Python / NumPy、Tiling、UB 和尾块处理。
  实践：用 CPU 参考验证 NPU Add / Reduce，覆盖整块和非整除输入，输出同环境基准。
  门槛：C++ 毕业实验和 NPU 实践分别验收，记录代码、命令、环境与结果。
  建议投入：Hot 100 继续，先做精度与边界，再调性能
- 基础算子验收后 · 2027 赛程以公告为准｜往届赛题 → 天梯赛 → 正式备赛
  学习：先选一道往届或公开同类题，读规格，独立复现后再对照公开实现。
  实践：正确性基线 → Profiling → 单项优化 → 同环境复测 → 提交或复现报告。
  门槛：至少一道题有可复现结果，再按当期规则选天梯题。具体赛季、硬件和版本逐项核对。
  建议投入：CANN 优先，软挑按时间选做
- CANN 基线稳定后 · 非备赛冲刺期｜模型与推理引擎深化
  学习：Transformer、prefill / decode、KV Cache、vLLM、量化和系统调度。
  实践：先做小模型单路基线，再对比并发与端到端瓶颈，记录精度、吞吐与尾延迟。
  门槛：固定工作负载和测量口径，并有可复现的正确性与性能记录。
  建议投入：按项目和设备条件推进
- 单卡训练稳定且多卡资源可用后｜分布式训练与通信补全
  学习：从 DDP 推进到 FSDP / ZeRO 与 TP / PP，先理解通信机制，再测真实扩展性。
  实践：单卡梯度对照、通信时间线、多卡吞吐和扩展效率实验。
  门槛：分别记录机制验证、实机多卡结果和各自环境。
  建议投入：按资源安排
- 有可复现课题基线后｜课题项目 → 系统研究
  学习：结合雷达等实验室课题，固定任务质量与数据划分，定位动态 shape、流式窗口或调度瓶颈。
  实践：形成公平基线、明确假设、对照和消融，整理复现材料与论文稿。
  门槛：由实验结果决定研究问题和投稿时机。
  建议投入：按课题与可用环境推进
- 有可复现交付后 · 2027 滚动准备｜作品集与 AI Infra 实习
  学习：用 Hot 100、C++ 工程和 CANN 实验组织面试复习，讲清每项测量与优化依据。
  实践：整理 C++ 工程、算子练习或赛题复现的代码与报告，按岗位投递和复盘。
  门槛：简历中的结果与个人贡献可通过实际记录核对。
  建议投入：与长期研究交错推进

### Linux 与开发环境｜共同基础 · 持续复习

#### L01 文件、文本与 Shell 管道
前置：无；已有入门记录
验收：独立定位日志并统计；覆盖空输入、无匹配和缺失文件；保留命令与输出。
- 文件系统、路径与查找｜已实践
  学习范围：根目录/家目录与绝对相对路径；pwd / ls / cd / mkdir；cp / mv / rm；find 与文件匹配；当前目录与脚本目录
- grep / 管道 / 重定向｜已验收｜★重点
  学习范围：grep -n 与大小写匹配；管道连接命令；wc -l 计数；> 覆盖与 >> 追加；stdout / stderr 区分
- sed / awk 与文本处理｜待复习
  学习范围：sed 替换与 errror 拼写修正；awk 字段与聚合；正则与边界情况；修改前备份与复测

#### L02 可靠脚本与环境变量
前置：L01
验收：check_log.sh 在不同工作目录运行；验证默认参数、文件名报错、退出码与 source 的差异。
- 分支、循环、函数与参数｜已实践｜★重点
  学习范围：if / case / for / while；函数与 return / exit；$0 / $1 / $# / shift；日志检查三分支；默认参数与错误消息
- PATH / source / Bash 路径｜待复习｜★重点｜▲难点
  学习范围：PATH / export / .bashrc；command -v；source 与子进程；BASH_SOURCE[0] / dirname / realpath；$(命令) 与带空格路径
- 权限、执行方式与退出状态｜已实践
  学习范围：rwx 与 755 / 644 / 600；chmod 与可执行位；bash script.sh / ./script.sh；Shebang 固定路径与 env；退出码与权限错误

#### L03 进程、网络与系统排错
前置：L01–L02
验收：完成一个 CPU/内存/网络排错案例，说明证据如何支持结论；不随意重启核心服务。
- 进程、信号与资源监控｜有笔记｜★重点
  学习范围：ps / top / htop；PID 与父子进程；kill / 信号；前后台任务；CPU / 内存 / 磁盘资源
- IP / DNS / 端口与连接排查｜有笔记
  学习范围：ip addr / route；ping / curl；DNS解析；ss 与监听端口；连接超时和服务排查
- APT / systemd / journalctl｜已实践
  学习范围：apt update / upgrade / install；软件源与包状态；systemctl status；loaded / active / enabled / static；journalctl 与日志轮转

#### L04 远程环境与工程工具
前置：L02–L03；C++33–40 配合
验收：远程建立可恢复会话；用 Git+CMake+调试器构建并排查一个多文件 C++ 项目。
- SSH 密钥、远程开发与 tmux｜已实践｜★重点
  学习范围：ssh -V / ssh-keygen；Ed25519公私钥与权限；authorized_keys与真实连接；scp / rsync基础；tmux 创建/分离/恢复
- Git 分支、提交与冲突处理｜有笔记
  学习范围：init / status / add / commit；diff / log；分支与合并；冲突处理；.gitignore 与远程协作
- 编译 / CMake / GDB 或 LLDB｜已实践｜★重点
  学习范围：编译、链接与可执行文件；Make / CMake；Debug / Release；GDB / LLDB断点与栈；跨目录构建与小项目

### C++ 与 CPU 工程｜当前主线 · 原 48 节

#### C01 语法、生命周期与所有权
前置：既有第1–14节
验收：通过值/引用、深拷贝、移动赋值、自移动与析构实验；保留第14节 Rule of Zero 复习项。
- 编译、类型、函数与引用｜已实践｜★重点
  学习范围：clang与C++20；变量与类型；值传递/引用传递；const与作用域；函数接口
- 指针、类、RAII 与智能指针入门｜已实践｜★重点｜▲难点
  学习范围：地址、数组与指针；动态内存与悬空问题；构造/析构；初始化列表；RAII与资源所有权
- 拷贝 / 移动与五法则｜已实践｜★重点｜▲难点
  学习范围：拷贝构造/拷贝赋值；浅拷贝与深拷贝；std::move语义；移动构造/移动赋值；self-move与五法则

#### C02 标准库、容器与数据处理
前置：C01；原15–24节
验收：交付第24节数据处理工具；测试空输入、越界风险与失效迭代器，不访问已失效对象。
- 类型、参数与 const 复核｜已实践
  学习范围：函数参数与返回值；重载与类型；const正确性；引用生命周期；统计与整数除法
- string / vector / array / span / 迭代器｜已验收｜★重点｜▲难点
  学习范围：string与string_view；vector的size/capacity/reserve；array与span；迭代器失效；sort / find / accumulate
- 关联容器、Lambda 与阶段项目｜已实践｜★重点
  学习范围：map / unordered_map / set；词频统计与复杂度；Lambda与捕获；STL组合；第24节数据处理工具

#### C03 泛型与现代 C++
前置：C02；原25–32节
验收：安全数据模块通过拷贝/移动/异常边界测试；解释 unique_ptr、shared_ptr 与 Rule of Zero 的取舍。
- 模板、constexpr 与标准库类型｜已实践｜▲难点
  学习范围：函数/类模板；类型推导与约束入门；constexpr；optional / variant等类型；程序组织
- Rule of Zero、智能指针与移动进阶｜已实践｜★重点｜▲难点
  学习范围：unique_ptr / shared_ptr / weak_ptr；Rule of Zero；值语义与所有权；移动语义进阶；循环引用
- 异常安全与安全数据模块｜已实践｜★重点
  学习范围：异常传播；基本/强异常保证；RAII清理；边界测试；安全数据模块

#### C04 构建、调试与测试工程
前置：C03；原33–40节
验收：多文件工程可从干净目录构建；CTest 通过；用 Sanitizer/调试器定位一个真实错误。
- 头文件、CMake、Debug / Release｜进行中｜★重点
  学习范围：头文件与编译单元；链接与ODR；CMake target；Debug/Release编译选项；多文件工程
- Sanitizer、LLDB 与单元测试｜未开始｜★重点
  学习范围：LLDB断点/观察/调用栈；AddressSanitizer / UBSan；内存错误定位；单元测试；CTest
- Git、文档与模块化项目｜未开始
  学习范围：Git提交与版本；README与使用例；模块化接口；干净环境构建；工程阶段验收

#### C05 性能、并发与 CPU 算子
前置：C04；原41–48节
验收：CPU 算子有正确性测试、预热/重复测量、基线与优化对照，解释缓存、向量化或同步瓶颈。
- 内存布局、对齐与 CPU Cache｜未开始｜★重点｜▲难点
  学习范围：sizeof / alignof / padding；连续与离散布局；缓存行与局部性；AoS / SoA；带宽与访存模式
- Benchmark、Profiling 与向量化｜未开始｜★重点｜▲难点
  学习范围：预热与重复测量；单调时钟与基线；Profiling与热点；编译优化；自动向量化
- 线程、同步、原子与毕业项目｜未开始｜★重点｜▲难点
  学习范围：thread / jthread；mutex与条件变量；数据竞争；atomic与内存序入门；CPU算子毕业项目

### Python 与张量编程｜下一阶段 · 模型桥梁

#### P01 Python 工程基础
前置：C++基础；不用等待语言细节全部精通
验收：交付带 CLI、配置和测试的数据处理包；固定依赖与随机种子。
- 容器、函数、迭代与异常｜未开始｜★重点
  学习范围：list / dict / set；函数/类/迭代器；生成器与上下文管理；异常；类型提示
- 模块、虚拟环境、依赖与 pytest｜未开始
  学习范围：venv与依赖固定；模块/包/导入；argparse；pytest；代码布局与配置
- 文件 / JSON / 数据管线与可视化｜未开始
  学习范围：文件与JSON/CSV；NumPy数据转换；批处理管线；Matplotlib可视化；日志与实验配置

#### P02 NumPy 与数值验证
前置：P01；线性代数同步补
验收：用 NumPy 建立 Add/Reduce/Matmul 参考；覆盖广播、非连续布局与浮点误差。
- shape、stride、广播与向量化｜未开始｜★重点｜▲难点
  学习范围：shape / axis / dtype；stride与连续性；广播规则；切片/视图/复制；向量化与归约
- FP32/FP16、误差与稳定性｜未开始｜★重点｜▲难点
  学习范围：浮点舍入；绝对/相对误差；FP32 / FP16 / BF16；数值稳定Softmax；容差与随机参考测试
- 基准脚本、统计与实验数据存档｜未开始
  学习范围：预热、同步与计时；重复次数与分位数；shape/dtype测试矩阵；结果CSV/JSON；可复现实验脚本

#### P03 PyTorch 训练与扩展接口
前置：P02；M01–M02 配合
验收：训练一个小模型并保存/恢复；对照 autograd 与手推结果，正确计时异步设备。
- Tensor、device、autograd 与 nn.Module｜未开始｜★重点
  学习范围：Tensor与device；requires_grad与计算图；autograd；nn.Module / Parameter；train / eval / no_grad
- DataLoader、优化器与训练循环｜未开始｜★重点
  学习范围：Dataset / DataLoader；loss与optimizer；训练/验证划分；checkpoint；随机种子与恢复
- Profiler、扩展算子接口与编译入门｜未开始｜▲难点
  学习范围：PyTorch Profiler；CPU/设备trace；自定义算子接口；torch.compile概念；扩展正确性检查

### 计算机系统与平台｜贯穿全程 · 用实验补齐

#### S01 操作系统与内存层次
前置：Linux基础；C++资源管理
验收：用进程/线程、缺页与缓存实验说明时间和内存变化，区分虚拟内存与显存。
- 进程线程、调度、锁与 IO｜未开始｜★重点｜▲难点
  学习范围：进程/线程与上下文切换；调度；阻塞/非阻塞IO；锁与并发；系统调用
- 虚拟内存、页表、mmap 与 NUMA｜未开始｜▲难点
  学习范围：虚拟地址与页表；缺页；mmap；内存分配；NUMA与数据放置
- Cache、SIMD、带宽与 Roofline｜未开始｜★重点｜▲难点
  学习范围：多级Cache与局部性；SIMD；内存带宽；算术强度；Roofline模型

#### S02 异构架构与通信基础
前置：S01；数值与矩阵运算
验收：画出 CPU↔GPU/NPU 数据流；测量拷贝/计算开销；解释拓扑与集合通信成本。
- GPU/NPU 执行与存储层级｜未开始｜★重点｜▲难点
  学习范围：Host / Device；GPU线程/块与NPU AI Core；寄存器/本地/全局存储；异步搬运；计算单元与同步
- TCP、RPC、RDMA 与带宽/时延｜未开始｜▲难点
  学习范围：TCP连接；RPC与序列化；带宽与往返延迟；RDMA概念；设备互联与拓扑
- 并行分解、同步与通信成本｜未开始｜★重点
  学习范围：数据/任务分解；负载均衡；同步成本；Amdahl定律；通信与计算重叠

#### S03 编译图与系统工程
前置：C++工程；PyTorch前向
验收：导出小模型计算图，比较图优化前后正确性和耗时；解释动态 shape 引起的变化。
- 编译链接、IR 与计算图｜未开始｜▲难点
  学习范围：预处理/编译/链接；中间表示IR；计算图；静态/动态shape；编译缓存
- 融合、调度、内存规划与动态 shape｜未开始｜★重点｜▲难点
  学习范围：常量折叠；算子融合；执行调度；内存复用；动态shape特化
- Runtime、异步执行与内存分配器｜未开始｜▲难点
  学习范围：异步执行队列；执行依赖；内存池；启动开销；Host/Device同步点

#### S04 部署平台与可观测性
前置：Linux网络；Python工程
验收：容器化服务可复现启动；采集日志、延迟、资源曲线并做一次故障定位。
- Docker、依赖隔离与镜像｜未开始｜★重点
  学习范围：Dockerfile；镜像与容器；卷/网络/设备映射；依赖固定；复现与资源限制
- Kubernetes / GPU调度基础与任务队列｜未开始
  学习范围：Kubernetes基本对象；GPU/NPU资源调度概念；任务队列；配额与优先级；弹性扩缩容
- 日志、Metrics、Trace 与服务可靠性｜未开始｜★重点
  学习范围：结构化日志；Metrics；Trace与热点；错误率与SLO；一次故障复盘

### 深度学习与大模型｜必要模型理解 · 与算子对应

#### M01 数学、自动微分与训练基础
前置：P01–P02
验收：手推并数值检验一个层的梯度；解释损失、过拟合与训练/验证划分。
- 矩阵、概率、链式法则与数值误差｜未开始｜★重点
  学习范围：矩阵乘与张量维度；概率与期望；导数与链式法则；梯度检验；数值误差
- MLP/CNN、反向传播与优化器｜未开始｜★重点
  学习范围：MLP / CNN；前向与反向；损失函数；SGD / Adam；过拟合与泛化
- 训练稳定性、混合精度与评估｜未开始｜▲难点
  学习范围：数据划分与泄漏；归一化；混合精度/损失缩放；训练稳定性；验证与测试指标

#### M02 Transformer 的张量视角
前置：M01；P03
验收：实现小型多头 Attention / Transformer block；逐层标注 shape、FLOPs、激活与权重内存。
- QKV、Attention、Mask 与 Softmax｜未开始｜★重点｜▲难点
  学习范围：Q/K/V投影；缩放点积；因果Mask；多头Attention；Softmax稳定性
- Norm、FFN、位置编码与残差｜未开始｜★重点
  学习范围：LayerNorm / RMSNorm；FFN / 激活；残差连接；位置编码 / RoPE概念；Transformer block
- 算量、显存、序列长度与瓶颈｜未开始｜★重点｜▲难点
  学习范围：FLOPs与参数量；激活/权重内存；序列长度影响；Attention复杂度；计算受限/访存受限

#### M03 LLM 训练与推理机制
前置：M02；小规模模型可运行
验收：比较 prefill/decode；估算并实测 KV Cache；理解小规模微调与 MoE 路由，不追求训练大模型。
- Tokenizer、自回归、KV Cache 与解码｜未开始｜★重点｜▲难点
  学习范围：Tokenizer；自回归生成；prefill / decode；KV Cache容量；采样与停止条件
- SFT、LoRA、量化/蒸馏基础｜未开始
  学习范围：SFT与数据；LoRA/参数高效微调；PTQ/QAT概念；蒸馏；质量回归与资源取舍
- MoE、稀疏与多模态工作负载｜未开始｜▲难点
  学习范围：专家与路由；负载不均衡；稀疏计算；多模态输入；专家通信开销

### Ascend C 与算子优化｜近期专业主修 · CANN

#### K01 Ascend 编程模型与基础算子
前置：C++ 资源管理与工程构建基础，第 35–40 节期间可入门，按需补 P02 与 S01–S02
验收：核对 NPU 和 CANN 版本，运行社区 Add 样例，保存与 CPU 或 NumPy 参考的对照。
- Host/Device、AI Core 与内存模型｜未开始｜★重点｜▲难点
  学习范围：Host Tiling / Device Kernel；AI Core架构；Vector / Cube；GM与Local Memory；版本与工具链
- Tensor、CopyIn/Compute/CopyOut 与同步｜未开始｜★重点｜▲难点
  学习范围：GlobalTensor / LocalTensor；TPipe / TQue / TBuf；CopyIn/Compute/CopyOut；缓冲分配；同步与依赖
- shape/dtype、边界与精度测试｜未开始｜★重点
  学习范围：参考实现；随机/边界shape；dtype与溢出；误差容限；空/小/非整除场景

#### K02 Tiling 与并行搬运
前置：K01 的 Add 基线通过
验收：对 Add / Reduce 实现多核和核内切分，覆盖尾块、对齐、UB 容量与非整除 shape。
- Host Tiling、多核划分与负载均衡｜未开始｜★重点｜▲难点
  学习范围：TilingData与参数；多核分块；核内切分；shape分支；负载均衡
- 尾块、对齐、UB容量与内存复用｜未开始｜★重点｜▲难点
  学习范围：地址与搬运对齐；尾核/尾块；UB容量预算；内存复用；边界保护
- 流水、DoubleBuffer 与同步消融｜未开始｜★重点｜▲难点
  学习范围：计算与搬运流水；DoubleBuffer；同步与事件；流水空泡；优化消融

#### K03 模型高频算子与优化方法
前置：K02；M02
验收：从 Reduce→Softmax/LayerNorm→Matmul 递进；选1–2类深入，报告多 shape/dtype 精度和真实性能。
- 归约、Softmax 与 LayerNorm｜未开始｜★重点｜▲难点
  学习范围：归约切分；Softmax稳定性；LayerNorm统计；小/大shape策略；精度与带宽
- GEMM / Cube / 矩阵分块｜未开始｜★重点｜▲难点
  学习范围：矩阵分块；Cube计算；矩阵布局；复用与搬运；不同M/N/K形状
- 融合、Attention 与自动调优｜未开始｜▲难点
  学习范围：融合边界与收益；Attention数据流；特定shape优化；搜索空间；自动调优与泛化

#### K04 Profiling、赛题复现与工程接入
前置：K02，框架接入补 S03 / P03
验收：在匹配的 NPU 环境复现一道往届题，提供正确性、msprof 记录与优化前后对照，再进入天梯赛。
- msprof、瓶颈与公平 Benchmark｜未开始｜★重点｜▲难点
  学习范围：CPU孪生精度调试；NPU上板；msprof trace；瓶颈假设；基线/多次测量/加速比
- 算子包、aclnn 与 PyTorch 适配｜未开始｜★重点
  学习范围：算子原型与shape推导；算子编译/部署；aclnn调用；PyTorch适配；CI与回归矩阵
- 不同 NPU 与 CANN 版本的移植验证｜未开始｜▲难点
  学习范围：NPU 型号与 CANN 版本；算子支持范围；同规格精度回归；基准不可跨环境直接比较

### 推理引擎与服务优化｜专业拓展 · 从算子到系统

#### I01 模型执行与端到端基线
前置：P03；M02–M03；S03
验收：部署一个可运行模型；区分冷启动、预热、稳态；定位预处理、模型与后处理热点。
- 加载、图执行、导出与后端适配｜未开始｜★重点
  学习范围：模型加载；导出/编译；执行后端；冷启动与稳态；预处理/前向/后处理
- KV Cache、显存预算与分页管理｜未开始｜★重点｜▲难点
  学习范围：KV Cache容量估算；分页管理；碎片与复用；长上下文；显存预算
- 吞吐、TTFT、TPOT、p95与显存｜未开始｜★重点
  学习范围：吞吐tokens/s与requests/s；TTFT；TPOT / ITL；p50/p95/p99；峰值显存与失败率

#### I02 调度、精度与服务优化
前置：I01；Kernel基础
验收：逐项比较 batch、序列长度与并发；在相同质量约束下比较量化、调度及内存策略。
- Continuous Batching / Chunked Prefill｜未开始｜★重点｜▲难点
  学习范围：连续批处理；Chunked Prefill；队列与调度；延迟/吞吐取舍；混合请求负载
- PTQ/QAT、KV压缩与精度回归｜未开始｜▲难点
  学习范围：PTQ / QAT；权重/激活量化；KV压缩；校准数据；质量与性能回归
- 投机解码、前缀缓存与图优化｜未开始｜▲难点
  学习范围：投机解码；接受率与额外计算；前缀缓存；计算图优化；不同负载收益

#### I03 引擎阅读、扩展与在线可靠性
前置：I01–I02；Linux网络/容器
验收：选 vLLM 或同类引擎追踪一次请求；交付扩展/修复、压测报告与失败率、尾延迟分析。
- vLLM请求路径、Runtime 与扩展点｜未开始｜★重点｜▲难点
  学习范围：请求入口→调度→执行；KV管理；后端与算子扩展点；阅读调用链；最小修复/扩展
- TP/PP、PD分离、路由与伸缩｜未开始｜▲难点
  学习范围：张量/流水并行；Prefill/Decode分离；KV跨节点传输；请求路由；资源扩缩容
- API、限流、队列、压测与可观测性｜未开始｜★重点
  学习范围：API与流式返回；限流与队列；负载生成；质量约束；可观测性和尾延迟

### 分布式训练与通信｜后续拓展 · 正确性先行

#### D01 从单卡到 DDP
前置：单卡训练稳定；S02通信基础
验收：验证梯度与单卡参考一致；解释 rank/world size、采样器和通信顺序；记录一轮 trace。
- AllReduce / AllGather / ReduceScatter｜未开始｜★重点｜▲难点
  学习范围：Broadcast；AllReduce；AllGather；ReduceScatter；Ring/树与通信成本
- torchrun、DDP、梯度同步与数据划分｜未开始｜★重点
  学习范围：rank / world_size；torchrun；进程组与梯度同步；DistributedSampler；全局batch与随机性
- 死锁、超时、随机种子与数值一致性｜未开始｜▲难点
  学习范围：通信顺序一致性；梯度与单卡对照；超时/死锁；数据重复；数值误差与复现

#### D02 状态切分与混合并行
前置：D01；M03；显存预算
验收：比较 DDP 与 FSDP/ZeRO 的状态占用；理解 TP/PP；用真实资源验证吞吐/显存取舍。
- FSDP / ZeRO 与检查点｜未开始｜★重点｜▲难点
  学习范围：参数/梯度/优化器状态；ZeRO分阶段；FSDP切分；峰值显存；检查点格式
- Tensor / Pipeline / Expert Parallel｜未开始｜▲难点
  学习范围：Tensor Parallel；Pipeline Parallel；Expert Parallel；混合并行布局；流水气泡
- 拓扑、NCCL/HCCL 与通信计算重叠｜未开始｜★重点｜▲难点
  学习范围：NCCL / HCCL；设备与网络拓扑；bucket与调度；计算通信重叠；trace与瓶颈

#### D03 训练系统实验与容错
前置：D02；平台可观测性
验收：报告固定工作负载的扩展效率、吞吐、显存和通信占比；验证恢复训练与数据加载瓶颈。
- 多机调度、扩展效率与资源利用率｜未开始｜★重点
  学习范围：单机/多机资源；弱/强扩展；吞吐与扩展效率；设备利用率；调度和成本
- 断点恢复、故障定位与训练稳定性｜未开始
  学习范围：保存/恢复状态；随机数与数据位置；故障注入；恢复一致性；稳定性排查
- 分布式数据管线与 IO 优化｜未开始
  学习范围：数据分片；预取与缓存；CPU解码/预处理；存储IO；输入管线与设备空转

### 项目、竞赛与研究实习｜贯穿全程 · 产出闭环

#### E01 工程交付与实验可信度
前置：从第24节项目开始持续执行
验收：仓库含测试、依赖、环境、运行命令与结果；实验有基线、预热、重复测量、误差与局限。
- Hot 100 · 数据结构与算法复杂度｜未开始｜★重点
  学习范围：Hot 100 哈希与双指针；滑动窗口和前缀和；链表、树与图；回溯、二分与动态规划；复杂度、边界用例与复做
- Git/CI、代码审查、文档与测试｜未开始｜★重点
  学习范围：测试与边界；CI自动构建；代码审查；依赖/版本固定；README与运行命令
- 实验设计、统计、消融与复现｜未开始｜★重点｜▲难点
  学习范围：公平基线；控制变量；预热/重复测量；置信与波动；消融、失败案例与复现

#### E02 CANN 往届赛题、天梯赛与软挑支线
前置：K01–K02 验收后从同类赛题复现起步
验收：记录 CANN 正确性与性能迭代。按主线进度安排天梯赛与正式备赛，软挑按时间选做。
- 2027 CANN/Ascend 算子竞赛备赛｜未开始｜★重点
  学习范围：CANNJudge 开放题库；往届题独立复现；天梯赛泛化要求；硬件与 CANN 版本；正确性回归与性能对照
- 2027 软件精英挑战赛（可选）｜未开始
  学习范围：算法与数据结构；限时工程实现；启发式与调参；性能评测；主线投入上限
- 开源阅读、Issue/PR 与技术表达｜未开始
  学习范围：阅读开源仓库；最小可复现问题；测试/文档贡献；Issue与PR规范；技术说明

#### E03 雷达课题到系统研究
前置：课题基线可复现；模型与性能基础
验收：固定数据划分与算法质量，测量雷达预处理→骨骼/生命体征模型→后处理；寻找可推广系统问题。
- 骨骼/HR/RR模型基线与质量指标｜未开始｜★重点
  学习范围：雷达预处理与数据划分；骨骼模型复现；HR/RR参考与窗口；精度指标；可复现基线
- 流式窗口、动态shape与实时推理｜未开始｜★重点｜▲难点
  学习范围：预处理→模型→后处理时延；流式窗口；动态shape；内存/融合/调度策略；精度约束下系统收益
- 相关工作、创新假设、对照与论文写作｜未开始｜▲难点
  学习范围：相关工作矩阵；可推广研究问题；创新假设；公平对照与消融；局限、代码与论文稿

#### E04 实习准备与岗位查缺
前置：有可复现的 C++ 工程和 CANN 实验，能解释优化依据
验收：按目标JD整理技能证据；完成项目讲解与系统/编程模拟面试，再开始滚动申请。
- 项目简历、性能报告与作品集｜未开始｜★重点
  学习范围：两个可复现项目；优化前后证据；个人贡献；性能报告；项目简历与讲解
- C++/系统/算法/模型面试查缺｜未开始
  学习范围：C++与内存；系统/并发/网络；算法练习；模型/算子数据流；模拟面试与查缺
- AI Infra/异构计算实习申请与复盘｜未开始
  学习范围：匹配JD与技能证据；实习时间与岗位筛选；申请记录；面试复盘；按反馈调整学习

## 使用规则
只以网站已保存的学习摘要为来源；不推测时长或补写实验。读取失败时应明确告知用户，不能把历史缓存视为最新进度。原始笔记、身份、凭据和私密文件不在本镜像中。
