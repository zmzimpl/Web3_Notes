## 序言和介绍
 - 偶然的一次机会,在与客户谈论时,他提到了一个以太坊仪式召唤,并把进行的画面截图给笔者,觉得挺有意思的 。
于是乎笔者查询相关网站,在推特等社交媒体在了解片刻之时,就发现一个的问题。
例如推特的一些KOL 在介绍以太坊召唤仪式之时，只是进行了简单操作,并没有教大家如何进行"高效"的操作。
在阅读相关推文时,发现大部分人开启浏览器进行仪式召唤，不能说不"正确"，但笔者认为进行以太坊召唤仪式不够 "科学",不够Geek,效率低下，所以特开此文抛砖引玉,传授经验于各位小白读者，如何进行"科学",高效的进行以太坊召唤仪式。
 - 如有错误。请各路大神斧正。
<!-- TOC -->
  * [序言和介绍](#序言和介绍)
      * [作者:Web3inFlare](#作者--web3inflare)
  * [1) 如何脱离浏览器进行以太坊召唤仪式。](#1--如何脱离浏览器进行以太坊召唤仪式)
  * [2) 如何微操多个账户参与以太坊召唤仪式。](#2--如何微操多个账户参与以太坊召唤仪式)
  * [3) 结束语](#3--结束语)
<!-- TOC -->
#### 作者:Web3inFlare
## 1) 如何脱离浏览器进行以太坊召唤仪式。
 - 在撸一个项目之时,我们应当知道项目硬性要求以及如何操作
 - 通过阅读相关`[https://ceremony.ethereum.org/]` 
网站得知,召唤仪式可以脱离浏览器进行 也就是可以进行CLI执行 `[https://github.com/ethereum/kzg-ceremony#client-implementations]`
 - 通过检索相关网站得知 提供了各类语言的CLI 客户端。
 - 我们选择一个客户端进行操作。
 - `go-kzg-ceremony-client` `[https://github.com/jsign/go-kzg-ceremony-client]`
 - OK 我们选择了使用那个工具进行以太坊召唤仪式。
 - 现在要知道参与的硬性条件,参与以太坊召唤仪式有两种方式: 以太坊钱包,GITHUB账户。
 - 以太坊钱包以,GITHUB账户 参与条件如下:

> 1.在以太坊主网上区块高度15537393之前有3笔交易
> 
> 2.Github 注册日期在 UTC 2022年8月1日之前注册

至于如何获得符合条件的账户。我相信各位读者八仙过海,自有妙计，在这就不在在叙述。
笔者在这里使用的是GITHUB账户，因为笔者手里也没有符合ETH的账户,但是操作过程大同小异。
---
- 阅读`[go-kzg-ceremony-client]` 工具文档,得知我需要得到一个 `session-id`。
- 打开网站`[https://seq.ceremony.ethereum.org/auth/request_link]` 我们获得以下以JSON格式的页面。
```json
{
    "eth_auth_url": "https://oidc.signinwithethereum.org/authorize?response_type=code&client_id=5aeae9f0-56a3-41dd-beea-a6c456ad1c5f&state=eyJyZWRpcmVjdCI6bnVsbH0&redirect_uri=https%3A%2F%2Fseq.ceremony.ethereum.org%2Fauth%2Fcallback%2Feth&scope=openid", 
    "github_auth_url": "https://github.com/login/oauth/authorize?response_type=code&client_id=8e9f2341df6bb3317dd6&state=eyJyZWRpcmVjdCI6bnVsbH0&redirect_uri=https%3A%2F%2Fseq.ceremony.ethereum.org%2Fauth%2Fcallback%2Fgithub"
}
```
- 笔者使用的是Github,那么获得 `session-id` 方法就是使用 `github_auth_url`内的端点路径。
- 打开 `[https://github.com/login/oauth/authorize?response_type=code&client_id=8e9f2341df6bb3317dd6&state=eyJyZWRpcmVjdCI6bnVsbH0&redirect_uri=https%3A%2F%2Fseq.ceremony.ethereum.org%2Fauth%2Fcallback%2Fgithub]`
- 进行授权，以太坊账户就是使用 `eth_auth_url`内的端点路径
- 授权完毕 会返回一个JSON格式的页面,在页面中有一个`session_id`值, 类似于 `504d898c-e975-4e13-9a48-4f8b95d754fb`,这就是我们需要的`session_id`
- 在获取`session_id` 值时候。可能会出现以下问题:
  * `AuthErrorPayload::UserCreatedAfterDeadline`: 以太坊地址不符合要求
  * `AuthErrorPayload::InvalidAuthCode`: 登陆超时,请重新登陆
  * `AuthErrorPayload::UserAlreadyContributed`: 以太坊和Github地址,已经进行了以太坊召唤仪式
- 好了,我们需要的`session_id` 值已经获取成功。我们开始使用工具进行以太坊召唤。
- 笔者这里使用的是 VPS Linux Ubuntu 服务器。
- 所以执行的命令是Linux命令,在Window下大同小异，就不便叙述。
- 工具下载地址 `[https://github.com/jsign/go-kzg-ceremony-client/releases]`
  * Linux `[kzgcli-v1.0.3-linux-amd64.tar.gz]` 
  * Window `[kzgcli-v1.0.3-windows-amd64.zip]`

 - 笔者在Linux Ubuntu 服务器执行命令如下:
---
```shell
# 下载
wget https://github.com/jsign/go-kzg-ceremony-client/releases/download/v1.0.3/kzgcli-v1.0.3-linux-amd64.tar.gz
# 解压文件
tar -zxvf kzgcli-v1.0.3-linux-amd64.tar.gz
# 授权文件. 在Linux 下 文件权限非常严格,所以要给予文件权限才能运行
chmod +x kzgcli
```
---
我们使用命令查看以下目前有多少人进行召唤仪式。
 - `./kzgcli status`
```shell
root@Web3inFlare:~# ./kzgcli status
Lobby size: 3688
Number of contributions: 35389
Sequencer address: 0xfAA3A87713253D44E33C994556f7727AC71937f0
```
在编写本文时 目前有3万多人进行召唤仪式,人还是比较多的。
我们开始进行召唤仪式,执行命令如下。
```shell
root@Web3inFlare:~# ./kzgcli contribute --session-id 你的session_id --drand --urlrand https://ihagopian.com
```
我来解释一下命令。
```shell
--session-id # 后面跟着你的session-id
--drand # 使用 drand 网络,提取网络中可用的熵
--urlrand # 使用页面中的正文字节作为 熵与CSRNG的混合,也就是网页中的密语.
```
执行完毕之后我们获得一下回显。
```shell
root@Web3inFlare:~# ./kzgcli contribute --session-id 你的session_id --drand --urlrand https://ihagopian.com
Pulling entropy from drand... Got it! (length: 32, round: 2677787)
Pulling entropy from https://ihagopian.com... Got it! (length: 54220)
Waiting for our turn to contribute...
Still isn't our turn, waiting 30s for retrying...
```
工具正常运行,目前进行召唤仪式的人特别多所以还在排队进行贡献。
如果贡献成功,会出现以下字符串。
```shell
Sending contribution...
Success!
```
  * my_contribution.json
  * contribution_receipt.json
同时会产生两个Json文件。

如果你想进行后台运行 可用使用以下命令。
```shell
# 后台执行工具
nohup ./kzgcli contribute --session-id 你的session_id --drand --urlrand https://ihagopian.com &
# 使用cat 查看回显
cat nohup.out
```
 - 在笔者的Linux 4H服务器上使用 kzgcli 工具CPU占用率不及百分之5之五，我的客户在使用32核CPU的台式上仅只能开启21个浏览器,相比之下,同等配置效率要高出许多倍。
 - 据笔者之前测试时，一个小时内将有64位幸运儿能召唤成功。所以请各位读者耐心等候
 - 仪式召唤成功后可用打开 `[https://ceremony.ethereum.org/#/record]` 输入的你Github用户名或者以太坊钱包地址查询也可以使用 `./kzgcli verify-transcript`命令查看。
 - 在window系统上大同小异。请各位读者自行使用Cmd进行操作。
 - 读到这里各位读者应该学会如何脱离浏览器进行操作.但是撸一个项目的时候。绝大部分人不会就一个账户来撸，所以如何高效的撸多个账户呢？ 
 - 请听笔者娓娓道来。
## 2) 如何微操多个账户参与以太坊召唤仪式。
 - 在撸一个项目的时候，往往我们不止一个账户。有些读者仅仅只有几个账户，想着多执行几个命令不就完事了吗？
 - 但是对于一些读者来说。召唤仪式是以太坊官方开展的。谁也不知道最后得到什么,或者是POPA? NFT? 这都不好说。
 - 在WEB3当中,我也发现了比较有意思的事情。冒着反撸的风险.宁可多撸也绝对不会少撸,以免日后拍断大腿。毕竟前车之鉴历历在目 例如APTOS。

OK,进入正题

现在笔者介绍一个叫做 `Docker`东东,如何使用`Docker`进行微操多个账户。

我来介绍一下什么是 `Docker`,它是一个类似于 Window 上的VM虚拟机，可用容器化各类程序实现,程序之间的隔离.一般用于Linux上，部署各种应用程序。
>Docker 是一个开源的应用容器引擎，让开发者可以打包他们的应用以及依赖包到一个可移植的镜像中，然后发布到任何流行的 Linux或Windows操作系统的机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口。

为什么要使用`Docker`呢？因为我们进行多个账户的时候。或许会使用`nohup`命令执行多个。但是这会导致nohup.out出现重复等问题。

聪明的读者也许会使用文件夹进行隔离。但是面对几十个，上百个账户。笔者认为在不修改代码的情况下,这不是什么优雅的方式。同时对小白读者来说并不能接受。

所以我们可用使用Python配合`Docker` 进行微操多个账户。实现容器隔离`kzgcli`工具,创建多个容器互不相关的环境,参与以太坊召唤仪式。


或许有人会问，在同一个ip上能多开吗，根据笔者的经验以及相关推文推断，不需要多ip 只需要你提供的session就行了

说完实现方式，现在就开始实战微操！

---

笔者同样使用Linux Ubuntu 服务器进行操作,之所以使用Linux,主要是笔者手里也没有Window系统的环境。笔者已经不使用Window作为主力系统进行日常工作将近十年了。

日常有空时仅限于网吧使用,打打CSGO,永劫无间。

所以想使用Window的读者。请查阅`[https://www.runoob.com/docker/windows-docker-install.html]` 安装Docker

步骤如下:
1.安装Dockerfile环境
2.编写Dockerfile,构建容器环境。
3.编写Python脚本批量创建容器。
4.其他命令介绍

在Window上大同小异

---
1.我们开始安装`Docker`环境:

执行命令如下:
```shell
# 下载bash脚本进行安装Docker环境,需要等待许久时间
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```
```shell
#  出现这个提示 没有关系
To run the Docker daemon as a fully privileged service, but granting non-root
users access, refer to https://docs.docker.com/go/daemon-access/

WARNING: Access to the remote API on a privileged Docker daemon is equivalent
         to root access on the host. Refer to the 'Docker daemon attack surface'
         documentation for details: https://docs.docker.com/go/attack-surface/
```
```shell
# 执行命令查看是否安装正确
sudo docker run hello-world
```
```shell
# 会出现这个回显 说明安装成功
root@Web3inFlare:~# sudo docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
2db29710123e: Pull complete 
Digest: sha256:aa0cc8055b82dc2509bed2e19b275c8f463506616377219d9642221ab53cf9fe
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```
2.开始编写Dockerfile文件

创建一个`Dockerfile` 文件并与`kzgcli`在同一个目录下,文件内容如下并带有注释说明代码的意思:
```dockerfile
# 使用ubuntu 镜像
FROM ubuntu:latest
# 维护作者名字
MAINTAINER Web3inflare
# 给Ubuntu镜像添ca证书
RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends ca-certificates curl
# 把kzgcli 添加到 /app目录
COPY  ./kzgcli /app/
# 设置 app目录为工作目录
WORKDIR /app
# 添加一个环境变量 用于启动容器时 指定session 值
ENV session ""
# 添加入口点,也就是启动容器时 执行命令
ENTRYPOINT [ "sh", "-c", "./kzgcli contribute --session-id $session --drand --urlrand https://ihagopian.com"]
```
执行构造镜像
```shell

# 镜像名字为kzg,版本号为v1 注意 v1 后有一个.
docker build -t kzg:v1 .
```

查看镜像是否创建成功 执行命令 `docker images`
```shell
root@Web3inFlare:~# docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
kzg          v1        9321e8d3f386   21 hours ago   145MB
```
3.开始编写Python脚本批量创建容器 创建一个bath.py 文件填写以下内容

```python
"""
@Time ： 2023/2/7 21:15
@Auth ： Web3inFlare
@File ：bath.py
@IDE ：PyCharm
@Motto: 咕咕嘎嘎
"""
import subprocess


def run():
    # 读取list.txt 中的值session
    with open('list.txt', 'r') as file:
        # 定义一个值 用于区分容器的名字
        name = 0
        for line in file.readlines():
            # 定义一个值作为累加,方便知道执行到第几个
            name += 1
            # 更改格式去掉回车
            rs = line.replace('\n', '')
            # 打印输出
            print(f"[*] [{name}]正在创建 {rs} 镜像")
            cmd = f'docker run -d -P --name kzg-{name} -e session="{rs}" kzg:v1'
            # 使用subprocess 执行命令
            call = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                    encoding="utf-8")
            # 获取返回值
            docker_id = call.stdout.read().replace('\n', '')
            print(f"[*] {rs} 镜像创建成功 ID: {docker_id}")
            # 写入日志 保存文件
            with open('docker-out.txt', 'a') as f:
                f.write(f"kzg-{name} session:{rs} docker-id:{docker_id}\n")


if __name__ == '__main__':
    run()
```
 - 将你要进行召唤仪式的session值一行一个填入list.txt中
 - 然后执行`python3 bath.py`
```shell
root@Web3inFale:~# python3 bath.py 
[*] [1]正在创建 5510b992-efa3-4a9b-add6-df14d5b26016 镜像
[*] 5510b992-efa3-4a9b-add6-df14d5b26016 镜像创建成功 ID: 75c5718b68fb9073f9c2324ce3734944d2f6b8c3ef9a2afd3bd6740ba889631f
[*] [2]正在创建 5510b992-efa3-4a9b-add6-df14d5b26016 镜像
[*] 5510b992-efa3-4a9b-add6-df14d5b26016 镜像创建成功 ID: 3e2a23621d64f8bc4ba3b1beece817ecad0a4b3394efcca557433127dbb0a6a8
[*] [3]正在创建 5510b992-efa3-4a9b-add6-df14d5b26016 镜像
[*] 5510b992-efa3-4a9b-add6-df14d5b26016 镜像创建成功 ID: 1758ad96708b416a9492ac253550186963104b4f1edfb41526cd346c094639b0
```
 - 这样子就可以批量进行以太坊仪式召唤了,实现工具之间的隔离

4.其他命令介绍 
```shell
docker ps # 查看正在运行的docker容器
docker stop CONTAINER ID  #  暂停容器 CONTAINER ID 通过docker ps 获得
docker rm CONTAINER ID # 删除容器
docker logs CONTAINER ID  # 查看容器内的kzgcli输出
docker stop $(docker ps -a -q) # 暂停所有的容器
docker rm $(docker ps -a -q) # 删除所有的容器
```

注1: 附赠所有代码。
## 3) 结束语

文章写到这,也将告一段落。笔者相信许多读者应该收获颇丰,简单的学习到`Docker`与`Python`使用以及编写`Dockerfile`，如何微操且"正确"的进行以太坊召唤。

笔者也相信部分读者会对`Python`以及`Docker`感兴趣,更高阶的使用方式,还需要各位读者下决心去学习研究。学习是人生必修课。

笔者第一次发表文章,如有不对之处请海涵

如有什么问题或有什么有意思的东西 可在推特[`web3inflare`]上DM笔者,与笔者探讨。

期待下次与各位读者见面！

![](img/template_1466726616.jpeg)

文章写于 2023.2.8 完成于 2022.2.9
