# Sekai Subtitle

**最近事比较多 开发进程缓慢 敬请谅解**

新一代世界计划多彩舞台剧情对话自动打轴姬 使用Python语言编写 基于OpenCV
自动获取的数据文件来自于 https://pjseka.ai/ 和 [Sekai Viewer](https://github.com/Sekai-World/sekai-master-db-diff)

## 开发进度

- [x] 自适应视频分辨率样式、遮罩

- [x] 防抖处理

- [x] 多任务处理

- [x] 在线获取json文件

- [x] 整合Sekai Support - 合并翻译文件与json文件

- [ ] 对视频处理流程进行改进 多线程运行
    - ~~视频处理进程分离 失败 会导致帧序列错乱~~

- [ ] 整合Sekai Text - 一站式世界计划剧情翻译平台

- [ ] *更多需求请提出**issue***

## 安装

- 需求：Python 3.10.7

- 下载克隆本仓库

  ```shell
  git clone https://github.com/Icexbb/SekaiSubtitle-Python.git
  ```

- 安装依赖

  ```shell
  python -r requirements.txt
  ```

## 使用

```shell
cd src
python gui_old_main.py
```

### 自动打轴

- 选择录制文件
- 选择数据文件获得方式
- 【在线获取】更新列表-》选择对应话数-》点击载入下载
- 【本地获取】点击载入选择本地文件
- 加入队列
- 开始队列
