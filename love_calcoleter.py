print("welcome to love calcolater")
name1 = input("what is your name ?? \n")
name2 = input("what is your crach name ?? \n")
name1.lower()
name2.lower()
lc1 = name1.count("l")
lc2 = name2.count("l")
oc1 = name1.count("o")
oc2 = name2.count("o")
vc1 = name1.count("v")
vc2 = name2.count("v")
ec1 = name1.count("e")
ec2 = name2.count("e")
love = lc1+ lc2 +oc1 + oc2 +vc1 + vc2 + ec1 +ec2
tc1 = name1.count("t")
tc2 = name2.count("t")
rc1 = name1.count("r")
rc2 = name2.count("r")
uc1 = name1.count("u")
uc2 = name2.count("u")
Ec1 = name1.count("e")
Ec2 = name2.count("e")
truec = tc1 + tc2 + rc1 + rc2 + uc1 +uc2 + Ec1 +Ec2 
p = str(truec) + str(love)
final_per = int(p)
if(final_per < 10 or final_per > 90 ):
    print(f"your score is {final_per}, you go to gether like coke and mentos ")
elif(final_per >= 40 and final_per <= 50):
    print(f"your scoure is {final_per}, you are alright together ")
else:
    print(f"your scoure is {final_per}")

