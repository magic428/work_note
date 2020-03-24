# label_tools 

## Usage

1) 标注数据, 假设数据的存放目录为: /path/to/data. 

```bash
python3 label_tool.py -p /path/to/data
```

2) 清洗并整理数据   

对于图片中没有目标的数据, 应该删除; 同时将标注数据和图片数据分开存放到 JPEGImages/ 和 Annotations/ 目录下.  

```bash
python3 clearNoObjSample.py -p /path/to/data
```

## ChangeLog

2018-08-13:  

1) 修改了 clear(按键 c ) 时不是删除所有类别的 BBOX, 而是只删除当前标注类别的框;  
2) 在想要删除的 BndBox 区域内点击鼠标右键即可删除所选框;  


2018-08-14:   

1) 支持剩余未标注图片数量显示;   
2) 支持回到上一张标注结果;

2019-07-10：   

1) 支持复制上一个标注文件中某一类的所有标注框到当前标注文件；   
2) 丰富了右键的功能： 
  如果在当前标注文件中，右键点击的当前区域中没有框，那么就会在上一个标注文件中查找该区域中是否存在标注框，如果存在就将这些 Bbox 拷贝到当前标注文件中；  
3) 判断标注框的大小，如果像素之间差别很小，那么不作为有效框进行保存。  