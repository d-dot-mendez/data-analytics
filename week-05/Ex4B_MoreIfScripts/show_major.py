student_name   = input("What is your name?")
student_major  = input("What is the major code?")

if student_major == BIOL:
    print("BIOL-Biology-Science Bldg, Room 310")
elif student_major == CSCI:
     print("CSCI-Computer Science-Sheppard Hall, Room 314")
elif student_major == ENG:
     print("ENG-English-Kerr Hall, Room 201")
elif student_major == HIST:
     print("HIST-History-Kerr Hall, Room 114")
elif student_major == MKT:
     print("MKT-Marketing-Westley Hall, Room 310")
elif student_major == ASTRO:
     print("ASTRO-Astronomy-Luminary Hall, Room 101")
else:
    print("Invalid code!")