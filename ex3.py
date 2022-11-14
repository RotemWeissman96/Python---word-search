def list_sum(list1):
    """
    sums all the variables inside of list
    :param list1: the list to sum
    :return: the sum of the list's variables
    """
    sum1 = 0.0
    for x in range(len(list1)):
        sum1 += list1[x]
    return sum1


def input_list():
    """
    receive a list of numbers from user input
    :return: the created list with the sum of all the numbers in its last index
    """
    l1 = []  # the list
    argument = input()  # receive the arguments form user input
    while argument != "":  # continue to receive until user type nothing
        l1.append(float(argument))
        argument = input()
    if not l1:  # if our list is empty = the user typed nothing
        l1.append(0)
        return l1
    else:
        l1.append(list_sum(l1))  # adds the summery at the last index
        return l1


def inner_product(vec_1, vec_2):
    """
    multiply 2 vectors
    :param vec_1: first vector
    :param vec_2: second vector
    :return: the result of multiplying the two vectors
    """
    answer = 0  # calculate the sum of all the multiplied arguments
    if len(vec_1) != len(vec_2): return  # if the length of the vectors are not equal
    if not vec_1: return 0  # if there are no arguments in the vector
    for x in range(len(vec_1)): answer += float(vec_1[x])*float(vec_2[x])
    return answer


def sequence_monotonicity(sequence):
    """
    check if a list is organized in descending, increasing or equal and one of them
    :param sequence: the list of numbers to check
    :return: list of boolean answers: [0] equal or increasing [1]  increasing [2] equal or decreasing [3] decreasing
    """
    result = [True, True, True, True]  # the list of boolean answers
    if sequence == False or len(sequence) == 1: return result  # if the list is empty or has only 1 index
    for x in range(len(sequence)-1):  # for loop to check all the numbers
        if result == [False, False, False, False]: return result  # if all the options were disqualified
        if sequence[x] < sequence[x+1]: result[2] = False; result[3] = False  # if its no longer decreasing
        if sequence[x] > sequence[x + 1]: result[0] = False; result[1] = False  # if its no longer increasing
        if sequence[x] == sequence[x + 1]: result[1] = False; result[3] = False  # if it has equals arguments
    return result


def monotonicity_inverse(def_bool):
    """
    give an example for a series of numbers that fit the definitions from sequence_monotonicity
    :param def_bool: list of boolean : [0] equal or increasing [1]  increasing [2] equal or decreasing [3] decreasing
    :return: an example that fit all the True definitions from the list
    """
    if def_bool[0]:
        if def_bool[1]: return [1, 2, 3, 4]  # if its only increasing
        if def_bool[2]: return [1, 1, 1, 1]  # if its both equal or increasing and equal or decreasing
        return [1, 1, 2, 4]  # if its equal or increasing
    if def_bool[2]:
        if def_bool[3]: return [4, 3, 2, 1]  # if only decreasing
        return [4, 4, 3, 2]  # if its equal or decreasing
    return None  # if its not any valid option


def is_it_prime(number, lower_prime_list):
    """
    check if a number is prime
    :param number: the number to check
    :param lower_prime_list: recieve all the primes lower then number in a list
    :return: True if the number is prime, or False if not
    """
    if number == 2 or number == 3: return True
    if number % 2 == 0 or (number > 10 and (number % 10 == 0 or number % 10 == 5 )): return False
    # if the number is pair or dividable by 5 don't check it, return False
    if len(lower_prime_list) % 2 == 0: half_prime_list = lower_prime_list[0:int(len(lower_prime_list)/2)]
    # half_prime cuts the prime list in half in order to check less possibilities for number division
    else: half_prime_list = lower_prime_list[0:int((len(lower_prime_list)-1)/2)]  # if prime list cant be divided by 2
    for x in half_prime_list:  # check the lower half of prime numbers which are lower then number
        if number % x == 0: return False
    return True


def primes_for_asafi(n):
    """
    finds n prime numbers
    :param n: number of prime numbers wanted
    :return: list of n prime numbers
    """
    if n == 0: return None
    if n == 1: return [2]
    l1 = [2, 3]
    for x in range(n-2):  # finds n-2 numbers because 2 and 3 are already inside
        next_prime = l1[len(l1)-1]+2  # next number to check add by 2 to avoid checking pairs
        while not is_it_prime(next_prime, l1):
            next_prime += 2  # if the number is not prime, check the next odd number
        l1.append(next_prime)
    return l1


def sum_of_vectors(vec_lst):
    """
    sum's any number of vectors in list into 1 vector
    :param vec_lst: list of all the vectors
    :return: a vector which contains the sum of all the vectors from list
    """
    if not vec_lst: return None
    if not vec_lst[0]: return []
    new_list = []  # receive the new vector
    for j in range(0, len(vec_lst[0])):  # going through all the argument inside the vectors
        sum1 = 0
        for i in range(0, len(vec_lst)):  # going through all the vectors
            sum1 += vec_lst[i][j]
        new_list.append(sum1)
    return new_list


def num_of_orthogonal(vectors):
    """
    counts the number of pairs of vectors the their multiply is equal 0 in the vector list
    :param vectors: a list of vectors to check
    :return: how many pairs of vectors where multiply and resulted 0
    """
    counter = 0  # counts the pairs
    for i in range(0, len(vectors)):  # go through all vectors
        for j in range(i+1, len(vectors)):  # go through all vectors that haven't been check with the 'i' vector
            if inner_product(vectors[i], vectors[j]) == 0:
                counter += 1
    return counter

