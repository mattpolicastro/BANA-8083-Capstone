import math

def evaluate(units, individual):
    units = units.copy()
    units.district = individual

    # Aggregate into districts for comparison
    zones = units.dissolve(by='district', aggfunc='sum')

    compactness_score = evaluate_compactness(zones)
    crime_score = evaluate_count(zones.crimes)
    population_score = evaluate_count(zones.population)

    del units, zones

    return(compactness_score, crime_score, population_score)


def evaluate_count(counts):
    total = sum(counts)
    max_delta = max(counts) - min(counts)

    # Find p and set to 1 if extremely large
    p_ratio = max_delta / total
    if p_ratio > 1:
        p_ratio = 1

    return p_ratio


def evaluate_compactness(zones):
    zones.compactness = (4 * math.pi * zones.area) / zones.length
    return min(zones.compactness)

# Define helper function for plotting chromosomes
def plot_chromosome(units, individual, dissolve):

    units = units.copy()
    units['district'] = individual

    if dissolve == True:
        units.dissolve(by='district').plot()
    else:
        units.plot(column='district', colormap='Accent')
