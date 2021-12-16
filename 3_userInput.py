def pocasi(teplota):
    if teplota > 7:
        return "Warm"
    else:
        return "Cold"

#user_input = float(input("Zadej teplotu: "))

#print(type(user_input), user_input, pocasi(user_input))

jmeno = input("Zadej sve jmeno: ")
prijmeni = input("Zadej sve prijmeni: ")
#zprava = "Ahoj %s" %zadani
zprava = f"Hello {jmeno} {prijmeni}"
print (zprava)