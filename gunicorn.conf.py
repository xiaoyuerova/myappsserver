import multiprocessing

# 绑定的ip与端口
bind = "127.0.0.1:8687"

# 核心数
workers = 2

# 发生错误时log的路径
# errorlog = '/home/wxt/myapps/myappsserver/log/gunicorn.error.log'

# 正常时的log路径
# accesslog = '/home/wxt/myapps/myappsserver/log/gunicorn.access.log'

#loglevel = 'debug'   #日志等级
proc_name = 'gunicorn_project_wxt_wj_app'   #进程名
