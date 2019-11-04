clc;
clear all;close all;
clc;
 
image = imread('/home/magic/data_dl/tdmc_objs/td_all/JPEGImages/miner_00269.jpg');

image = imresize(image, 0.5);
% u = 4 * x and v = 2 * y
T = [4 0 0; 0 2 0; 0 0 1];
 
% create spatial transformation structure.
transformation = maketform('affine', T);
 
% apply 2D spatial transformation to image.
transformationResult = imtransform(image, transformation, 'FillValues',[255;255;255]);
figure(1)
imshow(uint8(transformationResult)); 


%% method1,用3组点集对图像进行仿射变换，调用matlab系统函数  
src=(imread('/home/magic/data_dl/tdmc_objs/td_all/JPEGImages/miner_00269.jpg'));  
fixedPoints = [1,1; 1,100;100,100];  
movingPoints = [20,20; 120,80; 160,200];  
tic;
tform = fitgeotrans(movingPoints,fixedPoints,'affine');  
dst_img = imwarp(src,tform,'FillValues',255);  
t_sys = toc;
figure;imshow(dst_img);
%title(['系统函数的仿射变换图像，耗时（s）：',num2str(t_sys)])  
  


%% 读取原图像
clear ;
close all;
%src=rgb2gray(imread('/home/magic/data_dl/tdmc_objs/td_all/JPEGImages/miner_00269.jpg'));  
src=(imread('/home/magic/data_dl/tdmc_objs/td_all/JPEGImages/miner_00269.jpg'));  
imshow(src);  
  
%% method1,用3组点集对图像进行仿射变换，调用matlab系统函数  
fixedPoints = [1,1; 1,100;100,100];  
movingPoints = [20,20; 120,80; 160,200];  
tic;
tform = fitgeotrans(movingPoints,fixedPoints,'affine');  
dst_img = imwarp(src,tform);  
t_sys = toc;
figure;imshowpair(src,dst_img,'montage');
title(['系统函数的仿射变换图像，耗时（s）：',num2str(t_sys)])  
  
%% method2,用3组点集对图像进行仿射变换，解方程求变换矩阵  
% T = [a11,a12,a13;a21,a22,a33];  
% 满足fixed_pt_matrix = T*moving_pt_matrix;
tic;
fixed_pt_matrix = fixedPoints';
moving_pt_matrix = [movingPoints';ones(1,size(movingPoints,1))]; 
T = fixed_pt_matrix/moving_pt_matrix;  

width = size(src,2);
height = size(src,1);
[moving_pt_x,moving_pt_y] = meshgrid(1:width,1:height);
coridate_affine = T*[moving_pt_x(:)';% 对原来图像所有坐标点变换到新平面上
    moving_pt_y(:)';
    ones(1,width*height)];
x_temp = coridate_affine(1,:);
y_temp = coridate_affine(2,:);
fixed_pt_x = reshape(x_temp,...
    size(moving_pt_x))+...
    abs(min(x_temp))+1;
fixed_pt_y = reshape(y_temp,...
    size(moving_pt_y))+...
    abs(min(y_temp))+1;
fixed_pt_x = round(fixed_pt_x);
fixed_pt_y = round(fixed_pt_y);

dst_affine_img = zeros(round(max(y_temp)-min(y_temp))+1,...
    round(max(x_temp)-min(x_temp))+1);
for i = 1:height
    for j = 1:width
        dst_affine_img(fixed_pt_y(i,j),fixed_pt_x(i,j)) = src(i,j);
    end
end
t_manual = toc;
figure;imshowpair(src,uint8(dst_affine_img),'montage');
title(['计算的仿射变换图像，耗时(s)：',num2str(t_manual)])  

%% 插值处理
[index_i,index_j] = find(dst_affine_img);
for i = 1:size(dst_affine_img,1)
    for j = 1:size(dst_affine_img,2)
        [min_distance,index_near] = min(sqrt((i-index_i).^2+(j-index_j).^2));
        if dst_affine_img(i,j)==0 && min_distance<=1
            dst_affine_img(i,j) = dst_affine_img(index_i(index_near),index_j(index_near));
        end 
    end
end
figure; imshowpair(src,uint8(dst_affine_img),'montage');
title('插值后图像')