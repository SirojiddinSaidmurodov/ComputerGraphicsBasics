function PuassonAndVinerFiltering(file)
image = imread(file);
figure, imshow(image);title("Original image")
noised = imnoise(image,'poisson');
figure, imshow(noised);title("Image with Poisson noise")
R = noised(:,:,1);
G = noised(:,:,2);
B = noised(:,:,3);
R = wiener2(R,[5 5]);
G = wiener2(G,[5 5]);
B = wiener2(B,[5 5]);
image(:,:,1) = R;
image(:,:,2) = G;
image(:,:,3) = B;
figure, imshow(image);title("Filtered image")
end