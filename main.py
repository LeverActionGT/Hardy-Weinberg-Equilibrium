import simulation
import csv

SETTINGS = {
    'pop_size': 100000,
    'num_generations': 25,
    'initial_p': 0.1,
    'initial_q': 0.9,
    'print_stats': False
}

FITNESS = {
    'AA_fitness': .5,
    'Aa_fitness': 1,
    'aa_fitness': 0 
}

def main():
    # make sure p+q=1
    SETTINGS['initial_q'] = 1 - SETTINGS['initial_p']

    sim = simulation.Simulation(SETTINGS, FITNESS)
    output = sim.run_simulation() # {gen#:{}} where {} is the stats for that generation

    # write the output to a csv file
    file = open('output/output.csv', 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(['gen', 'p', 'q', 'p^2', 'q^2', '2pq'])
    for gen in output:
        writer.writerow([gen, output[gen]['p'], output[gen]['q'], output[gen]['p2'], output[gen]['q2'], output[gen]['2pq']])

if __name__ == '__main__':
    main() 