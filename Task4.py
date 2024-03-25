class BMICalculator:
    def __init__(self, weight, height):
        self.weight = weight  # berat dalam pounds
        self.height = height  # tinggi dalam kaki

    def BMI_Value(self):
        # konversi tinggi dari kaki ke meter
        height_meters = self.height * 0.3048
        # kalkulasi BMI menggunakan rumus: Weight/Height^2
        bmi = self.weight / (height_meters ** 2)
        return round(bmi, 2)

    def __eq__(self, other):
        # membandingkan berat dan tinggi dari dua objek BMICalculator
        return self.weight == other.weight and self.height == other.height

        # membuat dua objek BMICalculator
        person1 = BMICalculator(120, 90.8)
        person2 = BMICalculator(180, 81.5)

        # Menghitung BMI untuk dua objek
        bmi1 = person1.BMI_Value()
        bmi2 = person2.BMI_Value()

        # Mencetak nilai BMI
        print(f"BMI of person1: {bmi1}")  # cetak output person1
        print(f"BMI of person2: {bmi2}")  # cetak output person2

        # Membandingkan dua objek BMICalculator
print(person1 == person2)  # cetak output booleannya
