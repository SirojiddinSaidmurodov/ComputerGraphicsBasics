function outputArg = linear(inputArg)
outputArg = inputArg;
Xmax = max(max(inputArg(:,:,1)));
Xmin = min(min(inputArg(:,:,1)));
Ymin = 0;
Ymax = 255;
rows = size(inputArg, 1);
columns = size(inputArg,2);

for i = 1 : rows
    for j = 1 : columns
        for k = 1:3
            x1=uint16(inputArg(i,j,k) - Xmin);
            x2=uint16(Xmax - Xmin);
            y = (Ymax -Ymin);
        
            outputArg(i,j,k) = ((x1*y)/x2)+Ymin;
        end
    end
end
end

