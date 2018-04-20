# Grab_Images
Grab images from website
This code is used to grab images from some website.
ImgID is bottom file where the images are saved and the file name of the images.
URL is the website.
SavePath is the absolute path where the images are saved,and the default path is "F://get_img//test//".
For example.
When
ImgID:0001
URL:http://newcar.xcar.com.cn/photo/
SavePath:F://get_img//test//
you will find images in F://get_img//test//0001
named in 
0001_0.jpg
0001_1.jpg
0001_2.jpg
...
if you want to grab images in other website you can change the code in line 42

42 reg = r'src="(.+?\.jpg)" width="?"'


