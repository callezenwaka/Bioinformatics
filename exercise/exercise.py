Last login: Sat Nov  2 10:11:25 on ttys002
-bash: all: command not found
Callis-MacBook-Pro:~ mac$ python
Python 3.7.1 (default, Dec 14 2018, 13:28:58) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 806**2 + 866**2
1399592
>>> (806**2 + 866**2)**2
1958857766464
>>> sqrt(1399592)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqrt' is not defined
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> math.sqrt(1399592)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
>>> import math  
>>> x = 806**2 + 866**2
>>> x
1399592
>>> y = math.sqrt(x)
>>> y
1183.0435325887208
>>> x = 827**2 + 935**2
>>> y = math.sqrt(x)
>>> y
1248.2603895021264
>>> x = 895**2 + 850**2
>>> y = math.sqrt(x)
>>> y
1234.3115490021148
>>> dna = 'AGGTATCACTGCACAGCGCATCGTCACAGGGTTACCATTATGGTTACAGACCTAATTGTTTCACCACATTCCCCGGCTGCGTAGGACGACTTGAACTGAGTGCGGCGTCATAGCCGGTTCCCAGGCAGCGTTCGTACCCCCAAACCCCCCATTTCAATACCATAGACGGACTGTTATCTGAGACGACGGAGTGGACCTCGCGGTGATCCGCTTGCATGTTGACCTTATCATCCGGCTATTCTTAACTAAACGTGCACATGTCTGTCTAGATCTGCCGGCGCTTAGCTCTCCAAACGACTACACCACAGATCGGTGAAGGGCGAGTGTTAACTAAAATCTCTCTAGTATGCATAACATCTCGTTCGCCAGCCCGAAATTTTTAGGGTCTTTAATCCGATACTACTAGCGCGTAGTTAAGGAAGAGGAGCGCTGAGATCTGTAGCGCACGGTCTCGGCGTTCAGCAACCTGCACATTTAGCTCATTGACTTCTACCGGCGCACCCGCAATGATTCGGTAACGATACTCAGTCAGTCGCTTCGCGCACTAATCCTTGCCGATGAACCTCATTAGCTGCAACCATGGTTTCTGAGTTTGGTAGTGTCCTAATCACTGAGCCGATACATACGTGCGTATTGCTGCAGAACTGTGGGGGCAACGATTTCGGTCGAGTGTTTGGGAGGGAATGCTCATAGTTATTACGAATAGGCTTCCTACCCGTAGGGCCCACATAACTGCTGCGTCACGCATAGCGGGCGTGTACCATGGTGCATTGTCTTTCAGACGTGGGTGGCCCAATTAGAAATTGGAACCGATTCTGGCCTTTTGCACCAGTTTCCAGACACTTTAGATGTGGCCTATGCAATGCGTTGTTGATCCAGCCTTAAGTGTTCTCAACATTTTGAGGCACTATACGAATTGACCAATCCGGGGTCCTTCAAGTCACCCATGCCGACCATGGAGTACTTGAGCTAATGGACGGTCACGAC'
>>> len(dna)
987
>>> for i in range(len(dna)):
... if(i == 'A'):
  File "<stdin>", line 2
    if(i == 'A'):
     ^
IndentationError: expected an indented block
>>> for i in range(len(dna)):
... if(i == 'A'):{
  File "<stdin>", line 2
    if(i == 'A'):{
     ^
IndentationError: expected an indented block
>>> for i in range(len(dna)):
... if i == 'A'
  File "<stdin>", line 2
    if i == 'A'
     ^
IndentationError: expected an indented block
>>> import sys
>>> print(sys.executable)
/Users/mac/anaconda3/bin/python
>>> dna = 'GTAAGTTCTCCTGTGTTATACGGTCCACAAGCAATATAGACTACTGGCGAGACGGCATCACGATGCGACCTCGTAATGGTGTGATATAATGAAACATTGTGGTGGCTCATGGCCAAATTTAACACACTGTACATTGGTTCGGCTAAAGTAGGCCGGCTTTACCGGTAGGTGCGGATCAAGGTGAACGTGGTCCAAGAGCTACCGTCAAGGAAGTCAGGTGCGCAAGTGAGAGGGGCCAGGTCCTTTGGTAAATCTCCCTCGCTCTCCAGTGTCTGTCTCAAGGATCTGAATAAGCGCCGTATATTAACGGAGGATTCGTGGTACAGCATCCTACTTGTAGCAGACGGTGTGTGCCTATGATCGAGTCTGGCTCGCGATACCGTTGGGATCTGTGGGTTTTCTATGGGCAGCGGCGAGGTTTGCACACCGGATCAAGTTGATGATTTGTCAATGGTTGGAACCCTGTGACCCGGGACGTGTTATAGGGGGAGGCATCTGGGGGTGATTCACGGTCAAGCACTTCTAACTTTAGTGTTGGGTCTCGAAAAGCAAGCCACCGACGTACTTATCAAGGCGCCTATTGTTGAAGTGGACTTGCCGGGATCCAGCCTACTCAAGGGGTGCAATGATGCAAATCGGAGGCTGATCCTCTAGTAAGCTTTTAGTTGTCGGGGGCAGTAGAATGATCCGGGCTACTTACCGACGCTGGATCGCGGGTCACGTAATGACCTAACCCGCGTGAGACCGAGTAAGTTAAATTTGGGCCTAGTCGAGGTGCCCTGTACACTGGTTGTAGACATGG
  File "<stdin>", line 1
    dna = 'GTAAGTTCTCCTGTGTTATACGGTCCACAAGCAATATAGACTACTGGCGAGACGGCATCACGATGCGACCTCGTAATGGTGTGATATAATGAAACATTGTGGTGGCTCATGGCCAAATTTAACACACTGTACATTGGTTCGGCTAAAGTAGGCCGGCTTTACCGGTAGGTGCGGATCAAGGTGAACGTGGTCCAAGAGCTACCGTCAAGGAAGTCAGGTGCGCAAGTGAGAGGGGCCAGGTCCTTTGGTAAATCTCCCTCGCTCTCCAGTGTCTGTCTCAAGGATCTGAATAAGCGCCGTATATTAACGGAGGATTCGTGGTACAGCATCCTACTTGTAGCAGACGGTGTGTGCCTATGATCGAGTCTGGCTCGCGATACCGTTGGGATCTGTGGGTTTTCTATGGGCAGCGGCGAGGTTTGCACACCGGATCAAGTTGATGATTTGTCAATGGTTGGAACCCTGTGACCCGGGACGTGTTATAGGGGGAGGCATCTGGGGGTGATTCACGGTCAAGCACTTCTAACTTTAGTGTTGGGTCTCGAAAAGCAAGCCACCGACGTACTTATCAAGGCGCCTATTGTTGAAGTGGACTTGCCGGGATCCAGCCTACTCAAGGGGTGCAATGATGCAAATCGGAGGCTGATCCTCTAGTAAGCTTTTAGTTGTCGGGGGCAGTAGAATGATCCGGGCTACTTACCGACGCTGGATCGCGGGTCACGTAATGACCTAACCCGCGTGAGACCGAGTAAGTTAAATTTGGGCCTAGTCGAGGTGCCCTGTACACTGGTTGTAGACATGG
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ^
SyntaxError: EOL while scanning string literal
>>> dna = 'GTAAGTTCTCCTGTGTTATACGGTCCACAAGCAATATAGACTACTGGCGAGACGGCATCACGATGCGACCTCGTAATGGTGTGATATAATGAAACATTGTGGTGGCTCATGGCCAAATTTAACACACTGTACATTGGTTCGGCTAAAGTAGGCCGGCTTTACCGGTAGGTGCGGATCAAGGTGAACGTGGTCCAAGAGCTACCGTCAAGGAAGTCAGGTGCGCAAGTGAGAGGGGCCAGGTCCTTTGGTAAATCTCCCTCGCTCTCCAGTGTCTGTCTCAAGGATCTGAATAAGCGCCGTATATTAACGGAGGATTCGTGGTACAGCATCCTACTTGTAGCAGACGGTGTGTGCCTATGATCGAGTCTGGCTCGCGATACCGTTGGGATCTGTGGGTTTTCTATGGGCAGCGGCGAGGTTTGCACACCGGATCAAGTTGATGATTTGTCAATGGTTGGAACCCTGTGACCCGGGACGTGTTATAGGGGGAGGCATCTGGGGGTGATTCACGGTCAAGCACTTCTAACTTTAGTGTTGGGTCTCGAAAAGCAAGCCACCGACGTACTTATCAAGGCGCCTATTGTTGAAGTGGACTTGCCGGGATCCAGCCTACTCAAGGGGTGCAATGATGCAAATCGGAGGCTGATCCTCTAGTAAGCTTTTAGTTGTCGGGGGCAGTAGAATGATCCGGGCTACTTACCGACGCTGGATCGCGGGTCACGTAATGACCTAACCCGCGTGAGACCGAGTAAGTTAAATTTGGGCCTAGTCGAGGTGCCCTGTACACTGGTTGTAGACATGG'
>>> print(dna.count("A"))
185
>>> print(dna.count("C"))
173
>>> print(dna.count("G"))
240
>>> print(dna.count("T"))
204
>>> RNA = ''
>>> DNA = 'AGCACAAAGTCGGTGGGCACTTCAGTAAAACCCACTCCCCAAGAAGGAGCGAACGAATTGTCTATAAAGTCACTCCCTAAAACTTGTGATCTCAGGGGTGGGGATAGTGCCTAGCGATCCTCGTCGGATCCCGTAGTTGGAAGAGTATTCTGAGACTTCGAACCGCGCTCGGAAAAAGCCAAGACACCCTTACCGTAGGCCTGGATTTCATGCGAAGTTGAGCACATTACTTAGCATTAGCAAACAGTTCTTCGGATCTTTTTCTATTATTACAAGTACCCACCCCTAAAGCTATGCAATCATAGCCACCCGATGAATCCTTTAACAGGGCAGGGGTAAAACATCAGCCAGACTGGTCCCTTATCTTATGCGTCGCCATTCAATTGCCGCGTATAAAACCGGCGATGACCTATTCCTTTAAGGGAGGGTGTGTACCCAGCCCGCTGTGACGCCTGCCTCACCGTATAAGATCAGCCAGTGTTATCGCATGTGGTTTCTGTAAAATGTATTACGACCGTTTTCTTACGGGTATCCGCTCAGTAGTCAGGCTGCAGGTTAACTGTGCGCGCTGGTGGTCGCTTCTCCCCCATGGCACTCCCGAGTTGCGACGCTCAACCACGACTGCTAAGTCCCCTCGGATAGTGTCGTGTTTTAAGCTATCGCGCCGCTCGGGGTCCCTGGCCTTAACTTTGGAACTTCGTGCCTTGTTTCAAAATTACACAGATAGATTTGCGCACATTTTCTAATCAAGATTAAGCCGACTACTACACCTCCCCATAGAGTTAGTTGGTGTTATGACCGCAAGGATAAACTAAGCACACCGGTTCGGCGGGGATGTAACAGATTGCAGTGATACCGCGTTTCCTGGAGCGAATCTCGGTACGAAGTTGAAGAGGGCCGTGTCTGCACAGTGGGATAATGATGGGGGCCTCTGCATAACGCCATCCTCTGAGGCTTCCATAGTAAGG
  File "<stdin>", line 1
    DNA = 'AGCACAAAGTCGGTGGGCACTTCAGTAAAACCCACTCCCCAAGAAGGAGCGAACGAATTGTCTATAAAGTCACTCCCTAAAACTTGTGATCTCAGGGGTGGGGATAGTGCCTAGCGATCCTCGTCGGATCCCGTAGTTGGAAGAGTATTCTGAGACTTCGAACCGCGCTCGGAAAAAGCCAAGACACCCTTACCGTAGGCCTGGATTTCATGCGAAGTTGAGCACATTACTTAGCATTAGCAAACAGTTCTTCGGATCTTTTTCTATTATTACAAGTACCCACCCCTAAAGCTATGCAATCATAGCCACCCGATGAATCCTTTAACAGGGCAGGGGTAAAACATCAGCCAGACTGGTCCCTTATCTTATGCGTCGCCATTCAATTGCCGCGTATAAAACCGGCGATGACCTATTCCTTTAAGGGAGGGTGTGTACCCAGCCCGCTGTGACGCCTGCCTCACCGTATAAGATCAGCCAGTGTTATCGCATGTGGTTTCTGTAAAATGTATTACGACCGTTTTCTTACGGGTATCCGCTCAGTAGTCAGGCTGCAGGTTAACTGTGCGCGCTGGTGGTCGCTTCTCCCCCATGGCACTCCCGAGTTGCGACGCTCAACCACGACTGCTAAGTCCCCTCGGATAGTGTCGTGTTTTAAGCTATCGCGCCGCTCGGGGTCCCTGGCCTTAACTTTGGAACTTCGTGCCTTGTTTCAAAATTACACAGATAGATTTGCGCACATTTTCTAATCAAGATTAAGCCGACTACTACACCTCCCCATAGAGTTAGTTGGTGTTATGACCGCAAGGATAAACTAAGCACACCGGTTCGGCGGGGATGTAACAGATTGCAGTGATACCGCGTTTCCTGGAGCGAATCTCGGTACGAAGTTGAAGAGGGCCGTGTCTGCACAGTGGGATAATGATGGGGGCCTCTGCATAACGCCATCCTCTGAGGCTTCCATAGTAAGG
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ^
SyntaxError: EOL while scanning string literal
>>> DNA = 'AGCACAAAGTCGGTGGGCACTTCAGTAAAACCCACTCCCCAAGAAGGAGCGAACGAATTGTCTATAAAGTCACTCCCTAAAACTTGTGATCTCAGGGGTGGGGATAGTGCCTAGCGATCCTCGTCGGATCCCGTAGTTGGAAGAGTATTCTGAGACTTCGAACCGCGCTCGGAAAAAGCCAAGACACCCTTACCGTAGGCCTGGATTTCATGCGAAGTTGAGCACATTACTTAGCATTAGCAAACAGTTCTTCGGATCTTTTTCTATTATTACAAGTACCCACCCCTAAAGCTATGCAATCATAGCCACCCGATGAATCCTTTAACAGGGCAGGGGTAAAACATCAGCCAGACTGGTCCCTTATCTTATGCGTCGCCATTCAATTGCCGCGTATAAAACCGGCGATGACCTATTCCTTTAAGGGAGGGTGTGTACCCAGCCCGCTGTGACGCCTGCCTCACCGTATAAGATCAGCCAGTGTTATCGCATGTGGTTTCTGTAAAATGTATTACGACCGTTTTCTTACGGGTATCCGCTCAGTAGTCAGGCTGCAGGTTAACTGTGCGCGCTGGTGGTCGCTTCTCCCCCATGGCACTCCCGAGTTGCGACGCTCAACCACGACTGCTAAGTCCCCTCGGATAGTGTCGTGTTTTAAGCTATCGCGCCGCTCGGGGTCCCTGGCCTTAACTTTGGAACTTCGTGCCTTGTTTCAAAATTACACAGATAGATTTGCGCACATTTTCTAATCAAGATTAAGCCGACTACTACACCTCCCCATAGAGTTAGTTGGTGTTATGACCGCAAGGATAAACTAAGCACACCGGTTCGGCGGGGATGTAACAGATTGCAGTGATACCGCGTTTCCTGGAGCGAATCTCGGTACGAAGTTGAAGAGGGCCGTGTCTGCACAGTGGGATAATGATGGGGGCCTCTGCATAACGCCATCCTCTGAGGCTTCCATAGTAAGG'
>>> for i in DNA:
... if i == 'T':
  File "<stdin>", line 2
    if i == 'T':
     ^
IndentationError: expected an indented block
>>> for i in DNA:
...     if i == 'T':
...             RNA += 'U'
...     else:
...             RNA += i
... 
>>> RNA
'AGCACAAAGUCGGUGGGCACUUCAGUAAAACCCACUCCCCAAGAAGGAGCGAACGAAUUGUCUAUAAAGUCACUCCCUAAAACUUGUGAUCUCAGGGGUGGGGAUAGUGCCUAGCGAUCCUCGUCGGAUCCCGUAGUUGGAAGAGUAUUCUGAGACUUCGAACCGCGCUCGGAAAAAGCCAAGACACCCUUACCGUAGGCCUGGAUUUCAUGCGAAGUUGAGCACAUUACUUAGCAUUAGCAAACAGUUCUUCGGAUCUUUUUCUAUUAUUACAAGUACCCACCCCUAAAGCUAUGCAAUCAUAGCCACCCGAUGAAUCCUUUAACAGGGCAGGGGUAAAACAUCAGCCAGACUGGUCCCUUAUCUUAUGCGUCGCCAUUCAAUUGCCGCGUAUAAAACCGGCGAUGACCUAUUCCUUUAAGGGAGGGUGUGUACCCAGCCCGCUGUGACGCCUGCCUCACCGUAUAAGAUCAGCCAGUGUUAUCGCAUGUGGUUUCUGUAAAAUGUAUUACGACCGUUUUCUUACGGGUAUCCGCUCAGUAGUCAGGCUGCAGGUUAACUGUGCGCGCUGGUGGUCGCUUCUCCCCCAUGGCACUCCCGAGUUGCGACGCUCAACCACGACUGCUAAGUCCCCUCGGAUAGUGUCGUGUUUUAAGCUAUCGCGCCGCUCGGGGUCCCUGGCCUUAACUUUGGAACUUCGUGCCUUGUUUCAAAAUUACACAGAUAGAUUUGCGCACAUUUUCUAAUCAAGAUUAAGCCGACUACUACACCUCCCCAUAGAGUUAGUUGGUGUUAUGACCGCAAGGAUAAACUAAGCACACCGGUUCGGCGGGGAUGUAACAGAUUGCAGUGAUACCGCGUUUCCUGGAGCGAAUCUCGGUACGAAGUUGAAGAGGGCCGUGUCUGCACAGUGGGAUAAUGAUGGGGGCCUCUGCAUAACGCCAUCCUCUGAGGCUUCCAUAGUAAGG'
>>> DNA
'AGCACAAAGTCGGTGGGCACTTCAGTAAAACCCACTCCCCAAGAAGGAGCGAACGAATTGTCTATAAAGTCACTCCCTAAAACTTGTGATCTCAGGGGTGGGGATAGTGCCTAGCGATCCTCGTCGGATCCCGTAGTTGGAAGAGTATTCTGAGACTTCGAACCGCGCTCGGAAAAAGCCAAGACACCCTTACCGTAGGCCTGGATTTCATGCGAAGTTGAGCACATTACTTAGCATTAGCAAACAGTTCTTCGGATCTTTTTCTATTATTACAAGTACCCACCCCTAAAGCTATGCAATCATAGCCACCCGATGAATCCTTTAACAGGGCAGGGGTAAAACATCAGCCAGACTGGTCCCTTATCTTATGCGTCGCCATTCAATTGCCGCGTATAAAACCGGCGATGACCTATTCCTTTAAGGGAGGGTGTGTACCCAGCCCGCTGTGACGCCTGCCTCACCGTATAAGATCAGCCAGTGTTATCGCATGTGGTTTCTGTAAAATGTATTACGACCGTTTTCTTACGGGTATCCGCTCAGTAGTCAGGCTGCAGGTTAACTGTGCGCGCTGGTGGTCGCTTCTCCCCCATGGCACTCCCGAGTTGCGACGCTCAACCACGACTGCTAAGTCCCCTCGGATAGTGTCGTGTTTTAAGCTATCGCGCCGCTCGGGGTCCCTGGCCTTAACTTTGGAACTTCGTGCCTTGTTTCAAAATTACACAGATAGATTTGCGCACATTTTCTAATCAAGATTAAGCCGACTACTACACCTCCCCATAGAGTTAGTTGGTGTTATGACCGCAAGGATAAACTAAGCACACCGGTTCGGCGGGGATGTAACAGATTGCAGTGATACCGCGTTTCCTGGAGCGAATCTCGGTACGAAGTTGAAGAGGGCCGTGTCTGCACAGTGGGATAATGATGGGGGCCTCTGCATAACGCCATCCTCTGAGGCTTCCATAGTAAGG'
>>> m_rna_seq = DNA.replace(’T’,’U’)
  File "<stdin>", line 1
    m_rna_seq = DNA.replace(’T’,’U’)
                              ^
SyntaxError: invalid character in identifier
>>> m_rna_seq = DNA.replace('T','U')
>>> m_rna_seq
'AGCACAAAGUCGGUGGGCACUUCAGUAAAACCCACUCCCCAAGAAGGAGCGAACGAAUUGUCUAUAAAGUCACUCCCUAAAACUUGUGAUCUCAGGGGUGGGGAUAGUGCCUAGCGAUCCUCGUCGGAUCCCGUAGUUGGAAGAGUAUUCUGAGACUUCGAACCGCGCUCGGAAAAAGCCAAGACACCCUUACCGUAGGCCUGGAUUUCAUGCGAAGUUGAGCACAUUACUUAGCAUUAGCAAACAGUUCUUCGGAUCUUUUUCUAUUAUUACAAGUACCCACCCCUAAAGCUAUGCAAUCAUAGCCACCCGAUGAAUCCUUUAACAGGGCAGGGGUAAAACAUCAGCCAGACUGGUCCCUUAUCUUAUGCGUCGCCAUUCAAUUGCCGCGUAUAAAACCGGCGAUGACCUAUUCCUUUAAGGGAGGGUGUGUACCCAGCCCGCUGUGACGCCUGCCUCACCGUAUAAGAUCAGCCAGUGUUAUCGCAUGUGGUUUCUGUAAAAUGUAUUACGACCGUUUUCUUACGGGUAUCCGCUCAGUAGUCAGGCUGCAGGUUAACUGUGCGCGCUGGUGGUCGCUUCUCCCCCAUGGCACUCCCGAGUUGCGACGCUCAACCACGACUGCUAAGUCCCCUCGGAUAGUGUCGUGUUUUAAGCUAUCGCGCCGCUCGGGGUCCCUGGCCUUAACUUUGGAACUUCGUGCCUUGUUUCAAAAUUACACAGAUAGAUUUGCGCACAUUUUCUAAUCAAGAUUAAGCCGACUACUACACCUCCCCAUAGAGUUAGUUGGUGUUAUGACCGCAAGGAUAAACUAAGCACACCGGUUCGGCGGGGAUGUAACAGAUUGCAGUGAUACCGCGUUUCCUGGAGCGAAUCUCGGUACGAAGUUGAAGAGGGCCGUGUCUGCACAGUGGGAUAAUGAUGGGGGCCUCUGCAUAACGCCAUCCUCUGAGGCUUCCAUAGUAAGG'
>>> if m_rna_seq === RNA ? True : False
  File "<stdin>", line 1
    if m_rna_seq === RNA ? True : False
                   ^
SyntaxError: invalid syntax
>>> if m_rna_seq == RNA ? True : False
  File "<stdin>", line 1
    if m_rna_seq == RNA ? True : False
                        ^
SyntaxError: invalid syntax
>>> m_rna_seq == RNA
True
>>> new_dna = 'aCgAAGTTGAAGAGGGCCGTGTCtgCACAGTGGGATAATGATGGGgGCCTCTGCATAACGcCATCCTCTGAGGCTTCcATAGtAAGG'
>>> new_dna = new_dna.upper()
>>> new_dna
'ACGAAGTTGAAGAGGGCCGTGTCTGCACAGTGGGATAATGATGGGGGCCTCTGCATAACGCCATCCTCTGAGGCTTCCATAGTAAGG'
>>> new_rna = new_dna.replace('T','U')
>>> new_rna
'ACGAAGUUGAAGAGGGCCGUGUCUGCACAGUGGGAUAAUGAUGGGGGCCUCUGCAUAACGCCAUCCUCUGAGGCUUCCAUAGUAAGG'
>>> orig_dna = 'ACGAAGTTGAAGAGGGCCGTGTCTGCACAGTGGGATAATGATGGGGGCCTCTGCATAACGCCATCCTCTGAGGCTTCCATAGTAAGG'
>>> orig_rna = orig_dna.replace('T','U')
>>> orig_rna = new_rna
>>> orig_dna = 'ACGAAGTTGAAGAGGGCCGTGTCTGCACAGTGGGATAATGATGGGGGCCTCTGCATAACGCCATCCTCTGAGGCTTCCATAGTAAGG'
>>> orig_rna = orig_dna.replace('T','U')
>>> orig_rna == new_rna
True
>>> complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'};
>>> rc_dna = ''
>>> dna = 'TGTGGTAGATGCGTTAAGCAGTGGAGAATCCTATGCTGTAGAGACCCTCGGTCTCACGATAAGTGCGCGGTATCCATTGTTCCGTCTGACCGCAAATAACTTGTAGGCTAAAACACGATTTTAGCATATTGTTTTGACTTTCCTAACCTCGGCAGCCAGGTCCGGCATGTTTTTTGCCACCTCTGGATCACAACACGCAGACCCCGTGCTTTGCCATCGCCTGACGCAGGATCAAAGACGCAAGAGGTCAAATGTGGCCCTTAGTACAGTTGTAGTCGTCATTGACAGTCCTTTTAGTGTACAGTAAGGGTGGGGTCAGCTGGTATATCCCTGTTATCTAAAGATCTTGGATCGCGAGCCAGGTTTACGCGCAACTGTTTCTCCTTGTGTATCTTGCGGGATAAGCCCCAGGAGCCATCAAGTCTCGCGAGTAGGTCTGGCTGAGCGAATACTCAACAGCGCGTTGGCTGGCCTACAACACATGGAGAATTGGATAAGTTTCTATGGCACCGAAGTTATCACGAGCAATTTTCAGCCCATGCGGGTCTCTCATACGCGCATGGAGTTTGTCCGACGGGTCGCTCGCTAAGTTGTCGCTACGCTCACTCCCAACTTGAGGTTCGAGAGCAGTCACAAACGGCCACTTATGGTCGTATCGTGGATTCTGACGGTTGCTACTTTCCTCATGAGGATCACCGGGGCGCGATGCGACGACGAATTCCATTTAGTTGTATCCTACTGGTACCCAATGATTGTTTGGATTCTTCTCTCTCACTACGCATCTCGTTTATTTGCTTTATACGTACTGGGATTGGTACAGAACTGACCTAGCTTGAGGTTGATTGTCTCACGCTTTCGGCATGGCCACATAAAACATCAGTACCGATACTGGTCGAACTTGTACACGAACATATGTGTCCGTAATAAATACCCCTGATGTATATT
  File "<stdin>", line 1
    dna = 'TGTGGTAGATGCGTTAAGCAGTGGAGAATCCTATGCTGTAGAGACCCTCGGTCTCACGATAAGTGCGCGGTATCCATTGTTCCGTCTGACCGCAAATAACTTGTAGGCTAAAACACGATTTTAGCATATTGTTTTGACTTTCCTAACCTCGGCAGCCAGGTCCGGCATGTTTTTTGCCACCTCTGGATCACAACACGCAGACCCCGTGCTTTGCCATCGCCTGACGCAGGATCAAAGACGCAAGAGGTCAAATGTGGCCCTTAGTACAGTTGTAGTCGTCATTGACAGTCCTTTTAGTGTACAGTAAGGGTGGGGTCAGCTGGTATATCCCTGTTATCTAAAGATCTTGGATCGCGAGCCAGGTTTACGCGCAACTGTTTCTCCTTGTGTATCTTGCGGGATAAGCCCCAGGAGCCATCAAGTCTCGCGAGTAGGTCTGGCTGAGCGAATACTCAACAGCGCGTTGGCTGGCCTACAACACATGGAGAATTGGATAAGTTTCTATGGCACCGAAGTTATCACGAGCAATTTTCAGCCCATGCGGGTCTCTCATACGCGCATGGAGTTTGTCCGACGGGTCGCTCGCTAAGTTGTCGCTACGCTCACTCCCAACTTGAGGTTCGAGAGCAGTCACAAACGGCCACTTATGGTCGTATCGTGGATTCTGACGGTTGCTACTTTCCTCATGAGGATCACCGGGGCGCGATGCGACGACGAATTCCATTTAGTTGTATCCTACTGGTACCCAATGATTGTTTGGATTCTTCTCTCTCACTACGCATCTCGTTTATTTGCTTTATACGTACTGGGATTGGTACAGAACTGACCTAGCTTGAGGTTGATTGTCTCACGCTTTCGGCATGGCCACATAAAACATCAGTACCGATACTGGTCGAACTTGTACACGAACATATGTGTCCGTAATAAATACCCCTGATGTATATT
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ^
SyntaxError: EOL while scanning string literal
>>> dna = 'TGTGGTAGATGCGTTAAGCAGTGGAGAATCCTATGCTGTAGAGACCCTCGGTCTCACGATAAGTGCGCGGTATCCATTGTTCCGTCTGACCGCAAATAACTTGTAGGCTAAAACACGATTTTAGCATATTGTTTTGACTTTCCTAACCTCGGCAGCCAGGTCCGGCATGTTTTTTGCCACCTCTGGATCACAACACGCAGACCCCGTGCTTTGCCATCGCCTGACGCAGGATCAAAGACGCAAGAGGTCAAATGTGGCCCTTAGTACAGTTGTAGTCGTCATTGACAGTCCTTTTAGTGTACAGTAAGGGTGGGGTCAGCTGGTATATCCCTGTTATCTAAAGATCTTGGATCGCGAGCCAGGTTTACGCGCAACTGTTTCTCCTTGTGTATCTTGCGGGATAAGCCCCAGGAGCCATCAAGTCTCGCGAGTAGGTCTGGCTGAGCGAATACTCAACAGCGCGTTGGCTGGCCTACAACACATGGAGAATTGGATAAGTTTCTATGGCACCGAAGTTATCACGAGCAATTTTCAGCCCATGCGGGTCTCTCATACGCGCATGGAGTTTGTCCGACGGGTCGCTCGCTAAGTTGTCGCTACGCTCACTCCCAACTTGAGGTTCGAGAGCAGTCACAAACGGCCACTTATGGTCGTATCGTGGATTCTGACGGTTGCTACTTTCCTCATGAGGATCACCGGGGCGCGATGCGACGACGAATTCCATTTAGTTGTATCCTACTGGTACCCAATGATTGTTTGGATTCTTCTCTCTCACTACGCATCTCGTTTATTTGCTTTATACGTACTGGGATTGGTACAGAACTGACCTAGCTTGAGGTTGATTGTCTCACGCTTTCGGCATGGCCACATAAAACATCAGTACCGATACTGGTCGAACTTGTACACGAACATATGTGTCCGTAATAAATACCCCTGATGTATATT'
>>> rc_dna.join([complement[base] for base in dna[::-1]]);
'AATATACATCAGGGGTATTTATTACGGACACATATGTTCGTGTACAAGTTCGACCAGTATCGGTACTGATGTTTTATGTGGCCATGCCGAAAGCGTGAGACAATCAACCTCAAGCTAGGTCAGTTCTGTACCAATCCCAGTACGTATAAAGCAAATAAACGAGATGCGTAGTGAGAGAGAAGAATCCAAACAATCATTGGGTACCAGTAGGATACAACTAAATGGAATTCGTCGTCGCATCGCGCCCCGGTGATCCTCATGAGGAAAGTAGCAACCGTCAGAATCCACGATACGACCATAAGTGGCCGTTTGTGACTGCTCTCGAACCTCAAGTTGGGAGTGAGCGTAGCGACAACTTAGCGAGCGACCCGTCGGACAAACTCCATGCGCGTATGAGAGACCCGCATGGGCTGAAAATTGCTCGTGATAACTTCGGTGCCATAGAAACTTATCCAATTCTCCATGTGTTGTAGGCCAGCCAACGCGCTGTTGAGTATTCGCTCAGCCAGACCTACTCGCGAGACTTGATGGCTCCTGGGGCTTATCCCGCAAGATACACAAGGAGAAACAGTTGCGCGTAAACCTGGCTCGCGATCCAAGATCTTTAGATAACAGGGATATACCAGCTGACCCCACCCTTACTGTACACTAAAAGGACTGTCAATGACGACTACAACTGTACTAAGGGCCACATTTGACCTCTTGCGTCTTTGATCCTGCGTCAGGCGATGGCAAAGCACGGGGTCTGCGTGTTGTGATCCAGAGGTGGCAAAAAACATGCCGGACCTGGCTGCCGAGGTTAGGAAAGTCAAAACAATATGCTAAAATCGTGTTTTAGCCTACAAGTTATTTGCGGTCAGACGGAACAATGGATACCGCGCACTTATCGTGAGACCGAGGGTCTCTACAGCATAGGATTCTCCACTGCTTAACGCATCTACCACA'
>>> c = 876**2 + 830**2
>>> c
1456276
>>> word = 'iSKHirundo225te1BZrBGF7vtHIk3aVsgzgh0tOAmrfd0N7yV7Nm3SxuS43hgnaCB0xQjktaa8st8AVJIwmScKKquOKZ1LLngsNj06t5cFBAEw1L9YGEVKvi1bY9bHMwMXaSzzJC0ZEY0zFdJBxba7d17qWd6SpMjzAljTUk09vARsuH7QxAcaudicinctusOQa.'
>>> len(word)
196
>>> word[3:10]
'Hirundo'
>>> word[180:192]
'caudicinctus'
>>> new = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'
>>> new[22:28]
'Humpty'
>>> for i in range(4653, 9302):
...     if i % 2 == 1:
...             sum += i
... print(sum)
  File "<stdin>", line 4
    print(sum)
        ^
SyntaxError: invalid syntax
>>> sum = 0
>>> for i in range(4653, 9302):
...     if i % 2 == 1:
...             sum += i
... print(sum)
  File "<stdin>", line 4
    print(sum)
        ^
SyntaxError: invalid syntax
>>> for i in range(4653, 9302):
...     if i % 2 == 1:
...             sum += i
... sum
  File "<stdin>", line 4
    sum
      ^
SyntaxError: invalid syntax
>>> for i in range(4653, 9302):
...     if i % 2 == 1:
...             sum += i
... return sum
  File "<stdin>", line 4
    return sum
         ^
SyntaxError: invalid syntax
>>> for i in range(4653, 9302):
...     if i % 2 == 1:
...             sum += i
... 
>>> sum
16221525
>>> f = open("users/mac/Downloads/rosalind_ini5.txt", "r")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'users/mac/Downloads/rosalind_ini5.txt'
>>> f = open("/Users/mac/Downloads/rosalind_ini5.txt", "r")
>>> f = open("/Users/mac/Downloads/rosalind_ini5.txt", "r")
>>> for x in f:
...     if x % 2 == 0:
...             print(x)
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: not all arguments converted during string formatting
>>> f
<_io.TextIOWrapper name='/Users/mac/Downloads/rosalind_ini5.txt' mode='r' encoding='UTF-8'>
>>> for x in f:
...     print(x)
... 
Some things in life are bad, they can really make you mad

  Did gyre and gimble in the wabe:

Other things just make you swear and curse

All mimsy were the borogoves,

When you're chewing on life's gristle, don't grumble give a whistle

  And the mome raths outgrabe.

This will help things turn out for the best

"Beware the Jabberwock, my son!

Always look on the bright side of life

  The jaws that bite, the claws that catch!

Always look on the right side of life

Beware the Jubjub bird, and shun

If life seems jolly rotten, there's something you've forgotten

  The frumious Bandersnatch!"

And that's to laugh and smile and dance and sing

He took his vorpal sword in hand:

When you're feeling in the dumps, don't be silly, chumps

  Long time the manxome foe he sought --

Just purse your lips and whistle, that's the thing

So rested he by the Tumtum tree,

So, always look on the bright side of death

  And stood awhile in thought.

Just before you draw your terminal breath

And, as in uffish thought he stood,

Life's a counterfeit and when you look at it

  The Jabberwock, with eyes of flame,

Life's a laugh and death's the joke, it's true

Came whiffling through the tulgey wood,

You see, it's all a show, keep them laughing as you go

  And burbled as it came!

Just remember the last laugh is on you

One, two! One, two! And through and through

Always look on the bright side of life

  The vorpal blade went snicker-snack!

And always look on the right side of life

He left it dead, and with its head

Always look on the bright side of life

  He went galumphing back.

And always look on the right side of life

>>> for x in f:
...     if (
... 
... 
... 
KeyboardInterrupt
>>> for i in f:
...     if (i+1) % 
KeyboardInterrupt
>>> len(f)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type '_io.TextIOWrapper' has no len()
>>> f
<_io.TextIOWrapper name='/Users/mac/Downloads/rosalind_ini5.txt' mode='r' encoding='UTF-8'>
>>> f = open("/Users/mac/Downloads/rosalind_ini5.txt", "r")
>>> f
<_io.TextIOWrapper name='/Users/mac/Downloads/rosalind_ini5.txt' mode='r' encoding='UTF-8'>
>>> for x in f:
...     if (x + 1) % 2 == 1:
...             print(x)
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: can only concatenate str (not "int") to str
>>> D = 10
>>> for x in D:
...     print(x)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> num = 0
>>> for x in f:
...     if (num + 1) % 2 == 1:
...             print(x)
... 
Some things in life are bad, they can really make you mad

  Did gyre and gimble in the wabe:

Other things just make you swear and curse

All mimsy were the borogoves,

When you're chewing on life's gristle, don't grumble give a whistle

  And the mome raths outgrabe.

This will help things turn out for the best

"Beware the Jabberwock, my son!

Always look on the bright side of life

  The jaws that bite, the claws that catch!

Always look on the right side of life

Beware the Jubjub bird, and shun

If life seems jolly rotten, there's something you've forgotten

  The frumious Bandersnatch!"

And that's to laugh and smile and dance and sing

He took his vorpal sword in hand:

When you're feeling in the dumps, don't be silly, chumps

  Long time the manxome foe he sought --

Just purse your lips and whistle, that's the thing

So rested he by the Tumtum tree,

So, always look on the bright side of death

  And stood awhile in thought.

Just before you draw your terminal breath

And, as in uffish thought he stood,

Life's a counterfeit and when you look at it

  The Jabberwock, with eyes of flame,

Life's a laugh and death's the joke, it's true

Came whiffling through the tulgey wood,

You see, it's all a show, keep them laughing as you go

  And burbled as it came!

Just remember the last laugh is on you

One, two! One, two! And through and through

Always look on the bright side of life

  The vorpal blade went snicker-snack!

And always look on the right side of life

He left it dead, and with its head

Always look on the bright side of life

  He went galumphing back.

And always look on the right side of life

>>> 0 % 2 == 0
True
>>> for x+2 in f:
...     print(x+2)
... 
  File "<stdin>", line 1
SyntaxError: can't assign to operator
>>> for x in f:
...     if 'NR%2==0':
...             print(x)
... 
>>> for x in f:
...     print(x)
... 
>>> 
>>> f = open("/Users/mac/Downloads/rosalind_ini5.txt", "r")
>>> for x in f:
...     print(x)
... 
`Twas brillig, and the slithy toves

Some things in life are bad, they can really make you mad

  Did gyre and gimble in the wabe:

Other things just make you swear and curse

All mimsy were the borogoves,

When you're chewing on life's gristle, don't grumble give a whistle

  And the mome raths outgrabe.

This will help things turn out for the best

"Beware the Jabberwock, my son!

Always look on the bright side of life

  The jaws that bite, the claws that catch!

Always look on the right side of life

Beware the Jubjub bird, and shun

If life seems jolly rotten, there's something you've forgotten

  The frumious Bandersnatch!"

And that's to laugh and smile and dance and sing

He took his vorpal sword in hand:

When you're feeling in the dumps, don't be silly, chumps

  Long time the manxome foe he sought --

Just purse your lips and whistle, that's the thing

So rested he by the Tumtum tree,

So, always look on the bright side of death

  And stood awhile in thought.

Just before you draw your terminal breath

And, as in uffish thought he stood,

Life's a counterfeit and when you look at it

  The Jabberwock, with eyes of flame,

Life's a laugh and death's the joke, it's true

Came whiffling through the tulgey wood,

You see, it's all a show, keep them laughing as you go

  And burbled as it came!

Just remember the last laugh is on you

One, two! One, two! And through and through

Always look on the bright side of life

  The vorpal blade went snicker-snack!

And always look on the right side of life

He left it dead, and with its head

Always look on the bright side of life

  He went galumphing back.

And always look on the right side of life

>>> for x in f:
...     if 'NR%2==0':
...             print(x)
... 
>>> 
>>> for x in f:
...     if x % 2 == 0:
...             print(x)
... 
>>> 
>>> 
>>> f = open("/Users/mac/Downloads/rosalind_ini5.txt", "r")
>>> for x in f:
...     if x % 2 == 0:
...             print(x)
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: not all arguments converted during string formatting
>>> for x in f:
...     if int(x) % 2 == 0:
...             print(x)
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: invalid literal for int() with base 10: 'Some things in life are bad, they can really make you mad\n'
>>> cont = fn.readlines() 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fn' is not defined
>>> cont = f.readlines() 
>>> cont = fn.readlines() 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fn' is not defined
>>> type(cont) 
<class 'list'>
>>> cont
['  Did gyre and gimble in the wabe:\n', 'Other things just make you swear and curse\n', 'All mimsy were the borogoves,\n', "When you're chewing on life's gristle, don't grumble give a whistle\n", '  And the mome raths outgrabe.\n', 'This will help things turn out for the best\n', '"Beware the Jabberwock, my son!\n', 'Always look on the bright side of life\n', '  The jaws that bite, the claws that catch!\n', 'Always look on the right side of life\n', 'Beware the Jubjub bird, and shun\n', "If life seems jolly rotten, there's something you've forgotten\n", '  The frumious Bandersnatch!"\n', "And that's to laugh and smile and dance and sing\n", 'He took his vorpal sword in hand:\n', "When you're feeling in the dumps, don't be silly, chumps\n", '  Long time the manxome foe he sought --\n', "Just purse your lips and whistle, that's the thing\n", 'So rested he by the Tumtum tree,\n', 'So, always look on the bright side of death\n', '  And stood awhile in thought.\n', 'Just before you draw your terminal breath\n', 'And, as in uffish thought he stood,\n', "Life's a counterfeit and when you look at it\n", '  The Jabberwock, with eyes of flame,\n', "Life's a laugh and death's the joke, it's true\n", 'Came whiffling through the tulgey wood,\n', "You see, it's all a show, keep them laughing as you go\n", '  And burbled as it came!\n', 'Just remember the last laugh is on you\n', 'One, two! One, two! And through and through\n', 'Always look on the bright side of life\n', '  The vorpal blade went snicker-snack!\n', 'And always look on the right side of life\n', 'He left it dead, and with its head\n', 'Always look on the bright side of life\n', '  He went galumphing back.\n', 'And always look on the right side of life\n']
>>> len(cont)
38
>>> for x in f:
...     print(x)
... 
>>> 
>>> f = open("/Users/mac/Downloads/rosalind_ini5.txt", "r")
>>> for x in range(1, len(cont) + 1):
...     if x % 2 == 0:
...             print(x)
... 
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
>>> for x in range(1, len(cont) + 1):
...     if x % 2 == 0:
...             print(cont[x])
... 
All mimsy were the borogoves,

  And the mome raths outgrabe.

"Beware the Jabberwock, my son!

  The jaws that bite, the claws that catch!

Beware the Jubjub bird, and shun

  The frumious Bandersnatch!"

He took his vorpal sword in hand:

  Long time the manxome foe he sought --

So rested he by the Tumtum tree,

  And stood awhile in thought.

And, as in uffish thought he stood,

  The Jabberwock, with eyes of flame,

Came whiffling through the tulgey wood,

  And burbled as it came!

One, two! One, two! And through and through

  The vorpal blade went snicker-snack!

He left it dead, and with its head

  He went galumphing back.

Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
IndexError: list index out of range
>>> len(cont) + 1
39
>>> for x in range(1, len(cont) + 1):
...     if x % 2 == 0:
...             print(cont[x])
... 
All mimsy were the borogoves,

  And the mome raths outgrabe.

"Beware the Jabberwock, my son!

  The jaws that bite, the claws that catch!

Beware the Jubjub bird, and shun

  The frumious Bandersnatch!"

He took his vorpal sword in hand:

  Long time the manxome foe he sought --

So rested he by the Tumtum tree,

  And stood awhile in thought.

And, as in uffish thought he stood,

  The Jabberwock, with eyes of flame,

Came whiffling through the tulgey wood,

  And burbled as it came!

One, two! One, two! And through and through

  The vorpal blade went snicker-snack!

He left it dead, and with its head

  He went galumphing back.

Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
IndexError: list index out of range
>>> for x in range(1, len(cont)):
...     if x % 2 == 0:
...             print(cont[x])
... 
All mimsy were the borogoves,

  And the mome raths outgrabe.

"Beware the Jabberwock, my son!

  The jaws that bite, the claws that catch!

Beware the Jubjub bird, and shun

  The frumious Bandersnatch!"

He took his vorpal sword in hand:

  Long time the manxome foe he sought --

So rested he by the Tumtum tree,

  And stood awhile in thought.

And, as in uffish thought he stood,

  The Jabberwock, with eyes of flame,

Came whiffling through the tulgey wood,

  And burbled as it came!

One, two! One, two! And through and through

  The vorpal blade went snicker-snack!

He left it dead, and with its head

  He went galumphing back.

>>> f = open("/Users/mac/Downloads/rosalind_ini5.txt", "r")
>>> f
<_io.TextIOWrapper name='/Users/mac/Downloads/rosalind_ini5.txt' mode='r' encoding='UTF-8'>
>>> for x in f:
...     print(x)
... 
`Twas brillig, and the slithy toves

Some things in life are bad, they can really make you mad

  Did gyre and gimble in the wabe:

Other things just make you swear and curse

All mimsy were the borogoves,

When you're chewing on life's gristle, don't grumble give a whistle

  And the mome raths outgrabe.

This will help things turn out for the best

"Beware the Jabberwock, my son!

Always look on the bright side of life

  The jaws that bite, the claws that catch!

Always look on the right side of life

Beware the Jubjub bird, and shun

If life seems jolly rotten, there's something you've forgotten

  The frumious Bandersnatch!"

And that's to laugh and smile and dance and sing

He took his vorpal sword in hand:

When you're feeling in the dumps, don't be silly, chumps

  Long time the manxome foe he sought --

Just purse your lips and whistle, that's the thing

So rested he by the Tumtum tree,

So, always look on the bright side of death

  And stood awhile in thought.

Just before you draw your terminal breath

And, as in uffish thought he stood,

Life's a counterfeit and when you look at it

  The Jabberwock, with eyes of flame,

Life's a laugh and death's the joke, it's true

Came whiffling through the tulgey wood,

You see, it's all a show, keep them laughing as you go

  And burbled as it came!

Just remember the last laugh is on you

One, two! One, two! And through and through

Always look on the bright side of life

  The vorpal blade went snicker-snack!

And always look on the right side of life

He left it dead, and with its head

Always look on the bright side of life

  He went galumphing back.

And always look on the right side of life

>>> for x in range(1, len(cont)):
...     if x % 2 == 0:
...             print(cont[x])
... 
All mimsy were the borogoves,

  And the mome raths outgrabe.

"Beware the Jabberwock, my son!

  The jaws that bite, the claws that catch!

Beware the Jubjub bird, and shun

  The frumious Bandersnatch!"

He took his vorpal sword in hand:

  Long time the manxome foe he sought --

So rested he by the Tumtum tree,

  And stood awhile in thought.

And, as in uffish thought he stood,

  The Jabberwock, with eyes of flame,

Came whiffling through the tulgey wood,

  And burbled as it came!

One, two! One, two! And through and through

  The vorpal blade went snicker-snack!

He left it dead, and with its head

  He went galumphing back.

>>> for x in f:
...     print(x)
...     
... 
>>> 
>>> for x in f:
...     print(x)
... 
>>> f = open("/Users/mac/Downloads/rosalind_ini5.txt", "r")
>>> for x in f:
...     print(x)
... 
`Twas brillig, and the slithy toves

Some things in life are bad, they can really make you mad

  Did gyre and gimble in the wabe:

Other things just make you swear and curse

All mimsy were the borogoves,

When you're chewing on life's gristle, don't grumble give a whistle

  And the mome raths outgrabe.

This will help things turn out for the best

"Beware the Jabberwock, my son!

Always look on the bright side of life

  The jaws that bite, the claws that catch!

Always look on the right side of life

Beware the Jubjub bird, and shun

If life seems jolly rotten, there's something you've forgotten

  The frumious Bandersnatch!"

And that's to laugh and smile and dance and sing

He took his vorpal sword in hand:

When you're feeling in the dumps, don't be silly, chumps

  Long time the manxome foe he sought --

Just purse your lips and whistle, that's the thing

So rested he by the Tumtum tree,

So, always look on the bright side of death

  And stood awhile in thought.

Just before you draw your terminal breath

And, as in uffish thought he stood,

Life's a counterfeit and when you look at it

  The Jabberwock, with eyes of flame,

Life's a laugh and death's the joke, it's true

Came whiffling through the tulgey wood,

You see, it's all a show, keep them laughing as you go

  And burbled as it came!

Just remember the last laugh is on you

One, two! One, two! And through and through

Always look on the bright side of life

  The vorpal blade went snicker-snack!

And always look on the right side of life

He left it dead, and with its head

Always look on the bright side of life

  He went galumphing back.

And always look on the right side of life

>>> cont = f.readlines() 
>>> cont
[]
>>> print(cont)
[]
>>> f = open("/Users/mac/Downloads/rosalind_ini5.txt", "r")
>>> cont = f.readlines() 
>>> type(cont)
<class 'list'>
>>> cont
['`Twas brillig, and the slithy toves\n', 'Some things in life are bad, they can really make you mad\n', '  Did gyre and gimble in the wabe:\n', 'Other things just make you swear and curse\n', 'All mimsy were the borogoves,\n', "When you're chewing on life's gristle, don't grumble give a whistle\n", '  And the mome raths outgrabe.\n', 'This will help things turn out for the best\n', '"Beware the Jabberwock, my son!\n', 'Always look on the bright side of life\n', '  The jaws that bite, the claws that catch!\n', 'Always look on the right side of life\n', 'Beware the Jubjub bird, and shun\n', "If life seems jolly rotten, there's something you've forgotten\n", '  The frumious Bandersnatch!"\n', "And that's to laugh and smile and dance and sing\n", 'He took his vorpal sword in hand:\n', "When you're feeling in the dumps, don't be silly, chumps\n", '  Long time the manxome foe he sought --\n', "Just purse your lips and whistle, that's the thing\n", 'So rested he by the Tumtum tree,\n', 'So, always look on the bright side of death\n', '  And stood awhile in thought.\n', 'Just before you draw your terminal breath\n', 'And, as in uffish thought he stood,\n', "Life's a counterfeit and when you look at it\n", '  The Jabberwock, with eyes of flame,\n', "Life's a laugh and death's the joke, it's true\n", 'Came whiffling through the tulgey wood,\n', "You see, it's all a show, keep them laughing as you go\n", '  And burbled as it came!\n', 'Just remember the last laugh is on you\n', 'One, two! One, two! And through and through\n', 'Always look on the bright side of life\n', '  The vorpal blade went snicker-snack!\n', 'And always look on the right side of life\n', 'He left it dead, and with its head\n', 'Always look on the bright side of life\n', '  He went galumphing back.\n', 'And always look on the right side of life\n']
>>> cont[1]
'Some things in life are bad, they can really make you mad\n'
>>> cont[0]
'`Twas brillig, and the slithy toves\n'
>>> for x in range(0, len(cont)):
...     if(x % 2 == 1):
...             print(cont[x])
... 
Some things in life are bad, they can really make you mad

Other things just make you swear and curse

When you're chewing on life's gristle, don't grumble give a whistle

This will help things turn out for the best

Always look on the bright side of life

Always look on the right side of life

If life seems jolly rotten, there's something you've forgotten

And that's to laugh and smile and dance and sing

When you're feeling in the dumps, don't be silly, chumps

Just purse your lips and whistle, that's the thing

So, always look on the bright side of death

Just before you draw your terminal breath

Life's a counterfeit and when you look at it

Life's a laugh and death's the joke, it's true

You see, it's all a show, keep them laughing as you go

Just remember the last laugh is on you

Always look on the bright side of life

And always look on the right side of life

Always look on the bright side of life

And always look on the right side of life

>>> 
>>> f = open("/Users/mac/Downloads/rosalind_ini5.txt", "r")
>>> cont = f.readlines() 
>>> for x in range(0, len(cont)):
...     if(x % 2 == 1):
...             print(cont[x])
... 
Some things in life are bad, they can really make you mad

Other things just make you swear and curse

When you're chewing on life's gristle, don't grumble give a whistle

This will help things turn out for the best

Always look on the bright side of life

Always look on the right side of life

If life seems jolly rotten, there's something you've forgotten

And that's to laugh and smile and dance and sing

When you're feeling in the dumps, don't be silly, chumps

Just purse your lips and whistle, that's the thing

So, always look on the bright side of death

Just before you draw your terminal breath

Life's a counterfeit and when you look at it

Life's a laugh and death's the joke, it's true

You see, it's all a show, keep them laughing as you go

Just remember the last laugh is on you

Always look on the bright side of life

And always look on the right side of life

Always look on the bright side of life

And always look on the right side of life

>>> 
str = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
>>> counts = dict()
>>> words = str.split()
>>> for word in words:
...         if word in counts:
...             counts[word] += 1
...         else:
...             counts[word] = 1
... 
>>> for count in counts:
...     print(count,counts[count])
... 
# Fibonacci sequence
>>> def fib_seq(n, k):
...     f1, f2, result = 1, 1, 0
...     for i in range(1, n + 1):
...         print(i)
...         # if i == f1 or i == f2:
...         if i == f1:
...             result = f1
...             print('The result is: ', result)
...             # pass
...         elif i == 2:
...             result = f2
...             print('The result is: ', result)
...         #     pass
...         elif i >= 3 :
...             result = f1 * k + f2
...             print('The result is: ', result)
...             f1 = f2
...             f2 = result
...     print('The result is: ', result)
...     return result
... 
>>> print(fib_seq(35, 5))