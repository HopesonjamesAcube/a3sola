import frappe



def validate(doc,methods):
    

    #check for capacity and unit per kw is defined 
    #calculate all fields from the base of capacity and unit per kw
    if doc.capacity_of_plant and doc.unit_perkw:
        capacity=doc.capacity_of_plant
        unitkw=doc.unit_perkw
        per_day_gen=capacity*unitkw
        monthly_gen=per_day_gen*30
        bimonthly_gen=monthly_gen*2
        yearly_gen=monthly_gen*12

        doc.monthly_gen=monthly_gen
        doc.per_day_gen=per_day_gen
        doc.monthly_gen=monthly_gen
        doc.bimonthly_gen=bimonthly_gen
        doc.yearly_generation=yearly_gen
        
        


