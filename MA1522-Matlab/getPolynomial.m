function [coeffsStartWithConst, poly] = getPolynomial(inputs, outputs)
    % @param inputs     the inputs to the polynomial.
    % @param outputs    the values of the polynomial at the inputs.

    % @return coeffs... the coefficients of the polynomial,
    %                   starting from the constant. (i.e. 3x^2 + 1
    %                   is represented as [1 0 3]'

    % @return poly      the polynomial form (i.e. 3x^2 + 0x + 1)
    

    % getPolynomial force inputs and outputs to be column vectors
    inputs = inputs(:);
    outputs = outputs(:);

    % Fit a polynomial to the data
    coeffsStartWithConst = polyfit(inputs, outputs, length(inputs) - 1);
    syms x;
    coeff = [];
    for k = 0:length(inputs)-1
        coeff = [x^k coeff];
    end
    poly = coeffsStartWithConst * transpose(coeff);
end