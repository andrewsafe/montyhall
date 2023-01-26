import random

def run_trial(switch_doors, ndoors=3):

    chosen_door = random.randint(1, ndoors)
    if switch_doors:
        revealed_door = 3 if chosen_door == 2 else 2
        available_doors = [dnum for dnum in range(1,ndoors+1)
                                if dnum not in (chosen_door, revealed_door)]
        chosen_door = random.choice(available_doors)

    return chosen_door == 1

def run_trials(ntrials, switch_doors, ndoors=3):

    nwins = 0
    for i in range(ntrials):
        if run_trial(switch_doors, ndoors):
            nwins += 1
    return nwins

ndoors, ntrials = 3, 1000
nwins_without_switch = run_trials(ntrials, False, ndoors)
nwins_with_switch = run_trials(ntrials, True, ndoors)

print('Monty Hall Problem with {} doors'.format(ndoors))
print('Percentage of wins without switching: {:.4f}'
            .format(nwins_without_switch/ntrials))
print('Percentage of wins with switching: {:.4f}'
            .format(nwins_with_switch/ntrials))