'''
DESCRIPTION:
Simple program that prints out a story created through collaboration.
Students add a line within the story() method.
Used to introduce Github to students at CSU Fresno in CSCI150 -- Software Engineering
Made by Hannah Scott (the lab TA) on July 21, 2016


INSTRUCTIONS:
0. Run in Python 3 (NOT 2!)
1. Add at least one line to the story by appending a string to the list
in the story() method below. You can run (f5 in IDLE, or just run story_main.py) to see what's there so far.
2. Save the file in the repository.
3. Commit the change.
4. Get points. 

RULES:
1. Don't do anything illegal / disturbingly immoral (e.g. detailed murder plans, giving away gma's secret cookie recipe)

2. Don't be super mean to anyone in the class.
(Celebrities are fair game. Except Trump. I'm sick of hearing about Trump.)
(Probably you shouldn't say anything about Clinton either. Or Obama. I don't want to P.O. the Secret Service.)
(And I guess you shouldn't say anything about Kanye West, Kim Kardashian or Taylor Swift--God knows what could happen.)
(Actually, probably you should avoid celebrities. Unless they are super cool.)

3. Don't be super weird, like to the point that it ruins it and makes things awk for everyone. (just ... OK?)

4. If you try to run this and it doesn't work, you can get credit for fixing it
instead of adding a line to the story.
(Just put a note about what you fixed in the code when you commit.)

5. You can add to any of the lists in the rand_ methods e.g. rand_adj()
*****as long as you follow the rules above. 
'''

import random
rc = random.choice

def story():
    '''
    (Added by Hannah S.)
    You can use add_line("your contribution") to append a string as demonstrated,
    or lines.append("your contribution")
    You can add import lines, methods, etc. to the program if you are feeling creative.
    And you can call any of the rand_ methods below if you want to use the mad-lib features provided.
    Or, you can just add a boring old line.
    See rules outlined at the top of this file if you are uncertain.

    Newlines will be inserted for you. 
    '''
    lines = list()
    add_line = lines.append

    #Get some random strings to use in examples
    protagonist = rand_classmem()
    antagonist = rand_classmem()
    v_0 = rand_verb()
    adv_0 = rand_adv()
    num_0 = rand_num()
    q_0 = rand_quote()
    adj_0 = rand_adj()
    n_0 = rand_noun()

    #Kick off the story with a few lines
    add_line("It was a {0} afternoon in Fresno, California. {1} was just sitting there with {2}, minding their own business in CSCI150 ".format(adj_0, protagonist, n_0))
    add_line("when, suddenly, something unexpected happened:")
    #examples to use in class:
    add_line("{0} {1} {2} {3} {4} times in 2 minutes".format(antagonist, adv_0, v_0, n_0, num_0))
    add_line("{0} {1} said, looking at {2}.".format(q_0, protagonist, antagonist))
    
#############################################################################################
#           HERE'S WHERE YOU ADD TO THE STORY                                               #
#           Use the template provided below.                                                #
#############################################################################################
    
    #copy-pasta provided below for your convenience (seriously, I can't make this any easier):  
    #add_line("") #no wild cards                                                                
    #add_line("{0}".format(var)) #with wild card

    
    return("\n".join(lines))


def rand_adj():
    '''
    Returns an adjective String which can be inserted into a line.
    (Added by Hannah S.)
    '''
    adjs = ["vicious",
            "larger-than-life",
            "smelly",
            "tall",
            "boring",
            "cute",
            "pleasant"
            ]
            
    return rc(adjs)

def rand_adv():
    '''
    Returns an adverb String which can be used in a line.
    (Added by Hannah S.)
    '''
    advs =["atrociously",
           "endearingly",
           "very, very, VERY reluctantly",
           "heart-wrenchingly",
           "robustly",
           "tremulously",
           "refreshingly",
           "ignorantly",
           "severely",
           "aggressively",
           "gingerly",
           "sneakily",
           "clumsily",
           "randomly",
           "deftly",
           "pointlessly",
           "passionately",
           "boldly",
           "deliberately"
           
        ]
    return rc(advs)

def rand_noun():
    '''
    Returns a noun String from a list, which can be used in a line.
    (Added by Hannah S.)
    '''
    nouns = ["the you-know-what",
             "the widget",
             "the piglet the size of a dongle",
             "the genetically-modified cucumber",
             "Pikachu",
             "Charizard",
             "the herd of unicorns",
             "the batmobile",
             "Eric Cartman",
             "the man in a 3-piece suit with a piece of toilet paper stuck to his left shoe",
             "the paper-mache representation of the meaning of life",
             "Illidan's left-hand warglaive"
             ]
    return rc(nouns)

def rand_verb():
    '''
    Returns a past-tense transitive verb phrase String from a list, to be used in a line.
    (Added by Hannah S.)
    '''
    verbs = ["vitiated the natural development of",
             "dissillusioned",
             "encouraged",
             "avoided",
             "snuggled",
             "tripped and fell on",
             "lectured about",
             "pick-pocketed",
             "sang a moving, tragic ballad about",
             "set fire to"
             ]

    return rc(verbs)

def rand_classmem():
    '''
    Returns a classmate's name as a String.
    (Added by Hannah S.)
    '''
    names = ["Hannah",
             "Dr. Liu",
             "Dr. Wilson",
             "Dr. Ruby",
             "Mr. Banerjee",
             "Dr. Park",
             "Dr. Auernheimer",
             "Dr. Li"
             ]
    return rc(names)

def rand_num():
    '''
    Returns an amount as a String.
    (Added by Hannah S.)
    '''
    nums = ["1,000,000",
            "a basquillion",
            "a larger number than anyone has ever heard of",
            "an amount equivalent to the number of skin cells on an elephant's tum-tum",
            "a single",
            "precisely 2.718281828459045235360287471352662497757 (AKA 'e')",
            "approximately 24",
            "a benjamin",
            "way more than necessary",
            "OVER 9,000 (!)"
            ]
    
    return rc(nums)

def rand_quote():
    '''
    Returns a quote as a String, which can be used in a line.
    (Added by Hannah S.)
    '''

    quotes = ["'OH YEAH!'",
              "'Um, excuse me, but ... who is that?'",
              "'I guess I should have eaten more fiber last year.'",
              "'How can this be?? The fortune-teller should have warned me!'",
              "'Well, I suppose it is better to be a good liar than a bad con artist.'",
              "'I really wish I had studied more in CSCI 41.'",
              "'I think I watched a South Park episode where this happened...'",
              "'Oh noes!'",
              "'If only I hadn't let that dratted hobbit take the ring of power!'",
              "'I know who is to blame for this!'",
              "'So, it has come to this.'",
              "'My robot lemur assassins should be able to handle this!'",
              "'Does anyone else think that guy looks like the Estonian Prime Minister?'",
              "'Can anyone really prove that Harry isn't here right now wearing his invisibility cloak?'"
              ]


    return rc(quotes)

print(story())
