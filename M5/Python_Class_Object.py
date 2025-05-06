class Laptop:
    def __init__(self, brand, release_year, color, RAM):
        self.laptop_brand = brand
        self.laptop_release_year = release_year
        self.laptop_color = color
        self.laptop_RAM = RAM
#indent aligned with class
laptop_1 = Laptop("Dell", 2021, "Grey", 8)
laptop_2 = Laptop("Asus", 2022, "Black", 16)
laptop_3 = Laptop("Macbook", 2022, "Silver", 8)

# print(Laptop)
# print(laptop_1)
# print(laptop_1.laptop_brand)

class Laptop:
    def __init__(self, brand, release_year, color, RAM):
        self.laptop_brand = brand
        self.laptop_release_year = release_year
        self.laptop_color = color
        self.laptop_RAM = RAM
    def information(self):
        return f"{self.laptop_color} Laptop {self.laptop_brand} release in {self.laptop_release_year} with {self.laptop_RAM} RAM"
    def coding(self):
        print("Laptop used for coding ....")
        print("RAM usage : 2GB")
        self.laptop_RAM -= 2;
        print("Remaining RAM : " + str(self.laptop_RAM) + " GB")
    def office(self):
        print("Laptop used for office ....")
        print("RAM usage : 1GB")
        self.laptop_RAM -= 1;
        print("Remaining RAM : " + str(self.laptop_RAM) + " GB")
    def editingVideo(self):
        print("Laptop used for editing video ....")
        print("RAM usage : 3GB")
        self.laptop_RAM -= 1;
        print("Remaining RAM : " + str(self.laptop_RAM) + " GB")

class GamingLaptop(Laptop):
    def __init__(self, brand, release_year, color, RAM, VGA):
        super().__init__(brand, release_year, color, RAM)
        self.laptop_VGA = VGA

laptop_1 = Laptop("Dell", 2021, "Grey", 8)
laptop_2 = GamingLaptop("Asus", 2022, "Black", 16, "RTX 1650")
laptop_3 = Laptop("Macbook", 2022, "Silver", 8)

print(laptop_1.laptop_brand)

print(laptop_1.information())
laptop_1.coding()
laptop_1.office()
laptop_1.editingVideo()
print(laptop_2.information())
laptop_2.office()
laptop_2.gaming()
print(laptop_3.information())
laptop_3.coding()
laptop_3.office()
laptop_3.editingVideo()
laptop_2.office()
laptop_2.gaming()