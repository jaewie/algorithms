def linear_regression(pts, slope=-1.0, y_intercept=0, iterations=500):
    if not iterations: return slope, y_intercept

    slope, y_intercept = step_gradient(slope, y_intercept, pts)
    return linear_regression(pts, slope, y_intercept, iterations - 1)

def slope_partial_deriv(f, pts):
    '''The partial derivative of the error function respect to the slope.'''
    pt_error = lambda pt: -pt.x * (pt.y - f(pt.x))
    return (2 / len(pts)) *  sum(pt_error(pt) for pt in pts)

def y_intercept_partial_deriv(f, pts):
    '''The partial derivative of the error function respect to the y-intercept.'''
    pt_error = lambda pt: -(pt.y - f(pt.x))
    return (2 / len(pts)) * sum(pt_error(pt) for pt in pts)

def step_gradient(slope, y_intercept, pts, learn_rate=0.0005):
    f = lambda x: slope * x + y_intercept
    new_slope_gradient = slope - learn_rate * slope_partial_deriv(f, pts)
    new_y_intercept_gradient = y_intercept - learn_rate * y_intercept_partial_deriv(f, pts)

    return new_slope_gradient, new_y_intercept_gradient
