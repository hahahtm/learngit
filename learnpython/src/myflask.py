#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""author:hahahtm
   date:

"""
"""第一部分，初始化：所有的Flask都必须创建程序实例，
web服务器使用wsgi协议，把客户端所有的请求都转发给这个程序实例
程序实例是Flask的对象，一般情况下用如下方法实例化
Flask类只有一个必须指定的参数，即程序主模块或者包的名字，__name__是系统变量，该变量指的是本py文件的文件名"""

from flask import Flask

app = Flask(__name__)


#  第二部分，路由和视图函数：
#  客户端发送url给web服务器，web服务器将url转发给flask程序实例，程序实例
#  需要知道对于每一个url请求启动那一部分代码，所以保存了一个url和python函数的映射关系。
#  处理url和函数之间关系的程序，称为路由
#  在flask中，定义路由最简便的方式，是使用程序实例的app.route装饰器，把装饰的函数注册为路由

@app.route('/')
def hello_world():
    return  "lovecong"


#  第三部分：程序实例用run方法启动flask集成的开发web服务器
#  __name__ == '__main__'是python常用的方法，表示只有直接启动本脚本时候，才用app.run方法
#  如果是其他脚本调用本脚本，程序假定父级脚本会启用不同的服务器，因此不用执行app.run()
#  服务器启动后，会启动轮询，等待并处理请求。轮询会一直请求，直到程序停止。

if __name__ == '__main__':
    print('dd', __name__)
    app.run()