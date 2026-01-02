function [loc] = Satellite(CoordsThenDistRow)
    % triangulation for any number of dimensions.

    % @param Coords...  A matrix such that each row represents a 
    %                   point (or GPS satellite). The format of 
    %                   each row is expected to be [[coords] dist],
    %                   where [coords] is a vector representing the 
    %                   position of the satellite in Cartesian-coordinates,
    %                   and dist is the Euclidean distance from the 
    %                   satellite to the target point.

    % @return loc       the position vector of the target point

    % loc is coordinates of the point
    % we assume system is uniquely solvable

    % hw1 question

    %{ 
        we assume each row of coords is
        [[coords] dist]
    %}

    nCols = width(CoordsThenDistRow);
    nRows = height(CoordsThenDistRow);

    coords = CoordsThenDistRow(:, 1:nCols-1); % Extract coordinates from the input
    % coords now looks like [v1' ; v2' ; v3' ; ...] 

    dist = CoordsThenDistRow(:, nCols); % last col should be the distances

    %{
    ([x1 x2 x3 ...] - v1)^2 = d1^2
    
    (x1^2 + x2^2 + ...) - 2(v1x1.x1 + v1x2.x2 + ...) + v1.v1 = d1^2

    2[(v1x1.x1 - v2x1.x1) + (v1x2.x2 - v2x2.x2) + ...] = (d2^2 - d1^2) - (v2^2 - v1^2)

    2[(v1x1 - v2x1) (v1x2 - v2x2) (v1x3 - v2x3) ...] = [(d2^2 - d1^2) - (v2^2 - v1^2)]

    seems like each row is just 2[v1' - vi'] = [(di^2 - d1^2) - (vi^2 - v1^2)]

    I am pretty sure di^2 is diagonal of dist*dist'
    and vi^2 = diagonal of coords * coords'
    %}

    distSquared = dist.^2; % recommended by copilot so I shall use it lol
    coordsSquared = diag(coords * coords');

    % subtract row one from each row of coords
    rowDiffs = coords(2:end, :) - coords(1, :); % Subtract the first row of coords from all rows
    LHS = -2 * rowDiffs; % Calculate the scaled differences

    % same for distSquared and coordsSquared
    distDiffs = distSquared(2:end) - distSquared(1);
    coordsDiffs = coordsSquared(2:end) - coordsSquared(1);
    RHS = (distDiffs) - (coordsDiffs);
    final_mat =  [LHS RHS];
    loc = LHS \ RHS; % Solve for the location using left division 
end