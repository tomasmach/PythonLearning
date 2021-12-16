def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

pondelni_teploty = [9.1, 8.8, 7.5]
mylist = {"Karhal": 9.1, "Autak": 8.8, "Fael": 3.2}

print(mean(pondelni_teploty))