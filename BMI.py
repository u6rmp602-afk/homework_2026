"""BMI 計算程式：使用公斤與公分輸入，提供可攜式命令列介面。"""
import math

def calculate_bmi(weight_kg, height_cm):
    """計算 BMI。體重單位為 kg，身高單位為 cm。"""
    try:
        weight, height = float(weight_kg), float(height_cm)
    except (TypeError, ValueError):
        raise ValueError("體重與身高必須是有效數字。") from None
    if not math.isfinite(weight) or not math.isfinite(height):
        raise ValueError("體重與身高必須是有限數值。")
    if weight <= 0:
        raise ValueError("體重必須大於 0。")
    if height <= 0:
        raise ValueError("身高必須大於 0。")
    try:
        result = weight / ((height / 100) ** 2)
    except (OverflowError, ZeroDivisionError):
        raise ValueError("輸入數值超出可計算範圍。") from None
    if not math.isfinite(result):
        raise ValueError("計算結果超出可處理範圍。")
    return result

def ask_positive_number(prompt):
    """持續詢問，直到使用者輸入有限的正數。"""
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print("輸入格式錯誤，請輸入數字。")
            continue
        if not math.isfinite(value) or value <= 0:
            print("請輸入大於 0 的有限數字。")
            continue
        return value

def main():
    print("=== BMI 計算程式 ===")
    weight = ask_positive_number("請輸入體重（kg）：")
    height = ask_positive_number("請輸入身高（cm）：")
    bmi = calculate_bmi(weight, height)
    print(f"您的 BMI 為：{bmi:.2f}")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyboardInterrupt, EOFError):
        print("\n已取消輸入。")
        raise SystemExit(1)
