"""
@Time ： 2023/2/7 21:15
@Auth ： Web3inFlare
@File ：bath.py
@IDE ：PyCharm
@Motto: 咕咕嘎嘎
"""
import subprocess


def run():
    # 读取session
    with open('list.txt', 'r') as file:
        # 定义一个值 用于区分 容器的名字
        name = 0
        for line in file.readlines():
            # 定义一个值作为累加,方便知道执行到第几个
            name += 1
            # 更改格式去掉回车
            rs = line.replace('\n', '')
            # 打印输出
            print(f"[*] [{name}]正在创建 {rs} 镜像")
            cmd = f'docker run -d -P --name kzg-{name} -e session=“{rs}” kzg:v1'
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

