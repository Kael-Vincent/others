Skip
to
content
titletitle
administrator | 注销

查找

Jenkins
Fis6
.7
.7
.0
1
_python_sql标准版6770
配置
返回面板
状态
修改记录
工作空间
Build
with Parameters
    删除
    Project
配置
Email
Template
Testing
Send
Mail
Subversion
Polling
Log
Move
collapse构建历史80 % Build
History
x
find
Success > 控制台输出  # 1?24 2018-7-31 下午5:58
Success > 控制台输出  # 1?23 2018-7-31 下午5:47
Success > 控制台输出  # 1?22 2018-7-31 下午5:33
Success > 控制台输出  # 1?21 2018-7-31 下午5:33
Failed > 控制台输出  # 1?20 2018-7-31 下午5:27
Success > 控制台输出  # 1?19 2018-7-31 下午2:00
Success > 控制台输出  # 1?18 2018-7-31 下午2:00
Success > 控制台输出  # 1?17 2018-7-31 下午1:45
Success > 控制台输出  # 1?16 2018-7-31 下午1:30
Success > 控制台输出  # 1?15 2018-7-31 下午1:15
Success > 控制台输出  # 1?14 2018-7-31 上午9:53
Success > 控制台输出  # 1?13 2018-7-31 上午1:50
Success > 控制台输出  # 1?12 2018-7-30 下午8:00
Success > 控制台输出  # 1?11 2018-7-30 下午5:00
Success > 控制台输出  # 1?10 2018-7-30 下午2:50
Feed
RSS
全部
Feed
RSS
失败
项目名称
1
_python_sql标准版6770
描述
数据库升级打包
[Plain text]
预览
GitHub
project
Throttle
builds
Help
for feature: Throttle
builds
丢弃旧的构建
Help
for feature: 丢弃旧的构建
Strategy
保持构建的天数
如果非空，构建记录将保存此天数
保持构建的最大个数
15
如果非空，最多此数目的构建记录将被保存

高级...
参数化构建过程
Help
for feature: 参数化构建过程
String
Parameter
[Help]
名字
PATCH_NAME
Help
for feature: 名字
默认值
D:\uppack\Fis6
.7
.7
.0
Help
for feature: 默认值
描述
升级包名 * 必填 *
[Plain text]
预览
Help
for feature: 描述
删除
String
Parameter
[Help]
名字
Start_version
Help
for feature: 名字
默认值
27322
Help
for feature: 默认值
描述
起始版本号 * 必填 *
[Plain text]
预览
Help
for feature: 描述
删除
String
Parameter
[Help]
名字
TO_VERSION
Help
for feature: 名字
默认值
HEAD
Help
for feature: 默认值
描述
终止版本号 * 必填，默认为：最新 *
[Plain text]
预览
Help
for feature: 描述
删除
String
Parameter
[Help]
名字
mysvn_url
Help
for feature: 名字
默认值
https: // 10.200
.0
.4 / ZQ / fis / Fis / src / branches / 6.7
.7
.0
Help
for feature: 默认值
描述
svn地址
[Plain text]
预览
Help
for feature: 描述
删除
String
Parameter
[Help]
名字
Client_version
Help
for feature: 名字
默认值
6.7
.7
.0
Help
for feature: 默认值
描述
前端版本号
[Plain text]
预览
Help
for feature: 描述
删除
String
Parameter
[Help]
名字
Lbmdll_version
Help
for feature: 名字
默认值
6.7
.7
.0
Help
for feature: 默认值
描述
后台blmdll版本号
[Plain text]
预览
Help
for feature: 描述
删除
String
Parameter
[Help]
名字
Sql_version
Help
for feature: 名字
默认值
Fis6
.7
.7
.0(R)
Help
for feature: 默认值
描述
数据库的版本号
[Plain text]
预览
Help
for feature: 描述
删除
String
Parameter
[Help]
名字
first
Help
for feature: 名字
默认值
0
Help
for feature: 默认值
描述
0
为不写入版本号，第一次编译为全部编译，以后只编译变化部分；1
为写入版本号并全部编译
默认为0, 需要重新全部编译时，构建时手动修改值为1。
[Plain text]
预览
Help
for feature: 描述
删除
String
Parameter
[Help]
名字
ProjectAll
Help
for feature: 名字
默认值
D:\packworkpath\lbmdll_pack\6.7
.7
.0\lbmdll\ProjectAll.sln
Help
for feature: 默认值
描述
lbmdll
编译总工程文件
ProjectAll.snl
的预期的具体位置
例如：
https: // 10.200
.0
.4 / ZQ / fis / Fis / src / branches / 6.7
.3
.0
对应的路径为：
D:\packworkpath\lbmdll_pack\6.7
.3
.0\lbmdll\ProjectAll.sln

代码里是以svn链接最后一个“ / ”后面的字符串命名的文件夹并生成文件夹，把代码下载到这个文件夹里。
[Plain text]
预览
Help
for feature: 描述
删除
添加参数
关闭构建(重新开启构建前不允许进行新的构建)
Help
for feature: 关闭构建(重新开启构建前不允许进行新的构建)
在必要的时候并发构建
Help
for feature: 在必要的时候并发构建
Restrict
where
this
project
can
be
run
Help
for feature: Restrict
where
this
project
can
be
run
Label
Expression
master
Help
for feature: Label
Expression
Label is serviced
by
1
node
高级项目选项
本区块的一个或多个字段已经被修改。
高级...
源码管理
None
CVS
CVS
Projectset
Git
Subversion
Modules
Repository
URL
https: // 10.200
.0
.4 / ZQ / fis / Fis / src / branches / 6.7
.7
.0 @ HEAD
Help
for feature: Repository
URL
"/Fis/src/branches/6.7.7.0"
doesn
't exist in the repository. Maybe you meant "/Fis/src/branches/6.7.7.1"?
Local
module
directory(optional)
.
Help
for feature: Local
module
directory(optional)
Repository
depth
Help
for feature: Repository
depth
Ignore
externals
Help
for feature: Ignore
externals

Add
more
locations...
Check - out
Strategy
Use
'svn update'
whenever
possible, making
the
build
faster.But
this
causes
the
artifacts
from the previous

build
to
remain
when
a
new
build
starts.
源码库浏览器
Help
for feature: 源码库浏览器

高级...
Visual
Source
Safe
构建触发器
触发远程构建(例如, 使用脚本)
Help
for feature: 触发远程构建(例如, 使用脚本)
Build
after
other
projects
are
built
Help
for feature: Build
after
other
projects
are
built
Build
periodically
Help
for feature: Build
periodically
GitHub
hook
trigger
for GITScm polling    Help for feature: GitHub
hook
trigger
for GITScm polling
    Poll
    SCM
    Help
    for feature: Poll
    SCM
日程表
H / 10 * * * *
Help
for feature: 日程表
Would
last
have
run
at
2018
年8月18日
星期六
上午10时10分50秒
CST;
would
next
run
at
2018
年8月18日
星期六
上午10时10分50秒
CST.
Ignore
post - commit
hooks
Help
for feature: Ignore
post - commit
hooks
构建环境
Send
files or execute
commands
over
SSH
before
the
build
starts
Help
for feature: Send
files or execute
commands
over
SSH
before
the
build
starts
Send
files or execute
commands
over
SSH
after
the
build
runs
Help
for feature: Send
files or execute
commands
over
SSH
after
the
build
runs
构建
Execute
Python
script
[Help]
Script

# -*- coding:gb2312 -*-
# python变量分大小写，bat不分大小写，python菜鸟学习网址:http://www.runoob.com/python/python-tutorial.html
import pysvn, os, re, shutil, sys

reload(sys)
sys.setdefaultencoding('gb2312')

# 引用参数begin
# 读取和设置环境变量:os.getenv() 与os.putenv()
PATCH_NAME = os.getenv("PATCH_NAME")
mysvn_url = os.getenv("mysvn_url")
Start_version = os.getenv("Start_version")
TO_VERSION = os.getenv("TO_VERSION")
Client_version = os.getenv("Client_version")
Lbmdll_version = os.getenv("Lbmdll_version")
Sql_version = os.getenv("Sql_version")
workspace = os.getenv("workspace")
SVN_REVISION = os.getenv("SVN_REVISION")
# 引用参数end

# 声明全局变量pysvn.Revision,begin

revision_start = pysvn.Revision(pysvn.opt_revision_kind.number, int(Start_version))
revision_start1 = pysvn.Revision(pysvn.opt_revision_kind.number, int(Start_version) + 1)
revision_end = pysvn.Revision(pysvn.opt_revision_kind.head)
peg_revision = pysvn.Revision(pysvn.opt_revision_kind.unspecified)

# 声明全局变量pysvn.Revision,end

# 获取版本，生成工作目录begin
last_path = os.path.basename(mysvn_url)
work_path = workspace + "\\" + last_path
if os.path.exists(work_path):
    print(work_path)
else:
    os.makedirs(work_path)
    # 获取版本，生成工作目录end
    print("获取版本，生成工作目录end")

os.chdir(work_path)  # 切换到工作目录work_path下工作
os.system("svn diff --summarize -r %Start_version%:%TO_VERSION% %mysvn_url%/server>1.txt")

s = open('1.txt', 'r+').read()  # 读取文件1.txt
num1 = len(s)  # 计算文件1.txt字长
print(num1)  # 打印文件字长的值
if num1 == 0:
    print("数据库没有代码更新")  # 文件1.txt如果为空,数据库没有代码更新
else:
    print("数据库代码有更新")  # 文件1.txt如果不为空,数据库代码有更新

    # 更新源码,先把server目录check out到本地begin

    os.chdir(work_path)  # 切换到工作目录下工作
    if os.path.exists("version.txt"):
        print("version.txt已经存在")
        s = open('version.txt', 'w+')
        s.write(SVN_REVISION)
        s.close()
        p = pysvn.Client()
        p.update(work_path + "\\server", revision_end)  # 更新代码svn update.
    else:
        p = pysvn.Client()
        p.checkout(mysvn_url + "/server", work_path + "\\server")
        s = open('version.txt', 'w+')
        s.write(SVN_REVISION)
        s.close()

    # 更新源码,先把 server目录check out到本地end
    print("更新源码,先把server目录check out到本地end")

    # 生成所需要更新文件的目录结构，方便后面打包编写升级脚本begin
    # len(mysvn_url)计算mysvn_urlL长度
    # 获取路径名: os.path.dirname()
    # 获取文件名：os.path.basename()
    # 分离扩展名：os.path.splitext()

    os.system("svn diff --summarize -r %Start_version%:%TO_VERSION% server>11.txt")

    newserver = work_path + "\\newserver"
    if os.path.exists(newserver):
        shutil.rmtree(newserver)
        os.mkdir(newserver)  # 清空后再生成目录
    else:
        os.makedirs(newserver)
    os.chdir(newserver)  # 切换到工作目录newserver下工作
    s = open(work_path + "\\11.txt")
    for line in s.readlines():
        if re.match("A", line) or re.match("M", line):
            if os.path.exists(os.path.dirname(line[8:])):
                print(os.path.dirname(line[8:]) + "已经存在")

            else:
                print(os.path.dirname(line[8:]))
                os.makedirs(os.path.dirname(line[8:]))

    print("#生成所需要更新文件的目录结构，方便后面打包编写升级脚本end")
    # 生成所需要更新文件的目录结构，方便后面打包编写升级脚本end


    # 全量文件处理begin

    os.chdir(newserver)  # 切换到工作目录下工作

    # 处理全量目录 query,proc,FISUPDATE,proc_opt,report,stat,begin
    p = pysvn.Client()
    s = open(work_path + "\\11.txt", 'rb')
    for line in s.readlines():
        if ".sql" in line and re.match("A", line) or ".sql" in line and re.match("M", line):
            if "\\proc\\" in line or "\\query\\" in line or "\\FISUPDATE\\" in line or "\\proc_opt\\" in line or "\\report\\" in line or "\\stat\\" in line:
                svnurlfile = ''.join(
                    line[8:].split())  # 原因是因为第一行line的后面多了个回车键.#去掉回车符(\r)、换行符(\n)、水平制表符(\t)、垂直制表符(\v)、换页符(\f)）
                print(svnurlfile)
                fp1 = os.path.dirname(svnurlfile)  # 文件所在的上一级目录
                fp2 = svnurlfile.replace('\\', '/')
                svnurl1 = mysvn_url + "/" + fp2
                svnurl = unicode(svnurl1, 'GB2312')  # 转换成svn识别编码，主要是为了能识别中文的svn链接
                localpath1 = newserver + "\\" + fp1
                localpath = unicode(localpath1, 'GB2312')
                print("fp1:")
                print(fp1)
                print("svnurl:")
                print(svnurl)
                print(localpath)
                p.export(svnurl, localpath, force=True)

    # 处理全量目录 query,proc,FISUPDATE,proc_opt,report,stat,end
    print
    "处理全量目录 query,proc,FISUPDATE,proc_opt,report,stat,end"

    # 处理增量目录 query的querymenu.sql,dict,init,begin

    os.chdir(work_path)
    s = open(work_path + "\\11.txt", 'rb')
    for line in s.readlines():
        if ".sql" in line and re.match("M", line):
            if "\\querymenu.sql" in line or "\\dict\\" in line or "\\init\\" in line or "\\addorg\\" in line:
                svnurlfile = ''.join(line[8:].split())  # 去掉回车符(\r)、换行符(\n)、水平制表符(\t)、垂直制表符(\v)、换页符(\f)）
                print(svnurlfile)  # 下面所有print都是为了方便看日志
                fp1 = os.path.dirname(svnurlfile)
                fp2 = svnurlfile.replace('\\', '/')
                svnurl1 = mysvn_url + "/" + fp2
                svnurl = unicode(svnurl1, 'GB2312')  # 转换成svn识别编码，主要是为了能识别中文的svn链接
                filename = os.path.basename(svnurlfile)
                diff_test = p.diff_peg('', svnurl, peg_revision, revision_start, revision_end,
                                       diff_options=['-b', '-w'], diff_deleted=False,
                                       diff_added=True)  # 版本之间文件的差异,忽略所有空格,空白的变化。
                f = open('media.txt',
                         'wb+')  # media.txt是一个内容会变化的文件,先生成写入diff_test，再读取每一行的数据,以二进制方式写入，保证后面sql文件是doc/windows,GB2312格式
                f.write(
                    diff_test)  # 把差异内容写入media.txt，media中文意思为介质的意思,意思是把文件一个一个有顺序地处理，处理完成一个才轮到下一个文件。所以media.txt的内容只保留处理最后一个文件的内容
                f.close()  # 关闭文件才完成写入动作
                f = open('media.txt', 'r')  # 必须关闭文件后才能读取文件
                C = p.cat(svnurl, revision_end, peg_revision)
                f1 = open('media1.txt', 'wb+')
                f1.write(C)
                f1.close()
                f1 = open('media1.txt', 'rb')  # 必须关闭文件后才能读取文件
                f2 = open(newserver + "\\" + svnurlfile, 'wb+')  # 生成文件
                L = set()
                for i in f1.readlines():  # 只要一个use
                    if re.match("^use ", i):  # 只从每一行的开始匹配字符串use,match函数只匹配开头的字符
                        if i.split()[0] not in L:
                            f2.writelines(i.split()[0] + " " + i.split()[1])
                            L.add(i.split()[0])
                f2.write("\r\n")
                f2.write("go\r\n")
                f2.close()
                f2 = open(newserver + "\\" + svnurlfile, 'a')  # 增加内容
                # f2.write("go\n")#换行符\n必须要,往下是换行后再写入内容,否则go与下一句可能会同行
                for line1 in f.readlines():
                    if re.match("\+", line1) and not re.match("\+\+\+", line1) and not re.match("\+ {0,}--",
                                                                                                line1) and not re.match(
                            "\+use",
                            line1):  # 只把+的筛选出来，把+++，@@,+--（注释sql的语句）过滤掉,\+的\为转义字符,match函数只匹配开头的字符,这里也可以用re.search("^+",line1),re.search("\A\+",line1),^+或者\A\+均表示开头匹配。
                        print
                        line1
                        f2.write(line1.lstrip(
                            "+"))  # 把开头的“+”去掉;循环写完一个文件，再关闭文件，不能才写完一行就关闭文件。Python中的strip用于去除字符串的首尾字符，同理，lstrip用于去除左边的字符，rstrip用于去除右边的字符
                        # f2.close()  #所以不能在这里关闭。以下就是关闭的正确姿势
                f2.write("go\n")  # 最后加一个go
                f2.close()  # 循环写完一个文件，再关闭文件
        if ".sql" in line and re.match("A", line):
            if "\\querymenu.sql" in line or "\\dict\\" in line or "\\init\\" in line:
                svnurlfile = ''.join(line[8:].split())  # 去掉回车符(\r)、换行符(\n)、水平制表符(\t)、垂直制表符(\v)、换页符(\f)）
                print(svnurlfile)  # 下面所有print都是为了方便看日志
                fp1 = os.path.dirname(svnurlfile)
                fp2 = svnurlfile.replace('\\', '/')
                svnurl1 = mysvn_url + "/" + fp2
                svnurl = unicode(svnurl1, 'GB2312')  # 转换成svn识别编码，主要是为了能识别中文的svn链接
                localpath1 = newserver + "\\" + fp1
                localpath = unicode(localpath1, 'GB2312')
                print("fp1:")
                print(fp1)
                print("svnurl:")
                print(svnurl)
                print(localpath)
                p.export(svnurl, localpath, force=True)

    # 处理增量目录 query的querymenu.sql,dict,init,end
    print
    "处理增量目录 query的querymenu.sql,dict,init,end"

    # 处理增量目录 table begin
    os.chdir(work_path)
    s = open(work_path + "\\11.txt", 'rb')
    for line in s.readlines():  # 这里的line表示mysvn_url地址
        if ".sql" in line and re.match("M", line):
            if "\\table\\" in line:
                svnurlfile = ''.join(line[8:].split())  # 去掉回车符(\r)、换行符(\n)、水平制表符(\t)、垂直制表符(\v)、换页符(\f)）
                print(svnurlfile)  # 下面print都是为了方便看日志
                fp1 = os.path.dirname(svnurlfile)
                fp2 = svnurlfile.replace('\\', '/')
                svnurl1 = mysvn_url + "/" + fp2
                svnurl = unicode(svnurl1, 'GB2312')  # 转换成svn识别编码，主要是为了能识别中文的svn链接
                filename = os.path.basename(svnurlfile)  # 目标表的sql脚本名称
                p = pysvn.Client()
                f = open(r"file.txt", "wb+")
                file_text = p.cat(svnurl, revision_end, peg_revision)  # 把目标表sql脚本整个输出
                f.write(file_text)
                f.close()

                # 找出 table 与 table 的行号 begin，即每一个 table 的开始行与结束行

                x = open(r"file.txt", "rb")
                y = open(r"tables.txt", "w+")
                for num, line in enumerate(x):
                    if re.match("--====================", line):
                        y.write(str(num))
                        y.write("\n")
                y.close()

                # 找出 table 与 table 的行号 end

                # 写入最后一行的行号 begin

                x = open(r"file.txt", "rb")
                y = open(r"tables.txt", "a")
                lastline = x.readlines()
                y.write(str(len(lastline)))
                y.close()

                # 写入最后一行的行号 end

                # 筛选出 table 变化的行 begin
                x = open(r"changelist.txt", "w+")
                changelist = p.annotate(svnurl, revision_start1, revision_end, peg_revision)
                N = 0
                while (N <= len(changelist)):
                    x.write(str(changelist[N:N + 1]))
                    x.write("\n")
                    N = N + 1
                x.close()
                y = open(r"changelist.txt", "r")
                z = open(r"changelinelist.txt", "w+")
                for line in y.readlines():
                    t = re.sub("{'date':" + "(.*?)" + "author': u'", '', line, flags=re.S)
                    if len(t) > 5:
                        t1 = re.compile("number': " + "(.*?)" + ", 'author", flags=re.S)
                        t2 = t1.findall(line)
                        z.write(str(t2[0]))
                        z.write("\n")
                z.close()
                # 筛选出 table 变化的行 end

                # 筛选出变化的行所在的表 begin

                # 处理变化行的行号 begin
                y = open(r"tables.txt", "r")
                z = open(r"changelinelist.txt", "r")
                Y = list(y)
                N = 0
                while N < len(Y):
                    I = ''.join(Y[N].split())  # 把换行符去掉
                    Y[N] = I
                    N += 1
                print(Y)
                Z = list(z)
                N = 0
                while N < len(Z):
                    I = ''.join(Z[N].split())  # 把换行符去掉
                    Z[N] = I
                    N += 1
                print(Z)

                # 处理变化行的行号 end

                # 每一变化的行的行号跟目标表的开始行与结束行的行号作比较，即找出变化的行所在的表 begin

                N = 0
                M = 0
                y = open(r"tablesout.txt", "wb+")
                while (M < len(Z)):
                    while (N < len(Y)):
                        if int(Z[M]) >= int(Y[N]) and int(Z[M]) < int(Y[N + 1]) and int(Z[M]) <> int(len(lastline) - 1):
                            y = open(r"tablesout.txt", "a")
                            print(Y[N], Z[M], Y[N + 1])
                            y.write(str(Y[N]) + " " + str(Y[N + 1]))
                            y.write("\n")
                            N += 1
                        else:
                            N += 1
                    M += 1
                    y.close()
                    N = N - len(Y)  # 把N的值重新设置为0，一直到M结束
                # 每一变化的行的行号跟目标表的开始行与结束行的行号作比较，即找出变化的行所在的表 end

                # 筛选出变化的行所在的表 end

                # 去掉重复输出的表 begin,即多行在同一个 table 表里变化，只输出一个 table 表，lineset=set()为行的集合
                lineset = set()
                outfile = open(r"tablesout2.txt", "w+")
                for line in open(r"tablesout.txt", "r"):
                    if line not in lineset:
                        outfile.write(line)
                        lineset.add(line)
                outfile.close()
                # 去掉重复的行 end

                # 开始把有变化的 table 表 写入到目标文件 begin

                f1 = open('file.txt', 'rb')  # 必须关闭文件后才能读取文件
                f2 = open(newserver + "\\" + svnurlfile, 'wb+')  # 生成文件
                L = set()
                for i in f1.readlines():  # 只要一个use
                    if re.match("use", i):  # 只从每一行的开始匹配字符串use,match函数只匹配开头的字符
                        if i.split()[0] not in L:
                            f2.writelines(i.split()[0] + " " + i.split()[1])
                            L.add(i.split()[0])
                f2.write("\r\n")
                f2.write("go\r\n")
                f2.close()
                y = open(r"tablesout2.txt", "r")
                for i in y.readlines():
                    print(i)
                    line1 = int(i.split()[0])  # 以空格为分割符获取第一个数，即行号
                    line2 = int(i.split()[1])  # 以空格为分割符获取第二个数，即行号
                    x = open(r"file.txt", "r")
                    z = open(newserver + "\\" + svnurlfile, "a")
                    for line in x.readlines()[line1:line2]:
                        if not re.match(" {0,}--", line):
                            print(line)
                            z.write(line)
                # z=open(newserver+"\\"+svnurlfile,"a")
                # z.write("go\n")
                z.close()
                # 对新增加的sql文件进行去注释(/*……*/)处理
                a = open(newserver + "\\" + svnurlfile, 'rb')
                b = a.read()
                c = open(newserver + "\\" + svnurlfile, 'wb')
                d = re.compile(" {0,}/\*.*?\*/", re.S)
                e = re.sub(d, "", b)
                c.write(e)
                c.close()
                a.close()
                # 开始把有变化的 table 表 写入到目标文件 end

        if ".sql" in line and re.match("A", line):
            if "\\table\\" in line:
                svnurlfile = ''.join(line[8:].split())  # 去掉回车符(\r)、换行符(\n)、水平制表符(\t)、垂直制表符(\v)、换页符(\f)）
                print(svnurlfile)  # 下面所有print都是为了方便看日志
                fp1 = os.path.dirname(svnurlfile)
                fp2 = svnurlfile.replace('\\', '/')
                svnurl1 = mysvn_url + "/" + fp2
                svnurl = unicode(svnurl1, 'GB2312')  # 转换成svn识别编码，主要是为了能识别中文的svn链接
                localpath1 = newserver + "\\" + fp1
                localpath = unicode(localpath1, 'GB2312')
                print("fp1:")
                print(fp1)
                print("svnurl:")
                print(svnurl)
                print(localpath)
                p.export(svnurl, localpath, force=True)
                # 对新增加的sql文件进行去注释(/*……*/)处理
                a = open(newserver + "\\" + svnurlfile, 'rb')
                b = a.read()
                c = open(newserver + "\\" + svnurlfile, 'wb')
                d = re.compile("^ {0,}--.*", re.M)
                d1 = re.compile(" {0,}/\*.*?\*/", re.S)
                e = re.sub(d, "", b)
                f = re.sub(d1, "", e)
                c.write(f)
                c.close()
                a.close()

    # 处理增量目录 table end
    print("处理增量目录 table end")

    # 清空升级包目录再生成目录 begin
    if os.path.exists(PATCH_NAME + "\\server"):
        shutil.rmtree(PATCH_NAME + "\\server")
        shutil.rmtree(PATCH_NAME + "\\doc")
        os.makedirs(PATCH_NAME + "\\server")
        os.makedirs(PATCH_NAME + "\\doc")
    else:
        os.makedirs(PATCH_NAME + "\\server")
        os.makedirs(PATCH_NAME + "\\doc")
    # 清空升级包目录再生成目录 end

    # KD30SQL.exe 处理
    os.chdir(work_path + "\\server\\tradedb")
    if os.path.exists(work_path + "\\server\\tradedb\\KD30SQL.exe"):
        shutil.copy(work_path + "\\server\\tradedb\\KD30SQL.exe", work_path + "\\newserver\\server")
    else:
        print(work_path + "\\server\\tradedb\\KD30SQL.exe" + "不存在")
    # NTWDBLIB.DLL 处理
    if os.path.exists(work_path + "\\server\\tradedb\\NTWDBLIB.DLL"):
        shutil.copy(work_path + "\\server\\tradedb\\NTWDBLIB.DLL", work_path + "\\newserver\\server")
    else:
        print(work_path + "\\server\\tradedb\\NTWDBLIB.DLL" + "不存在")
    # PatchVer.sql 处理
    os.chdir(work_path + "\\newserver\\server")
    a = open('PatchVer.sql', 'w+')
    a.write('''use run
go
exec nb_add_version \'''' + Sql_version + '''\'
go
  ''')
    a.close()

    # 升级脚本文件处理
    # 01_交易服务器(run).bat begin
    os.chdir(work_path + "\\newserver\\server")
    # run顺序列表，列表特点之一是有顺序的，以后顺序变了，可以调一下以下列表的顺序，或者有新的目录增加，按照先后顺序在列表中添加即可。
    orderrunlist = ["tradedb\\table\\", "tradedb\\stat\\", "tradedb\\init\\", "tradedb\\dict\\", "tradedb\\query\\",
                    "tradedb\\proc_opt\\", "tradedb\\proc\\", "tradedb\\FISUPDATE\\proc\\",
                    "tradedb\\interface_vip\\table\\", "tradedb\\interface_vip\\init\\",
                    "tradedb\\interface_vip\\dict\\", "tradedb\\interface_vip\\query\\",
                    "tradedb\\interface_vip\\proc\\", "tradedb\\report\\", "tradedb\\DBCONTROL\\table\\",
                    "tradedb\\DBCONTROL\\init\\", "tradedb\\DBCONTROL\\proc\\", "tradedb\\init\\datafix.sql"]
    # 目录存在，则写入Q1_交易.bat文件，哪些目录该写入哪个bat按打包手册规定的为准。
    if os.path.exists(work_path + "\\newserver\\server\\tradedb"):
        b = open("01_交易服务器(run).bat", "w+")
        b.write('''@ECHO ========================================================================
@ECHO    新一代Win版 融资融券''' + Sql_version + '''升级包  交易服务器(run).bat
@ECHO ------------------------------------------------------------------------
@ECHO 为保证正常执行升级脚本请注意以下几点：
@ECHO    1. 请关闭所有的数据库连接
@ECHO    2. 本升级包有创建新的表,请停止你的数据库复制
@ECHO ========================================================================
pause
kd30sql -T -U交易库用户名 -P交易库密码 -S交易库服务器地址  -ESQL .\PatchVer.sql

''')
        b.close()
        # 从顺序列表orderrunlist中获取数组迭代写入bat,存在则写入，不存在则跳过，每一个顺序迭代，都使用sort正序进行排序，方便前后两个版本对比bat，避免顺序错乱不好对比。
        for i in orderrunlist:
            print("run顺序：" + i)
            a = open(work_path + "\\11.txt", 'rb')
            c = open("01_交易服务器(run).bat", "a")
            drun = ("noexist")
            lrun = []
            for line in a.readlines():
                if "server\\tradedb" in line and re.match("A", line) or "server\\tradedb" in line and re.match("M",
                                                                                                               line):
                    if i in line:
                        lrun.append(line)
            lrun.sort()  # 正序排序
            for i in lrun:
                c.write(re.sub(r"\r", "", i))
                drun = ("exist")
            if drun == ("exist"):  # 按书写规范，有每一个顺序结束后换行进行分类。
                c.write("\n")
        c = open("01_交易服务器(run).bat", "a")
        c.write("pause\n")
        c.close()
        a.close()
        c = open("01_交易服务器(run).bat", "rb")
        f = c.read()
        c1 = open("01_交易服务器(run).bat", "wb")
        p = re.compile(".*server\\\\", re.M)
        q = re.sub(p, r"kd30sql -T -U交易库用户名 -P交易库密码 -S交易库服务器地址  -ESQL .\\", f)  # 按打包手册规范书写，re.sub字符查找并替换，详细百度re.sub
        c1.write(q)
        c1.close()
        # 把前面的datafix.sql去掉 begin
        a = open("01_交易服务器(run).bat", "rb")
        b = []  # 建立一个空列表用来存放Q1_交易.bat每一行
        for i in a.readlines():
            b.append(i)
        for i in b:
            if "datafix.sql" in i:
                I = i
                b.remove(I)  # remove只去除匹配的那一个datafix.sql
                break  # 只找前面一个
        print(b)
        # 把前面的datafix.sql去掉 end
        c = open("01_交易服务器(run).bat", "wb")
        for i in b:
            c.write(i)
            print(i)
        c.close()
        # 01_交易服务器(run).bat end
        # 02_交易服务器(report).bat begin
    os.chdir(work_path + "\\newserver\\server")
    # run顺序列表，列表特点之一是有顺序的，以后顺序变了，可以调一下以下列表的顺序，或者有新的目录增加，按照先后顺序在列表中添加即可。
    orderrunlist = ["reportdb\\table\\", "reportdb\\proc\\"]
    # 目录存在，则写入Q1_交易.bat文件，哪些目录该写入哪个bat按打包手册规定的为准。
    if os.path.exists(work_path + "\\newserver\\server\\reportdb"):
        b = open("02_交易服务器(report).bat", "w+")
        b.write('''@ECHO ========================================================================
@ECHO    新一代Win版 融资融券''' + Sql_version + '''升级包  交易服务器(report).bat
@ECHO ------------------------------------------------------------------------
@ECHO 为保证正常执行升级脚本请注意以下几点：
@ECHO    1. 请关闭所有的数据库连接
@ECHO    2. 本升级包有创建新的表,请停止你的数据库复制
@ECHO ========================================================================
pause

''')
        b.close()
        # 从顺序列表orderrunlist中获取数组迭代写入bat,存在则写入，不存在则跳过，每一个顺序迭代，都使用sort正序进行排序，方便前后两个版本对比bat，避免顺序错乱不好对比。
        for i in orderrunlist:
            print("run顺序：" + i)
            a = open(work_path + "\\11.txt", 'rb')
            c = open("02_交易服务器(report).bat", "a")
            drun = ("noexist")
            lrun = []
            for line in a.readlines():
                if "server\\reportdb" in line and re.match("A", line) or "server\\reportdb" in line and re.match("M",
                                                                                                                 line):
                    if i in line:
                        lrun.append(line)
            lrun.sort()  # 正序排序
            for i in lrun:
                c.write(re.sub(r"\r", "", i))
                drun = ("exist")
            if drun == ("exist"):  # 按书写规范，有每一个顺序结束后换行进行分类。
                c.write("\n")
        c = open("02_交易服务器(report).bat", "a")
        c.write("pause\n")
        c.close()
        a.close()
        c = open("02_交易服务器(report).bat", "rb")
        f = c.read()
        c1 = open("02_交易服务器(report).bat", "wb")
        p = re.compile(".*server\\\\", re.M)
        q = re.sub(p, r"kd30sql -T -U交易库用户名 -P交易库密码 -S交易库服务器地址  -ESQL .\\", f)  # 按打包手册规范书写，re.sub字符查找并替换，详细百度re.sub
        c1.write(q)
        c1.close()
    # 02_交易服务器(report).bat end
    # 03_风控服务器(run).bat begin
    os.chdir(work_path + "\\newserver\\server")
    # 风控run顺序列表，列表特点之一是有顺序的，以后顺序变了，可以调一下以下列表的顺序，或者有新的目录增加，按照先后顺序在列表中添加即可。
    orderfkrunlist = ["tradedb\\table\\", "tradedb\\stat\\", "tradedb\\init\\", "tradedb\\dict\\", "tradedb\\query\\",
                      "tradedb\\proc_opt\\", "tradedb\\proc\\", "tradedb\\FISUPDATE\\proc\\",
                      "tradedb\\interface_vip\\table\\", "tradedb\\interface_vip\\init\\",
                      "tradedb\\interface_vip\\dict\\", "tradedb\\interface_vip\\query\\",
                      "tradedb\\interface_vip\\proc\\", "tradedb\\report\\", "tradedb\\DBCONTROL\\table\\",
                      "tradedb\\DBCONTROL\\init\\", "tradedb\\DBCONTROL\\proc\\"]
    # 目录存在，则写入Q1_风控.bat文件，哪些目录该写入哪个bat按打包手册规定的为准。
    if os.path.exists(work_path + "\\newserver\\server\\tradedb"):
        b = open("03_风控服务器(run).bat", "w+")
        b.write('''@ECHO ========================================================================
@ECHO    新一代Win版 融资融券''' + Sql_version + '''升级包  风控服务器(run).bat
@ECHO ------------------------------------------------------------------------
@ECHO 为保证正常执行升级脚本请注意以下几点：
@ECHO    1. 请关闭所有的数据库连接
@ECHO    2. 本升级包有创建新的表,请停止你的数据库复制
@ECHO ========================================================================
pause
kd30sql -T -U风控库用户名 -P风控库密码 -S风控库服务器地址  -ESQL .\PatchVer.sql

''')
        b.close()
        # 从顺序列表orderfkrunlist中获取数组迭代写入bat,存在则写入，不存在则跳过，每一个顺序迭代，都使用sort正序进行排序，方便前后两个版本对比bat，避免顺序错乱不好对比。
        for i in orderfkrunlist:
            print("fkrun顺序：" + i)
            a = open(work_path + "\\11.txt", 'rb')
            c = open("03_风控服务器(run).bat", "a")
            dfkrun = ("noexist")
            lfkrun = []
            for line in a.readlines():
                if "server\\tradedb" in line and re.match("A", line) or "server\\tradedb" in line and re.match("M",
                                                                                                               line):
                    if i in line:
                        lfkrun.append(line)
            lfkrun.sort()  # 正序排序
            for i in lfkrun:
                c.write(re.sub(r"\r", "", i))
                dfkrun = ("exist")
            if dfkrun == ("exist"):  # 按书写规范，有每一个顺序结束后换行进行分类。
                c.write("\n")
        c = open("03_风控服务器(run).bat", "a")
        c.write("pause\n")
        c.close()
        a.close()
        c = open("03_风控服务器(run).bat", "rb")
        f = c.read()
        c1 = open("03_风控服务器(run).bat", "wb")
        p = re.compile(".*server\\\\", re.M)
        q = re.sub(p, r"kd30sql -T -U风控库用户名 -P风控库密码 -S风控库服务器地址  -ESQL .\\", f)  # 按打包手册规范书写，re.sub字符查找并替换，详细百度re.sub
        c1.write(q)
        c1.close()
        # 把前面的datafix.sql去掉 把后面的datafix_riskdb.sql begin
        a = open("03_风控服务器(run).bat", "rb")
        b = []  # 建立一个空列表用来存放Q1_风控.bat每一行
        for i in a.readlines():
            b.append(i)
        for i in b:
            if "datafix.sql" in i:
                print("I0:" + i)
                I0 = i
                b.remove(I0)  # remove只去除匹配的那一个datafix.sql
                break  # 只找前面一个
        I1 = ''
        datafix = ''
        for i in b:
            if "datafix_riskdb.sql" in i:
                I1 = i
                datafix = ('exist')
        if datafix == 'exist':
            for i in enumerate(b):
                if i[1] == I1:
                    I2 = i[0]
            del b[I2]
        print(b)
        # 把前面的datafix.sql去掉 把后面的datafix_riskdb.sql begin end
        c = open("03_风控服务器(run).bat", "wb")
        for i in b:
            c.write(i)
            print(i)
        c.close()
        # 03_风控服务器(run).bat end
        # 04_风控服务器(riskdb).bat begin
    os.chdir(work_path + "\\newserver\\server")
    # 风控run顺序列表，列表特点之一是有顺序的，以后顺序变了，可以调一下以下列表的顺序，或者有新的目录增加，按照先后顺序在列表中添加即可。
    orderfkrunlist = ["riskdb\\init\\datafix_riskdb.sql", "riskdb\\table\\", "riskdb\\init\\", "riskdb\\proc\\"]
    # 目录存在，则写入04_风控服务器(riskdb).bat文件，哪些目录该写入哪个bat按打包手册规定的为准。
    if os.path.exists(work_path + "\\newserver\\server\\riskdb"):
        b = open("04_风控服务器(riskdb).bat", "w+")
        b.write('''@ECHO ========================================================================
@ECHO    新一代Win版 融资融券''' + Sql_version + '''升级包  风控服务器(riskdb).bat
@ECHO ------------------------------------------------------------------------
@ECHO 为保证正常执行升级脚本请注意以下几点：
@ECHO    1. 请关闭所有的数据库连接
@ECHO    2. 本升级包有创建新的表,请停止你的数据库复制
@ECHO ========================================================================
pause

''')
        b.close()
        # 从顺序列表orderfkrunlist中获取数组迭代写入bat,存在则写入，不存在则跳过，每一个顺序迭代，都使用sort正序进行排序，方便前后两个版本对比bat，避免顺序错乱不好对比。
        for i in orderfkrunlist:
            print("fkrun顺序：" + i)
            a = open(work_path + "\\11.txt", 'rb')
            c = open("04_风控服务器(riskdb).bat", "a")
            dfkrun = ("noexist")
            lfkrun = []
            for line in a.readlines():
                if "server\\riskdb" in line and re.match("A", line) or "server\\riskdb" in line and re.match("M", line):
                    if i in line:
                        lfkrun.append(line)
            lfkrun.sort()  # 正序排序
            for i in lfkrun:
                c.write(re.sub(r"\r", "", i))
                dfkrun = ("exist")
            if dfkrun == ("exist"):  # 按书写规范，有每一个顺序结束后换行进行分类。
                c.write("\n")
        c = open("04_风控服务器(riskdb).bat", "a")
        c.write("pause\n")
        c.close()
        a.close()
        c = open("04_风控服务器(riskdb).bat", "rb")
        f = c.read()
        c1 = open("04_风控服务器(riskdb).bat", "wb")
        p = re.compile(".*server\\\\", re.M)
        q = re.sub(p, r"kd30sql -T -U风控库用户名 -P风控库密码 -S风控库服务器地址  -ESQL .\\", f)  # 按打包手册规范书写，re.sub字符查找并替换，详细百度re.sub
        c1.write(q)
        c1.close()
        # 把前面的datafix.sql去掉 把后面的datafix_riskdb.sql begin
        a = open("04_风控服务器(riskdb).bat", "rb")
        b = []  # 建立一个空列表用来存放Q1_风控.bat每一行
        for i in a.readlines():
            b.append(i)
        for i in b:
            if "datafix.sql" in i:
                print("I0:" + i)
                I0 = i
                b.remove(I0)  # remove只去除匹配的那一个datafix.sql
                break  # 只找前面一个
        I1 = ''
        datafix = ''
        for i in b:
            if "datafix_riskdb.sql" in i:
                I1 = i
                datafix = ('exist')
        if datafix == 'exist':
            for i in enumerate(b):
                if i[1] == I1:
                    I2 = i[0]
            del b[I2]
        print(b)
        # 把前面的datafix.sql去掉 把后面的datafix_riskdb.sql begin end
        c = open("04_风控服务器(riskdb).bat", "wb")
        for i in b:
            c.write(i)
            print(i)
        c.close()
    # 04_风控服务器(riskdb).bat end
    # 05_历史服务器(run).bat begin
    # his顺序列表 begin
    orderhislist = ["\\TCrt_rundbProc.sql", "\\Thist_run.sql", "\\THist_run_credit.sql", "\\THist_run_openfund.sql"]
    if os.path.exists(work_path + "\\newserver\\server\\querydb"):
        b = open("05_历史服务器(run).bat", "w+")
        b.write('''@ECHO ========================================================================
@ECHO    新一代Win版 融资融券''' + Sql_version + '''升级包  历史服务器(run).bat
@ECHO ------------------------------------------------------------------------
@ECHO 为保证正常执行升级脚本请注意以下几点：
@ECHO    1. 请关闭所有的数据库连接
@ECHO    2. 本升级包有创建新的表,请停止你的数据库复制
@ECHO ========================================================================
pause
''')
        b.close()
        for i in orderhislist:
            print("his顺序：" + i)
            a = open(work_path + "\\11.txt", 'rb')
            c = open("05_历史服务器(run).bat", "a")
            dhis = ("noexist")
            lhis = []
            for line in a.readlines():
                if "server\\querydb" in line and re.match("A", line) or "server\\querydb" in line and re.match("M",
                                                                                                               line):
                    if i in line:
                        lhis.append(line)
            lhis.sort()
            for i in lhis:
                c.write(re.sub(r"\r", "", i))
                dhis = ("exist")
            if dhis == ("exist"):
                c.write("\n")
        c = open("05_历史服务器(run).bat", "a")
        c.write("pause\n")
        c.close()
        a.close()
        c = open("05_历史服务器(run).bat", "rb")
        f = c.read()
        c1 = open("05_历史服务器(run).bat", "wb")
        p = re.compile(".*server\\\\", re.M)
        q = re.sub(p, r"kd30sql -T -U历史库用户名 -P历史库密码 -S历史库服务器地址  -ESQL .\\", f)
        print(q)
        c1.write(q)
        c1.close()
        # 05_历史服务器(run).bat end
    # 06_历史服务器(his).bat begin
    # his顺序列表 begin
    orderhislist = ["querydb\\table\\", "querydb\\init\\", "querydb\\FISUPDATE\\proc\\"]
    if os.path.exists(work_path + "\\newserver\\server\\querydb"):
        b = open("06_历史服务器(his).bat", "w+")
        b.write('''@ECHO ========================================================================
@ECHO    新一代Win版 融资融券''' + Sql_version + '''升级包  历史服务器(his).bat
@ECHO ------------------------------------------------------------------------
@ECHO 为保证正常执行升级脚本请注意以下几点：
@ECHO    1. 请关闭所有的数据库连接
@ECHO    2. 本升级包有创建新的表,请停止你的数据库复制
@ECHO ========================================================================
pause
''')
        b.close()
        for i in orderhislist:
            print("his顺序：" + i)
            a = open(work_path + "\\11.txt", 'rb')
            c = open("06_历史服务器(his).bat", "a")
            dhis = ("noexist")
            lhis = []
            for line in a.readlines():
                if "server\\querydb" in line and re.match("A", line) or "server\\querydb" in line and re.match("M",
                                                                                                               line):
                    if "\\TCrt_rundbProc.sql" not in line and re.match("A",
                                                                       line) or "\\TCrt_rundbProc.sql" not in line and re.match(
                            "M", line):
                        if "\\Thist_run.sql" not in line and re.match("A",
                                                                      line) or "\\Thist_run.sql" not in line and re.match(
                                "M", line):
                            if "\\THist_run_credit.sql" not in line and re.match("A",
                                                                                 line) or "\\THist_run_credit.sql" not in line and re.match(
                                    "M", line):
                                if "\\THist_run_openfund.sql" not in line and re.match("A",
                                                                                       line) or "\\THist_run_openfund.sql" not in line and re.match(
                                        "M", line):
                                    if i in line:
                                        lhis.append(line)
            lhis.sort()
            for i in lhis:
                c.write(re.sub(r"\r", "", i))
                dhis = ("exist")
            if dhis == ("exist"):
                c.write("\n")
        c = open("06_历史服务器(his).bat", "a")
        c.write("pause\n")
        c.close()
        a.close()
        c = open("06_历史服务器(his).bat", "rb")
        f = c.read()
        c1 = open("06_历史服务器(his).bat", "wb")
        p = re.compile(".*server\\\\", re.M)
        q = re.sub(p, r"kd30sql -T -U历史库用户名 -P历史库密码 -S历史库服务器地址  -ESQL .\\", f)
        print(q)
        c1.write(q)
        c1.close()
        # 06_历史服务器(his).bat end

See
the
list
of
available
environment
variables
删除
Execute
Windows
batch
command
[Help]
命令
setlocal
EnableDelayedExpansion

:加载环境变量
set

set
BUILD_ID = NOKILL

rem
获取工作路径
set
mysvn_url = % mysvn_url: =\ %
for / f "tokens=*" % % i in ("%mysvn_url%.$") do set  last_path= % % ~ni
set
work_path = % WORKSPACE %\ % last_path %

if exist % work_path %\newserver (
xcopy % work_path % \newserver % PATCH_NAME % / s / h / y
)
参阅
可用环境变量列表
删除
增加构建步骤
构建后操作
Editable
Email
Notification
[Help]
Disable
Extended
Email
Publisher
Help
for feature: Disable
Extended
Email
Publisher
Allows
the
user
to
disable
the
publisher,
while maintaining the settings
Project
Recipient
List
$DEFAULT_RECIPIENTS
Help
for feature: Project
Recipient
List
Comma - separated
list
of
email
address
that
should
receive
notifications
for this project.
    Project
    Reply - To
    List
$DEFAULT_REPLYTO
Help
for feature: Project
Reply - To
List
Comma - separated
list
of
email
address
that
should
be in the
Reply - To
header
for this project.
    Content
    Type
    Help
    for feature: Content
    Type
    Default
    Subject
$DEFAULT_SUBJECT
Help
for feature: Default
Subject
Default
Content
$SVN_URL已经更新至$SVN_REVISION, 自动打包中
构建的公共参数值列表如下：
升级包路径及名称：$PATCH_NAME
侦听的svn地址：$SVN_URL
svn地址：$mysvn_url
起始版本号：$Start_version
终止版本号：$TO_VERSION
前端版本号：$Client_version
后台blmdll版本号：$Lbmdll_version
数据库的版本号：$Sql_version
0
为不写入版本号, 1
为写入版本号并全部编译：$first
lbmdll
编译总工程文件
ProjectAll.snl
的预期的具体位置：$ProjectAll
Help
for feature: Default
Content
Attachments
Help
for feature: Attachments
Can
use
wildcards
like
'module/dist/**/*.zip'.See
the @ includes
of
Ant
fileset
for the exact format.The base directory is the workspace.
Attach
Build
Log
Help
for feature: Attach
Build
Log
Content
Token
Reference
Help
for feature: Content
Token
Reference

Advanced
Settings...
删除
Trigger
parameterized
build
on
other
projects
[Help]
Build
Triggers
Projects
to
build
2
_python_client标准版6770
Help
for feature: Projects
to
build
Trigger
when
build is Help
for feature: Trigger
when
build is
Trigger
build
without
parameters
Help
for feature: Trigger
build
without
parameters
Current
build
parameters
Help
for feature: Build
Triggers
删除
Add
Parameters

Add
trigger...
删除
增加构建后操作步骤
保存
应用
帮助我们本地化当前页
生成
页面: 2018 - 8 - 18
上午10时10分40秒REST
APIJenkins
ver.
1.651