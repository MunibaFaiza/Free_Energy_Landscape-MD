#!/usr/bin/env python

import sys

"""
Utility tool to convert xpm files generated by GROMACS to a 3-column text file.
"""

USAGE = "USAGE: xpm2txt.py -f input.xpm -o output.txt [-s]\n"
USAGE+= "Options:\n"
USAGE+= "\t-s\t(int)\tSorts the output by a given column"
USAGE+= "\n" # always keep this line

'''
THIS SCRIPT IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND 
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER 
IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT 
OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

# Parse arguments
read_input, read_output, sort = False, False, False
xpm_file, out_file, column_sort = None, None, None
for arg in sys.argv[1:]:
    if read_input:
        read_input = False
        xpm_file = arg
    elif read_output:
        read_output = False
        out_file = arg
    elif sort:
        sort = False
        column_sort = int(arg)
    if arg[0] == "-":
        if arg == "-f":
            read_input = True
            continue
        elif arg == "-o":
            read_output = True
            continue
        elif arg == "-s":
            sort = True
        else:
            print USAGE
            sys.stderr.write('ERROR: Option not recognized: %s\n' %arg)
            sys.exit(1)

if not xpm_file:
    print USAGE
    sys.stderr.write('ERROR: You forgot to provide an input file.\n')
    sys.exit(1)
if not out_file:
    out_file = "out.txt"

# Parse XPM file
xpm_handle = open(xpm_file)
xpm_data = []
x_axis, y_axis = [], []
letter_to_value = {}
for line in xpm_handle:
    if line.startswith("/* x-axis"):
        x_axis = map(float, line.split()[2:-2]) # We trim the last value

    if line.startswith("/* y-axis"):
        y_axis = map(float, line.split()[2:-2]) # We trim the last value

    if line.startswith('"') and x_axis and y_axis: # Read data
        xpm_data.insert(0, line.strip().strip(',')[1:-1])

    if line.startswith('"') and len(line.split()) > 4:
        letter = line.split()[0][1:]
        value = float(line.split()[-2][1:-1])
        letter_to_value[letter] = value
xpm_handle.close()

# Match x/y/data
txt_values = []
for y_index, data_value in enumerate(xpm_data):
    y_value = y_axis[y_index]
    for x_index, x_value in enumerate(x_axis):
        txt_values.append([x_value, y_value, letter_to_value[data_value[x_index]]])

# Apply sorting if requested
if column_sort:
    try:
        txt_values.sort(key=lambda x: x[column_sort-1])
    except IndexError:
        print USAGE
        sys.stderr.write('ERROR: Column not found (%s)\n' %(column_sort))
        sys.exit(1)

# Print to file
out_handle = open(out_file, 'w')
for x, y, z in txt_values:
    out_handle.write("%3.5f\t%3.5f\t%3.5f\n" %(x,y,z))
out_handle.close()
    
    

