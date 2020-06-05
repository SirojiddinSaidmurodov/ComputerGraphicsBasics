function contrast(file)
image = imread(file);
figure, imshow(image);title("Оригинальное изображение");
figure, imhist(image);title("Original image");
R = image(:,:,1);
G = image(:,:,2);
B = image(:,:,3);
output = image;
output(:,:,1) = prep(R);
output(:,:,2) = prep(G);
output(:,:,3) = prep(B);
figure, imshow(output);title("Контрастирование методом препарирования");
figure, imhist(output);title("Контрастирование методом препарирования");
output=linear(image);
figure, imshow(output);title("Линейное контрастирование");
figure, imhist(output);title("Линейное контрастирование");
end
