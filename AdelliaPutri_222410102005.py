print("==== Program Sederhana Menghitung BMI ====")

weight = float (input("Masukkan berat badan anda (kg) = "))
height = float (input("Masukkan tinggi badan anda (m) = "))

BMI = weight / height**2

print(weight, "/", height**2, "=", BMI)
if BMI < 18.5:
    print("underweight")
elif 18.5 < BMI < 24.9:
    print("normal weight")
elif 25.0 < BMI < 29.9:
    print("overweight")
elif 30.0 < BMI < 34.9:
    print("obesity class I")
elif 35.0 < BMI < 39.9:
    print("obesity class II")
elif 40 < BMI:
    print("obesity class III")
