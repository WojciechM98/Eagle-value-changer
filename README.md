# Eagle-value-changer (EVC)
<hr/>
A script that automates batch changes to Eagle.sch files.

## How does ECV works
Move .sch files to **data** folder or multiple folders with .sch files in them.
Specify a field (box) where interested value may be located. Change variable called **replacement_value**
with new value. Run the script. 

Works only for static values like revision, scheme name etc.
Note that the box containing a value position can only contain that one value.