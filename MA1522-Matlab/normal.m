function [Result, ScaleSquare] = normal(columns)
   % @param columns     The vectors to be (L2) normalised

   % @return Result     The normalised columns.
   % @return ScaleSq    Square of the scaling factors, 
   %                    for easier reading.

   dots = columns' * columns;
   ScaleSquare = diag(diag(dots));
   Scale = sqrtm(ScaleSquare);
   Result = columns / Scale;

end