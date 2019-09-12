# !/usr/bin/python3
# -*-encoding:utf-8-*-

from git import Repo
import os

repo = Repo('')


def get_current_dir():
    array = os.path.split(__file__)
    if array is not None and len(array) == 2:
        return array[0]


def test():
    dir_name = get_current_dir()
    print(dir_name)
    repo = Repo(dir_name)

    is_dirty(repo)

    # 新建分支
    # repo.create_head("jiayan")
    # print("创建dev分支")

    # 当前的分支名称
    branchs = repo.active_branch
    print(branchs)

    # 获取缓存区
    index = repo.index
    index.add(["wtf.txt"])
    index.commit("gitpython test commit")

    remote = repo.remote()
    remote.push()


def is_dirty(repo):
    # 当前工作区是否干净
    is_dirty = repo.is_dirty()
    print('工作区是否干净：', is_dirty)


if __name__ == '__main__':
    test()
