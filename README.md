## JPG2Ascii

将图片转换成ascii图像, 推荐选择线条比较少，色彩比较单一而且颜色差距大的图片.
后端为tornado， 接受请求后使用[jp2a](https://csl.name/jp2a/)进行转换.

演示地址: [jpg2ascii.herokuapp.com](https://jpg2ascii.herokuapp.com/)

## 截屏

![home][1]
![show][2]

## 关于在heroku编译

首先使用

```shell
heroku run /bin/bash
```

然后获得一个属于你当前app的shell环境

然后
进行wget包, configure 环境, make 之后, make install .
然后把jp2a 命令scp到一个公有环境的服务器.
然后git add到包里面完成打包工作.


## License

The MIT License (MIT)

Copyright (c) 2015 JackeyGao

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


[1]:https://raw.githubusercontent.com/jackeyGao/Flask-JPG2ASCII/master/ScreenCapture/screenCapture-1.png
[2]:https://raw.githubusercontent.com/jackeyGao/Flask-JPG2ASCII/master/ScreenCapture/screenCapture-2.png

