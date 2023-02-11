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
ENTRYPOINT [ "sh", "-c", "./kzgcli contribute --session-id $sessio --drand --urlrand https://ihagopian.com"]


