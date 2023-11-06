import numpy as np
# import matplotlib.pyplot as plt
from scipy.stats import chi2, uniform, expon, norm
import matplotlib.pyplot as plt

n = 10000 # Кількість чисел
bins = 30
#для першої формули
l_array = [0.5,1,2,5]
#для другої формули
a_array = [2,3,5,5,3,1,3]
sigma_array = [1,2,4,6,4,2,3]
#для третьої формули
a = 5 ** 13
c = 2 ** 31
z0=3
  # перевірка за допомогою критерію згоди x**2
def checking_1(random_numbers, l):
    
    observed_frequencies, intervals = np.histogram(random_numbers, bins, density=True)
    if any(observed_frequencies < 5):
        print("Кількість влучень в один або декілька інтервалів менше за 5. Критерій не може бути застосований.")
        return
    expected_frequencies = expon.pdf((intervals[:-1] + intervals[1:]) / 2, scale=1/l)
    chi_squared = sum((observed_frequencies - expected_frequencies) ** 2 / expected_frequencies)

    degrees_of_freedom = len(intervals) - 1  -1   #  кількість ступенів свободи
    alpha = 0.05
    critical_value = chi2.ppf(1 - alpha, degrees_of_freedom)

    if chi_squared <= critical_value:
        print("Пройшло перевірку за допомогою критерію згоди x**2")
    else:
        print("Не пройшло перевірку за допомогою критерію згоди x**2")

        
def formula_1():
    for l in l_array:
        print("Лямбда = ",l)
    # сама формула
        random_numbers = - (1 / l) * np.log(np.random.rand(n))
    # перевірка за допомогою критерію згоди x**2
        checking_1(random_numbers, l)
        average = np.mean(random_numbers)
        print("Середне значення = ",average)
        variance = np.var(random_numbers)
        print("Дисперсія = ",variance)
        plt.hist(random_numbers, bins, density=True, color='g', alpha=0.6, label=f'l = {l}')

        # Обчислюємо теоретичну щільність ймовірності для експоненційного розподілу
        x = np.linspace(random_numbers.min(), random_numbers.max(), 1000)
        pdf = l * np.exp(-l * x)
        plt.plot(x, pdf, 'r', lw=2, label='Експоненційний  розподіл')
        plt.title('Гістрограма')
        plt.xlabel('random_numbers')
        plt.ylabel('PDF')
        plt.legend()
        plt.show()



    return random_numbers

  # перевірка за допомогою критерію згоди x**2
def checking_2(random_numbers):
    observed_frequencies, intervals = np.histogram(random_numbers, bins, density=True)
    if any(observed_frequencies < 5):
        print("Кількість влучень в один або декілька інтервалів менше за 5. Критерій не може бути застосований.")
        return
    expected_frequencies = norm.pdf( (intervals[:-1] + intervals[1:]) / 2, loc=np.mean(random_numbers), scale=np.std(random_numbers))

    chi_squared = sum((observed_frequencies - expected_frequencies) ** 2 / expected_frequencies)
    degrees_of_freedom = len(intervals) - 1  -2   #  кількість ступенів свободи
    alpha = 0.05
    critical_value = chi2.ppf(1 - alpha, degrees_of_freedom)
    if chi_squared <= critical_value:
        print("Пройшло перевірку за допомогою критерію згоди x**2")
    else:
        print("Не пройшло перевірку за допомогою критерію згоди x**2")

def formula_2():
    for i  in range(7):
        a = a_array[i]
        sigma = sigma_array[i]
        print("a = ",a, " sigma = ", sigma)
        # формули
        oi = np.random.uniform(0, 1, size=(n, 12))
        mi = np.sum(oi, axis=1) - 6
        random_numbers = sigma * mi + a
  # перевірка за допомогою критерію згоди x**2
        checking_2(random_numbers)
        average = np.mean(random_numbers)
        print("Середне значення = ",average)
        variance = np.var(random_numbers)
        print("Дисперсія = ",variance)
        plt.hist(random_numbers, bins, density=True, alpha=0.6, color='g', label=f'a = {a}, sigma = {sigma}')

        # Обчислення теоретичної функції щільності ймовірності для нормального розподілу і її побудова
        x = np.linspace(random_numbers.min(), random_numbers.max(), 1000)
        pdf = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((x - a) ** 2) / (2 * sigma ** 2))
        plt.plot(x, pdf, 'r', label='Нормальний розподіл(Гауса)')
        plt.title('гістограма')
        plt.xlabel('random_numbers')
        plt.ylabel('PDF')
        plt.legend()
        plt.show()


  # перевірка за допомогою критерію згоди x**2
def checking_3(random_numbers):
    observed_frequencies, intervals = np.histogram(random_numbers, bins, density=True)
    if any(observed_frequencies < 5):
        print("Кількість влучень в один або декілька інтервалів менше за 5. Критерій не може бути застосований.")
        return
    expected_frequencies = uniform.pdf(np.linspace(0, 1, bins))
    chi_squared = sum((observed_frequencies - expected_frequencies) ** 2 / expected_frequencies)

    degrees_of_freedom = len(intervals) - 1  -2   #  кількість ступенів свободи
    alpha = 0.05
    critical_value = chi2.ppf(1 - alpha, degrees_of_freedom)

    if chi_squared <= critical_value:
        print("Пройшло перевірку за допомогою критерію згоди x**2")
    else:
        print("Не пройшло перевірку за допомогою критерію згоди x**2")    

def formula_3():
    # формули
    z = np.zeros(n)
    z[0] = z0
    for i in range(1, n):
        z[i] = (a * z[i - 1]) % c
    random_numbers = z / c
  # перевірка за допомогою критерію згоди x**2
    checking_3(random_numbers)
    average = np.mean(random_numbers)
    print("Середне значення = ",average)
    variance = np.var(random_numbers)
    print("Дисперсія = ",variance)

    plt.hist(random_numbers, bins, density=True, alpha=0.6, color='g', label='Гістограма випадкових чисел')
    x = np.linspace(0, 1, 1000)
    uniform_pdf = np.ones_like(x)
    plt.plot(x, uniform_pdf, 'r', label='Рівномірний розподіл')
    plt.title('Гістограма')
    plt.xlabel('random_numbers')
    plt.ylabel('PDF')
    plt.legend()
    plt.show()




if __name__ == "__main__":
    formula_1()
    formula_2();
    formula_3()



