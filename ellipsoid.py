import math


def get_params(ellipsoid_name: str) -> tuple:
    ellipsoids = {
        "Красовского": (6378245, 298.3),
        "WGS-84": (6378137, 298.25),
        "ПЗ-90": (6378136, 298.2577839),
        "ГСК 2011": (6378136.5, 298.2564151),
        "GRS-80": (6378137, 298.257222101)
    }
    return ellipsoids[ellipsoid_name]


def to_rads(mins: int) -> float:
    return mins * math.pi / (180 * 60)


# расчет значений параметров эллипсоида
def calculate(a, one_alpha: float, n: int) -> None:
    alpha = 1 / one_alpha
    b = a * (1 - alpha)
    e_1 = alpha * (2 - alpha)
    e_2 = e_1 / (1 - e_1)
    c = math.pow(a, 2) / b
    print("Значение малой полуоси: ", b, sep='\t')
    print("Квадрат значения первого эксцентриситета: ", e_1, sep='\t')
    print("Квадрат значения второго эксцентриситета: ", e_2, sep='\t')
    print("Значение полярого радиуса кривизны", c, sep='\t')
    control_params(a, alpha, b, e_1, e_2, c)

    # сфероидические функции и их контроль
    B = to_rads(55 * 60 + 10 * n)
    L = to_rads(37 * 60 + 10 * n)
    W = math.sqrt(1 - e_1 * math.pow(math.sin(B), 2))
    V = math.sqrt(1 + e_2 * math.pow(math.cos(B), 2))
    print(f" B: {B}\n L: {L}\n W: {W}, V: {V}")
    control_spheroid = a * W - b * V == 0
    print(a * W, b * V)
    print('Контроль значения 1-й и 2-ой сфероидических функций ВЫПОЛНЕН') if control_spheroid else print(
        "Контроль значения 1-й и 2-ой сфероидических функций НЕ ВЫПОЛНЕН")

    # расчет главных радиусаов кривизны главных нормальных сечений и ср. радиуса кривизны
    M = c / math.pow(V, 3)
    N = c / V
    R_avg = math.sqrt(M * N)
    print(f" M: {M}\n N: {N}\n R средний: {R_avg}")
    control_curvature = N / M - math.pow(V, 2) == 0
    print(N / M, math.pow(V, 2))
    print('Контроль значений меридиана и вертикала ВЫПОЛНЕН') if control_curvature else print(
        "Контроль значений меридиана и вертикала НЕ ВЫПОЛНЕН")

    # расчет значений декартовых координат
    U = math.atan(math.sqrt(1 - e_1) * math.tan(B))  # приведенная широта
    x = a * math.cos(U) * math.cos(L)
    y = a * math.cos(U) * math.sin(L)
    z = b * math.sin(U)
    control_coords_x = x - N * math.cos(B) * math.cos(L) == 0
    control_coords_y = y - N * math.cos(B) * math.sin(L) == 0
    control_coords_z = z - N * (1 - e_1) * math.sin(B) == 0
    print(x, N * math.cos(B) * math.cos(L))
    print('Контроль по x ВЫПОЛНЕН') if control_coords_x else print(
        "Контроль по x НЕ ВЫПОЛНЕН")
    print(y, N * math.cos(B) * math.sin(L))
    print('Контроль по y ВЫПОЛНЕН') if control_coords_y else print(
        "Контроль по y НЕ ВЫПОЛНЕН")
    print(z, N * (1 - e_1) * math.sin(B))
    print('Контроль по z ВЫПОЛНЕН') if control_coords_z else print(
        "Контроль по z НЕ ВЫПОЛНЕН")


def control_params(a, alpha, b, e_1, e_2, c: float):
    control1 = b - a * a / c == 0
    print(b, a * a / c)
    print('Контроль значения малой полуоси ВЫПОЛНЕН') if control1 else print(
        "Контроль значения малой полуоси НЕ ВЫПОЛНЕН")
    control2 = e_1 - (math.pow(a, 2) - math.pow(b, 2)) / math.pow(a, 2)
    print(e_1, (math.pow(a, 2) - math.pow(b, 2)) / math.pow(a, 2))
    print('Контроль значения 1-го эксцентриситета ВЫПОЛНЕН') if control2 else print(
        "Контроль 1-го эксцентриситета НЕ ВЫПОЛНЕН")
    control3 = e_2 - (math.pow(a, 2) - math.pow(b, 2)) / math.pow(b, 2)
    print(e_2, (math.pow(a, 2) - math.pow(b, 2)) / math.pow(b, 2))
    print('Контроль значения 2-го эксцентриситета ВЫПОЛНЕН') if control3 else print(
        "Контроль значения 2-го эксцентриситета НЕ ВЫПОЛНЕН")
    control4 = alpha - (a - b) / a
    print(alpha, (a - b) / a)
    print('Контроль полярного радиуса кривизны ВЫПОЛНЕН') if control4 else print(
        "Контроль полярного радиуса кривизны НЕ ВЫПОЛНЕН")


def main():
    ellipsoids = ("Красовского", "WGS-84", "ПЗ-90", "ГСК 2011", "GRS-80")
    n = int(input('Введите свой номер по списку: '))
    for el in ellipsoids:
        ellipsoid_params = get_params(el)
        print('\n', el, end='\n\n')
        calculate(*ellipsoid_params, n)


if __name__ == "__main__":
    main()
