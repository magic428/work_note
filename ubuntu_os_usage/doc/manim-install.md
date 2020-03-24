# manim - 安装, 制作 3Blue1Brown 风格的视频 

> 明确声明, Python >= 3.6  

## 1. 安装使用的第三方库 - ffmpeg 和 Latex 渲染工具  

```bash
sudo apt install python3-cairo ffmpeg texlive-science texlive-fonts-extra
```

其中, texlive-fonts-extra 是字体包; texlive-science 是数学物理计算机科学的包.  

## 2. 源码安装

```bash
git clone https://github.com/3b1b/manim.git
cd manim
pip3 install -r requirements.txt
python3 manim.py example_scenes.py SquareToCircle -pl
```

这个时候, manim 就已经可以运行了.  

## 两个例子  

(1) 绘制圆到矩形的转换 

```bash
$ python3 -m manim example_scenes.py SquareToCircle -pl

File ready at /pwd/videos/example_scenes/480p15/SquareToCircle.mp4
```

(2) Latex 公式渲染  

```bash
python3 -m manim example_scenes.py OpeningManimExample -pl

Media will be written to ./media/. You can change this behavior with the --media_dir flag.
Writing "\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}" to Tex/6dfa92e9cf68d3d2.tex
Writing "\centering That was a transform" to Tex/80098dbd03d57c6a.tex           
Writing "\centering This is a grid" to Tex/2df44e40361311b3.tex                 
Writing "\centering That was a non-linear function \\applied to the grid" to Tex/5c0ec9c18b3100c3.tex
                                                                                
File ready at /pwd/videos/example_scenes/480p15/OpeningManimExample.mp4

Played 10 animations
```

## 使用资料  

(想学着制作 3Blue1Brown 风格的视频吗？你还要能写点代码！)[https://www.bilibili.com/read/cv19963]   