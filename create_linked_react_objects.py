"""
React objects start with capital letters
print(create_linked_react_objects(["Party","Table","Guest"])) generates

function Party(){
		return (
		<Table></Table>
	);
}
function Table(){
		return (
		<Guest></Guest>
	);
}
function Guest(){
		return (
		<div></div>
	);
}

"""

t="\t"
nl="\n"
def second_half_div_object(): return "return (<div></div>); }"

def react_object_str(parent_str,child_str):
    return "function "+parent_str+"(){"+nl+(t*2)+"return ("+nl+(t*2)+"<"+child_str+"></"+child_str+">"+nl+(t*2)+");"+nl+"}"+nl


def create_linked_react_objects (arr_str):#CALL
    rslt = ""
    if(len(arr_str)==1):return react_object_str(arr_str[0],"div")
    if(len(arr_str)==2):return react_object_str(arr_str[0],arr_str[1])+ react_object_str( arr_str[len(arr_str)-1], "div" )
    for  k in range( len(arr_str)-1 ):
        rslt = rslt + react_object_str(arr_str[k],arr_str[k+1])
    rslt = rslt + react_object_str( arr_str[len(arr_str)-1], "div" )
    return rslt
