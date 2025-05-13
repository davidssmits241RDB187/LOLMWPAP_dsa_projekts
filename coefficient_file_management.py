from coefficients_class import Coefficients



def flatten_coeffs(coeffs: Coefficients):
    coefficients = []
    for w_l in coeffs.__dict__.values():
        for value in w_l:
            coefficients.append(str(value))
    return coefficients

def write_match_to_file(coefficients: Coefficients):
    filename =  "coefficients.txt"
    flattened = flatten_coeffs(coefficients)
    line = ";".join(flattened)
    with open(filename, "w") as f:
        f.write(line)

def read_matches_from_file():
    filename =  "coefficients.txt"
    try:
        with open(filename, "r") as f:
            line = f.readline()
            if not line:
                return Coefficients()
            #
            values = list(map(float, line.split(";")))
            
            #list of the keys of the coefficient dataclass converted to a dictionary
            attributes = list(Coefficients().__dict__.keys())
            
            coeff_data = {}
            for i, attribute in enumerate(attributes):
                # coeff data dict key gets asigned values [x, y] from starting index to ending index (not included)
                coeff_data[attribute] = values[i*2:i*2+2]

            return Coefficients(**coeff_data)
    except FileNotFoundError:
        return Coefficients()
