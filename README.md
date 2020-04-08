## 1. Thoth
个人博客源码，名称 `Thoth` 起源于古埃及神话中的托特神。

托特（Thoth），是古埃及神话中智慧之神，同时也是月亮、数学、医药之神，埃及象形文字的发明者，众神的文书；在《亡灵书》中被描绘为立姿审判者。以佩戴满月圆盘及新月冠鹮头人身的形象出现。

## 2. 技术栈

技术栈如下表所示：

|  技术  | 版本     |
| :----------: | :-----------:  |
|  CentOS  | 8     |
|  Python  | 3.7.4     |
|  Django    | 3.0    |

## 3. 使用

1. 从Github Clone下来源码后，进入项目目录下，运行如下指令：

    > docker build -t sabiner/thoth:v1 .
    
    > docker run -d -it -p 8000:8000 --name thoth sabiner/thoth:v1 /bin/bash

2. 进入容器，启动服务：

    > docker exec -it thoth /bin/bash
    
    > python manage.py runserver 0.0.0.0:8000

    按住 Ctrl+P，点击Q，守护服务退出容器
   
3. 配置 Nginx 后访问 IP 地址：
    
    > nginx.conf proxy_pass http://0.0.0.0:8000


