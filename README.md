# Send email by python
 
_闲的无聊一晚上写的_

打算做个包加到程序里，在模型训练完后不论我在哪里都能收到训练结果

## 开始

### 发一封简单的邮件

示例：

```python
host = 'smtp.qq.com' # qq 可以替换成其他邮箱
user = # 你的邮箱账户
password = # 密码，有些邮箱需要授权码

sender = # 发信人，你的邮箱
receivers = [''] # 收件人，可以填多个
message = '' # 内容
title = '' # 标题

email = Mail(host, user, password)
email.send(message, title, sender, receivers)
```

### 在邮件中添加附件

`email.add_file(filePath, fileName)`

`email.add_img(imgPath, imgName)`

参数：
- filePath & imgPath: 文件或图片路径，包括文件名
- fileName & imgName: 给附件起的名字，注意要加扩展名
