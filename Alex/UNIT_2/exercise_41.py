

#basic notes and the frequency values
octaves : dict[str,float] = {
    "C4" : 261.63,
    "D4" : 293.66,
    "E4" : 329.63,
    "F4" : 349.23,
    "G4" : 392.00,
    "A4" : 440.00,
    "B4" : 493.88
}

#available notes
available_notes : list[str] = ["C","D","E","F","G","A","B"]

try:
    #user input
    input_note  : str = input("Enter the value of the note : ")

    #validation of note size
    if len(input_note) > 2:
        raise ValueError("The length of the note can not be more than 2")

    #validation of the note
    note : str = input_note[0:1]
    if note.upper() not in available_notes:
        raise ValueError("Not a valid note. Should be : C,D,E,F,G,A or B")


    #validation of the range(0-8)
    range : int = int(input_note[1:2])
    if range < 0 or range > 8:
        raise ValueError("Not a valid range. Should be : 0,1,2,3,4,5,6,7 or 8")


    #output of octaves
    if input_note.upper() in octaves.keys():
        print(f"The value of the {input_note.upper()} note is : {octaves.get(input_note.upper())}Hz")

    #output all the rest of the notes

    
except ValueError as vaerr:
    print(vaerr)