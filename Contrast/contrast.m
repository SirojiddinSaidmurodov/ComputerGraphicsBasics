function contrast(file)
image = imread(file);
figure, imshow(image);title("������������ �����������");
figure, imhist(image);title("Original image");
R = image(:,:,1);
G = image(:,:,2);
B = image(:,:,3);
output = image;
output(:,:,1) = prep(R);
output(:,:,2) = prep(G);
output(:,:,3) = prep(B);
figure, imshow(output);title("���������������� ������� ��������������");
figure, imhist(output);title("���������������� ������� ��������������");
output=linear(image);
figure, imshow(output);title("�������� ����������������");
figure, imhist(output);title("�������� ����������������");
end
