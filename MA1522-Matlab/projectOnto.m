function [Res, Xs, NullSp] = projectOnto(ColSp, Cols)
    % @param ColSp  the Column Space to be projected onto
    % @param Cols   the vectors to be projected

    % @return Res   projections of Cols onto ColSp

    % if the projection is not perfect, 
    % @return Xs    the least square solutions to (ColSp)x = Cols
    % @return NSp   the nullspace of (ColSp) so you can add to x if needed

    AtA = ColSp' * ColSp;
    Atb = ColSp' * Cols;
    
    sol = rref([AtA Atb]);
    skipCols = width(AtA);

    [~, order] = independent(AtA);

    Xs = sol(:, skipCols+1:end);
    Xs(:, :) = Xs(order, :);
    Res = ColSp * Xs;
    NullSp = null(sym(AtA));
end