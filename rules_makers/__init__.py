from skfuzzy import control as ctrl

def add_rule(sqft_living,sqft_lot,sqft_basement,view,bedrooms,bathrooms,floors,condition,distance,price,input_vars,output_var):
    return ctrl.Rule(input_vars['sqft_living'][sqft_living] & input_vars['sqft_lot'][sqft_lot] &
    input_vars['sqft_basement'][sqft_basement] & input_vars['sqft_basement'][sqft_basement] &
    input_vars['view'][view] & input_vars['bedrooms'][bedrooms] & input_vars['bathrooms'][bathrooms] &
    input_vars['floors'][floors] & input_vars['condition'][condition] & input_vars['distance'][distance],output_var[price])