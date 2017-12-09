# formal-automated-test
课工场正式环境自动化测试

*如果你有协作者账号请使用协作者账号提交；此仓库不接受Pull Request*

# 执行Xvfb虚拟测试说明

## 1.检查是否有已经开启的Xvfb进程
```ps -aux | grep -i xvfb```

## 2.如果没有已经启动的Xvfb进程，通过下面的命令启动
```Xvfb -ac -br -nolisten tcp -screen 0 2880x1720x24 :1121```

*Tip:1121可以更换为其他数字*

## 3.设置环境变量
```export DISPLAY=:1121```

*Tip:1121为启动Xvfb进程时指定的编号*

## 4.执行测试
```python3 main.py```
