## 说明

修改二进制文件依赖libc的版本

原本项目地址
[https://github.com/matrix1001/glibc-all-in-one](https://github.com/matrix1001/glibc-all-in-one)

在原项目的基础上进行了修改

## 运行

``` bash
python get_env.py  
sudo ln -s /home/tower/glibc-all-in-one/clibc /usr/bin/clibc  #设置软链接需要绝对路径
```

修改二进制文件的依赖库

``` bash
clibc pwn_printf 2.23   #pwn_printf是例子程序
```

## 运行结果
修改过的二进制文件（左）和原始二进制文件（右）没什么区别

![结果](https://raw.githubusercontent.com/tower111/picture/main/小书匠/1606831396379.png)


