class Pixel:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class Image:
    pixels = []

    def read(self, file):
        with open(file) as kep:
            rowcnt = 0
            for line in kep.readlines():
                cnt = 0
                self.pixels.append([])
                splitline = line.split(' ')
                for rgb in splitline:
                    if cnt % 3 == 0:
                        red = rgb
                        cnt += 1
                    elif cnt % 3 == 1:
                        green = rgb
                        cnt += 1
                    elif cnt % 3 == 2:
                        blue = rgb
                        self.pixels[rowcnt].append(Pixel(red, green, blue))
                        cnt += 1
                rowcnt += 1

    def search(self, row, col):
        print(f'A képpont színe RGB({self.pixels[row][col].r},{self.pixels[row][col].g},{self.pixels[row][col].b})')

    def brightcnt(self):
        brightcnt = 0
        for row in self.pixels:
            for pixel in row:
                if int(pixel.r) + int(pixel.g) + int(pixel.b) > 600:
                    brightcnt += 1
        return brightcnt

    def darkcnt(self):
        dark = 1000
        for row in self.pixels:
            for pixel in row:
                if int(pixel.r) + int(pixel.g) + int(pixel.b) < dark:
                    dark = int(pixel.r) + int(pixel.g) + int(pixel.b)
        return dark
    
    def searchrgb(self, num):
        for row in self.pixels:
            for pixel in row:
                if int(pixel.r) + int(pixel.g) + int(pixel.b) == num:
                    print(f'RGB({pixel.r},{pixel.g},{pixel.b})')

    # 5. feladat
    def hatar(self, row, limit):
        cnt = 0
        for pixel in self.pixels[row]:
            if cnt == 0:
                cnt += 1
            else:
                if abs(int(pixel.b) - int(self.pixels[row][cnt-1].b)) > int(limit):
                    return True
                cnt += 1
        return False



kep = Image()
kep.read("kep.txt")

# 2. feladat
print("2. feladat:")
pixelrow = int(input("Kérem egy képpont adatait!\nSor:"))
pixelcol = int(input("Oszlop:"))
kep.search(pixelrow, pixelcol)

# 3. feladat
print("3. feladat:")
print(f"A világos képpontok száma: {kep.brightcnt()}")


# 4. feladat
print("4. feladat")
print(f"A legsötétebb pont RGB összege: {kep.darkcnt()}")
print(f"A legsötétebb pixelek színe: ")
kep.searchrgb(kep.darkcnt())

# 6. feladat
min = 1000
max = 0
for row in kep.pixels:
    idx = kep.pixels.index(row)
    if kep.hatar(idx, 10):
        min = idx if idx < min else min
        max = idx if idx > max else max

print("5. feladat")
print(f'A felhő legfelső sora: {min+1}')
print(f'A felhő legalsó sora: {max+1}')