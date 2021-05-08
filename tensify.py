class PAST:
    def __init__(self,past):
        self.past = past
        def SPR2SPA(test_string):
            # test_string = input("Enter a sentence :")
            test_list =    ['get', 'eat','die','love','loves','live','lives','enjoys','enjoy','does','come','comes','do','need','needs','like','likes','are']
            replace_list = ['got','ate','died','loved','loved','lived','lived','enjoyed','enjoyed','did','came','came','did','needed','needed','liked','liked','were'] 
            res = [ele for ele in test_list if(ele in test_string)]
            for word in res:
                # print(word)# print("Index is: ")# print(test_list.index(word))
                indexNumber = test_list.index(word)
                replacedSentence = test_string.replace(word,replace_list[indexNumber])
                print(replacedSentence)
                # someVar = res.index()
                # print("String contain any list element : " + str(res[0]))
                # replaced = test_string.replace(res[0],replace_list[0])
                # print(replaced)

        SPR2SPA(past)