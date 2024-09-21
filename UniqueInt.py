#!/usr/bin/python3

import os
import time
import tracemalloc 

class UniqueInt:
    """
    A class to find the unique integers in a file, sort them, and save the result.
    """

    def __init__(self):

        input_dir = os.path.join(os.getcwd(), 'sample_inputs')
        self.filename = input("Please enter the filename (with extension): ")
        self.filepath = os.path.join(input_dir, self.filename)
        
        if os.path.isfile(self.filepath):
            print(f"File '{self.filename}' is found in {input_dir}.")
        else:
            print(f"File '{self.filename}' doesn't exist in '{input_dir}'. Exiting.")
            exit()

    def minval(self):
        """
        Find the minimum integer in the file.

        Returns:
            minval (int): The smallest integer found in the file.
        """
        minval = float('inf')
        with open(self.filepath, 'r') as f:
            for line in f:
                for word in line.split():
                    if word.isdigit() or (word.startswith('-') and word[1:].isdigit()):
                        num = int(word)
                        if num < minval:
                            minval = num
        return minval

    def maxval(self):
        """
        Find the maximum integer in the file.

        Returns:
            maxval (int): The largest integer found in the file.
        """
        maxval = float('-inf')
        with open(self.filepath, 'r') as f:
            for line in f:
                for word in line.split():
                    if word.isdigit() or (word.startswith('-') and word[1:].isdigit()):
                        num = int(word)
                        if num > maxval:
                            maxval = num
        return maxval

    def sorting(self):
        """
        Sort the unique integers in the file and save the sorted list in 'sample_results' directory.
        Also tracks the memory usage and execution time of the process.
        """
        start_time = time.time()
        tracemalloc.start()

        minval = self.minval()
        maxval = self.maxval()
        converter = -(minval)
        Range = maxval - minval + 1
        array = [False] * Range

        with open(self.filepath, 'r') as f1:
            for line in f1:
                for word in line.split():
                    if word.isdigit() or (word.startswith('-') and word[1:].isdigit()):
                        num = int(word)
                        i = num + converter
                        array[i] = True

        
        savedir = os.path.join(os.getcwd(), 'sample_results')
        if not os.path.exists(savedir):# check if sample_results' directory exists
            try:
                os.makedirs(savedir)
                print(f"Directory '{savedir}' created.")
            except Exception as e:
                print(f"Error creating directory '{savedir}': {e}")
                exit()

        save = os.path.basename(self.filename) + "_results.txt"
        save_file = os.path.join(savedir, save)

        with open(save_file, "w") as f2:
            for i in range(Range):
                if array[i]:
                    num = i - converter
                    f2.write(f"{num}\n")

        print(f"Results saved in: {save_file}")

        end_time = time.time()
        memory = tracemalloc.get_traced_memory()

        print(f"Memory usage: {memory} MB")
        print(f"Execution time: {end_time - start_time:.4f} seconds")

        tracemalloc.stop()

UniqueInt().sorting()
