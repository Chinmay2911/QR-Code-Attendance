from MyQR import myqr
import os


f = open('subjects.txt', 'r')
lines = f.read().split("\n")
print("Printing line now")

for i in range(0, len(lines)):
    name = str(lines[i])
    print("Actual Name: ", name)

    version, level, qr_name = myqr.run(
        name,
        version=2,
        level='H',
        picture=None,
        colorized=False,
        contrast=1.0,
        brightness=1.0,
        save_name=str(name)+".png",
        save_dir=os.getcwd()
    )
