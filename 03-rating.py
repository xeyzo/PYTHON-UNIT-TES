def rating(usia):
    if(usia >= 21):
        return("DEWASA") # Step 2.1
    elif(usia >= 13):
        return("REMAJA")
    elif(usia >= 9):
        return("BIMBINGAN ORANG TUA")
    else:
        return("SEMUA USIA")



print("FILM RATING :", rating(4))