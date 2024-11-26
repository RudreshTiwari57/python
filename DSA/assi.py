
"""
documentation:
    Task: to remove all the highlighted words in given string
    logic:  in the string all the highlighted words are repeating after
            one another in the string. Which can be implemented by removing duplicates words.
            i.e:
                we created the list of highlighted word and the removed words which are in list of highlighted word
                and are have "i and i+1" as same
    author: Rudresh Tiwari (rudreshtiwari57@gmail.com)
"""
def remove_highlighted_words(main_string,high_lighted_list):
    main_string_list = main_string.split(" ")
    final_string_list = []
    index = 0
    while len(main_string_list) > index:
        if len(main_string_list)-1 == index and main_string_list[index] not in high_lighted_list:
            final_string_list.append(main_string_list[index])
        elif main_string_list[index] in main_string_list[index+1]:
            final_string_list.append(main_string_list[index+1])
            high_lighted_list.remove(main_string_list[index+1])
            index = index+1
        else:
            final_string_list.append(main_string_list[index])
        index = index+1
    for high_lighted_word in high_lighted_list:
        final_string_list.remove(high_lighted_word)
    return final_string_list
main_string = "In the bustling bustling city city of New York, New York, the the bright bright lights lights and and the the constant constant hum hum of of activity activity create create an an atmosphere atmosphere that that is is both both exhilarating exhilarating and and exhausting exhausting. The bustling city lights and the constant hum of activity create an atmosphere that is both exhilarating and exhausting."
high_lighted_list = ["bustling","city","New","York,","the","bright",'lights',"and","the",'constant',"hum", "of","activity","create","an","atmosphere","that","is","both","exhilarating" ,"and", "exhausting."]
print(" ".join(remove_highlighted_words(main_string,high_lighted_list)))
