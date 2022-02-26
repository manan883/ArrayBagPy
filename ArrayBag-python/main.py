class ResizeableArrayBag:
    #hash maps: bags = {key:value,key:value}
    # b1 = bag('name')
    # bags = {'b1':b1}
    # bags['b1'].addItem('hello')
    # print(bags['b1'].doesItemExist('hello'))
    userInput = ''
    bags = {}
    # tests = {}
    def checkIfBagExists(self,s):
        if self.bags.get(s) is None:
            return False
        else:
            return True
    def checkIfBagIsNull(self,s):
        #assume bag exists
        if a.bags[s][0] is None:
            #is null
            return True
        else:
            #is not null
            return False
    def removePosition(self,s,name):
        try:
            s = int(s)
        except:
            return "Invalid Input!"
        print('before if')
        if a.checkIfBagExists(name) == False:
            return "ERROR: Bag does not exist!"
        else:
            x = a.bags[name]
            x.pop(s)
            a.bags[name] = x
    def listBag(self,s):
        if a.checkIfBagExists(s) == False:
            return "ERROR: Bag does not exist!"
        else:
            print(a.bags[s])
    def newBag(self,s):
        if a.checkIfBagExists(s) == True:
            return "Bag already exists!"
        else:
            c = s
            s = []
            a.bags[c] = s
    def deleteBag(self,s):
        if a.checkIfBagExists(s) == False:
            return "ERROR: Bag does not exist!"
        else:
            a.bags.pop(s)
    def addElement(self,bagN,e):
        if a.checkIfBagExists(bagN) == False:
            return "ERROR: Bag does not exist!"
        else:
            d = a.bags[bagN]
            d.append(e)
            a.bags[bagN] = d
    def union(self,bag1,bag2,newB):
        #combine 2 bags by adding lists together 
        if ((a.checkIfBagExists(bag1) == False) or (a.checkIfBagExists(bag2) == False)):
            return "ERROR: At least one bag does not exist!"
        elif a.checkIfBagExists(newB) == True:
            return "The new bag already exists!"
        else:
            i = a.bags[bag1]
            m = a.bags[bag2]
            x = i + m
            a.bags[newB] = x
            print("Bag " + newB + " was created with the contents listed below")
            a.listBag(newB)
    def intersection(self,bag1,bag2,newB):
        if ((a.checkIfBagExists(bag1) == False) or (a.checkIfBagExists(bag2) == False)):
            return "ERROR: At least one bag does not exist!"
        elif a.checkIfBagExists(newB) == True:
            return "The new bag already exists!"
        else:
            #set lists to each bag
            i = a.bags[bag1]
            m = a.bags[bag2]
            x = []
            #check which one is bigger and whichever one is will be on the outer loop 
            if len(i) > len(m):
                #i on the outside
                for k in i:
                    for q in m:
                        if k == q:
                            x.append(k)
            elif len(i) < len(m):
                #m on the outside
                for k in m:
                    for q in i:
                        if k == q:
                            x.append(k)
            else:
                #either on the outside
                for k in m:
                    for q in i:
                        if k == q:
                            x.append(k)
            a.bags[newB] = x
            print("Bag " + newB + " was created with the contents listed below")
            a.listBag(newB)
    def difference(self,bag1,bag2,newB):
        #set lists to each bag
        i = a.bags[bag1]
        m = a.bags[bag2]
        x = []
        #remove dupes from both bags and put the difference in the new one
        if ((a.checkIfBagExists(bag1) == False) or (a.checkIfBagExists(bag2) == False)):
            return "ERROR: At least one bag does not exist!"
        elif a.checkIfBagExists(newB) == True:
            return "The new bag already exists!"
        else:
            x = i + m
            x = list(set(x))
        a.bags[newB] = x
            


a = ResizeableArrayBag()
a.newBag("bag1")
a.newBag("bag2")
a.addElement("bag1","Hello")
a.addElement("bag2","Hello")
a.addElement("bag2","different2")
a.addElement("bag1","diff1")
a.addElement("bag2","nello")
a.addElement("bag1","nello")
a.difference("bag1","bag2","newB")
a.listBag("newB")



# AFK code
    # while (True):
    #     print('Welcome to the bag')
    #     print('Type "M" to make a new bag')        
    #     print("Type 'A' to add an element to a bag")
    #     print("Type 'R' to remove an element from a bag")
    #     print("Type 'D' to delete a bag")
    #     print("Type 'L' to list every bag name created")
    #     print("Type 'U' to combine 2 bags")
    #     print("Type 'I' to intersect 2 bags")
    #     print("Type 'F' to get the difference between 2 bags")
    #     print("Type 'Q' to quit")
    #     userInput = input()
    #     if userInput == "q":
    #         break
    #     elif userInput == "Q":
    #         break
    #     elif userInput == "r":
    #         # s = removePosition('self','1','name')
    #         print(test('','j'))
    # testing the new method 
    # m = []
    # n = []
    # l = []
    # a.test("hello")
    # a.test("kello")
    # a.test("new")
    # n = a.tests["kello"]
    # m = a.tests["hello"]
    # m.append("k")
    # l = m+n
    # a.tests["hello"] = m
    # a.tests["new"] = l
    # print(a.tests["new"][0])
        # def test(self,s):
        # c = s
        # s = []
        # s.append(c)
        # self.tests[c] = s