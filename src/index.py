from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print(f"Mehuvarasto: {mehua}, Olutvarasto: {olutta}")

    print("Mehu setterit:", "Lisätään 50.7 ja otetaan 3.14")
    mehua.lisaa_varastoon(50.7)
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

    print("olutta.lisaa_varastoon(1000.0)")
    print(f"Olutvarasto: {olutta}")

    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

if __name__ == "__main__":
    main()
