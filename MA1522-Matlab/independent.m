function [A, order] = independent(M)
    % @param M      The matrix to be reshuffled such that all
    %               independent columns are in front.

    % @return A     M with columns shifted so rref(A) = [I R].
    %               That is, all independent columns of M have been
    %               shifted to the front.
    % @return order The original position of each column of A, in
    %               the matrix M.

    R = rref(M);

    % find pivot columns of R
    order = 1:width(M);
    for row = 1:height(R)
        for col = 1:width(R)
            if R(row, col) ~= 0
                order([row col]) = order([col row]); % Store the pivot column index
                break; % Move to the next row after finding a pivot
            end
        end
    end
    
    A = M;
    A(:, 1:end) = A(:, order);


end