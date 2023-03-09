<br />
<p align="center"><img src="asset/icon.png" alt="Logo" width="150" height="150"></p>
<h2 align="center" style="font-weight: 600">Sekai Subtitle</h2>
<p align="center">新一代世界计划多彩舞台剧情对话自动打轴姬</p>
<p align="center">
<img alt="GitHub all releases" src="https://img.shields.io/github/downloads/Icexbb/SekaiSubtitle-Python/total">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/icexbb/sekaisubtitle-python">
<img alt="GitHub Release Date" src="https://img.shields.io/github/release-date/icexbb/sekaisubtitle-python">
<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/icexbb/sekaisubtitle-python">
<img alt="GitHub" src="https://img.shields.io/github/license/icexbb/sekaisubtitle-python">
<img alt="GitHub issues" src="https://img.shields.io/github/issues/icexbb/sekaisubtitle-python">
</p>

## 简介

使用Python语言编写 主要功能实现基于OpenCV

自动获取的数据文件来自于 [pjsek.ai](https://pjseka.ai/)
和 [Sekai Viewer](https://github.com/Sekai-World/sekai-master-db-diff)

GitHub 地址 [Icexbb/SekaiSubtitle-Python](https://github.com/Icexbb/SekaiSubtitle-Python)

Gitee 地址 [Icexbb/SekaiSubtitle-Python](https://gitee.com/Icexb/SekaiSubtitle-Python) （同步较慢）

## 开发进度

- [ ] *更多需求请提出**issue***

## 使用教程

### 安装配置

- 需求：Python 3.11

```shell
git clone https://github.com/Icexbb/SekaiSubtitle-Python.git
cd SekaiSubtitle-Python
pip install -r requirements.txt
python src/main.py
```

### 使用

#### 轴机

- 点击`准备就绪`或将视频/数据/翻译文件拖至框内创建任务
- 点击任务进度组件内绿色按钮开启任务进程

##### 注意

- 任务进行过程中的黄色按钮是停止任务，红色按钮是删除任务
- 任务进行不能暂停 停止后可再次点击绿色按钮重新开始任务

#### 自动下载

- 首先选择合适的数据源
- 点击`刷新`按钮刷新数据列表
- 在列表中选择对应的文件
- 点击`开始下载`

#### Sekai Text

- 载入Json文档
- 若进行翻译工作 则直接在界面进行填写
- 若进行校对工作 则点击打开按钮`打开`已经存在的文件

#### 自动更新

- 程序在启动时会自动检查一次更新
- 也可以通过点击关于窗口内的`检查更新`运行检查

## 灵感来源

- [Jeunette/ass-automation-java](https://github.com/Jeunette/ass-automation-java)
- [Sutedako/PRSK_Editor](https://github.com/Sutedako/PRSK_Editor)

## 开源许可与声明

本项目仅供个人学习研究使用，禁止用于商业及非法用途。
基于 [MIT license](https://opensource.org/licenses/MIT) 许可进行开源。

本项目所使用图像素材所有版权归其合法所有者所有，包括但不限于 Sega、Colorful Palette 和 Crypton

本项目与项目开发者所属组织与Sega或Colorful Palette没有官方关系
