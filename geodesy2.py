import math


def to_rads(mins: int) -> float:
    return mins * math.pi / (180 * 60)


def get_params(ellipsoid_name: str) -> tuple:
    ellipsoids = {
        "Красовского": (6378245, 298.3),
        "WGS-84": (6378137, 298.25),
        "ПЗ-90": (6378136, 298.2577839),
        "GRS-80": (6378137, 298.257222101)
    }
    return ellipsoids[ellipsoid_name]


def calculate(a, one_alpha: float, n: int):
    alpha = 1 / one_alpha
    b = a * (1 - alpha)
    e_1 = alpha * (2 - alpha)
    e_2 = e_1 / (1 - e_1)
    c = math.pow(a, 2) / b

    B1 = to_rads(55 * 60 + 10 * n)
    L = to_rads(37 * 60 + 10 * n)
    B2 = B1 + to_rads(2 * 60)





def main():
    ellipsoids = ("Красовского", "WGS-84", "ПЗ-90", "GRS-80")
    n = int(input('Введите свой номер по списку: '))
    for el in ellipsoids:
        ellipsoid_params = get_params(el)
        print('\n', el, end='\n\n')
        calculate(*ellipsoid_params, n)


if __name__ == "__main__":
    main()
