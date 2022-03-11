class Phrase:
    
    def display(self, active_phrase, guesses):
        self.active_phrase = active_phrase
        self.hidden_phrase = []
        blank = "_ "
        for letter in active_phrase:
            if letter in guesses:
                self.hidden_phrase.append(letter)
            if letter not in guesses:
                if letter != " ":
                    self.hidden_phrase.append(blank)
            if letter == " ":
                self.hidden_phrase.append(" ")
        self.display_phrase = "".join(self.hidden_phrase)
        print(self.display_phrase)
        return(self.display_phrase)
    
    def check_complete(self, lives, display_phrase, active_phrase):
        if lives == 0:
            return "lose"
        if display_phrase == active_phrase:
            return "win"
        if display_phrase != active_phrase and lives > 0:
            return "incomplete"
        
        
  