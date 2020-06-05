function output = prep(bit_grid)
rows = size(bit_grid, 1);
columns = size(bit_grid,2);
output = bit_grid;
for i = 1 : rows
    for j = 1 : columns
        
        if bit_grid(i,j)>127
            output(i,j)=255;
        else
            output(i,j) = 0;
        end
    end
end
end

