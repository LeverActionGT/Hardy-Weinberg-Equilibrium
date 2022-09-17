import simulation
import csv

SETTINGS = {
    'pop_size': 500,
    'num_generations': 200,
    'initial_p': 0.5,
    'initial_q': 0.5
}

FITNESS = {
    'AA_fitness': 0.5,
    'Aa_fitness': 1,
    'aa_fitness': 0.5 
}

def main():
    sim = simulation.Simulation(SETTINGS, FITNESS)
    output = sim.run_simulation() # {gen#:{}} where {} is the stats for that generation

    # write the output to a csv file
    file = open('output/output.csv', 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(['Generation', 'size', 'p', 'q', 'p^2', 'q^2', '2pq'])
    for gen in output:
        writer.writerow([gen, output[gen]['size'], output[gen]['p'], output[gen]['q'], output[gen]['p2'], output[gen]['q2'], output[gen]['2pq']])

if __name__ == '__main__':
    main()