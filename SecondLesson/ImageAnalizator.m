function ImageAnalizator(file)
image = imread(file);
subplot(2,3,[1:3])
imshow(image);
title("»сходное изображение");
R = image(:,:,1);
G = image(:,:,2);
B = image(:,:,3);
subplot(2,3,4);
imhist(R);
subplot(2,3,5);
imhist(G);
subplot(2,3,6);
imhist(B);
sgtitle("√истограмма €ркости исходного изображени€");
editedR = im2uint8(mat2gray(log(1+double(R))));
editedG = im2uint8(mat2gray(log(1+double(G))));
editedB = im2uint8(mat2gray(log(1+double(B))));
editedImage = image;
editedImage(:,:,1) = editedR;
editedImage(:,:,2) = editedG;
editedImage(:,:,3) = editedB;
subplot(2,3,[1,2,3]);
imshow(editedImage);
title("изображение после контрастировани€");
subplot(2,3,4);
imhist(editedR);

subplot(2,3,5);
imhist(editedG);
subplot(2,3,6);
imhist(editedB);
sgtitle("√истограмма €ркости изображени€ после контрастировани€");
end