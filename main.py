def main():
    class Book:
        def __init__(self,name,path):
            self.path = path
            self.name = name

        def count_words(self):
            with open(self.path) as book:
                return len(
                            book.read()
                           .split()
                           )
            
        def __count_letters(self):
            letters_count = {
                
            }
            words = []
            with open(self.path) as book:
                text = book.read()
                for letter in text:
                    if letter.lower() in letters_count:
                        letters_count[letter.lower()] += 1
                    else:
                        letters_count[letter.lower()] = 1
            return letters_count
                        
        def report(self):
            print (f"The report of {self.name} book in {self.path}")
            words = self.count_words()
            letters = []
            for letter in self.__count_letters():
                if letter.isalpha():
                    letters.append({"letter":letter,"number":self.__count_letters()[letter]})
            def sort_on(dict):
                return dict["number"]
            
            letters.sort(reverse=True,key=sort_on)
            print(f"Number of words: {words}")
            for letter in letters:
                print(f"The letter: {letter['letter']} was found {letter['number']} times in the current book")
            print(f"Report ended")


    book = Book("frankenstein","books/frankenstein.txt")
    book.report()

main()