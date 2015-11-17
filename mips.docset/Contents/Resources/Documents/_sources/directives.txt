Directives
==========


.. mips:instructions:: .align

   Align next data item on specified byte boundary (0=byte, 1=half, 2=word, 3=double)




.. mips:instructions:: .ascii

   Store the string in the Data segment but do not add null terminator




.. mips:instructions:: .asciiz

   Store the string in the Data segment and add null terminator




.. mips:instructions:: .byte

   Store the listed value(s) as 8 bit bytes




.. mips:instructions:: .data

   Subsequent items stored in Data segment at next available address




.. mips:instructions:: .double

   Store the listed value(s) as double precision floating point




.. mips:instructions:: .end_macro

   End macro definition.  See .macro




.. mips:instructions:: .eqv

   Substitute second operand for first. First operand is symbol, second operand is expression (like #define)




.. mips:instructions:: .extern

   Declare the listed label and byte length to be a global data field




.. mips:instructions:: .float

   Store the listed value(s) as single precision floating point




.. mips:instructions:: .globl

   Declare the listed label(s) as global to enable referencing from other files




.. mips:instructions:: .half

   Store the listed value(s) as 16 bit halfwords on halfword boundary




.. mips:instructions:: .include

   Insert the contents of the specified file.  Put filename in quotes.




.. mips:instructions:: .kdata

   Subsequent items stored in Kernel Data segment at next available address




.. mips:instructions:: .ktext

   Subsequent items (instructions) stored in Kernel Text segment at next available address




.. mips:instructions:: .macro

   Begin macro definition.  See .end_macro




.. mips:instructions:: .set

   Set assembler variables.  Currently ignored but included for SPIM compatability




.. mips:instructions:: .space

   Reserve the next specified number of bytes in Data segment




.. mips:instructions:: .text

   Subsequent items (instructions) stored in Text segment at next available address




.. mips:instructions:: .word

   Store the listed value(s) as 32 bit words on word boundary


