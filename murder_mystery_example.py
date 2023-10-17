from murder_mystery_printer.printer import Character, Event, Printer, NoEscape
import os

if __name__ == '__main__':
    
    c1 = Character('Character One', logo_fn='murder_mystery_printer/logos/char1.png')
    c2 = Character('Character Two', logo_fn='murder_mystery_printer/logos/char2.png')
    
    e1 = Event('Character One punched Character Two a year ago', act=1)
    e2 = Event('Character One & Character Two are secretly siblings', act=1, private=True)
    
    c1 += e1
    c1 += e2
    c2 += e1
    c2 += e2
    
    c1 += Event('Character One is not great', act=2)
    
    fight_yesterday = Event('Character One punched Character Two yesterday', act=3)
    c1 += fight_yesterday
    c2 += fight_yesterday
    
    #doc_class = os.path.join('.', 'murder_mystery_printer/murdermystery')
    #stop
    Printer('test', characters=[c1, c2], doc_class=NoEscape(r'murder_mystery_printer/murdermystery')).make_document()

