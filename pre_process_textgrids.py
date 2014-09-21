"""
Module docstring.

This serves as a long usage message.
"""
import sys
import os
import getopt
import tgt
import csv
import operator

def get_tg(filename):
    textgrid = tgt.io.read_textgrid(filename)
    #print textgrid.get_tier_names()

    if textgrid.has_tier("facilitator"):
        fac = textgrid.get_tier_by_name("facilitator")

    if textgrid.has_tier("participant"):
        par = textgrid.get_tier_by_name("participant")

    for tier_name in textgrid.get_tier_names():
        if str(tier_name) != "facilitator" and str(tier_name) != "participant":
            textgrid.delete_tier(tier_name)

    #if textgrid.has_tier("phone"):
        #textgrid.delete_tier("phone")

    #if textgrid.has_tier("task"):
        #textgrid.delete_tier("task")
    #print textgrid.get_tier_names()
    #overlap = tgt.util.get_overlapping_intervals(fac, par)
    #print overlap
    return textgrid

def write_tg(tg, filename="./test_tg.csv"):
    table = tgt.io.export_to_table(tg, separator="\t")
    #print table
    table = table.split('\n')
    table_csv = list(csv.reader(table, delimiter="\t"))
    #print table_csv

    # don't need to know what type of tier it is
    for row in table_csv:
        del row[1]

    convert_cells_to_floats(table_csv)
    
    # sort by starting time
    sorted_table = sorted(table_csv, key=operator.itemgetter(1))
    #print sorted_table

    export = []
    prev_speaker = None
    iterator = -1
    # combine adjacent speech rows into a string
    for row in sorted_table:
        if row[0] == prev_speaker:
            speech = " " + str(row[3])
            export[iterator][1] += speech
        else:
            # Silence on it's own doesn't tell us anything
            if row[3] != "{SL}" and row[3] != "sp":
                iterator += 1
                # print timestamps
                #time = str(row[1]) + " - " + str(row[2])
                export.append([row[0], row[3]])
                prev_speaker = row[0]
            else:
                print "{SL} or sp on its own"

    # move header row back to top
    export.insert(0, export.pop())

    with open(filename, 'w') as out:
        writer = csv.writer(out, delimiter='\t', quotechar='\"')
        for row in export:
            writer.writerow(row)

    #with open("./test_sort.csv", 'w') as out:
        #writer = csv.writer(out, delimiter='\t', quotechar='\"')
        #for row in sorted_table:
            #writer.writerow(row)

def process_dir_tg(input_dir, output_dir):
    for f in os.listdir(input_dir):
        if f.endswith("TextGrid"):
            print f
            input_path = os.path.join(input_dir, f)
            tg = get_tg(input_path)
            output_filename = f[:-8] + "tsv"
            output_path = os.path.join(output_dir, output_filename)
            write_tg(tg, output_path)

def convert_cells_to_floats(csv_cont):
    """ 
    Converts cells to floats if possible
    (modifies input CSV content list).
    
    """
    for row in range(len(csv_cont)):
        for cell in range(len(csv_cont[row])):
            try:
                csv_cont[row][cell] = float(csv_cont[row][cell])
            except ValueError:
                pass

process_dir_tg("ps16_dev_data/TextGrids/", "./transcripts/")

#tg = get_tg("./ps16_dev_data/TextGrids/AS1_T1_Stereo.TextGrid")
#write_tg(tg)
