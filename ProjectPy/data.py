from mobile import Mobile


def load_mobiles():
    mobiles = []

    mobiles.append(
        Mobile(
            1,
            "Samsung",
            "S25 Ultra",
            "12 GB",
            "256 GB",
            100000,
            10
        )
    )

    mobiles.append(
        Mobile(
            2,
            "Apple",
            "iPhone 16",
            "8 GB",
            "256 GB",
            120000,
            8
        )
    )

    mobiles.append(
        Mobile(
            3,
            "Nothing",
            "Phone 4a",
            "8 GB",
            "256 GB",
            35000,
            15
        )
    )

    mobiles.append(
        Mobile(
            4,
            "Oppo",
            "Reno 15",
            "12 GB",
            "512 GB",
            45000,
            5
        )
    )

    mobiles.append(
        Mobile(
            5,
            "Vivo",
            "V50",
            "8 GB",
            "128 GB",
            32000,
            12
        )
    )

    return mobiles