function [Q, ortho] = GramSchmidt(A)
    % @param A          any finite dimensional matrix

    % @return Q         the orthonormal basis of the 
    %                   column space of A.
    % @return ortho     the orthonormal basis of the nullspace 
    %                   of A-transpose.
    [Q, R] = qr(sym(A));
    
    count_non_zero_rows = 0;
    for i = 1:width(Q)
        row = R(i, :);
        if ~any(row) % if all zeroes
            break % stop counting
        end

        count_non_zero_rows = count_non_zero_rows + 1;
    end

    ortho = Q(:, count_non_zero_rows+1:end);
    Q = Q(:, 1:count_non_zero_rows);

end