import inspect 
def varname(x): 
    return [k for k,v in inspect.currentframe().f_back.f_locals.items() if v is x][0]
def list_members(parent_obj):
    members=dir(parent_obj)
    parent_obj_name=varname(parent_obj)       
    for mbr in members:
        child_obj=eval(parent_obj_name + '.' + mbr) 
        if not mbr.startswith('_'):
            print(mbr, type(child_obj))