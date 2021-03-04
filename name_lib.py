def name_to_uppercase(name="john"):
    return name.upper()


# EVO DOLE JE TAJ CODE KOJI SE IZVRSAVA U OVOM GLOBALNOM OBIMU

# OVIM MOGU DA OSIGURAM DA SE ON NE IZVRSAVA AKO SE FILE KORISTI KAO MODULE

if __name__ == "__main__":

    # OVDE TRBA DA SE NAPRAVI INDENTATION JER OVO TREBA A BUDE U
    # USLOVNOJ IZJAVI
    print("Kevin Kevanson")
    print(name_to_uppercase())

    print(f"dunnder name: {__name__}")
