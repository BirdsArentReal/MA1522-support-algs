function n = gcdVector(v)
    % given a vector with integer entries, return its gcd
    % mainly to quickly find the gcd of many numbers at once

    v = v(:);            % flattens a matrix into a vector
    curr = 0;
    len = length(v);    % length is flexible enough to handle row or col

    for i = 1:len
        curr = gcd(curr, v(i));
    end
    n = curr;
end