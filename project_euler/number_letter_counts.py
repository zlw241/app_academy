

number_dict = {
    0: '', 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 
    18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
    80: "eighty", 90: "ninety"
}


def generate_number_dict(base_dict):

    for t in [1,10,100,1000]:
        for i in range(1,10):
            num = i*t
            num_len = len(str(num))
            if num_len == 4:
                base_dict[num] = "{} thousand".format(base_dict[int(str(num)[0])])
            elif num_len == 3:
                base_dict[num] = "{} hundred".format(base_dict[int(str(num)[0])])
    return base_dict

full_number_dict = generate_number_dict(number_dict)


class Number_Word:


    def __init__(self, number):
        self.number = number
        self.length = self.get_length()
        self.number_dict = full_number_dict
        #self.number_word = self.str_number()
        

    def num_word_list(self, num):
        if len(str(num)) == 1:
            return [number_dict[num]]
        if 10 < num < 20:
            return [number_dict[num]]
        num_list = [int(i) for i in str(num)]
        ten_powers = reversed([10**i for i in range(len(str(num)))])
        digits_list = [number_dict[n*p] for n,p in zip(num_list, ten_powers) if number_dict[n*p]]
        return [digits_list[0]] + self.num_word_list(int(str(num)[1:]))

    def format_words(self, num_words):
        counter = 0
        num_words = list([w for w in num_words if w])
        len_word_list = len(num_words)
        while counter < len_word_list-1:
            if num_words[counter].endswith('hundred'):
                num_words.insert(counter+1, ' and ')
                len_word_list += 1
            elif num_words[counter] in [self.number_dict[i] for i in [20,30,40,50,60,70,80,90]]:
                num_words.insert(counter+1, '-')
                len_word_list += 1
            counter += 1
        return ''.join(num_words)


    def make_word(self):
        num = self.number
        word_list = self.num_word_list(num)
        formatted_word_list = self.format_words(word_list)
        return str(formatted_word_list)
        

    def get_length(self):
        return len(str(self.number))

    def __str__(self):
        return str(self.make_word())




nums_as_words_1000 = []
for i in range(1,1001):
    wn = Number_Word(i)
    nums_as_words_1000.append(wn)

print(len(nums_as_words_1000))
count = 0
for i in nums_as_words_1000:
    str_num = str(i)
    count += len(str_num.replace(' ', '').replace('-',''))



print(count)










