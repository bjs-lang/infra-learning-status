# 学习进度只读镜像

数据版本：80
网站最后保存：2026-11-19T13:45:52.475000Z
本次同步：2026-11-20T12:46:48.373852Z
最近学习：2026-11-19

每次使用请检查同步时间和 GitHub Actions 最近一次运行结果；文件可读取不代表同步服务始终正常。

## 当前 C++ 起点
48 节已全部记录为完成，请复盘。

## 已验证与记录边界
2026-11-19 · Atlas 200I DK A2 从存储卡启动，根分区剩余约 36 GiB。确认 NVMe SSD 尚未挂载，CANN Toolkit 为 7.0.RC1，Ascend 310B1 健康状态为 OK。ResNet50 识别 Standard Poodle 的最高概率为 0.9355。
llamafile 0.10.6 在 Atlas CPU 上运行 Qwen3.5‑2B Q4_K_M。通过 Mac 上的浏览器完成两轮中文文字对话，第二轮复述了第一轮给出的名字。首轮回复面板显示 16 tokens、4.7 秒、约 3.42 tokens/s。
2026-11-19 · 已首次进入 Atlas 200I DK A2 的 Linux 终端。fdisk -l 列出 mmcblk1（58.42 GiB，GPT，三个分区）和 nvme0n1（Great Wall GW3500 256GB，238.47 GiB）。
11 月 18 日 · MacBook Air 内置麦克风录得 10.00 秒单声道 Int16 音频，48,000 Hz，数组形状为 (480000, 1)。用 afplay 回放原文件，可以听见。afinfo 显示转换后的 WAV 为 16,000 Hz、单声道、Int16，仍为 10.00 秒，共 160,000 个采样帧，音频数据占 320,000 字节。
CANN-01 固定规格 Add 已验证跨核边界。下标 2047 的输出和 golden 均为 4.5，下标 2048 均为 5.5，程序报告整组精度校验通过。

11 月 15 日完成 DS04 栈双语练习（#20、#155、#739）。用户反馈 #739 的 Python 单调栈提交约 100 ms，击败 40%。

11 月 14 日完成 Python 基础第 1 课与 DS04 单调队列双语练习。Hot 100 #239 的 Python 和 C++ 版本均通过 5 组本地断言，终端输出 Python PASS 和 C++ PASS。

11 月 13 日 C++ 第 45–48 节已验收。CPU Add 校验通过，双线程求和、同步计数与矩阵乘法对照通过。毕业项目从提交 e97b459 干净克隆，两种构建均通过小矩阵与六轮逐元素校验。Hot 100 #239 已编码。

11 月 12 日 C++ 第 41–44 节已验收。完成布局和 AoS/SoA 对照、多轮基准、macOS 采样与填充改写验证。第 45 节已讲解。

11 月 10 日续学，#15 三数之和、#42 接雨水均有本人代码。修正版经助手本地 UBSan 和随机对拍通过，平台结果待补录。

11 月 9 日，C++ 第 36–40 节已验收。Sanitizer 三项修复复测通过，LLDB 定位累加逻辑，CTest 十个用例通过，模块化工程干净克隆复现。第 35 节双构建与断言实验在 11 月 8 日完成。

11 月 10 日，Hot 100 #438 已编码，用户确认 UBSan 报错解决。讨论 differ、missing 和同算法的计数容器对照，平台验收待补录。

2026-11-06 在 CANN 社区 Notebook 跑通固定规格 Add（float，8 × 2048，8 核），程序报告精度校验通过。泛化 Add 的独立实现和性能基线待验证。
C++ 第32–34节结课，累计34/48（70.8%），剩余14节。11月5日新验收12项实验：第32节3项、第33节4项、第34节5项。第33节实验2已讲解，按用户要求跳过实操。第35节已讲解，实验1待实操。
11-05 结课。11-04 已通过配置查询。11-05 验收实验2–4：合法更新为512，类型不符、缺键、负数均拒绝。模拟异常保持256/0.95，成功提交后为512/0.85。错误get<int>触发bad_variant_access，原配置保持512/0.85。
多文件编译、CMake、静态库、增量构建四项通过。对齐声明和定义的参数类型后解决arm64链接报错，IntelliSense改为C++20后红线消失。实验2头文件保护已讲解，用户跳过实操。
五项通过：规范目录与PUBLIC使用要求。故意改PRIVATE复现config.h缺失。生成约110KB的dylib。otool -L显示@rpath/libconfig_lib.dylib。otool -l显示LC_RPATH指向build目录。
已讲解Debug/Release、-g、-O0/-O2/-O3、NDEBUG和CMAKE_BUILD_TYPE。实验1已布置，待确认目录和源码后进行两套构建，尚缺实际输出。
此前验证：
2026-11-04新增验证：2026-11-04：C++第29–31节编程实验通过，主线31/48（64.6%）；第32节进行中，实验1配置查询通过。今日20项实验有运行/编译证据（6+6+7+1），包含预期失败和修复验证。第30节2道、第31节1道概念小测未提交。实际时长未提供；Jetson/CUDA没有新增实机实验。
6/6编程实验通过。异常捕获后继续运行；栈展开按B→A析构（模拟资源日志）；直接修改后保留40，临时副本失败则原值10/20/30不变；本机vector扩容有noexcept时Move A、去掉后Copy A。非GPU实验。
6/6编程实验通过。constexpr与static_assert、int/const/constexpr、运行期输入10→100；constexpr常量表达式故意编译失败为验证成功；多文件缺实现链接失败后修复输出25；-c目标文件108K/1.9K，链接运行输出25。末

## 疑问与薄弱点
待在 Mac 上确认 Vivian 试听、中文识别和语音对话的完整运行结果，并测量停口到首声的实际延迟。
中文语音识别待实测。外接 USB 声卡的录放待验证。
待复习 #155 的最小值恢复和 #739 的同温、多次弹栈。#20 与 #155 的平台成绩待补录，#739 跳跃版待提交验证。
Hot 100 #239 本地复测结束，力扣提交结果待补录。
第 48 节向量化报告与计时已留档，访存与计算各自的收益可继续分析。
第 44 节两种填充写法具体生成的优化指令待用报告或汇编核对。
复做 #15 的两级去重和 #42 的最高柱分界，记录边界用例与平台结果。
#3 与 #438 需独立复做并保存用例和提交结果。
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
下次在 Mac 重开两个终端。先启动 Atlas 对话服务和 SSH 隧道，再试听新版脚本的 Vivian 音色。试听通过后，做两轮中文语音问答，记录识别文本、回复和首声耗时。

## Linux / CANN 主线
每周建议投入 8–10 小时，阶段按实测交付验收。2027 年 5 月底为内部演示目标，正式赛程确定后倒排。先用 Mac 完成感知前端，再按需要迁移至拟购的飞凌 RK3588。C++、Linux、Python、数据结构、Hot 100 和 CANN 随当前实验复习。

## 最近学习摘要

### 2026-11-19｜Atlas 部署｜Atlas 真机环境与 ResNet50 推理
用 lsblk、findmnt、df 核对存储与挂载，用 npu-smi info 读 NPU 状态。在 Mac 浏览器里操作板端 JupyterLab，代码由板端内核运行。
实验结论：Atlas 200I DK A2 从存储卡启动，根分区剩余约 36 GiB。确认 NVMe SSD 尚未挂载，CANN Toolkit 为 7.0.RC1，Ascend 310B1 健康状态为 OK。ResNet50 识别 Standard Poodle 的最高概率为 0.9355。
掌握情况：已验证
疑问：JupyterLab 曾掉线并停在星号。校正板端时间、重启服务并用浏览器无痕窗口重新连接后恢复，单项变更的影响待复测。
下一步：需要复现 NPU 样例时，先检查板端时间、空闲空间、NPU 健康和 Jupyter 内核连通性。

### 2026-11-19｜本地推理｜部署 Qwen3.5‑2B，验证两轮中文对话
GGUF 量化模型通过 llamafile 在板端 CPU 上推理。Mac 通过 SSH 隧道访问仅在板端回环地址监听的服务。
实验结论：llamafile 0.10.6 在 Atlas CPU 上运行 Qwen3.5‑2B Q4_K_M。通过 Mac 上的浏览器完成两轮中文文字对话，第二轮复述了第一轮给出的名字。首轮回复面板显示 16 tokens、4.7 秒、约 3.42 tokens/s。
掌握情况：已验证
疑问：长对话、连续测速和语言模型的 NPU 部署仍待验证。
下一步：重新打开 Mac 终端运行启动脚本，待模型加载后用浏览器确认服务，再启动语音端。

### 2026-11-19｜语音与通信｜搭建语音对话，排查动漫音色脚本版本
Mac 录音后用中文 Zipformer 识别，发送识别文本给 Atlas。板端返回文字，Mac 用系统语音或 Qwen3‑TTS 播放。
实验结论：新版脚本已提供系统语音和 Qwen3‑TTS 两种播报方式，以及独立试听模式。旧文件运行时报 unrecognized arguments。已核验重新发出的 atlas_voice_chat_qwen.py 支持 --tts 和 --preview。
掌握情况：待实测
疑问：待在 Mac 上确认 Vivian 试听、中文识别和语音对话的完整运行结果，并测量停口到首声的实际延迟。
下一步：下次在 Mac 重开两个终端。先启动 Atlas 对话服务和 SSH 隧道，再试听新版脚本的 Vivian 音色。试听通过后，做两轮中文语音问答，记录识别文本、回复和首声耗时。

### 2026-11-19｜雷达心率支线｜五个距离格能否保留胸腔微动信息
雷达对每条扫频回波做距离 FFT，得到按距离排列的格子。本次围绕第 13 格（约 0.60 米），保留第 11–15 格，跟踪每一格复数回波的相位随时间如何变化。
实验结论：单组 P2 离线回放按 50 Hz 解码 2,000 帧，共 40 秒。前 5 秒与整段选出的中心格都是 13。16 个共同窗口中，全量基线与五格 Int16 的心率输出平均绝对差和最大差均为 0.000 BPM。原始 ADC 为 819,200,000 字节，五格 I/Q 的净载荷为 160,000 字节，另计帧号、缩放比例和元数据。
掌握情况：已验证
疑问：按文件名对齐的本组参考对照中，16 个窗口的雷达估计相对 Polar 的平均绝对误差约 4.42 BPM，相对 PPG 约 5.12 BPM。设备时钟偏差、运动时目标是否移出这五格，以及板端实时传输均待验证。
下一步：用相同参数回放另一组采集，检查换距离或轻微移动时的选格、有效窗口和对 Polar 的误差，再决定 Atlas 的输入格式。

### 2026-11-19｜Atlas 部署｜首次连接 Atlas，识别存储卡与 NVMe SSD
磁盘容量由 fdisk 给出。用 lsblk 查看磁盘、分区、文件系统和挂载点，用 findmnt 查挂载在 / 的文件系统，用 df 查剩余空间。
实验结论：已首次进入 Atlas 200I DK A2 的 Linux 终端。fdisk -l 列出 mmcblk1（58.42 GiB，GPT，三个分区）和 nvme0n1（Great Wall GW3500 256GB，238.47 GiB）。
掌握情况：已验证
疑问：根文件系统来源、SSD 的文件系统及挂载情况、NPU 驱动状态和板端推理样例待实测。
下一步：在已连上的 Atlas 终端运行 lsblk、findmnt、df 和 npu-smi info，记录根文件系统、剩余空间与 NPU 健康状态。

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
- 第 35 节｜Debug 与 Release｜已验收｜复习：回顾 -g、优化级别、NDEBUG 与 CMAKE_BUILD_TYPE 的作用。

区分 CMakeCache 中预设的 Release flags 与目标实际收到的 flags。不要把必须执行的输入校验或副作用放在 assert 里。
  - Debug/Release 双构建与编译参数对照｜已实验通过｜Debug 实际带 -g。将原先为空的 CMAKE_BUILD_TYPE 修正为 Release 后，目标 flags 出现 -O3 -DNDEBUG。两份程序均输出 Sum = 5。
  - assert 与 NDEBUG 对照｜已实验通过｜引入 <cassert> 后，Debug 打印 Before assert 后退出 134；Release 打印 After assert, Sum = 5 后退出 0。
  - 难点：CMAKE_BUILD_TYPE 是配置选择，编译器实际收到的 flags 要从构建记录核对。调试信息、优化与断言是不同属性。
    判断方法：确认工程目录，用同一份源码分别构建 Debug 和 Release，对比 flags 后运行两份程序。
    实际用途：为故障定位和性能测量准备各自可复现的构建配置。
    后续练习（未验收）：用同样的构建对照准备第 41–43 节性能实验。
    复习：回顾 -g、优化级别、NDEBUG 与 CMAKE_BUILD_TYPE 的作用。
    验证边界：11 月 8 日通过双构建、实际 flags 与 assert / NDEBUG 对照。
- 第 36 节｜Sanitizer 与内存错误定位｜已验收｜复习：先读错误类型和出错行，再读分配及释放栈。溢出修复要在加法之前扩大类型；shell 的续行反斜杠放在行尾。
  - ASan 堆数组越界｜已实验通过｜三元素数组后发生 READ of size 4；报告定位 main.cpp 第 8 行。修复后输出 10、20、30，退出 0。
  - ASan 释放后读取｜已实验通过｜报告把分配、释放和非法读取分别定位到第 4、5、7 行。修复后输出 Value = 42，退出 0。
  - UBSan 有符号整数溢出｜已实验通过｜UBSan 定位 2147483647 + 1 的 int 溢出。修复后输出 next = 2147483648，退出 0。
- 第 37 节｜LLDB 进阶调试｜已验收｜复习：单步前后的变量变化能解释结果错误。观察点已有 Linux 学习经历，本次按用户要求略过实操。
  - 条件断点、查看变量和调用栈｜已实验通过｜条件断点命中；frame variable 显示 num = 5、sum = 3，执行赋值后 sum = 5。修复重跑 Result = 8。
- 第 38 节｜单元测试与 CTest｜已验收｜复习：区分一个 CTest 测试入口和入口内的十个检查。复习 INT_MIN、INT_MAX 和累加前的范围校验。
  - 从失败用例到回归测试通过｜已实验通过｜同一测试先捕获混合输入的错误结果，修复后十个用例全部通过。
- 第 39 节｜Git 与项目文档｜已验收｜复习：把 README 作为复现实验的一部分。用干净克隆核对工程是否意外依赖本地构建产物或未提交文件。
  - 按 README 在干净克隆复测｜已实验通过｜docs/repro 已快进合并。新克隆可配置、构建和运行测试，十个用例通过。
- 第 40 节｜阶段项目：模块化工程｜已验收｜复习：分清库、命令行和测试职责。std::cerr 是错误输出流，std::errc 是错误码枚举。整数解析和求和都要检查各自的失败分支。
  - 静态库、CLI 与 CTest 接线｜已实验通过｜sum_core、sum_cli、sum_test 均构建成功。CLI 输出 Sum = 8，越界输入返回 exit = 1；十个用例通过。
  - 阶段项目干净克隆复测｜已实验通过｜在干净克隆重新配置和编译，CLI 输出 Sum = 8，CTest 1/1 通过，程序内部十个用例通过。
- 第 41 节｜内存布局与对齐｜已验收｜复习：画出 LayoutA 偏移 1–3 与 9–11 的填充。
说明 recordsA[2]{} 中 [2] 和 {} 分别负责什么。
  - 结构体大小、对齐与成员偏移｜已实验通过｜sizeof、alignof 和 offsetof 的输出与 12 字节、8 字节布局推导一致。
  - 数组初始化与对象步长｜已实验通过｜A[2] 和 B[2] 实测分别为 24 字节和 16 字节，第二个 A 的 count 相对数组起点为 12 + 4 = 16 字节。
  - 难点：sizeof 包含内部和尾部的填充，offsetof 给出的是成员相对对象起点的位置。
    判断方法：先按成员的对齐要求排偏移，再把对象总大小补齐到结构体的对齐要求，用相邻数组元素检验。
    实际用途：估算 CPU 批量记录的存储成本和访问步长，给 AoS 与 SoA 选型提供依据。
    后续练习（未验收）：第 42 节用同样的 8 字节记录比较只访问 count 时的开销。
    复习：画出 LayoutA 偏移 1–3 与 9–11 的填充。；说明 recordsA[2]{} 中 [2] 和 {} 分别负责什么。
    验证边界：两种字段排列与两组对象数组均有用户的终端实测。
- 第 42 节｜CPU Cache 与数据布局｜已验收｜复习：根据 8 字节记录和 4 字节整数推导两种 count 步长。
解释只扫描一列时，哪种布局在一条缓存行中放入更多参与运算的 count。
  - AoS 与 SoA 的单字段求和｜已实验通过｜同一批输入均得到 198000000。AoS 相邻 count 的起点间隔为 8 字节，SoA 为 4 字节。
  - 默认构建和 -O3 对照｜已实验通过｜优化后六个耗时均小于 1 ms。三轮中有一轮 AoS 更快，复测和顺序控制见第 43 节。
  - 难点：同样的循环次数可以产生不同的访问步长，每条缓存行中实际参与计算的元素数量随布局变化。
    判断方法：先列出循环消费的字段，再检查元素的内存间隔与布局，最后用一致的结果和多次计时验证。
    实际用途：为 CPU 张量预处理、按列扫描和算子归约选择与实际访问方式匹配的布局。
    后续练习（未验收）：第 43 节交换测量顺序，并跨规模复测单列扫描。
    复习：根据 8 字节记录和 4 字节整数推导两种 count 步长。；解释只扫描一列时，哪种布局在一条缓存行中放入更多参与运算的 count。
    验证边界：结论对应 400 万条记录的 count 求和及当时的编译配置。
- 第 43 节｜Benchmark 方法｜已验收｜复习：把 0.000250 ms 换算为 250 ns，说明为什么此时计时粒度值得关注。
解释 shell 中 || break 会在命令失败时提前结束所在循环。
  - 交替顺序与中位数｜已实验通过｜AoS 先测和后测的中位数为 0.548084/0.480625 ms，SoA 为 0.257375/0.226375 ms。两种布局后测的中位数都低约 12%，区间有重叠。十次同轮对照中 SoA 耗时都更短。
  - 三档规模对照｜已实验通过｜AoS 先测的 5 次中位数，4 千条为 0.000541/0.000250 ms，40 万条为 0.106500/0.052292 ms，400 万条为 0.548084/0.226375 ms。
  - 难点：固定顺序会把布局与先后位置绑定，短循环的计时粒度和时钟开销占比更高。
    判断方法：用同一编译配置和输入做配对比较，交替顺序并记录中位数与波动。测试不同规模时明确用的是哪种顺序。
    实际用途：为 CANN 算子优化和 CPU 基线记录可复现的数据规模、参数、正确性和耗时证据。
    后续练习（未验收）：测量更短的稳态循环时，练习预热和多次执行合计计时。
    复习：把 0.000250 ms 换算为 250 ns，说明为什么此时计时粒度值得关注。；解释 shell 中 || break 会在命令失败时提前结束所在循环。
    验证边界：已做顺序控制、多规模与重复测量。预热和批量计时在本次作为后续测量方法讨论。
- 第 44 节｜Profiling 入门｜已验收｜复习：说清 sample 的栈顶计数和 Call graph 的用途。
用 Checksum ÷ Rounds 验证两种填充写法的每轮结果。
  - macOS 进程采样与热点定位｜已实验通过｜sample 采样 3 秒，间隔设置为 1 ms。栈顶排名把 fillRecords 定位为最常被采到的用户代码函数；采样校验和正确。
  - 填充循环改写与直接运行复测｜已实验通过｜原式两次为 4181、4155 轮，递增回绕为 3120、3117 轮。四次 Checksum ÷ Rounds 均为 198000000。保留原式作为性能基线。
  - 难点：栈顶计数反映线程被采到时所处的函数，调用树上层还会包含被调函数的采样。
    判断方法：先用采样定位热点，再单独改一处代码，用同一构建配置和交替顺序比较正确性与整轮吞吐。
    实际用途：定位数据准备、内存清零和实际算子的开销，为 CPU、推理前处理和算子工程选择优化目标。
    后续练习（未验收）：第 45 节用编译器报告确认循环是否向量化，并区分已测结果与关于编译的假设。
    复习：说清 sample 的栈顶计数和 Call graph 的用途。；用 Checksum ÷ Rounds 验证两种填充写法的每轮结果。
    验证边界：热点和吞吐有用户实测。递增回绕引入的跨迭代依赖是可能解释，具体向量化行为待编译器报告确认。
- 第 45 节｜编译优化与向量化｜已验收｜复习：说明 out[i] = x[i] + y[i] 为什么适合按相邻元素分组。
解释 4,000,003 项在宽度 4 下的尾部处理。

解释 4 组各处理 4 项和单个向量宽度 4 的关系。
用 x[i] 与 *(x + i) 解释两种遍历访问的地址。
  - CPU Add 的 -O2 与 -O3 向量化对照｜已实验通过｜已给出 CPU Add 示例、编译命令和逐项校验方式。

add 循环均为 width 4、interleaved 4，4,000,003 项逐项校验通过。单次耗时分别为 1.24817 ms 和 0.612333 ms。
  - 下标与指针遍历的 -O3 对照｜已实验通过｜两种写法的 add 循环均为 width 4、interleaved 4。下标与指针版的三次中位耗时为 0.630084 和 0.942416 ms，逐轮快慢有波动。
  - 难点：同一文件有多个循环诊断，相同的向量宽度与交错组数也可能对应不同的执行开销。
    判断方法：按源码行定位 add 循环，记录 width、interleave 和最大绝对误差，再用同条件多轮计时比较。
    实际用途：建立可复现的 CPU Add 基线，给 CANN 算子的输出和尾部处理提供对拍依据。
    后续练习（未验收）：第 48 节用同样的报告与校验方法比较矩阵乘法循环。
    复习：解释 4 组各处理 4 项和单个向量宽度 4 的关系。；用 x[i] 与 *(x + i) 解释两种遍历访问的地址。
    验证边界：本机编译报告和逐项校验已核对。耗时样本支持本次记录中的中位数。
- 第 46 节｜线程基础｜已验收｜复习：用 5 个元素画出两个半开区间。
说明 return 放在内层作用域外的作用。
  - std::thread 分段求和与 join｜已实验通过｜两档均三次通过。4,003 项串行和双线程中位耗时为 0.416、53.833 μs。4,000,003 项为 0.957250、0.259792 ms。
  - std::jthread 的作用域与自动等待｜已实验通过｜内层作用域结束后合并部分和。两档均三次通过。4,003 项中位耗时为 0.500、64.584 μs。4,000,003 项为 0.327666、0.302542 ms。
  - 难点：两个线程要覆盖奇数长度的全部元素，主线程读取部分和时两个写入都必须已完成。
    判断方法：用 [0, mid) 与 [mid, n) 分段，各写自己的部分和。显式 join 或在内层作用域析构 jthread，之后才读 left 和 right。
    实际用途：并行归约、数据预处理和批量统计按任务规模选择线程划分。
    后续练习（未验收）：第 47 节把各自累加后合并的做法用于共享计数器。
    复习：用 5 个元素画出两个半开区间。；说明 return 放在内层作用域外的作用。
    验证边界：本机两种等待方式的正确性已验证。耗时包含创建和等待，串行固定先测。
- 第 47 节｜同步与原子操作｜已验收｜复习：解释 guard 构造和析构何时加锁和释放。
区分可并发只读的 nums 与两个线程都要修改的 total。
  - mutex、lock_guard 与 atomic 计数｜已实验通过｜两次 runTwoThreads 顺序执行，每次各启动两个线程。每线程加 100,000 次，mutex 和 atomic 版三轮均输出 200000、PASS。
  - 减少共享原子更新｜已实验通过｜逐项原子加一共 1,000,000 次，分段局部统计后每线程只执行一次 fetch_add。六轮都 PASS，局部合并版中位耗时约为逐项更新版的 1/12.82。
  - 难点：两个线程各有自己的 guard 和 local，却访问同一个 m 或 total。锁和原子操作都能保证指定计数正确，争用仍会影响吞吐。
    判断方法：多步共享更新用同一 mutex 保护临界区。独立计数可用 fetch_add，先在线程内部累计能降低共享更新频次。
    实际用途：优化任务处理计数、并行归约和多线程统计，减少热路径上的共享写入。
    后续练习（未验收）：把每项更新改为每线程一次合并，记录结果与耗时，作为后续并行算子的对照。
    复习：解释 guard 构造和析构何时加锁和释放。；区分可并发只读的 nums 与两个线程都要修改的 total。
    验证边界：两种同步写法和两种计数合并方式均有本机 PASS，普通 int 无同步的情况在对话中推演。
- 第 48 节｜毕业项目：CPU 算子优化｜已验收｜复习：解释 IKJ 中每个输出格仍要沿 p 累加 512 次。
比较 IJK 的跨行读与 IKJ 的连续读写，说明为何相同 SIMD 分组会有不同收益。
  - IJK 与 IKJ 正确性及基准｜已实验通过｜2×3 乘 3×2 得到 [58,64,139,154]。默认 -O3 交替测序六轮均 PASS，中位耗时 88.865550 / 7.308315 ms，IKJ 约快 12.16 倍。
  - 向量化报告与关闭自动向量化对照｜已实验通过｜两个内层均有 width 4 / interleaved 4 报告，IJK 另有成本模型放弃的报告。关闭循环和 SLP 向量化后六轮均 PASS，中位耗时 89.103100 / 32.539100 ms，IKJ 约快 2.74 倍。
  - 提交与干净克隆复现｜已实验通过｜e97b459 提交含 main.cpp 与 README.md。干净克隆后两种构建分别通过小矩阵和六轮逐项对照，默认及关闭向量化的加速比为 12.14 倍与 2.73 倍。
  - 难点：IJK 和 IKJ 做同样数量的乘加，但向量化的方向不同，向量宽度与交错组数不足以推断耗时。
    判断方法：先比对小矩阵预期与大矩阵逐项结果，再固定输入、-O3 和轮次，交替测序比较两种构建。结合 B、C 的步长与归约开销解释。
    实际用途：给后续算子开发建立行主序 GEMM 基线，练习读编译报告、设置公平对照和交付可复现结果。
    后续练习（未验收）：复用 README 中的校验与基准流程，为 Python / NumPy 参考实现及 Ascend C 算子准备对照。
    复习：解释 IKJ 中每个输出格仍要沿 p 累加 512 次。；比较 IJK 的跨行读与 IKJ 的连续读写，说明为何相同 SIMD 分组会有不同收益。
    验证边界：已在同一台 Mac 干净克隆复测正确性和性能。报告给出编译诊断，实际运行路径及缓存的单独贡献需另做实验。

## AI Infra全体系学习路线
用 Atlas 运行中文小模型，让桌面助手能认出已登记的用户、用声音交流、记住获准保存的偏好，并执行真实的本地工具。
每周建议投入 8–10 小时，阶段按实测交付验收。2027 年 5 月底为内部演示目标，正式赛程确定后倒排。先用 Mac 完成感知前端，再按需要迁移至拟购的飞凌 RK3588。C++、Linux、Python、数据结构、Hot 100 和 CANN 随当前实验复习。
规划版本：2026-11-18-atlas-companion-v1

## 设备与竞赛锚点
Atlas 200I DK A2 / MacBook Air / RTX 3090 / 飞凌 RK3588
环境状态：
目标赛事：
正式提交截止T：待核实；报名截止不作为T
首次连接：
准备窗口：

###  Atlas 桌面陪伴助手｜进行中

MVP：
可选增强：
下一步：下次在 Mac 重开两个终端。先启动 Atlas 对话服务和 SSH 隧道，再试听新版脚本的 Vivian 音色。试听通过后，做两轮中文语音问答，记录识别文本、回复和首声耗时。
仓库：
实际执行记录数：0
准备窗口：
计划启动：
预计体量：
实际首次执行日期：尚未开始
流程规则：

## 学习与实践时间轴
- 2026.11.18–11.30｜建立三端基线
  学习：Linux 设备、SSH、音频录放、tokenizer 和聊天模板
  实践：Atlas 运行 NPU 样例，Mac 录放音，3090 生成参考回复。
  门槛：保存板型、软件版本、样例输出、录音和五个固定问题的回答。
  建议投入：每周 8–10 小时，按实际记录
- 2026.12｜跑通离线语音对话
  学习：ONNX、ATC、OM、prefill / decode、KV cache 和 WebSocket
  实践：先用板端 Qwen3.5‑2B 和 Mac 按键录音建立基线，再验证流式回复和分句播报。
  门槛：断开公网连续交谈 10 轮，记录停口到首声的时间和前端型号。
  建议投入：每周 8–10 小时，按实际记录
- 2027.01｜让角色状态跨轮延续
  学习：离散状态方程、事件标注、JSONL 分组和盲评
  实践：设计两种人格；在相同台词下改变事件历史或响应参数。
  门槛：导出状态轨迹和回复，完成独立盲评，检查事实回答。
  建议投入：每周 8–10 小时，按实际记录
- 2027.02｜微调 Qwen 并回到真机
  学习：SFT、LoRA、学习率、验证损失、导出回归
  实践：在 3090 训练、合并适配器，在兼容的 Linux 环境转 OM，再部署到 Atlas。
  门槛：三组同题结果可回放，微调版本在板上产生真实回复。
  建议投入：每周 8–10 小时，按实际记录
- 2027.03｜接入视觉、记忆与工具
  学习：OpenCV、登记阈值、SQLite、工具参数与幂等
  实践：前端区分登记用户和访客；Atlas 执行计时、学习记录和授权偏好。
  门槛：演示访客流程、计时启动/查询/取消与偏好删除；双板版可脱离 Mac。
  建议投入：每周 8–10 小时，按实际记录
- 2027.04｜测量打断、并发与重连
  学习：有界队列、取消、分位数和性能定位
  实践：打断播报、撤销旧生成，重连后复用会话；比较摄像头开关下的延迟。
  门槛：连续运行 1 小时，记录首声 P50/P95、每板峰值内存和迟到片段。
  建议投入：每周 8–10 小时，按实际记录
- 2027.05｜冻结参赛演示版本
  学习：消融、回归测试、复现说明与答辩
  实践：复测离线、访客、打断、重连、工具失败，固定模型与依赖版本。
  门槛：一键启动、3 分钟离线演示、5 分钟讲解，附架构图、测试表和备用录像。
  建议投入：每周 8–10 小时，按实际记录

### Atlas 环境与部署｜Atlas 部署

#### board Atlas 环境与部署
前置：Linux、SSH、存储卡、SSD、CANN 版本匹配
验收：另一人能依环境清单复现样例。
- 核对板型，启动匹配镜像，保存一次 NPU 样例输出。｜已验收｜★重点
  学习范围：Linux、SSH、存储卡、SSD、CANN 版本匹配

### Qwen 本地推理｜本地推理

#### qwen Qwen 本地推理
前置：分词、聊天模板、ONNX → ATC → OM、KV cache
验收：模型和分词器版本可追溯，Atlas 断开公网后能回答新问题。
- 比较参考输出与板端输出，把 prefill 和 decode 分开计时。｜待复测｜★重点
  学习范围：分词、聊天模板、ONNX → ATC → OM、KV cache

### 中文语音与跨板通信｜语音与通信

#### speech 中文语音与跨板通信
前置：ASR、TTS、分句、WebSocket、会话号与轮次号
验收：十轮离线对话有录音、识别文本和首声时间。
- 从按键录音开始，经中文识别、Atlas 回复、分句合成到扬声器。｜进行中｜★重点
  学习范围：ASR、TTS、分句、WebSocket、会话号与轮次号

### 人格与情绪动力学｜人格与情绪

#### state 人格与情绪动力学
前置：角色基线、二维状态、事件增益与衰减、可控生成
验收：固定事实与解码条件，可比较角色差异和跨轮一致性。
- 同一个问题，分别在鼓励、打断和道歉后提问，记录角色恢复轨迹。｜未开始｜★重点
  学习范围：角色基线、二维状态、事件增益与衰减、可控生成

### 数据、SFT 与 LoRA｜模型训练

#### train 数据、SFT 与 LoRA
前置：Python、JSONL、按场景切分、损失掩码、学习率与 rank
验收：保存切分、种子、配置和独立测试结果。
- 训练 0.6B 适配器，逐次只变一个超参，比较合并前后和板端输出。｜未开始｜★重点
  学习范围：Python、JSONL、按场景切分、损失掩码、学习率与 rank

### 在场与登记识别｜视觉感知

#### vision 在场与登记识别
前置：OpenCV、相似度阈值、RKNN 适配与授权
验收：记录误识别与漏识别，未知者走访客流程。
- 先实现有人/无人，再区分自愿登记用户、访客和未知；只传状态。｜未开始｜★重点
  学习范围：OpenCV、相似度阈值、RKNN 适配与授权

### Agent 工具与授权记忆｜工具与记忆

#### agent Agent 工具与授权记忆
前置：工具定义、参数校验、SQLite、幂等请求、偏好删除
验收：启动、查询、取消有真实结果，重连不重复执行。
- 实现计时、学习记录和可撤回的偏好；回放重复工具请求。｜未开始｜★重点
  学习范围：工具定义、参数校验、SQLite、幂等请求、偏好删除

### 并发运行与端侧测量｜端侧性能

#### systems 并发运行与端侧测量
前置：C++ RAII、生产者消费者、环形队列、取消和时间戳
验收：一小时运行有原始日志，能解释首声延迟与异常案例。
- 本地先停播，Atlas 按轮取消，前端丢弃迟到片段；记录峰值内存。｜未开始｜★重点
  学习范围：C++ RAII、生产者消费者、环形队列、取消和时间戳

### 对照实验与参赛演示｜竞赛交付

#### delivery 对照实验与参赛演示
前置：固定基线、盲评、消融、复现与现场演示
验收：一键启动并演示识别、对话、工具和打断，附测试表与录像。
- 回放同一套语音和多轮台词，对照事实、角色一致性和首声延迟。｜未开始｜★重点
  学习范围：固定基线、盲评、消融、复现与现场演示

## 使用规则
只以网站已保存的学习摘要为来源；不推测时长或补写实验。读取失败时应明确告知用户，不能把历史缓存视为最新进度。原始笔记、身份、凭据和私密文件不在本镜像中。
