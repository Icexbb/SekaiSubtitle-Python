# Sekai Subtitle

新一代世界计划多彩舞台剧情对话自动打轴姬 使用Python语言编写 基于OpenCV
自动获取的数据文件来自于 https://pjseka.ai/ 和 [Sekai Viewer](https://github.com/Sekai-World/sekai-master-db-diff)

GITHUB地址 https://github.com/Icexbb/SekaiSubtitle-Python
## 开发进度

- [x] 视频无Json运行
- [x] 视频多Json运行
- [ ] 整合Sekai Text - 一站式世界计划剧情翻译平台
- [ ] *更多需求请提出**issue***

## 使用
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

*注意*

任务进行过程中的黄色按钮是停止任务

红色按钮是删除任务

任务进行不能暂停 停止后可再次点击绿色按钮重新开始任务

#### 自动下载
- 首先选择合适的数据源
- 点击刷新按钮刷新数据列表
- 在列表中选择对应的文件
- 点击下载即可
