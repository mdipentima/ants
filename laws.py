"""
Laws: (first run)

    1) grid size 100x100 (world)
    2) living creatures : ants (male and female) and anteater
    3) NON living: earth and grass
    4) ants lifestyle:
        - can move N,S,W,E,NW,NE,SW,SE, no movement
        - can only move one "square at a time
        - male vs male wins who ever has more age or a random toss (not between siblings or father)
        - female vs female nothing ----- future: add queen 
        - male vs female : reproduce (takes 3 instances for breeding one new ant... sex is random) (no sibling and edipo/electra complex allowed)
        - lifespawn is 50 instances (turns) --------------------
        - can only live 20 if doesnt eat grass -----------------
        - can only eat max 2 grass per lyfespawn (check this) --
    5) ant eater:
        -only one (for now): per game
        - it moves the same as ants
        - if there is ant where moving he eats it
    6) grass
        -grows random
    7) earth:
        -just earth
    


start: 
    -only 8 ants start (4 of each sex)
    -only 1 anteater
    -start 30 pieces of grass
    -instance (turn) is every x seconds 


"""