print("Part 2b:")
module = "CSC1009";   
match module: 
    case "CSC1006":   
        print("Mathematics 2");  
    case "CSC1007":   
        print("Operating Systems"); 
    case "CSC1008":   
        print("Data Structures and Algorithms"); 
    case "CSC1009":   
        print("Object-Oriented Programming"); 
    case "CSC1010":   
        print("Computer Networks");  
    case _:    
        print("Unknown Module"); 

print("Part 2c:")
for x in range(101,66,-2):
    print(x)

