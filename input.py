''' This code is to generate input files  to choose your basis set size for convergence testing
using Quantum Espresso software.'''
file_count = 0
in_name = str(input('enter the input the entire file directory  (with extension): ')) #Please enter the absolute path for the file
no_of_files = int(input('how many files you want to create: '))
out_dir= str(input('enter the entire output file directory : '))
out_name = str(input('enter the entire output file name  (without extension): '))
ecutwfc_start = int(input('enter the initial value for ecutwfc : '))
ecutwfc_add = int(input('enter the addition factor for subsequent files : '))
ecutrho_mult = int(input('enter the multiplication factor of ecutwfc: '))
ecutwfc = (ecutwfc_start - ecutwfc_add)/1
ecutrho = (ecutwfc_start * ecutrho_mult) / ecutrho_mult

'''The code below creates the files with user specified name.'''
for no in range(no_of_files):
    file_count += 1
    suf = str(file_count)
    temp=str(out_dir+'/'+out_name+'_'+suf+'.in')
    name = temp
    # #print(name)
####The code below creates the values for ecutwfc (basis set) and ecutrho (cutoff value) as per user specification.'''
    ecutwfc += ecutwfc_add
    str_ecutwfc = str(ecutwfc)
    # #print(ecutwfc)
    ecutrho = ecutwfc * ecutrho_mult
    str_ecutrho = str(ecutrho)
    # #print(ecutrho)
    value_a = '  ecutrho =   ' + str_ecutrho + '\n'
    value_b = '  ecutwfc =   ' + str_ecutwfc + '\n'
    value = value_a + value_b
    # #print(value)
####The code below reads the input file  provided by the user and creates new input files for basis set convergence testing.'''
    with open(in_name) as input_file:
        with open(name, 'w') as out:
            for i in input_file:
                if i.startswith('  ecutwfc'):
                    out.write(value)
                else:
                    out.write(i)

print('Please check', out_dir,'for the input files for basis set convergence testing!')
# /home/vishnu/qe_6.7/workQE/basic/tset/test
# /home/vishnu/Documents/python/python_for_everybody/input.in