def RunLength(strParam):
    results = ""
    current_run_character = ""
    run_length = 0

    for i in range(len(strParam)):
        if i == 0: 
            current_run_character = strParam[i]
            run_length = 1 
        else:
            current_char = strParam[i]
            if current_char == current_run_character:
                run_length += 1
            
            else:
               results += current_run_character + str(run_length)
               current_run_character = current_char
               run_length = 1
    results += current_run_character + str(run_length)           
    return results
original_text = input("Insira o texto que gostaria de comprimir: ")
print("Original text: " + original_text)
print("")
compressed_text = RunLength(original_text)
print("Compressed: " + compressed_text)
print("")

            
                