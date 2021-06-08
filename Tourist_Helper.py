from tkinter import *
from tkinter.ttk import *
import numpy as np
import pandas as pd
from PIL import ImageTk, Image
from operator import itemgetter
from tkinter import messagebox
import ahpy

window = Tk()
window.title("Travel Helper 1.0")
window.configure(background="white")


def Start_screen():
    background = Image.open("image1.jpg")
    bg = ImageTk.PhotoImage(background)

    canvas_start = Canvas(window)
    canvas_start.grid()

    background_label = Label(canvas_start, image=bg)
    background_label.image = bg
    background_label.grid()

    Label(canvas_start, text="TOURIST HELPER 1.0").grid(row=1, column=0)
    Label(canvas_start, text="Aby rozpocząć program przejdź do wypełnienia ankiety").grid(row=5, column=0)
    bt = Button(canvas_start, text="Rozpocznij ankietę", command=lambda: Transition(canvas_start))
    bt.grid(row=6, column=0)


def Transition(canvas_start):
    canvas_start.destroy()
    Ankieta()
    pass


def Ankieta():
    canvas_ankieta = Canvas(window)
    canvas_ankieta.grid()
    Label(canvas_ankieta, text="W skali od 0-5, gdzie 0 oznacza, że cię wogole nie interesuje.").grid(row=0, column=0)

    Label(canvas_ankieta, text="1. Jak ważna jest dla ciebie cena podróży?").grid(row=1, column=0)

    var0 = IntVar()

    kwadraty = Frame(canvas_ankieta)

    k1 = Checkbutton(kwadraty, text="1", variable=var0, onvalue=1)
    k2 = Checkbutton(kwadraty, text="2", variable=var0, onvalue=2)
    k3 = Checkbutton(kwadraty, text="3", variable=var0, onvalue=3)
    k4 = Checkbutton(kwadraty, text="4", variable=var0, onvalue=4)
    k5 = Checkbutton(kwadraty, text="5", variable=var0, onvalue=5)

    kwadraty.grid(row=2, column=0)
    k1.pack(side="left")
    k2.pack(side="left")
    k3.pack(side="left")
    k4.pack(side="left")
    k5.pack(side="left")

    Label(canvas_ankieta, text="2. Jak ważny jest dla ciebie czas podróży?").grid(row=4, column=0)

    var1 = IntVar()

    kwadraty = Frame(canvas_ankieta)

    k11 = Checkbutton(kwadraty, text="1", variable=var1, onvalue=1)
    k21 = Checkbutton(kwadraty, text="2", variable=var1, onvalue=2)
    k31 = Checkbutton(kwadraty, text="3", variable=var1, onvalue=3)
    k41 = Checkbutton(kwadraty, text="4", variable=var1, onvalue=4)
    k51 = Checkbutton(kwadraty, text="5", variable=var1, onvalue=5)

    kwadraty.grid(row=5, column=0)

    k11.pack(side="left")
    k21.pack(side="left")
    k31.pack(side="left")
    k41.pack(side="left")
    k51.pack(side="left")

    Label(canvas_ankieta, text="3. Jak ważna jest dla ciebie jakość zakwaterowania?").grid(row=6, column=0)

    var2 = IntVar()

    kwadraty = Frame(canvas_ankieta)

    k12 = Checkbutton(kwadraty, text="1", variable=var2, onvalue=1)
    k22 = Checkbutton(kwadraty, text="2", variable=var2, onvalue=2)
    k32 = Checkbutton(kwadraty, text="3", variable=var2, onvalue=3)
    k42 = Checkbutton(kwadraty, text="4", variable=var2, onvalue=4)
    k52 = Checkbutton(kwadraty, text="5", variable=var2, onvalue=5)

    kwadraty.grid(row=7, column=0)

    k12.pack(side="left")
    k22.pack(side="left")
    k32.pack(side="left")
    k42.pack(side="left")
    k52.pack(side="left")

    Label(canvas_ankieta, text="4. Jak ważne jest dla ciebie bezpieczeństwo?").grid(row=8, column=0)

    var3 = IntVar()

    kwadraty = Frame(canvas_ankieta)

    k13 = Checkbutton(kwadraty, text="1", variable=var3, onvalue=1)
    k23 = Checkbutton(kwadraty, text="2", variable=var3, onvalue=2)
    k33 = Checkbutton(kwadraty, text="3", variable=var3, onvalue=3)
    k43 = Checkbutton(kwadraty, text="4", variable=var3, onvalue=4)
    k53 = Checkbutton(kwadraty, text="5", variable=var3, onvalue=5)

    kwadraty.grid(row=9, column=0)
    k13.pack(side="left")
    k23.pack(side="left")
    k33.pack(side="left")
    k43.pack(side="left")
    k53.pack(side="left")

    Label(canvas_ankieta, text="5. Jak ważna jest dla ciebie czystość?").grid(row=12, column=0)

    var4 = IntVar()

    kwadraty = Frame(canvas_ankieta)

    k15 = Checkbutton(kwadraty, text="1", variable=var4, onvalue=1)
    k25 = Checkbutton(kwadraty, text="2", variable=var4, onvalue=2)
    k35 = Checkbutton(kwadraty, text="3", variable=var4, onvalue=3)
    k45 = Checkbutton(kwadraty, text="4", variable=var4, onvalue=4)
    k55 = Checkbutton(kwadraty, text="5", variable=var4, onvalue=5)

    kwadraty.grid(row=13, column=0)

    k15.pack(side="left")
    k25.pack(side="left")
    k35.pack(side="left")
    k45.pack(side="left")
    k55.pack(side="left")

    Label(canvas_ankieta, text="6. Jak ważna jest dla ciebie jakość jedzenia?").grid(row=14, column=0)

    var5 = IntVar()

    kwadraty = Frame(canvas_ankieta)

    k17 = Checkbutton(kwadraty, text="1", variable=var5, onvalue=1)
    k27 = Checkbutton(kwadraty, text="2", variable=var5, onvalue=2)
    k37 = Checkbutton(kwadraty, text="3", variable=var5, onvalue=3)
    k47 = Checkbutton(kwadraty, text="4", variable=var5, onvalue=4)
    k57 = Checkbutton(kwadraty, text="5", variable=var5, onvalue=5)

    kwadraty.grid(row=15, column=0)

    k17.pack(side="left")
    k27.pack(side="left")
    k37.pack(side="left")
    k47.pack(side="left")
    k57.pack(side="left")

    Label(canvas_ankieta, text="7. Jaki rodzaj zakwaterowania preferujesz?").grid(row=16, column=0)

    var6 = IntVar()

    kwadraty = Frame(canvas_ankieta)

    k06 = Checkbutton(kwadraty, text="apartament", variable=var6, onvalue=0)
    k16 = Checkbutton(kwadraty, text="hotel", variable=var6, onvalue=1)
    k26 = Checkbutton(kwadraty, text="obojętne", variable=var6, onvalue=2)

    kwadraty.grid(row=17, column=0)

    k06.pack(side="left")
    k16.pack(side="left")
    k26.pack(side="left")

    Label(canvas_ankieta, text="8. Czy jesteś skłonna/skłonny się szczepić?").grid(row=18, column=0)

    var7 = IntVar()

    kwadraty = Frame(canvas_ankieta)

    k011 = Checkbutton(kwadraty, text="TAK", variable=var7, onvalue=0)
    k111 = Checkbutton(kwadraty, text="NIE", variable=var7, onvalue=1)

    kwadraty.grid(row=19, column=0)

    k011.pack(side="left")
    k111.pack(side="left")

    Label(canvas_ankieta, text="9. Czy przesiadki wykluczają kierunek?").grid(row=20, column=0)

    var8 = IntVar()

    kwadraty = Frame(canvas_ankieta)

    k08 = Checkbutton(kwadraty, text="TAK", variable=var8, onvalue=0)
    k18 = Checkbutton(kwadraty, text="NIE", variable=var8, onvalue=1)

    kwadraty.grid(row=21, column=0)

    k08.pack(side="left")
    k18.pack(side="left")

    Label(canvas_ankieta, text="10. Czy chcesz All Inclusive?").grid(row=22, column=0)

    var9 = IntVar()

    kwadraty = Frame(canvas_ankieta)

    k09 = Checkbutton(kwadraty, text="TAK", variable=var9, onvalue=0)
    k19 = Checkbutton(kwadraty, text="NIE", variable=var9, onvalue=1)

    kwadraty.grid(row=23, column=0)

    k09.pack(side="left")
    k19.pack(side="left")

    Label(canvas_ankieta, text="11. Czy wiza wyklucza kierunek?").grid(row=24, column=0)

    var10 = IntVar()

    kwadraty = Frame(canvas_ankieta)

    k010 = Checkbutton(kwadraty, text="TAK", variable=var10, onvalue=0)
    k110 = Checkbutton(kwadraty, text="NIE", variable=var10, onvalue=1)
    kwadraty.grid(row=25, column=0)

    k010.pack(side="left")
    k110.pack(side="left")

    Label(canvas_ankieta, text="12. Jedziesz wypocząć, czy pozwiedzać i się zabawić?").grid(row=26, column=0)

    var11 = IntVar()

    kwadraty = Frame(canvas_ankieta)

    k012 = Checkbutton(kwadraty, text="Wypocząć", variable=var11, onvalue=0)
    k112 = Checkbutton(kwadraty, text="Pozwiedzać i zabawić", variable=var11, onvalue=1)
    k212 = Checkbutton(kwadraty, text="Lecę na całość", variable=var11, onvalue=2)
    kwadraty.grid(row=27, column=0)

    k012.pack(side="left")
    k112.pack(side="left")
    k212.pack(side="left")

    kwadraty = Frame(canvas_ankieta)

    answers = [var0, var1, var2, var3, var4, var5, var6, var6, var8, var9, var10, var11]
    submit = Button(kwadraty, text="Zatwierdź Odpowiedzi i wyszukaj miejsca",
                    command=lambda: Save_answers(answers, canvas_ankieta))

    kwadraty.grid(row=28, column=0)
    submit.pack()

    pass


def Save_answers(odpo, canvas):
    answers_values = []
    for i in range(len(odpo)):
        answers_values.append(odpo[i].get())
    canvas.destroy()
    canvas_page2 = Canvas(window)
    canvas_page2.grid()

    """Obliczanie wag dla opdpowiedzi 1-6"""

    answers_values_sum = sum(answers_values[0:6])

    p = []

    for i in range(0, 6):
        p.append(answers_values[i] / answers_values_sum)

    answers = []

    for i in range(6, 12):
        answers.append(answers_values[i])
    print(answers)

    print(p)
    print(sum(p))
    print(answers_values)

    ###### FUNKCJA CELU
    plik = pd.read_csv("baza_podroz.csv", delimiter=";")
    kolumny = []
    for i in plik.columns:
        kolumny.append(i)

    wiersze = len(plik.index)

    # CHOP CHOP

    indexes_to_drop = []

    for i in range(wiersze):

        czy_juz_jest = i in indexes_to_drop

        # Odpowiedz 1 Przesiadki
        if answers[2] == 0:

            if plik['przesiadki'][i] == 1:
                print(i)
                indexes_to_drop.append(i)
                czy_juz_jest = i in indexes_to_drop

        # Apartament
        if answers[0] == 0:

            if plik['rodzaj zakwaterowania'][i] == 'apartament':

                if czy_juz_jest:
                    pass
                else:
                    indexes_to_drop.append(i)
                    czy_juz_jest = i in indexes_to_drop

        # Hotel
        if answers[0] == 1:

            if plik['rodzaj zakwaterowania'][i] == 'hotel':

                if czy_juz_jest:
                    pass
                else:
                    indexes_to_drop.append(i)
                    czy_juz_jest = i in indexes_to_drop

        if answers[0] == 2:
            print("działa")

            pass

        # Szczepienia

        if answers[1] == 1:

            if plik['szczepienia '][i] == 1:

                if czy_juz_jest:
                    pass
                else:
                    indexes_to_drop.append(i)
                    czy_juz_jest = i in indexes_to_drop

        # ALL INCLUSIVE

        if answers[3] == 1:

            if plik['all inclusive'][i] == 1:

                if czy_juz_jest:
                    pass
                else:
                    indexes_to_drop.append(i)
                    czy_juz_jest = i in indexes_to_drop

        # WIZA

        if answers[4] == 0:

            if plik['wiza'][i] == 1:

                if czy_juz_jest:
                    pass
                else:
                    indexes_to_drop.append(i)
                    czy_juz_jest = i in indexes_to_drop

        # Wypoczynek i zabawa

        if answers[5] == 1:

            # Wypocząć

            if plik['wypoczynek/zwiedzanie/zabawa'][i] == 'odpoczynek':

                if czy_juz_jest:
                    pass
                else:
                    indexes_to_drop.append(i)
                    czy_juz_jest = i in indexes_to_drop

        if answers[5] == 0:

            if plik['wypoczynek/zwiedzanie/zabawa'][i] == 'zabawa/zwiedzanie':

                if czy_juz_jest:
                    pass
                else:
                    indexes_to_drop.append(i)
                    czy_juz_jest = i in indexes_to_drop

        if answers[5] == 2:
            print("lece na całość")
            pass

    # szczytywanie wartości wierszy

    x = 0
    list_points = []
    while x < wiersze:
        list_help = []
        for i in kolumny[0:7]:
            list_help.append(plik[i][x])
        list_points.append([list_help])
        x = x + 1

    # Obliczanie funkcji celu

    funtion_values = []
    values_and_location = {}
    indexes_and_location = {}
    for i in range(len(list_points)):
        Z = 0
        for j in range(1, 7):
            Z += (p[j - 1] / 5 * list_points[i][0][j]) * 100

        funtion_values.append(Z)
        values_and_location[list_points[i][0][0]] = round(Z, 2)

    print(indexes_to_drop)

    for i in indexes_to_drop:
        name = plik['Lokacje'][i]
        values_and_location[name] = 0

    top_lokacje = dict(sorted(values_and_location.items(), key=itemgetter(1), reverse=True)[:5])
    Label(canvas_page2, text="WYBRANE LOKALIZACJE DLA CIEBIE: \n \n \n \n ").grid(row=1, column=0)
    d = 0
    for i in top_lokacje:
        index = plik[plik["Lokacje"] == i].index[0]
        language = plik['język'][index]
        transport = plik['rodzaj transportu'][index]
        Label(canvas_page2,
              text="{}   :   {} % zgodne z twoimi preferencjami \n \n Języki:{} // Rodzaj transportu:{} \n".format(i,
                                                                                                                   top_lokacje[
                                                                                                                       i],
                                                                                                                   language,
                                                                                                                   transport)).grid(
            row=8 + d, column=0)
        d = d + 1
    submit = Button(canvas_page2, text="Kliknij jeżeli chcesz przejść dalej i wybrać swoje oferty",
                    command=lambda: Select_location(canvas_page2,values_and_location))
    submit.grid()

    button2 = Button(canvas_page2, text = 'Kliknij jeżeli chciałbyś dalej porównać dobrane oferty',
                     command =lambda: Ahp_questions_2(canvas_page2, top_lokacje, values_and_location) )
    button2.grid()

def Select_location(canvas,values_and_location):

    plik = pd.read_csv("baza_podroz.csv", delimiter=";")
    canvas.destroy()
    canvas_page4 = Canvas(window)
    canvas_page4.pack()
    Label(canvas_page4, text = 'Wybierz Lokalizacje które chcesz dodać do porównania (Max 5)').pack()
    Label(canvas_page4, text = '').pack()
    lista_lokalizacji = Frame(canvas_page4)
    scrollbar = Scrollbar(lista_lokalizacji)


    listbox = Listbox(lista_lokalizacji, yscrollcommand = scrollbar.set)

    scrollbar.config(command = listbox.yview)


    scrollbar.pack(side = 'right', fill = Y)
    lista_lokalizacji.pack()
    listbox.pack()



    lokacje = []

    for i in plik['Lokacje']:
        lokacje.append(i)

    for i in lokacje:

        listbox.insert(END, i)

    global wybrane
    wybrane = []

    def Select():


        wybrane.append(listbox.get(ANCHOR))


        if len(wybrane) > 5:
            messagebox.showwarning('Ostrzeżenie', 'Masz już maksymalną ilość dodanych miejsc ')
            wybrane.remove(wybrane[-1])
        Label(canvas_page4, text='Dodałeś {}'.format(wybrane[-1])).pack()


    def Delete():
        wybrane = []
        Label(canvas_page4, text = "Miejca usunięte").pack()



    but = Button(canvas_page4, text = 'Dodaj miejsca ', command =lambda :Select())
    but.pack()
    Button(canvas_page4, text = 'Usuń wybrane miejsca', command = lambda :Delete()).pack()


    button = Button(canvas_page4, text = 'Zatwierdz miejsca i przejdź dalej ',
                    command =lambda :Ahp_questions(canvas_page4,wybrane,values_and_location))
    button.pack()


def Ahp_questions_2(canvas, top_lokacje,values_and_location):



    canvas.destroy()
    canvas_page4 = Canvas(window)
    canvas_page4.grid()

    Label(canvas_page4, text = 'Ustaw swoje preferencje względem wybranych miejsc').grid()
    global variables
    placeholder = []
    print(top_lokacje)
    for i in top_lokacje:
        placeholder.append(i)

    top_lokacje = placeholder

        
    variables = []




    for i in range(len(top_lokacje)):
        for j in range(len(top_lokacje)):
            if i >= j:
                pass
            else:
                Label(canvas_page4, text = "").grid()
                Label(canvas_page4, text="Jak preferujesz miejsce {} względem miejsca {}"
                      .format(top_lokacje[i], top_lokacje[j])).grid()
                d = StringVar()
                OPTIONS = ['Tak samo preferuję oba miejsca',
                           'Preferuje miejsce 1'.format(top_lokacje[i]),
                           'Preferuje bardziej miejsce 1'.format(top_lokacje[i]),
                           'Preferuje o wiele bardziej miejsce 1'.format(top_lokacje[i]),
                           'Preferuje miejsce 2'.format(top_lokacje[j]),
                           'Preferuje bardziej miejsce 2'.format(top_lokacje[j]),
                           'Preferuje o wiele bardziej miejsce 2'.format(top_lokacje[j])]
                d.set(OPTIONS[0])
                variables.append(d)
                w = OptionMenu(canvas_page4, d, *OPTIONS)
                w.grid()

    def printuj():
        kalko = variables[0].get()
        kalko2 = variables[1].get()
        print(kalko)
        print(kalko2)
    global to_ahp

    def zatw():
        global to_ahp
        to_ahp = []
        for i in range(len(variables)):

                    if variables[i].get() == 'Tak samo preferuję oba miejsca':
                        tymczas = 1
                        to_ahp.append(tymczas)
                    elif variables[i].get() == 'Preferuje miejsce 1':
                        tymczas = 3
                        to_ahp.append(tymczas)
                    elif variables[i].get() == 'Preferuje bardziej miejsce 1':
                        tymczas = 6
                        to_ahp.append(tymczas)
                    elif variables[i].get() == 'Preferuje o wiele bardziej miejsce 1':
                        tymczas = 9
                        to_ahp.append(tymczas)
                    elif variables[i].get() == 'Preferuje miejsce 2':
                        tymczas = 1/3
                        to_ahp.append(tymczas)
                    elif variables[i].get() == 'Preferuje bardziej miejsce 2':
                        tymczas = 1/6
                        to_ahp.append(tymczas)
                    elif variables[i].get() == 'Preferuje o wiele bardziej miejsce 2':
                        tymczas = 1/9
                        to_ahp.append(tymczas)
        print('zatwierdzone')





    Button(canvas_page4, text = "Zatwierdź Preferencje ", command=lambda:zatw()).grid()

    Button(canvas_page4, text = 'Przejdz dalej',
           command = lambda:Final_screen(canvas_page4, to_ahp, top_lokacje,values_and_location)).grid()



def Ahp_questions(canvas, top_lokacje,values_and_location):


    if len(top_lokacje) > 5:
        messagebox.showwarning("Ostrzeżenie", "Ilość wybranych miejsc przekroczyła maximum")
        return
    if len(top_lokacje) < 2:
        messagebox.showwarning('Ostrzeżenie', 'Ilość wybranych miejsc musi być minimum 2 ')
        return


    canvas.destroy()
    canvas_page4 = Canvas(window)
    canvas_page4.grid()

    Label(canvas_page4, text = 'Ustaw swoje preferencje względem wybranych miejsc').grid()
    global variables
    variables = []




    for i in range(len(top_lokacje)):
        for j in range(len(top_lokacje)):
            if i >= j:
                pass
            else:
                Label(canvas_page4, text="Jak preferujesz miejsce {} względem miejsca {}"
                      .format(top_lokacje[i], top_lokacje[j])).grid()
                d = StringVar()
                OPTIONS = ['Tak samo preferuję oba miejsca',
                           'Preferuje miejsce 1'.format(top_lokacje[i]),
                           'Preferuje bardziej miejsce 1'.format(top_lokacje[i]),
                           'Preferuje o wiele bardziej miejsce 1'.format(top_lokacje[i]),
                           'Preferuje miejsce 2'.format(top_lokacje[j]),
                           'Preferuje bardziej miejsce 2'.format(top_lokacje[j]),
                           'Preferuje o wiele bardziej miejsce 2'.format(top_lokacje[j])]
                d.set(OPTIONS[0])
                variables.append(d)
                w = OptionMenu(canvas_page4, d, *OPTIONS)
                w.grid()

    def printuj():
        kalko = variables[0].get()
        kalko2 = variables[1].get()
        print(kalko)
        print(kalko2)
    global to_ahp

    def zatw():
        global to_ahp
        to_ahp = []
        for i in range(len(variables)):

                    if variables[i].get() == 'Tak samo preferuję oba miejsca':
                        tymczas = 1
                        to_ahp.append(tymczas)
                    elif variables[i].get() == 'Preferuje miejsce 1':
                        tymczas = 3
                        to_ahp.append(tymczas)
                    elif variables[i].get() == 'Preferuje bardziej miejsce 1':
                        tymczas = 6
                        to_ahp.append(tymczas)
                    elif variables[i].get() == 'Preferuje o wiele bardziej miejsce 1':
                        tymczas = 9
                        to_ahp.append(tymczas)
                    elif variables[i].get() == 'Preferuje miejsce 2':
                        tymczas = 1/3
                        to_ahp.append(tymczas)
                    elif variables[i].get() == 'Preferuje bardziej miejsce 2':
                        tymczas = 1/6
                        to_ahp.append(tymczas)
                    elif variables[i].get() == 'Preferuje o wiele bardziej miejsce 2':
                        tymczas = 1/9
                        to_ahp.append(tymczas)
        print('zatwierdzone')





    Button(canvas_page4, text = "Zatwierdź Preferencje ", command=lambda:zatw()).grid()

    Button(canvas_page4, text = 'Przejdz dalej',
           command = lambda:Final_screen(canvas_page4, to_ahp, top_lokacje,values_and_location)).grid()




def Final_screen(canvas, answers, top_lokacje,values_and_location):

    canvas.destroy()
    canvas_page4 = Canvas(window)
    canvas_page4.grid()
    comparison = {}
    print(answers)


    for i in range(len(top_lokacje)):
        for j in range(len(top_lokacje)):
            if i >= j:
                pass
            else:
                comparison[(top_lokacje[i], top_lokacje[j])] = 0
    f = 0
    for i in comparison:
        comparison[i] = answers[f]

        f += 1
    print(comparison)

    compare = ahpy.Compare(name = 'Wynik', comparisons=comparison, precision=3, random_index='saaty')
    print(compare.target_weights)


    final_weights = compare.target_weights
    final_dict = {}


    for i in top_lokacje:
        
        if values_and_location[i] == 0:
            values_and_location[i] = 1

        Z = values_and_location[i] * final_weights[i]
        final_dict[i] = Z


    print(final_dict)

    final_dict = dict(sorted(final_dict.items(), key=itemgetter(1), reverse=True)[:5])
    Label(canvas_page4, text = "Po analizie ranking destynacji podróży prezentuje się następująco ").grid()
    d = 1
    for i in final_dict:
        Label(canvas_page4, text = "{}   {} ".format(d, i)).grid()
        d = d+1


Start_screen()
window.mainloop()

