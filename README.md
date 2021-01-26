# Python-
A proxy pool built by Python.
这是利用python搭建的一个项目，用于提供采集数据时所需要的代理地址。
文档中共有6个文件，它们都是以.py为后缀的，分别是：api.py，config.py，db.py，getter.py，run.py，verify.py。
下面介绍每个.py文件的用途：
1.api.py：
在api.py中，它的功能是提供一个获取代理的接口，在这个接口上，利用python程序请求即可获取到所需要的代理。在api.py中，接口的搭建是通过flask进行的，它的端口号是默认的，5000；当启动这个服务后，您将可以通过下面列举出的几种方法来请求到您想要的代理数据：
