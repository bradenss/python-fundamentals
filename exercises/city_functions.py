def city_country(city, country):
    return city.title() + ", " + country.title()


def city_country1(city, country, population):
    output_string = city.title() + ", " + country.title()
    if population:
        output_string += ' - population ' + str(population)
    return output_string
