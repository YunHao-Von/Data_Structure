# 仓库介绍：  
本仓库用来提升作者及contributor的算法设计能力和规范性。  
包含Python版本(main)和Java版本（java）。  

# Python版编程规范   
## 命名规范
变量名采⽤⼩写蛇形⻛格，  
<font color = green>例如 coupon_name、 user_last_name 等；</font>     
常量名采⽤⼤写蛇形⻛格，  
<font color = green>例如 COUPON_NAME、 USER_LAST_NAME 等；</font>   
函数名采⽤⼩写蛇形⻛格，并要求以动词开头，  
<font color = green>例如 take_last_name、 translate 等；</font>   
类名采⽤⼤驼峰命名⻛格，  
<font color = green>例如 Storage、 ImageDownload 等；</font>   
接⼝名采⽤⼤驼峰命名⻛格，  
<font color = green>例如 StorageInterface、 AbstractDownload 等；</font>   
包名采⽤⼩写蛇形命名⻛格，  
<font color = green>例如 file_storage、 components 等；</font>   
⽂件名采⽤⼩写蛇形命名⻛格，  
<font color = green>例如 utils.py、 remote_cache.conf 等；</font>   
项⽬名采⽤⼩写蛇形命名⻛格，  
<font color = green>例如 sequence、 translation_machine 等；</font>   
类名、包名、⽂件名、项⽬名、变量名、常量名⽤名词或名词短语，如用名词短语，定语在前，名词在后；  
<font color = green>例如：ticket_vending_machine、document_management</font>     
函数名⽤动词或者动词短语，如用动词短语，动词在前，名词在后；例如：get_index  
表示数量的词统一使用“nums_单数”的形式；例如：nums_layer, nums_channel  
⻓度控制在 5 个单词内，追求⻅名知意；不要占⽤语⾔或者系统保留词；不要使⽤简短的字⺟或者非标准的单词缩写作为名称；  
<font color = green>例如：用layer_idx表示layer的index，用layer_id表示layer的identity，不要使用lay_id表示layer的index。</font>    
项⽬名、包名、⽂件名对应的单词可以⽤复数形式表示；  
接⼝名、抽象类名、基类名、异常类名、错误类名以特定的单词开头或结尾，  
<font color = green>例如 TimeException、StorageBase、 PermissionInterface、 ParseError 等；  </font>   
名称中除了字⺟和下划线外，不应包含其他字符（特殊字符和数字）；  
<font color = green>例如不要出现a2b这样的命名；  </font>   

-----

## 注释标准  
行尾注释：EXPIRE = 3600空格空格#空格调⽤⽅指定的时间数值  
单一空行注释：  <font color =red>
1）#空格函数添加类型注释   
2）"""只有 1 ⾏内容时，注释符号的开头和结尾在同⼀⾏"""  </font>  
多行注释："""消费者  
当有多⾏内容时，注释符号的结尾单独⼀⾏，且第⼀⾏⽂字注释紧跟在注释符号的后⾯  
"""  
类型注释：  
为每个变量给出类型注释name: str， number: int = 1003，   
from typing import Tuple, List, Dict   
coupons: Tuple [str, str, int] = ("编写类型注释", "像c/java", 100)  
函数注释：函数需要给出形参和返回值注释  
def send(message: str, host: str, name: str) --> str:  
""" 消息推送器  
将消息推送到指定服务器的指定队列中  
: param message: 消息体  
: param host: 服务器地址  
: param name: 队列名称  
: return: 推送结果  
"""  
除了让人更加能够阅读之外，另一个好处是print(send.__annotations__)时会看到更多的信息。  
文件注释：⽂件注释写在⽂件最开头，通常被⽤于表明法律或版权信息以及⽂件内容的相关信息  
"""  
@description: 关于⽂件注释的描述与示例  
@其他内容: 参考orion或其他项目，但是一般公司是不写author的名字等信息的  
"""  

----

## 代码缩进与空格的使用标准  
1、缩进：tab键需要变成4个空格；单⾏字符数限制在 79 个内，不要到达 80 个字符，如达到，需要采用悬挂缩进，如果悬挂缩进时有符号，将符号放下⼀⾏的⾏⾸；  
def reader(name: str, path: str, storage: FileStorage,   
header_line: int = 1, classify: str = "csv",  
threshold: int = 100) -> FileStorage:  
consumer = (age  
+ height  
+ weight  
* threshold )  
name空格=空格[  
"Java", "Python", "Golang",  
"Rust", "C++", "C",  
]  

2、空格：  
表达式中符号左右的对象与符号以 1 个空格进⾏分隔；例如：a == b  
括号内不要有空格；例如: spam(ham[1], {eggs: 2}, [])  
不要在逗号, 分号, 冒号前面加空格, 但应该在它们后面加(除了在行尾)；例如 x, y = y, x  
相邻⾏的表达式不应按照符号进⾏强制对⻬；  
参数列表, 索引或切片的左括号前  


-----
-----
-----


接下来的部分是介绍仓库架构：

# Data_Structure    
本项目下囊括Java数据结构与Python数据结构练习项目。  
Python数据结构（branch:main)：  
笔记见Blog文件夹下，  
课程代码放在了ClassCode里，按照单元进行存储，其中，.py文件为各种数据结构类为主，.ipynb则是各种测试文件。  
每日力扣题目放在了LeetCode文件夹下。  
同时本分支下保存了本仓库Python语言编程规范。    
参考书目《数据结构编程（Python语言描述）》，李春葆主编，2020年11月第1版。  
