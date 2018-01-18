#!/usr/bin/env python
# encoding=utf8
import random


def build_a_random_sequence(length=10):
    return random.sample(range(length), length)


def insert_sort(seq):
    for i in range(1, len(seq)):
        j = i
        tmp = seq[i]
        while j > 0 and seq[j - 1] > tmp:
            seq[j] = seq[j - 1]
            j -= 1
        seq[j] = tmp
        print(seq)
    return seq


def select_sort(seq):
    for i in range(len(seq)):
        k = i
        for j in range(i + 1, len(seq)):
            if seq[j] < seq[k]:
                k = j
        if k != i:
            seq[k], seq[i] = seq[i], seq[k]
        print(seq)
    return seq


def bubble_sort(seq):
    for i in range(len(seq)):
        is_sorted = True
        for j in range(1, len(seq)):
            if seq[j - 1] > seq[j]:
                seq[j - 1], seq[j] = seq[j], seq[j - 1]
                is_sorted = False
        if is_sorted:
            break
        print(seq)
    return seq


def exchange_and_select_sort(seq):
    for i in range(len(seq)):
        for j in range(i, len(seq)):
            if seq[j] < seq[i]:
                seq[j], seq[i] = seq[i], seq[j]
        print(seq)
    return seq


def quick_sort(seq):
    """
    reference: http://bbs.ahalei.com/thread-4419-1-1.html
    """

    def quick_rec(seq, lo, hi):
        if lo > hi:
            return
        left = lo
        right = hi
        while left < right:
            while seq[right] >= seq[lo] and left < right:
                right -= 1
            while seq[left] <= seq[lo] and left < right:
                left += 1
            #  if left < right:
            seq[left], seq[right] = seq[right], seq[left]
        seq[lo], seq[left] = seq[left], seq[lo]
        print(seq)
        quick_rec(seq, lo, left - 1)
        quick_rec(seq, left + 1, hi)

    quick_rec(seq, 0, len(seq) - 1)
    return seq


def quick_sort1(seq):
    """
    reference: http://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
    """

    def quick_rec(seq, lo, hi):
        if lo > hi:
            return
        left = lo + 1
        right = hi
        while left <= right:
            if seq[left] < seq[lo]:
                left += 1
                continue
            if seq[right] > seq[lo]:
                right -= 1
                continue
            if left < right:
                seq[left], seq[right] = seq[right], seq[left]
                left += 1
                right -= 1
        seq[right], seq[lo] = seq[lo], seq[right]
        print(seq)
        quick_rec(seq, lo, right - 1)
        quick_rec(seq, right + 1, hi)

    quick_rec(seq, 0, len(seq) - 1)
    return seq


if __name__ == '__main__':
    seq = build_a_random_sequence()
    print('original sequence: {}'.format(seq))
    #  print('insert sort: {}'.format(insert_sort(seq)))
    #  print('select sort: {}'.format(select_sort(seq)))
    #  print('bubble sort: {}'.format(bubble_sort(seq)))
    #  print('exchange_and_select sort: {}'.format(exchange_and_select_sort(seq)))
    # print('quick sort: {}'.format(quick_sort(seq)))
    print('quick sort1: {}'.format(quick_sort1(seq)))
