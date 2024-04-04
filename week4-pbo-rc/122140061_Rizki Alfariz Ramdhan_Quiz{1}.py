import random

stages = ["""
            ------
            |    |
            |
            |
            |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |
            |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |   /
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |   / \\
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |  --|
            |    |
            |   / \\
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |  --|--
            |    |
            |   / \\
            |
        ------------
        """]

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.guessed_letters = []
        self.attempts = 0

    def display_word(self):
        display_word = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                display_word += letter + ' '
            else:
                display_word += '_ '
        return display_word

    def guess_letter(self, letter):
        if letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            if letter in self.word:
                print('Correct guess!')
            else:
                self.attempts += 1
                print('Incorrect guess!')
                print('you have ',7-self.attempts,' attempts left')
        else :
          print('You have already guessed this letter.')

    def check_win(self):
        return bool('_' not in self.display_word() or self.attempts == 7)

    def display_stage(self):
        print(stages[self.attempts])

def main():
    word_list = ['algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
    'encryption', 'framework', 'function', 'garbage', 'hash', 'index', 'iterator',
    'javascript', 'json', 'library', 'loop', 'namespace', 'object', 'operator',
    'overload', 'polymorphism', 'queue', 'recursion', 'serialization', 'stack',
    'template', 'variable', 'virtual', 'web', 'xml', 'yaml', 'zip']
    game = Hangman(word_list)

    while True:
        game.display_stage()
        print(game.display_word())
        guess = input('Guess a word: ').lower()
        if len(guess) == 1:
            game.guess_letter(guess)
        else:
            print('Please guess only one letter!')

        if game.check_win():
            if '_' not in game.display_word():
                print('Congratulations, you`ve guessed the word ' + game.word)
            elif game.attempts == 7:
                print('Sorry, you lost. The word was ' + game.word)
            break

if __name__ == '__main__':
    main()