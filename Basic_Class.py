class Basic_Class:
    name = []

    def addNumbers(self, a, b):
        return a + b

    def generateLeetSpeak(self, text):
        replacements = (('a','4'), ('e','3'),
                 ('l','1'), ('o','0'), ('t','+'), ('s', '5') )

        leet_speek_text = text.lower()
        for old, new in replacements:
            leet_speek_text = leet_speek_text.replace(old, new)

        return leet_speek_text

if __name__ == '__main__':
    my_class = Basic_Class()
    a = 2
    b = 8
    text = 'This is a test text for transforming into leet speak'

    print('%i + %i = %i' % (a, b, my_class.addNumbers(a,b)))
    print('transforming "%s" into "%s"' %(text, my_class.generateLeetSpeak(text)))