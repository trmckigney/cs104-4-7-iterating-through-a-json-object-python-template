def main():
    data = [
    {"word": "little", "score": 1001}, {"word": "fine", "score": 1000}, {"word": "late", "score": 999},
    {"word": "young", "score": 998}, {"word": "bright", "score": 997}, {"word": "est", "score": 996},
    {"word": "lucky", "score": 995}, {"word": "ugly", "score": 994}, {"word": "easy", "score": 993},
    {"word": "tenin", "score": 992}, {"word": "whitey", "score": 991}, {"word": "subtle", "score": 990}
 ]    # data contains the json list for 'pretty'

    list = []
    # TODO: Iterate over the data and extract the adjectives for the word and store them in the list variable
    for x in range(0, len(data)):
        tempdict = data[x] # Temporary variable to extract dictionary from data
        list.append(tempdict["word"]) # Append the list with the adjective

    # TODO: Print the list variable, Example of print: Adjectives for the word "word" are: [list of adjectives]
    print(f"The adjectives for the word 'pretty' are: {list}")

if __name__ == '__main__':
    main()