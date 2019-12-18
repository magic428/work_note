# git 打 tag

通常在发布软件的时候打一个 tag, tag 会记录版本的 commit 号, 方便后期回溯.   

(1) 列出已有的 tag   

```bash
git tag
```

在 git tag 命令中加上 -l 参数可以使用通配符来过滤显示 tag.  

(2) 新建 tag

使用 git tag 命令跟上 tag 名字, 直接创建一个 tag.   

```bash
git tag v1.0
```

创建一个名为 v1.0 的 tag. 使用 git tag 命令可以看到新增加的 tag.   

还可以加上 -a 参数来创建一个带备注的 tag, 备注信息由 -m 指定. 如果你未传入 -m则创建过程系统会自动为你打开编辑器让你填写备注信息. 如下:   

```bash
git tag -a tagName -m "my tag"
```

(3) 查看 tag 详细信息 

`git show <tagName>` 命令可以查看 tag 的详细信息, 包括 commit 号等.   

```bash
git show v1.0
```

查看 v1.0 tag 的详细信息.  

tag 最重要的是有 git commit 号, 后期我们可以根据这个 commit 号来回溯代码.   

(4) 给指定的某个 commit 号加 tag  

打 tag 不必要在 head 之上, 也可在之前的版本上打, 这需要你知道某个提交对象的校验和（通过 git log 获取, 取校验和的前几位数字即可）.   

```bash
git tag -a v1.2 9fceb02 -m "my tag"
```

(5) 将 tag 同步到远程服务器  

同提交代码后, 使用 git push 来推送到远程服务器一样, tag 也需要进行推送才能到远端服务器.   
使用 `git push origin [tagName]` 推送单个分支.   

```bash
git push origin v1.0
```

推送本地所有 tag, 使用 `git push origin --tags`.   

(6) 切换到某个 tag  

跟分支一样, 可以直接切换到某个 tag 去. 这个时候不位于任何分支, 处于游离状态, 可以考虑基于这个 tag 创建一个分支.   

(7) 删除某个 tag  

```bash
# 本地删除:  
git tag -d v0.1.2 

# 远端删除
git push origin :refs/tags/<tagName>
git push origin :refs/tags/v0.1.2
```
