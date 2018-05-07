# 第一个 python 程序

* 在命令行模式运行.py文件和在Python交互式环境下直接运行Python代码有所不同。Python交互式环境会把每一行Python代码的结果自动打印出来，但是，直接运行Python代码却不会。

* 想要输出结果，必须自己用print()打印出来。

* Python交互模式的代码是输入一行，执行一行，而命令行模式下直接运行.py文件是一次性执行该文件内的所有代码。可见，Python交互模式主要是为了调试Python代码用的，也便于初学者学习，它不是正式运行Python代码的环境！

* 用文本编辑器写Python程序，然后保存为后缀为.py的文件，就可以用Python直接运行这个程序了。

* Python的交互模式和直接运行.py文件有什么区别呢？

	直接输入python进入交互模式，相当于启动了Python解释器，但是等待你一行一行地输入源代码，每输入一行就执行一行。

	直接运行.py文件相当于启动了Python解释器，然后一次性把.py文件的源代码给执行了，你是没有机会以交互的方式输入源代码的。

* python 代码运行助手
	
	Python代码运行助手可以让你在线输入Python代码，然后通过本机运行的一个Python脚本来执行代码。

	[python代码运行助手源码](https://github.com/MrQuJL/study-python/blob/master/01_第一个python程序/learning.py "python代码运行助手源码") （python环境安装好，启动后放到后台即可）

	[在该网页上写python代码即可](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432523496782e0946b0f454549c0888d05959b99860f000 "在线写python")

* print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出：

	```print('The quick brown fox', 'jumps over', 'the lazy dog')```
	输出：The quick brown fox jumps over the lazy dog

* 当你输入name = input()并按下回车后，Python交互式命令行就在等待你的输入了。这时，你可以输入任意字符，然后按回车后完成输入。

* 输入完成后，不会有任何提示，Python交互式命令行又回到>>>状态了。那我们刚才输入的内容到哪去了？答案是存放到name变量里了。可以直接输入name查看变量内容

* 但是程序运行的时候，没有任何提示信息告诉用户：“嘿，赶紧输入你的名字”，这样显得很不友好。幸好，input()可以让你显示一个字符串来提示用户，于是我们把代码改成：```name = input('please enter your name: ')```


