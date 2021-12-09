"""
Populate a hash tag triangle.


   #
  # #
 # # #
# # # # 

- Relative padding (eg. 4 wide requires 3 padding (4 blocks) of row 1
"""

base_wdth = 4




output = ""

# Parent loop for row control
for row in range(1, base_wdth + 1): # 4 loops
    row_str = ""
    
    # Pad beginning of string for left side structure
    for i in range(1, base_wdth - row + 1):
        row_str += " "
        
    # Fill the remaining row with padded #'s
    for i in range(1, row + 1):
        row_str += "# "
        

    row_str += "\n"
    output += row_str


print(output, end="")

