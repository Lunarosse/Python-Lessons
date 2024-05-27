original=['John','Daisy','Jack','Luna','Alex']
modified=[name.upper() for name in original if name !='John'and name !='Daisy'and name !='Jack']
print(modified)