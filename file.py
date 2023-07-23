import csv
import math
import numpy

SHARPNESS_MULTIPLIER = 100.0


def get_death_data():
    data = []
    with open('death_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def calculate():
    average_outcomes = []
    death_data = get_death_data()
    for sharpening_year in range(len(death_data)):
        results_for_sharpening_year = []
        current_sharpness = 1
        for age in range(len(death_data)):
            if age < sharpening_year:
                results_for_sharpening_year.extend(
                    [0] * int(death_data[age]["Number of deaths"].replace(",", "")))
                # current_sharpness = current_sharpness + \
                #    current_sharpness ** SHARPNESS_MULTIPLIER
                current_sharpness = current_sharpness + \
                    math.log(SHARPNESS_MULTIPLIER, current_sharpness+1)
            else:
                years_chopping = age - sharpening_year
                results_for_sharpening_year.extend(
                    [years_chopping * current_sharpness] * int(death_data[age]["Number of deaths"].replace(",", "")))

        array = numpy.array(results_for_sharpening_year)
        average_outcomes.append([sharpening_year, sum(
            results_for_sharpening_year)/len(results_for_sharpening_year), numpy.percentile(array, 90)])

    average_outcomes.sort(key=lambda a: a[2], reverse=True)
    for outcome in average_outcomes[:10]:
        print(outcome)


calculate()
