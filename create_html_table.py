"""
  print(html_table_string("myname",2,4))
  returns
  
  <table id="myname">
	<tr id=r0>
		<td r0c0>cell:r0c0</td>
		<td r0c1>cell:r0c1</td>
		<td r0c2>cell:r0c2</td>
	</tr>
	<tr id=r1>
		<td r1c0>cell:r1c0</td>
		<td r1c1>cell:r1c1</td>
		<td r1c2>cell:r1c2</td>
	</tr>
</table>
"""
def one_row_x_columns( row_num_int, col_int):
    nl = "\n"
    t  = "\t"
    r = str(row_num_int)
    tr_open_str = t + "<tr id=r"+ str(row_num_int) +">" + nl
    tr_close_str = t + "</tr>" + nl
    td_firsthalf_str = (t*2)+"<td r" + str(row_num_int) + "c"
    td_content_str = ""    
    for c in range(col_int):
        td_content_str = td_content_str + td_firsthalf_str + str(c) + ">" + "cell:r" + r + "c"+ str(c)+ "</td>" + nl
    return (tr_open_str + td_content_str + tr_close_str)
    
def create_html_table( table_id_str, row_int, col_int):#CALL
    rslt=""
    for r in range(row_int):
        rslt = rslt + one_row_x_columns( r,col_int )
    rslt="<table id=\""+table_id_str+"\">\n" + rslt + "</table>"
    return rslt

