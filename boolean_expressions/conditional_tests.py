#Conditional Test
user = "analyst"
role = "viewer"
faild = 3
port = 22
#test 1 ==
#if (user == "analyst"):
    #print(True) ملزومة بشكل معين للكود
print("\n is analys == user" , ",I think it's False")  
print('analys' == user)
print("\n is viewer == role" ,",I think it's True")
print(role == "viewer")  #True
print()

#Test 2 !=
print("\n Is port != 5" ,",I think it's True")
print(port != 5)
print("\n Is faild != 3" ,",I think it's False")
print(faild != 3)

#Test 3 > "greater"
print("\n Is faild > 2" ,",I think it's True")
print(faild > 2)
print("\n Is user > 10" ,",I think it's False ")
print (len(user)>10)

#Test 4 < "Less"
print("\n Is port > 432 or role != 23" ,",I think it's True")
print(port < 432 or role != 23)
print("\n Is not (faild < 3)" ,",I think it's True")
print(not (faild <3) )

# Test 5 >= greater than or equel and <= less than or equel  
print("\n Is role >= 4 " ,",I think it's True")
print(len(role) >= 4)
print("\n Is port <=12 and port == 22 " ,",I think it's False")
print(port <= 12 and port == 22)