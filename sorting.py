#!/usr/bin/env python
# encoding=utf8
import random
from collections import deque


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


def quick_sort2(seq):
    """
    reference: https://visualgo.net/en/sorting
    """
    def quick_rec(seq, lo, hi):
        if lo > hi:
            return
        left = lo + 1
        right = hi
        store_index = left
        while left <= right:
            if seq[left] < seq[lo]:
                seq[left], seq[store_index] = seq[store_index], seq[left]
                store_index += 1
            left += 1
        seq[lo], seq[store_index-1] = seq[store_index-1], seq[lo]
        print(seq)
        quick_rec(seq, store_index, hi)
        quick_rec(seq, lo, store_index-2)
    quick_rec(seq, 0, len(seq)-1)
    return seq


def merge_sort(seq):
    """
    reference: https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F
    """
    if len(seq) <= 1:
        return list(seq)
    def merge(seql, seqr):
        merged_seq, seql, seqr = deque(), deque(seql), deque(seqr)
        while seql and seqr:
            merged_seq.append(seql.popleft() if seql[0] < seqr[0] else seqr.popleft())
        merged_seq.extend(seql if seql else seqr)
        return list(merged_seq)
    mid = len(seq) // 2
    left_seq = merge_sort(seq[:mid])
    right_seq = merge_sort(seq[mid:])
    return merge(left_seq, right_seq)


def merge_sort1(seq):
    """
    https://visualgo.net/en/sorting?slide=10
    """
    def merge_recursive(sequence, low, high):
        if low < high:
            mid = (low+high) // 2
            merge_recursive(sequence, low, mid)
            merge_recursive(sequence, mid+1, high)
            merge(sequence, low, mid, high)
    def merge(sequence, low, mid, high):
        left = low
        right = mid + 1
        tmp = []
        while left <= mid and right <= high:
            if sequence[left] < sequence[right]:
                tmp.append(sequence[left])
                left += 1
            else:
                tmp.append(sequence[right])
                right += 1
        while left <= mid:
            tmp.append(sequence[left])
            left += 1
        while right <= high:
            tmp.append(sequence[right])
            right += 1
        sequence[low:high+1] = tmp
        print(sequence)
    seq = list(seq)
    merge_recursive(seq, 0, len(seq)-1)
    return seq
        

if __name__ == '__main__':
    seq = build_a_random_sequence()
    print('original sequence: {}'.format(seq))
    #  print('insert sort: {}'.format(insert_sort(seq)))
    #  print('select sort: {}'.format(select_sort(seq)))
    #  print('bubble sort: {}'.format(bubble_sort(seq)))
    #  print('exchange_and_select sort: {}'.format(exchange_and_select_sort(seq)))
    # print('quick sort: {}'.format(quick_sort(seq)))
    # print('quick sort1: {}'.format(quick_sort1(seq)))
    # print('quick sort2: {}'.format(quick_sort2(seq)))
    print('merge sort: {}'.format(merge_sort(seq)))
    # print('merge sort1: {}'.format(merge_sort1(seq)))
