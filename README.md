## 运行命令
```
    python manage.py makemigrations
```

```
    python manage.py migrate
```

```
    python manage.py runserver
```

## 部署
## 方案一
（失败）通过pycharm将Django项目部署到云服务器 uWSGI+Nginx+sqlite
- 参考： https://www.cnblogs.com/kongguanghua/p/13447559.html


### uWSGI
uWSGI是一个Web服务器，它实现了WSGI协议、uwsgi、http等协议。Nginx中HttpUwsgiModule的作用是与uWSGI服务器进行交换。

要注意 WSGI / uwsgi / uWSGI 这三个概念的区分。

- WSGI是一种通信协议。
- uwsgi同WSGI一样是一种通信协议。
- 而uWSGI是实现了uwsgi和WSGI两种协议的Web服务器。
uwsgi协议是一个uWSGI服务器自有的协议，它用于定义传输信息的类型（type of information），每一个uwsgi packet前4byte为传输信息类型描述，它与WSGI相比是两样东西。

为什么有了uWSGI为什么还需要nginx？

因为nginx具备优秀的静态内容处理能力，然后将动态内容转发给uWSGI服务器，这样可以达到很好的客户端响应。

### uWSGI安装
可以使用pip/conda安装
一般来说可以一条命令安装
```
    pip/conda install uwsgi
```

我在两台机器上尝试了。

- centos的服务器，按网上教程提前装了很多前置应用，结果后面怎么都装不上。新建环境（py36）仍然装不上
- ubuntu的服务器，新建环境（py36），用conda一条命令就装好了

## 方案二
pycharm连接服务器特定位置，上传代码。（gunicorn + supervisor）+ Nginx + sqlite
- 参考： https://www.jianshu.com/p/5600af9ff238
- 参考： https://blog.csdn.net/codeswarrior/article/details/107511960

本次后端部署，服务器使用的是非root用户（121.58.40.21:8687, wxt@wxt123）。



### 只用gunicorn启动

- gunicorn安装

使用`pip/conda install gunicorn`安装即可
- gunicorn启动文件

放在 `myappsserver/myappsserver` 目录下的wsgi.py文件
```
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myappsserver.settings")
application = get_wsgi_application()
```
- 运行

注：测试用
```
    gunicorn myappsserver.wsgi:application --bind 0.0.0.0:8080 --workers 2
    gunicorn 启动文件:app变量 -b 监听地址 -w work数量即监听进程数 -t 最大超时时间
```
### 使用supervisor启动
参考：非root用户下安装supervisor并使用supervisor和gunicorn部署项目：
https://blog.csdn.net/codeswarrior/article/details/107511960

- 安装supervisor

命令为``conda install supervisor``项目使用的环境为conda环境myapps。supervisor的位置在myapps环境的bin目录中。

可以用`which supervisorctl`来判断默认的是否是wxt用户下的，不是的话可以加环境变量或使用绝对路径
- supervisorctl 配置文件

根据教程，先导出配置文件，再改
supervisord.conf: `"/home/wxt/supervisor/supervisord.conf"`

- 进程管理配置文件配置文件

`/home/wxt/supervisor/conf.d`目录下的所以.conf结尾的文件都将被启动。（supervisorctl 配置文件中规定的）
本项目进程：`/home/wxt/supervisor/conf.d/myappsserver.conf`


- 运行

（1）启动 supervisorctl 
```
supervisorctl -c "/home/wxt/supervisor/supervisord.conf"
```
不带-c参数，是使用默认配置启动，这是错误的

（2）常用操作
```
# 更新进程配置
reload 

# 查看进程状态
status 

# 更新supervisorctl配置
update
```
