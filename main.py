import math


def tinh_dien_tich_hinh_tron(ban_kinh: float) -> float:
    if ban_kinh < 0:
        raise ValueError("Bán kính phải lớn hơn hoặc bằng 0")
    return math.pi * ban_kinh ** 2


if __name__ == "__main__":
    r = float(input("Nhập bán kính hình tròn: "))
    s = tinh_dien_tich_hinh_tron(r)
    print(f"Diện tích hình tròn là: {s:.2f}")
