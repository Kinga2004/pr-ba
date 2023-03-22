import math
import random


class Vector:

    def __init__(self, args=3):
        """
        Funkcja:
            Funkcja tworzy wektory o elementach '0'
        Input:
            args(integer) - ilość elementów wektora
        """
        self.args = args
        wektor = [0 for i in range(args)]
        self.wektor = wektor

    def create(self):
        """
        Funkcja:
            Funkcja wpisuje losowe współrzędne wektora.
        Output:
            wektor(list) - wektor o losowych współrzędnych
        """
        for i in range(self.args):
            self.wektor[i] = round(random.uniform(-10,10),2)
        return self.wektor

    def read_values(self, list):
        """
        Funkcja:
            Funkcja wczytuje elementu z listy podanej jako argument.
        Input:
            list(list) - lista ze współrzędnymi wektora
        Output:
            wektor(list) - wektor o podanych współrzędnych
        """
        self.list = list
        if self.args != len(list):
            return 'Podaj listę skłądającą się z {} elementów'.format(self.args)
        else:
            for i in range(len(list)):
                self.wektor[i] = list[i]
            return self.wektor

    def __add__(self, other):
        """
        Funkcja:
            Funkcja dodaje dwa wektory.
        Input:
            other(list) - wektor
        Output:
            wektor(list) - suma dwóch wektorów
        """
        if self.args != other.args:
            return 'Podaj wektor skłądającą się z {} elementów'.format(self.args)
        else:
            for i in range(self.args):
                self.wektor[i] = round (self.wektor[i] + other.wektor[i], 2)
            return self.wektor

    def __sub__(self, other):
        """
        Funkcja:
            Funkcja odejmuje dwa wektory.
        Input:
            other(list) - wektor
        Output:
            wektor(list) - różnica dwóch wektorów
        """
        if self.args != other.args:
            return 'Podaj wektor skłądającą się z {} elementów'.format(self.args)
        else:
            for i in range(self.args):
                self.wektor[i] = round (self.wektor[i] - other.wektor[i], 2)
            return self.wektor

    def __mul__(self, other):
        """
        Funkcja:
            Funkcja mnoży elementy wektora przez skalar.
        Input:
            other(float) - skalar
        Output:
            wektor(list) - wektor o elementach przemnożonych przez skalar
        """
        for i in range(self.args):
            self.wektor[i] = self.wektor[i]*other
        return self.wektor

    def length(self):
        """
        Funkcja:
            Funkcja liczy długość wektora.
        Output:
            l(float) - długość wektora
        """
        l = 0
        for i in range(self.args):
            l += self.wektor[i]**2
        l = math.sqrt(l)
        return l

    def sum(self):
        """
        Funkcja:
            Funkcja liczy sumę elementów wektora.
        Output:
            s(float) - suma elementów wektora
        """
        s = 0
        for i in range(self.args):
            s += self.wektor[i]
        return s

    def multi(self, other):
        """
        Funkcja:
            Funkcja liczy iloczyn skalarny dwóch wektorów.
        Input:
            other(list) - wektor
        Output:
            wektor(list) - iloczyn skalarny podanych wektorów
        """
        if self.args != other.args:
            return 'Podaj wektor skłądającą się z {} elementów'.format(self.args)
        else:
            liczba = 0
            for i in range(self.args):
                liczba += self.wektor[i] * other.wektor[i]
            return liczba

    def __str__(self):
        """
        Funkcja:
            Funkcja tworzy reprezentacja tekstową wektora.
        Output:
            wektor(string) - reprezentacja tekstowa wektora
        """
        return str(self.wektor)

    def __getitem__(self, item):
        """
        Funkcja:
            Funkcja tworzy operator [] pozwalający na dostęp do konkretnych elementów wektora.
        Input:
            item(integer) - numer elementu, który chcemy wyświetlić
        Output:
            args[item](float) - konkretny element wektora
        """
        if item > self.args-1 or item < -self.args:
            return 'Za mało elementów w wektorze'.format(self.args)
        else:
            return self.wektor[item]

    def __contains__(self, number):
        """
        Funkcja:
            Funkcja tworzy operator in sprawdzający przynależność elementu do wektora.
        Input:
            number(float) - liczba, którą chcemy sprawdzić, czy należy do wektora
        Output:
            (bool) - czy liczba należy do wektora
        """
        return number in self.wektor
