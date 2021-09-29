print("********************************************* Credit Appraisal Skills********************************************")
print('''RULES
    RIGHT ANSWER = +1000 rupees
    WRONG ANSWER = -500 rupees
        ALL THE BEST\n''')
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
score=0
name=input("Enter your name: ")


print("\n\nQuestion 1") 
print("What does CAD Breach relate to?")
answer_1 = input("\na)Breach of Individual Credit authority limits\nb)Breach of Individual Credit appraisal limits\nc)Both A & B\nd)Neither A and B\nEnter your answer : ")
if answer_1.lower() == "a" or answer_1.lower() == "Breach of Individual Credit authority limits":
    
    a = a + 1000 
    print("\nCorrect,\nCongratulations you have received ",a ,"rupees")
    print("\nCurrent balance",a,"rupees")

else:
    print("\nIncorrect,\n The correct option is a)Breach of Individual Credit authority limits")
    a = a - 500   
    print("\nCurrent balance",a,"rupees")

print("\n\nQuestion 2") 
print("An RBA related PAR error will lead to:")
answer_2 = input("\na)No change\nb)Just an adverse remark\nc)Penalisation of scores\nd)None of these\nEnter your answer : ")
if answer_2.lower() == "c" or answer_2.lower() == "Penalisation of scores":
    print("\nCorrect,\nCongratulations you have received 1000 rupees")
    b= b + 1000
    print("\nCurrent balance",a+b,"rupees")

else:
    print("\nIncorrect,\n The correct option is c)Penalisation of scores")
    b= b - 500
    print("\nCurrent balance",a+b,"rupees")



print("\n\nQuestion 3") 
print("The world's largest Microfinance database was established by this Credit Bureau:")
answer_3 = input("\na)Transunion CIBIL\nb)Equifax\nc)Experian\nd)CRIF Hi-mark\nEnter your answer : ")
if answer_3.lower() == "d" or answer_3.lower() == "CRIF Hi-mark":
    c= c + 1000
    print("\nCorrect,\nCongratulations you have received ",c,"rupees")
    print("\nCurrent balance",a+b+c,"rupees")

else:
    print("\nIncorrect,\n The correct option is d)CRIF Hi-mark ")  
    c= c - 500
    print("\nCurrent balance",a+b+c,"rupees")


print("\n\nQuestion 4") 
print("How are SMA cases classified ?")
answer_4 = input("\na)Standard Assets\nb)Sub-standard Asset\nc)Doubtful Assets\nd)Loss Assets\nEnter your answer : ")
if answer_4.lower() == "a" or answer_4 == "Standard Assets":
    d= d + 1000
    print("\nCorrect,\nCongratulations you have received ",d,"rupees")
    print("\nCurrent balance",a+b+c+d,"rupees")


else:
    print("\nIncorrect,\nThe correct option is a)Standard Assets")
    d= d - 500
    print("\nCurrent balance",a+b+c+d,"rupees")

print("\n\nQuestion 5")  
print("Large exposures which turn SMA have to be reported to :")
answer_5 = input("\na)CRILC\nb)CIRLC\nc)CIBIL\nd)CRIF Hi-mark\nEnter your answer : ")
if answer_5.lower() == "a" or answer_5.lower() == "CRILC":
    
    e= e + 1000
    print("\nCorrect,\nCongratulations you have received ",e,"rupees")
    print("\nCurrent balance",a+b+c+d+e,"rupees")
else:
    print("\nIncorrect,\n The correct option is a)CRILC")
    e= e - 500
    print("\nCurrent balance",a+b+c+d+e,"rupees")

print("\n\nQuestion 6") 
print("The Numerator for Total Debt: Equity ratio is.... ")
answer_6 = input("\na)Only Long Term Debt\nb)Long Term + Short Term Debt\nc)Long Term Debt + Short Term Debt + Creditors\nd)Preference Capital\nEnter your answer : ")
if answer_6.lower() == "b" or answer_6.lower() == "Long Term + Short Term Debt":
    
    f= f + 1000
    print("\nCorrect,\nCongratulations you have received ",f,"rupees")
    print("\nCurrent balance",a+b+c+d+e+f,"rupees")

else:
    print("\nIncorrect,\nThe correct option is b)Long Term + Short Term Debt")
    f= f - 500
    print("\nCurrent balance",a+b+c+d+e+f,"rupees")


print("\n\nQuestion 7") 
print("For which type of customers is a high Current Ratio be considered normal ?")
answer_7 = input("\na)Highly leveraged Customers\nb)Customers who have never availed any Credit facilities \nc)Customers with a low DSCR\nd)No of these\nEnter your answer : ")
if answer_7.lower() == "b" or answer_7.lower() == "Customers who have never availed any Credit facilities ":

    g= g + 1000
    print("\nCorrect,\nCongratulations you have received ",g,"rupees")
    print("\nCurrent balance",a+b+c+d+e+f+g,"rupees")

else:
    print("\nIncorrect,\nThe correct option is b)Customers who have never availed any Credit facilities")
    g= g - 500
    print("\nCurrent balance",a+b+c+d+e+f+g,"rupees")

print("\n\nQuestion 8") 
print("The denominator of a DSCR is annualised because...")
answer_8 = input("\na)the numerator is on an annual basis, the denominator needs to be on the same terms.\nb)the numerator is on a monthly basis, the denominator also needs to be on the same terms.\nc)the numerator is on a quarterly basis, the denominator also needs to be on the same terms.\nd)None of these\nEnter your answer : ")
if answer_8.lower() == "a" or answer_8.lower() == "the numerator is on an annual basis, the denominator needs to be on the same terms.":
    
    h= h + 1000
    print("\nCorrect,\nCongratulations you have received ",h,"rupees")
    print("\nCurrent balance",a+b+c+d+e+f+g+h,"rupees")


else:
    print("\nIncorrect,\nThe correct option is a)the numerator is on an annual basis, the denominator needs to be on the same terms.")
    h= h - 500
    print("\nCurrent balance",a+b+c+d+e+f+g+h,"rupees")

print("\n\nQuestion 9") 
print("In the five C's for Credit Effectiveness, what 'C' deals with the intention of the borrower to repay the loan?")
answer_9 = input("\na)Character\nb)Collateral\nc)Capacity\nd)Condition\nEnter your answer : ")
if answer_9.lower() == "a" or answer_9.lower() == "Character":

    i= i + 1000
    print("\nCorrect,\nCongratulations you have received ",i,"rupees")
    print("\nCurrent balance",a+b+c+d+e+f+g+h+i,"rupees")

else:
    print("\nIncorrect,\nThe correct option is a)Character")
    i= i - 500
    print("\nCurrent balance",a+b+c+d+e+f+g+h+i,"rupees")



print("\n\nQuestion 10") 
print("As per the new MSME definitions effective from July 1st, 2020, MSME's have been classified on the basis of:")
answer_10 = input("\na)Investment in Plant & Machinery or Equipment only\nb)Profit After Tax\nc)Turnover only\nd)Investment in Plant & Machinery or Equipment and Turnover\nEnter your answer : ")
if answer_10.lower() == "d" or answer_10.lower() == "Investment in Plant & Machinery or Equipment and Turnover":
    
    j= j + 1000
    print("\nCorrect,\nCongratulations you have received ",j,"rupees")
    print("\nCurrent balance",a+b+c+d+e+f+g+h+i+j,"rupees")

else:
    print("\nIncorrect,\nThe correct option is d)Investment in Plant & Machinery or Equipment and Turnover")
    j= j - 500
    print("\nCurrent balance",a+b+c+d+e+f+g+h+i+j,"rupees\n\n")

print("************************************RESULT*********************************************\n")
myList=[a,b,c,d,e,f,g,h,i,j]
#print(f"Points per question{myList}")
if sum(myList) > 0:
    print(f"{name} you won {sum(myList)} rupees!\n")
    print(f"To win more money play again!\n")
else:
    print(f"{name} you lost {sum(myList)} rupees\n")
    print("To win play again.\n")