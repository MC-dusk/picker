## 抽签器 v1.0

- 功能：自定义一个名单（文件名：list.txt，一行一个名字），放在程序相同目录下，随机抽取名单中的名字。
  - 用例：提供王者荣耀英雄列表，今天玩什么？

> 采用类进行封装

### 编译：

- 用`pyinstaller -F -w -i picker.ico picker_v1.0.py [--upx-dir <DIR>]`方式打包生成exe（8.97M）。
  - 其中`<DIR>`为upx文件夹的绝对路径，upx是用于压缩exe大小的，可选。
- exe文件：https://wwx.lanzoui.com/b01ihoygb (52pj)

### 截图：

[![WJHUk6.png](https://z3.ax1x.com/2021/07/19/WJHUk6.png)](https://imgtu.com/i/WJHUk6)

### TODO

- [ ] 历史记录（开关、保存）（退出时提示是否保存）
- [ ] 抽取模式（单个/批量）（一次n个）（最后不够->显示已抽尽）
- [ ] 重复模式（独立/连续）（被抽中的是否移出样本）
- [ ] 延时模式（立即/延时/手动）

### END

[![Page Views Count](https://badges.toozhao.com/badges/01G6ZJY3322Y59H9X1J3XHN2M5/green.svg)](https://badges.toozhao.com/stats/01G6ZJY3322Y59H9X1J3XHN2M5 "Get your own page views count badge on badges.toozhao.com")
