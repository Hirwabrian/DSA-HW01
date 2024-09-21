#!/usr/bin/python3

import os

class UniqueInt:
    def __init__(self):
        #fetches the input file pah from user input
        input_dir = os.path.join(os.getcwd(), 'sample_inputs')
        self.filename = input("Please enter the filename (with extension): ")
        self.filepath = os.path.join(input_dir, self.filename)
        if os.path.isfile(self.filepath):
            print(f"File '{self.filename}' is found in {input_dir}.")
        else:
            print(f"File '{self.filename}' doesn't exist in '{input_dir}'. Exiting.")
            exit()

    def minval(self):
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

        #Saves the results in a specific directory
        savedir = os.path.join(os.getcwd(), 'sample_results')
        if not os.path.exists(savedir):
            try:
                os.makedirs(savedir)
                print(f"Directory '{savedir}' created.")
            except Exception as e:
                print(f"Error creating directory '{savedir}': {e}")
                exit()

        # Save the result file in the sample_results directory
        save = os.path.basename(self.filename) + "_results.txt"
        save_file = os.path.join(savedir, save)

        with open(save_file, "w") as f2:
            for i in range(Range):
                if array[i]:
                    num = i - converter
                    f2.write(f"{num}\n")

        print(f"Results saved in: {save_file}")

# Run the sorting process
UniqueInt().sorting()
