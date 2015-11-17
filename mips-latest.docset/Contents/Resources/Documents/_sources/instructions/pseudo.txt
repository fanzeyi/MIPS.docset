Pseudo Instructions
===================


.. mips:instructions:: abs $t1, $t2

   ABSolute value : Set $t1 to absolute value of $t2 (algorithm from Hacker's Delight)

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: add $t1, $t2, -100

   ADDition : set $t1 to ($t2 plus 16-bit immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: add $t1, $t2, 100000

   ADDition : set $t1 to ($t2 plus 32-bit immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: addi $t1, $t2, 100000

   ADDition Immediate : set $t1 to ($t2 plus 32-bit immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: addiu $t1, $t2, 100000

   ADDition Immediate Unsigned: set $t1 to ($t2 plus 32-bit immediate), no overflow

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: addu $t1, $t2, 100000

   ADDition Unsigned : set $t1 to ($t2 plus 32-bit immediate), no overflow

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: and $t1, $t2, 100

   AND : set $t1 to ($t2 bitwise-AND 16-bit unsigned immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100: Parameter 2


.. mips:instructions:: and $t1, 100

   AND : set $t1 to ($t1 bitwise-AND 16-bit unsigned immediate)

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: andi $t1, $t2, 100000

   AND Immediate : set $t1 to ($t2 bitwise-AND 32-bit immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: andi $t1, 100

   AND Immediate : set $t1 to ($t1 bitwise-AND 16-bit unsigned immediate)

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: andi $t1, 100000

   AND Immediate : set $t1 to ($t1 bitwise-AND 32-bit immediate)

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: b label

   Branch : Branch to statement at label unconditionally

   :param label: Parameter 0


.. mips:instructions:: beq $t1, -100, label

   Branch if EQual : Branch to statement at label if $t1 is equal to 16-bit immediate

   :param $t1: Parameter 0
   :param -100: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: beq $t1, 100000, label

   Branch if EQual : Branch to statement at label if $t1 is equal to 32-bit immediate

   :param $t1: Parameter 0
   :param 100000: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: beqz $t1, label

   Branch if EQual Zero : Branch to statement at label if $t1 is equal to zero

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: bge $t1, $t2, label

   Branch if Greater or Equal : Branch to statement at label if $t1 is greater or equal to $t2

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bge $t1, -100, label

   Branch if Greater or Equal : Branch to statement at label if $t1 is greater or equal to 16-bit immediate

   :param $t1: Parameter 0
   :param -100: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bge $t1, 100000, label

   Branch if Greater or Equal : Branch to statement at label if $t1 is greater or equal to 32-bit immediate

   :param $t1: Parameter 0
   :param 100000: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bgeu $t1, $t2, label

   Branch if Greater or Equal Unsigned : Branch to statement at label if $t1 is greater or equal to $t2 (unsigned compare)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bgeu $t1, -100, label

   Branch if Greater or Equal Unsigned : Branch to statement at label if $t1 is greater or equal to 16-bit immediate (unsigned compare)

   :param $t1: Parameter 0
   :param -100: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bgeu $t1, 100000, label

   Branch if Greater or Equal Unsigned : Branch to statement at label if $t1 is greater or equal to 32-bit immediate (unsigned compare)

   :param $t1: Parameter 0
   :param 100000: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bgt $t1, $t2, label

   Branch if Greater Than : Branch to statement at label if $t1 is greater than $t2

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bgt $t1, -100, label

   Branch if Greater Than : Branch to statement at label if $t1 is greater than 16-bit immediate

   :param $t1: Parameter 0
   :param -100: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bgt $t1, 100000, label

   Branch if Greater Than : Branch to statement at label if $t1 is greater than 32-bit immediate

   :param $t1: Parameter 0
   :param 100000: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bgtu $t1, $t2, label

   Branch if Greater Than Unsigned: Branch to statement at label if $t1 is greater than $t2 (unsigned compare)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bgtu $t1, -100, label

   Branch if Greater Than Unsigned: Branch to statement at label if $t1 is greater than 16-bit immediate (unsigned compare)

   :param $t1: Parameter 0
   :param -100: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bgtu $t1, 100000, label

   Branch if Greater Than Unsigned: Branch to statement at label if $t1 is greater than 16-bit immediate (unsigned compare)

   :param $t1: Parameter 0
   :param 100000: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: ble $t1, $t2, label

   Branch if Less or Equal : Branch to statement at label if $t1 is less than or equal to $t2

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: ble $t1, -100, label

   Branch if Less or Equal : Branch to statement at label if $t1 is less than or equal to 16-bit immediate

   :param $t1: Parameter 0
   :param -100: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: ble $t1, 100000, label

   Branch if Less or Equal : Branch to statement at label if $t1 is less than or equal to 32-bit immediate

   :param $t1: Parameter 0
   :param 100000: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bleu $t1, $t2, label

   Branch if Less or Equal Unsigned : Branch to statement at label if $t1 is less than or equal to $t2 (unsigned compare)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bleu $t1, -100, label

   Branch if Less or Equal Unsigned : Branch to statement at label if $t1 is less than or equal to 16-bit immediate (unsigned compare)

   :param $t1: Parameter 0
   :param -100: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bleu $t1, 100000, label

   Branch if Less or Equal Unsigned : Branch to statement at label if $t1 is less than or equal to 32-bit immediate (unsigned compare)

   :param $t1: Parameter 0
   :param 100000: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: blt $t1, $t2, label

   Branch if Less Than : Branch to statement at label if $t1 is less than $t2

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: blt $t1, -100, label

   Branch if Less Than : Branch to statement at label if $t1 is less than 16-bit immediate

   :param $t1: Parameter 0
   :param -100: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: blt $t1, 100000, label

   Branch if Less Than : Branch to statement at label if $t1 is less than 32-bit immediate

   :param $t1: Parameter 0
   :param 100000: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bltu $t1, $t2, label

   Branch if Less Than Unsigned : Branch to statement at label if $t1 is less than $t2

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bltu $t1, -100, label

   Branch if Less Than Unsigned : Branch to statement at label if $t1 is less than 16-bit immediate

   :param $t1: Parameter 0
   :param -100: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bltu $t1, 100000, label

   Branch if Less Than Unsigned : Branch to statement at label if $t1 is less than 32-bit immediate

   :param $t1: Parameter 0
   :param 100000: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bne $t1, -100, label

   Branch if Not Equal : Branch to statement at label if $t1 is not equal to 16-bit immediate

   :param $t1: Parameter 0
   :param -100: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bne $t1, 100000, label

   Branch if Not Equal : Branch to statement at label if $t1 is not equal to 32-bit immediate

   :param $t1: Parameter 0
   :param 100000: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bnez $t1, label

   Branch if Not Equal Zero : Branch to statement at label if $t1 is not equal to zero

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: div $t1, $t2, $t3

   DIVision : Set $t1 to ($t2 divided by $t3, integer division)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: div $t1, $t2, -100

   DIVision : Set $t1 to ($t2 divided by 16-bit immediate, integer division)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: div $t1, $t2, 100000

   DIVision : Set $t1 to ($t2 divided by 32-bit immediate, integer division)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: divu $t1, $t2, $t3

   DIVision Unsigned :  Set $t1 to ($t2 divided by $t3, unsigned integer division)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: divu $t1, $t2, -100

   DIVision Unsigned :  Set $t1 to ($t2 divided by 16-bit immediate, unsigned integer division)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: divu $t1, $t2, 100000

   DIVision Unsigned :  Set $t1 to ($t2 divided by 32-bit immediate, unsigned integer division)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: l.d $f2, ($t2)

   Load floating point Double precision : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: l.d $f2, -100

   Load floating point Double precision : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: l.d $f2, 100000

   Load floating point Double precision : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: l.d $f2, 100000($t2)

   Load floating point Double precision : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: l.d $f2, label

   Load floating point Double precision : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: l.d $f2, label($t2)

   Load floating point Double precision : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: l.d $f2, label+100000

   Load floating point Double precision : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: l.d $f2, label+100000($t2

   )Load floating point Double precision : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param label+100000($t2: Parameter 1


.. mips:instructions:: l.s $f1, ($t2)

   Load floating point Single precision : Set $f1 to 32-bit value at effective memory word address

   :param $f1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: l.s $f1, -100

   Load floating point Single precision : Set $f1 to 32-bit value at effective memory word address

   :param $f1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: l.s $f1, 100000

   Load floating point Single precision : Set $f1 to 32-bit value at effective memory word address

   :param $f1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: l.s $f1, 100000($t2)

   Load floating point Single precision : Set $f1 to 32-bit value at effective memory word address

   :param $f1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: l.s $f1, label

   Load floating point Single precision : Set $f1 to 32-bit value at effective memory word address

   :param $f1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: l.s $f1, label($t2)

   Load floating point Single precision : Set $f1 to 32-bit value at effective memory word address

   :param $f1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: l.s $f1, label+100000

   Load floating point Single precision : Set $f1 to 32-bit value at effective memory word address

   :param $f1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: l.s $f1, label+100000($t2

   )Load floating point Single precision : Set $f1 to 32-bit value at effective memory word address

   :param $f1: Parameter 0
   :param label+100000($t2: Parameter 1


.. mips:instructions:: la $t1, ($t2)

   Load Address : Set $t1 to contents of $t2

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: la $t1, -100

   Load Address : Set $t1 to 16-bit immediate (sign-extended)

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: la $t1, 100

   Load Address : Set $t1 to 16-bit immediate (zero-extended)

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: la $t1, 100($t2)

   Load Address : Set $t1 to sum (of $t2 and 16-bit immediate)

   :param $t1: Parameter 0
   :param 100($t2): Parameter 1


.. mips:instructions:: la $t1, 100000

   Load Address : Set $t1 to 32-bit immediate

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: la $t1, 100000($t2)

   Load Address : Set $t1 to sum (of $t2 and 32-bit immediate)

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: la $t1, label

   Load Address : Set $t1 to label's address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: la $t1, label($t2)

   Load Address : Set $t1 to sum (of $t2 and label's address)

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: la $t1, label+100000

   Load Address : Set $t1 to sum (of label's address and 32-bit immediate)

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: la $t1, label+100000($t2)

   Load Address : Set $t1 to sum (of label's address, 32-bit immediate, and $t2)

   :param $t1: Parameter 0
   :param label+100000($t2): Parameter 1


.. mips:instructions:: lb $t1, ($t2)

   Load Byte : Set $t1 to sign-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: lb $t1, -100

   Load Byte : Set $t1 to sign-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: lb $t1, 100

   Load Byte : Set $t1 to sign-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: lb $t1, 100($t2)

   Load Byte : Set $t1 to sign-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param 100($t2): Parameter 1


.. mips:instructions:: lb $t1, 100000

   Load Byte : Set $t1 to sign-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: lb $t1, 100000($t2)

   Load Byte : Set $t1 to sign-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: lb $t1, label

   Load Byte : Set $t1 to sign-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: lb $t1, label($t2)

   Load Byte : Set $t1 to sign-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: lb $t1, label+100000

   Load Byte : Set $t1 to sign-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: lb $t1, label+100000($t2)

   Load Byte : Set $t1 to sign-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param label+100000($t2): Parameter 1


.. mips:instructions:: lbu $t1, ($t2)

   Load Byte Unsigned : Set $t1 to zero-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: lbu $t1, -100

   Load Byte Unsigned : Set $t1 to zero-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: lbu $t1, 100

   Load Byte Unsigned : Set $t1 to zero-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: lbu $t1, 100($t2)

   Load Byte Unsigned : Set $t1 to zero-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param 100($t2): Parameter 1


.. mips:instructions:: lbu $t1, 100000

   Load Byte Unsigned : Set $t1 to zero-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: lbu $t1, 100000($t2)

   Load Byte Unsigned : Set $t1 to zero-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: lbu $t1, label

   Load Byte Unsigned : Set $t1 to zero-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: lbu $t1, label($t2)

   Load Byte Unsigned : Set $t1 to zero-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: lbu $t1, label+100000

   Load Byte Unsigned : Set $t1 to zero-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: lbu $t1, label+100000($t2

   )Load Byte Unsigned : Set $t1 to zero-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param label+100000($t2: Parameter 1


.. mips:instructions:: ld $t1, ($t2)

   Load Doubleword : Set $t1 and the next register to the 64 bits starting at effective memory word address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: ld $t1, -100($t2)

   Load Doubleword : Set $t1 and the next register to the 64 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: ld $t1, 100000

   Load Doubleword : Set $t1 and the next register to the 64 bits starting at effective memory word address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: ld $t1, 100000($t2)

   Load Doubleword : Set $t1 and the next register to the 64 bits starting at effective memory word address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: ld $t1, label

   Load Doubleword : Set $t1 and the next register to the 64 bits starting at effective memory word address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: ld $t1, label($t2)

   Load Doubleword : Set $t1 and the next register to the 64 bits starting at effective memory word address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: ld $t1, label+100000

   Load Doubleword : Set $t1 and the next register to the 64 bits starting at effective memory word address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: ld $t1, label+100000($t2)

   Load Doubleword : Set $t1 and the next register to the 64 bits starting at effective memory word address

   :param $t1: Parameter 0
   :param label+100000($t2): Parameter 1


.. mips:instructions:: ldc1 $f2, ($t2)

   Load Doubleword Coprocessor 1 : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: ldc1 $f2, -100

   Load Doubleword Coprocessor 1 : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: ldc1 $f2, 100000

   Load Doubleword Coprocessor 1 : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: ldc1 $f2, 100000($t2)

   Load Doubleword Coprocessor 1 : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: ldc1 $f2, label

   Load Doubleword Coprocessor 1 : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: ldc1 $f2, label($t2)

   Load Doubleword Coprocessor 1 : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: ldc1 $f2, label+100000

   Load Doubleword Coprocessor 1 : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: ldc1 $f2, label+100000($t

   2)Load Doubleword Coprocessor 1 : Set $f2 and $f3 register pair to 64-bit value at effective memory doubleword address

   :param $f2: Parameter 0
   :param label+100000($t: Parameter 1


.. mips:instructions:: lh $t1, ($t2)

   Load Halfword : Set $t1 to sign-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: lh $t1, -100

   Load Halfword : Set $t1 to sign-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: lh $t1, 100

   Load Halfword : Set $t1 to sign-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: lh $t1, 100($t2)

   Load Halfword : Set $t1 to sign-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param 100($t2): Parameter 1


.. mips:instructions:: lh $t1, 100000

   Load Halfword : Set $t1 to sign-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: lh $t1, 100000($t2)

   Load Halfword : Set $t1 to sign-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: lh $t1, label

   Load Halfword : Set $t1 to sign-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: lh $t1, label($t2)

   Load Halfword : Set $t1 to sign-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: lh $t1, label+100000

   Load Halfword : Set $t1 to sign-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: lh $t1, label+100000($t2)

   Load Halfword : Set $t1 to sign-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param label+100000($t2): Parameter 1


.. mips:instructions:: lhu $t1, ($t2)

   Load Halfword Unsigned : Set $t1 to zero-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: lhu $t1, -100

   Load Halfword Unsigned : Set $t1 to zero-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: lhu $t1, 100

   Load Halfword Unsigned : Set $t1 to zero-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: lhu $t1, 100($t2)

   Load Halfword Unsigned : Set $t1 to zero-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param 100($t2): Parameter 1


.. mips:instructions:: lhu $t1, 100000

   Load Halfword Unsigned : Set $t1 to zero-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: lhu $t1, 100000($t2)

   Load Halfword Unsigned : Set $t1 to zero-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: lhu $t1, label

   Load Halfword Unsigned : Set $t1 to zero-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: lhu $t1, label($t2)

   Load Halfword Unsigned : Set $t1 to zero-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: lhu $t1, label+100000

   Load Halfword Unsigned : Set $t1 to zero-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: lhu $t1, label+100000($t2

   )Load Halfword Unsigned : Set $t1 to zero-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param label+100000($t2: Parameter 1


.. mips:instructions:: li $t1, -100

   Load Immediate : Set $t1 to 16-bit immediate (sign-extended)

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: li $t1, 100

   Load Immediate : Set $t1 to unsigned 16-bit immediate (zero-extended)

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: li $t1, 100000

   Load Immediate : Set $t1 to 32-bit immediate

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: ll $t1, ($t2)

   Load Linked : Paired with Store Conditional (sc) to perform atomic read-modify-write.  Treated as equivalent to Load Word (lw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: ll $t1, -100

   Load Linked : Paired with Store Conditional (sc) to perform atomic read-modify-write.  Treated as equivalent to Load Word (lw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: ll $t1, 100

   Load Linked : Paired with Store Conditional (sc) to perform atomic read-modify-write.  Treated as equivalent to Load Word (lw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: ll $t1, 100($t2)

   Load Linked : Paired with Store Conditional (sc) to perform atomic read-modify-write.  Treated as equivalent to Load Word (lw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param 100($t2): Parameter 1


.. mips:instructions:: ll $t1, 100000

   Load Linked : Paired with Store Conditional (sc) to perform atomic read-modify-write.  Treated as equivalent to Load Word (lw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: ll $t1, 100000($t2)

   Load Linked : Paired with Store Conditional (sc) to perform atomic read-modify-write.  Treated as equivalent to Load Word (lw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: ll $t1, label

   Load Linked : Paired with Store Conditional (sc) to perform atomic read-modify-write.  Treated as equivalent to Load Word (lw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: ll $t1, label($t2)

   Load Linked : Paired with Store Conditional (sc) to perform atomic read-modify-write.  Treated as equivalent to Load Word (lw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: ll $t1, label+100000

   Load Linked : Paired with Store Conditional (sc) to perform atomic read-modify-write.  Treated as equivalent to Load Word (lw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: ll $t1, label+100000($t2)

   Load Linked : Paired with Store Conditional (sc) to perform atomic read-modify-write.  Treated as equivalent to Load Word (lw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param label+100000($t2): Parameter 1


.. mips:instructions:: lw $t1, ($t2)

   Load Word : Set $t1 to contents of effective memory word address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: lw $t1, -100

   Load Word : Set $t1 to contents of effective memory word address

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: lw $t1, 100

   Load Word : Set $t1 to contents of effective memory word address

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: lw $t1, 100($t2)

   Load Word : Set $t1 to contents of effective memory word address

   :param $t1: Parameter 0
   :param 100($t2): Parameter 1


.. mips:instructions:: lw $t1, 100000

   Load Word : Set $t1 to contents of effective memory word address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: lw $t1, 100000($t2)

   Load Word : Set $t1 to contents of effective memory word address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: lw $t1, label

   Load Word : Set $t1 to contents of memory word at label's address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: lw $t1, label($t2)

   Load Word : Set $t1 to contents of effective memory word address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: lw $t1, label+100000

   Load Word : Set $t1 to contents of effective memory word address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: lw $t1, label+100000($t2)

   Load Word : Set $t1 to contents of effective memory word address

   :param $t1: Parameter 0
   :param label+100000($t2): Parameter 1


.. mips:instructions:: lwc1 $f1, ($t2)

   Load Word Coprocessor 1 : Set $f1 to 32-bit value from effective memory word address

   :param $f1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: lwc1 $f1, -100

   Load Word Coprocessor 1 : Set $f1 to 32-bit value from effective memory word address

   :param $f1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: lwc1 $f1, 100000

   Load Word Coprocessor 1 : Set $f1 to 32-bit value from effective memory word address

   :param $f1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: lwc1 $f1, 100000($t2)

   Load Word Coprocessor 1 : Set $f1 to 32-bit value from effective memory word address

   :param $f1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: lwc1 $f1, label

   Load Word Coprocessor 1 : Set $f1 to 32-bit value from effective memory word address

   :param $f1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: lwc1 $f1, label($t2)

   Load Word Coprocessor 1 : Set $f1 to 32-bit value from effective memory word address

   :param $f1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: lwc1 $f1, label+100000

   Load Word Coprocessor 1 : Set $f1 to 32-bit value from effective memory word address

   :param $f1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: lwc1 $f1, label+100000($t

   2)Load Word Coprocessor 1 : Set $f1 to 32-bit value from effective memory word address

   :param $f1: Parameter 0
   :param label+100000($t: Parameter 1


.. mips:instructions:: lwl $t1, ($t2)

   Load Word Left : Load from 1 to 4 bytes left-justified into $t1, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: lwl $t1, -100

   Load Word Left : Load from 1 to 4 bytes left-justified into $t1, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: lwl $t1, 100

   Load Word Left : Load from 1 to 4 bytes left-justified into $t1, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: lwl $t1, 100($t2)

   Load Word Left : Load from 1 to 4 bytes left-justified into $t1, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param 100($t2): Parameter 1


.. mips:instructions:: lwl $t1, 100000

   Load Word Left : Load from 1 to 4 bytes left-justified into $t1, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: lwl $t1, 100000($t2)

   Load Word Left : Load from 1 to 4 bytes left-justified into $t1, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: lwl $t1, label

   Load Word Left : Load from 1 to 4 bytes left-justified into $t1, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: lwl $t1, label($t2)

   Load Word Left : Load from 1 to 4 bytes left-justified into $t1, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: lwl $t1, label+100000

   Load Word Left : Load from 1 to 4 bytes left-justified into $t1, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: lwl $t1, label+100000($t2

   )Load Word Left : Load from 1 to 4 bytes left-justified into $t1, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param label+100000($t2: Parameter 1


.. mips:instructions:: lwr $t1, ($t2)

   Load Word Right : Load from 1 to 4 bytes right-justified into $t1, starting with effective memory byte address and continuing through the high-order byte of its word

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: lwr $t1, -100

   Load Word Right : Load from 1 to 4 bytes right-justified into $t1, starting with effective memory byte address and continuing through the high-order byte of its word

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: lwr $t1, 100

   Load Word Right : Load from 1 to 4 bytes right-justified into $t1, starting with effective memory byte address and continuing through the high-order byte of its word

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: lwr $t1, 100($t2)

   Load Word Right : Load from 1 to 4 bytes right-justified into $t1, starting with effective memory byte address and continuing through the high-order byte of its word

   :param $t1: Parameter 0
   :param 100($t2): Parameter 1


.. mips:instructions:: lwr $t1, 100000

   Load Word Right : Load from 1 to 4 bytes right-justified into $t1, starting with effective memory byte address and continuing through the high-order byte of its word

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: lwr $t1, 100000($t2)

   Load Word Right : Load from 1 to 4 bytes right-justified into $t1, starting with effective memory byte address and continuing through the high-order byte of its word

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: lwr $t1, label

   Load Word Right : Load from 1 to 4 bytes right-justified into $t1, starting with effective memory byte address and continuing through the high-order byte of its word

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: lwr $t1, label($t2)

   Load Word Right : Load from 1 to 4 bytes right-justified into $t1, starting with effective memory byte address and continuing through the high-order byte of its word

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: lwr $t1, label+100000

   Load Word Right : Load from 1 to 4 bytes right-justified into $t1, starting with effective memory byte address and continuing through the high-order byte of its word

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: lwr $t1, label+100000($t2

   )Load Word Right : Load from 1 to 4 bytes right-justified into $t1, starting with effective memory byte address and continuing through the high-order byte of its word

   :param $t1: Parameter 0
   :param label+100000($t2: Parameter 1


.. mips:instructions:: mfc1.d $t1, $f2

   Move From Coprocessor 1 Double : Set $t1 to contents of $f2, set next higher register from $t1 to contents of next higher register from $f2

   :param $t1: Parameter 0
   :param $f2: Parameter 1


.. mips:instructions:: move $t1, $t2

   MOVE : Set $t1 to contents of $t2

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: mtc1.d $t1, $f2

   Move To Coprocessor 1 Double : Set $f2 to contents of $t1, set next higher register from $f2 to contents of next higher register from $t1

   :param $t1: Parameter 0
   :param $f2: Parameter 1


.. mips:instructions:: mul $t1, $t2, -100

   MULtiplication : Set HI to high-order 32 bits, LO and $t1 to low-order 32 bits of the product of $t2 and 16-bit signed immediate (use mfhi to access HI, mflo to access LO)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: mul $t1, $t2, 100000

   MULtiplication : Set HI to high-order 32 bits, LO and $t1 to low-order 32 bits of the product of $t2 and 32-bit immediate (use mfhi to access HI, mflo to access LO)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: mulo $t1, $t2, $t3

   MULtiplication with Overflow : Set $t1 to low-order 32 bits of the product of $t2 and $t3

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: mulo $t1, $t2, -100

   MULtiplication with Overflow : Set $t1 to low-order 32 bits of the product of $t2 and signed 16-bit immediate

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: mulo $t1, $t2, 100000

   MULtiplication with Overflow : Set $t1 to low-order 32 bits of the product of $t2 and 32-bit immediate

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: mulou $t1, $t2, $t3

   MULtiplication with Overflow Unsigned : Set $t1 to low-order 32 bits of the product of $t2 and $t3

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: mulou $t1, $t2, -100

   MULtiplication with Overflow Unsigned : Set $t1 to low-order 32 bits of the product of $t2 and signed 16-bit immediate

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: mulou $t1, $t2, 100000

   MULtiplication with Overflow Unsigned : Set $t1 to low-order 32 bits of the product of $t2 and 32-bit immediate

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: mulu $t1, $t2, $t3

   MULtiplication Unsigned : Set HI to high-order 32 bits, LO and $t1 to low-order 32 bits of ($t2 multiplied by $t3, unsigned multiplication)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: mulu $t1, $t2, -100

   MULtiplication Unsigned :  Set HI to high-order 32 bits, LO and $t1 to low-order 32 bits of ($t2 multiplied by 16-bit immediate, unsigned multiplication)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: mulu $t1, $t2, 100000

   MULtiplication Unsigned :  Set HI to high-order 32 bits, LO and $t1 to low-order 32 bits of ($t2 multiplied by 32-bit immediate, unsigned multiplication)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: neg $t1, $t2

   NEGate : Set $t1 to negation of $t2

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: negu $t1, $t2

   NEGate Unsigned : Set $t1 to negation of $t2, no overflow

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: not $t1, $t2

   Bitwise NOT (bit inversion)

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: or $t1, $t2, 100

   OR : set $t1 to ($t2 bitwise-OR 16-bit unsigned immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100: Parameter 2


.. mips:instructions:: or $t1, 100

   OR : set $t1 to ($t1 bitwise-OR 16-bit unsigned immediate)

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: ori $t1, $t2, 100000

   OR Immediate : set $t1 to ($t2 bitwise-OR 32-bit immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: ori $t1, 100

   OR Immediate : set $t1 to ($t1 bitwise-OR 16-bit unsigned immediate)

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: ori $t1, 100000

   OR Immediate : set $t1 to ($t1 bitwise-OR 32-bit immediate)

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: rem $t1, $t2, $t3

   REMainder : Set $t1 to (remainder of $t2 divided by $t3)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: rem $t1, $t2, -100

   REMainder : Set $t1 to (remainder of $t2 divided by 16-bit immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: rem $t1, $t2, 100000

   REMainder : Set $t1 to (remainder of $t2 divided by 32-bit immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: remu $t1, $t2, $t3

   REMainder : Set $t1 to (remainder of $t2 divided by $t3, unsigned division)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: remu $t1, $t2, -100

   REMainder : Set $t1 to (remainder of $t2 divided by 16-bit immediate, unsigned division)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: remu $t1, $t2, 100000

   REMainder : Set $t1 to (remainder of $t2 divided by 32-bit immediate, unsigned division)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: rol $t1, $t2, $t3

   ROtate Left : Set $t1 to ($t2 rotated left by number of bit positions specified in $t3)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: rol $t1, $t2, 10

   ROtate Left : Set $t1 to ($t2 rotated left by number of bit positions specified in 5-bit immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 10: Parameter 2


.. mips:instructions:: ror $t1, $t2, $t3

   ROtate Right : Set $t1 to ($t2 rotated right by number of bit positions specified in $t3)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: ror $t1, $t2, 10

   ROtate Right : Set $t1 to ($t2 rotated right by number of bit positions specified in 5-bit immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 10: Parameter 2


.. mips:instructions:: s.d $f2, ($t2)

   Store floating point Double precision : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: s.d $f2, -100

   Store floating point Double precision : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: s.d $f2, 100000

   Store floating point Double precision : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: s.d $f2, 100000($t2)

   Store floating point Double precision : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: s.d $f2, label

   Store floating point Double precision : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: s.d $f2, label($t2)

   Store floating point Double precision : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: s.d $f2, label+100000

   Store floating point Double precision : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: s.d $f2, label+100000($t2

   )Store floating point Double precision : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param label+100000($t2: Parameter 1


.. mips:instructions:: s.s $f1, ($t2)

   Store floating point Single precision : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: s.s $f1, -100

   Store floating point Single precision : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: s.s $f1, 100000

   Store floating point Single precision : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: s.s $f1, 100000($t2)

   Store floating point Single precision : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: s.s $f1, label

   Store floating point Single precision : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: s.s $f1, label($t2)

   Store floating point Single precision : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: s.s $f1, label+100000

   Store floating point Single precision : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: s.s $f1, label+100000($t2

   )Store floating point Single precision : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param label+100000($t2: Parameter 1


.. mips:instructions:: sb $t1, ($t2)

   Store Byte : Store the low-order 8 bits of $t1 into the effective memory byte address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: sb $t1, -100

   Store Byte : Store the low-order 8 bits of $t1 into the effective memory byte address

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: sb $t1, 100

   Store Byte : Store the low-order 8 bits of $t1 into the effective memory byte address

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: sb $t1, 100($t2)

   Store Byte : Store the low-order 8 bits of $t1 into the effective memory byte address

   :param $t1: Parameter 0
   :param 100($t2): Parameter 1


.. mips:instructions:: sb $t1, 100000

   Store Byte : Store the low-order 8 bits of $t1 into the effective memory byte address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: sb $t1, 100000($t2)

   Store Byte : Store the low-order 8 bits of $t1 into the effective memory byte address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: sb $t1, label

   Store Byte : Store the low-order 8 bits of $t1 into the effective memory byte address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: sb $t1, label($t2)

   Store Byte : Store the low-order 8 bits of $t1 into the effective memory byte address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: sb $t1, label+100000

   Store Byte : Store the low-order 8 bits of $t1 into the effective memory byte address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: sb $t1, label+100000($t2)

   Store Byte : Store the low-order 8 bits of $t1 into the effective memory byte address

   :param $t1: Parameter 0
   :param label+100000($t2): Parameter 1


.. mips:instructions:: sc $t1, ($t2)

   Store Conditional : Paired with Load Linked (ll) to perform atomic read-modify-write.  Treated as equivalent to Store Word (sw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: sc $t1, -100

   Store Conditional : Paired with Load Linked (ll) to perform atomic read-modify-write.  Treated as equivalent to Store Word (sw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: sc $t1, 100

   Store Conditional : Paired with Load Linked (ll) to perform atomic read-modify-write.  Treated as equivalent to Store Word (sw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: sc $t1, 100($t2)

   Store Conditional : Paired with Load Linked (ll) to perform atomic read-modify-write.  Treated as equivalent to Store Word (sw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param 100($t2): Parameter 1


.. mips:instructions:: sc $t1, 100000

   Store Conditional : Paired with Load Linked (ll) to perform atomic read-modify-write.  Treated as equivalent to Store Word (sw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: sc $t1, 100000($t2)

   Store Conditional : Paired with Load Linked (ll) to perform atomic read-modify-write.  Treated as equivalent to Store Word (sw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: sc $t1, label

   Store Conditional : Paired with Load Linked (ll) to perform atomic read-modify-write.  Treated as equivalent to Store Word (sw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: sc $t1, label($t2)

   Store Conditional : Paired with Load Linked (ll) to perform atomic read-modify-write.  Treated as equivalent to Store Word (sw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: sc $t1, label+100000

   Store Conditional : Paired with Load Linked (ll) to perform atomic read-modify-write.  Treated as equivalent to Store Word (sw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: sc $t1, label+100000($t2)

   Store Conditional : Paired with Load Linked (ll) to perform atomic read-modify-write.  Treated as equivalent to Store Word (sw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param label+100000($t2): Parameter 1


.. mips:instructions:: sd $t1, ($t2)

   Store Doubleword : Store contents of $t1 and the next register to the 64 bits starting at effective memory word address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: sd $t1, -100($t2)

   Store Doubleword : Store contents of $t1 and the next register to the 64 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: sd $t1, 100000

   Store Doubleword : Store contents of $t1 and the next register to the 64 bits starting at effective memory word address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: sd $t1, 100000($t2)

   Store Doubleword : Store contents of $t1 and the next register to the 64 bits starting at effective memory word address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: sd $t1, label

   Store Doubleword : Store contents of $t1 and the next register to the 64 bits starting at effective memory word address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: sd $t1, label($t2)

   Store Doubleword : Store contents of $t1 and the next register to the 64 bits starting at effective memory word address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: sd $t1, label+100000

   Store Doubleword : Store contents of $t1 and the next register to the 64 bits starting at effective memory word address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: sd $t1, label+100000($t2)

   Store Doubleword : Store contents of $t1 and the next register to the 64 bits starting at effective memory word address

   :param $t1: Parameter 0
   :param label+100000($t2): Parameter 1


.. mips:instructions:: sdc1 $f2, ($t2)

   Store Doubleword Coprocessor 1 : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: sdc1 $f2, -100

   Store Doubleword Coprocessor 1 : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: sdc1 $f2, 100000

   Store Doubleword Coprocessor 1 : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: sdc1 $f2, 100000($t2)

   Store Doubleword Coprocessor 1 : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: sdc1 $f2, label

   Store Doubleword Coprocessor 1 : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: sdc1 $f2, label($t2)

   Store Doubleword Coprocessor 1 : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: sdc1 $f2, label+100000

   Store Doubleword Coprocessor 1 : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: sdc1 $f2, label+100000($t

   2)Store Doubleword Coprocessor 1 : Store 64 bits from $f2 and $f3 register pair to effective memory doubleword address

   :param $f2: Parameter 0
   :param label+100000($t: Parameter 1


.. mips:instructions:: seq $t1, $t2, $t3

   Set EQual : if $t2 equal to $t3 then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: seq $t1, $t2, -100

   Set EQual : if $t2 equal to 16-bit immediate then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: seq $t1, $t2, 100000

   Set EQual : if $t2 equal to 32-bit immediate then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: sge $t1, $t2, $t3

   Set Greater or Equal : if $t2 greater or equal to $t3 then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: sge $t1, $t2, -100

   Set Greater or Equal : if $t2 greater or equal to 16-bit immediate then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: sge $t1, $t2, 100000

   Set Greater or Equal : if $t2 greater or equal to 32-bit immediate then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: sgeu $t1, $t2, $t3

   Set Greater or Equal Unsigned : if $t2 greater or equal to $t3 (unsigned compare) then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: sgeu $t1, $t2, -100

   Set Greater or Equal Unsigned : if $t2 greater or equal to 16-bit immediate (unsigned compare) then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: sgeu $t1, $t2, 100000

   Set Greater or Equal Unsigned : if $t2 greater or equal to 32-bit immediate (unsigned compare) then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: sgt $t1, $t2, $t3

   Set Greater Than : if $t2 greater than $t3 then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: sgt $t1, $t2, -100

   Set Greater Than : if $t2 greater than 16-bit immediate then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: sgt $t1, $t2, 100000

   Set Greater Than : if $t2 greater than 32-bit immediate then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: sgtu $t1, $t2, $t3

   Set Greater Than Unsigned : if $t2 greater than $t3 (unsigned compare) then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: sgtu $t1, $t2, -100

   Set Greater Than Unsigned : if $t2 greater than 16-bit immediate (unsigned compare) then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: sgtu $t1, $t2, 100000

   Set Greater Than Unsigned : if $t2 greater than 32-bit immediate (unsigned compare) then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: sh $t1, ($t2)

   Store Halfword : Store the low-order 16 bits of $t1 into the effective memory halfword address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: sh $t1, -100

   Store Halfword : Store the low-order 16 bits of $t1 into the effective memory halfword address

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: sh $t1, 100

   Store Halfword : Store the low-order 16 bits of $t1 into the effective memory halfword address

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: sh $t1, 100($t2)

   Store Halfword : Store the low-order 16 bits of $t1 into the effective memory halfword address

   :param $t1: Parameter 0
   :param 100($t2): Parameter 1


.. mips:instructions:: sh $t1, 100000

   Store Halfword : Store the low-order 16 bits of $t1 into the effective memory halfword address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: sh $t1, 100000($t2)

   Store Halfword : Store the low-order 16 bits of $t1 into the effective memory halfword address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: sh $t1, label

   Store Halfword : Store the low-order 16 bits of $t1 into the effective memory halfword address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: sh $t1, label($t2)

   Store Halfword : Store the low-order 16 bits of $t1 into the effective memory halfword address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: sh $t1, label+100000

   Store Halfword : Store the low-order 16 bits of $t1 into the effective memory halfword address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: sh $t1, label+100000($t2)

   Store Halfword : Store the low-order 16 bits of $t1 into the effective memory halfword address

   :param $t1: Parameter 0
   :param label+100000($t2): Parameter 1


.. mips:instructions:: sle $t1, $t2, $t3

   Set Less or Equal : if $t2 less or equal to $t3 then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: sle $t1, $t2, -100

   Set Less or Equal : if $t2 less or equal to 16-bit immediate then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: sle $t1, $t2, 100000

   Set Less or Equal : if $t2 less or equal to 32-bit immediate then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: sleu $t1, $t2, $t3

   Set Less or Equal Unsigned: if $t2 less or equal to $t3 (unsigned compare) then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: sleu $t1, $t2, -100

   Set Less or Equal Unsigned: if $t2 less or equal to 16-bit immediate (unsigned compare) then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: sleu $t1, $t2, 100000

   Set Less or Equal Unsigned: if $t2 less or equal to 32-bit immediate (unsigned compare) then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: sne $t1, $t2, $t3

   Set Not Equal : if $t2 not equal to $t3 then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: sne $t1, $t2, -100

   Set Not Equal : if $t2 not equal to 16-bit immediate then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: sne $t1, $t2, 100000

   Set Not Equal : if $t2 not equal to 32-bit immediate then set $t1 to 1 else 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: sub $t1, $t2, -100

   SUBtraction : set $t1 to ($t2 minus 16-bit immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: sub $t1, $t2, 100000

   SUBtraction : set $t1 to ($t2 minus 32-bit immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: subi $t1, $t2, -100

   SUBtraction Immediate : set $t1 to ($t2 minus 16-bit immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: subi $t1, $t2, 100000

   SUBtraction Immediate : set $t1 to ($t2 minus 32-bit immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: subiu $t1, $t2, 100000

   SUBtraction Immediate Unsigned : set $t1 to ($t2 minus 32-bit immediate), no overflow

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: subu $t1, $t2, 100000

   SUBtraction Unsigned : set $t1 to ($t2 minus 32-bit immediate), no overflow

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: sw $t1, ($t2)

   Store Word : Store $t1 contents into effective memory word address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: sw $t1, -100

   Store Word : Store $t1 contents into effective memory word address

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: sw $t1, 100

   Store Word : Store $t1 contents into effective memory word address

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: sw $t1, 100($t2)

   Store Word : Store $t1 contents into effective memory word address

   :param $t1: Parameter 0
   :param 100($t2): Parameter 1


.. mips:instructions:: sw $t1, 100000

   Store Word : Store $t1 contents into effective memory word address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: sw $t1, 100000($t2)

   Store Word : Store $t1 contents into effective memory word address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: sw $t1, label

   Store Word : Store $t1 contents into memory word at label's address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: sw $t1, label($t2)

   Store Word : Store $t1 contents into effective memory word address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: sw $t1, label+100000

   Store Word : Store $t1 contents into effective memory word address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: sw $t1, label+100000($t2)

   Store Word : Store $t1 contents into effective memory word address

   :param $t1: Parameter 0
   :param label+100000($t2): Parameter 1


.. mips:instructions:: swc1 $f1, ($t2)

   Store Word Coprocessor 1 : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: swc1 $f1, -100

   Store Word Coprocessor 1 : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: swc1 $f1, 100000

   Store Word Coprocessor 1 : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: swc1 $f1, 100000($t2)

   Store Word Coprocessor 1 : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: swc1 $f1, label

   Store Word Coprocessor 1 : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: swc1 $f1, label($t2)

   Store Word Coprocessor 1 : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: swc1 $f1, label+100000

   Store Word Coprocessor 1 : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: swc1 $f1, label+100000($t

   2)Store Word Coprocessor 1 : Store 32-bit value from $f1 to effective memory word address

   :param $f1: Parameter 0
   :param label+100000($t: Parameter 1


.. mips:instructions:: swl $t1, ($t2)

   Store Word Left : Store high-order 1 to 4 bytes of $t1 into memory, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: swl $t1, -100

   Store Word Left : Store high-order 1 to 4 bytes of $t1 into memory, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: swl $t1, 100

   Store Word Left : Store high-order 1 to 4 bytes of $t1 into memory, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: swl $t1, 100($t2)

   Store Word Left : Store high-order 1 to 4 bytes of $t1 into memory, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param 100($t2): Parameter 1


.. mips:instructions:: swl $t1, 100000

   Store Word Left : Store high-order 1 to 4 bytes of $t1 into memory, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: swl $t1, 100000($t2)

   Store Word Left : Store high-order 1 to 4 bytes of $t1 into memory, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: swl $t1, label

   Store Word Left : Store high-order 1 to 4 bytes of $t1 into memory, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: swl $t1, label($t2)

   Store Word Left : Store high-order 1 to 4 bytes of $t1 into memory, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: swl $t1, label+100000

   Store Word Left : Store high-order 1 to 4 bytes of $t1 into memory, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: swl $t1, label+100000($t2

   )Store Word Left : Store high-order 1 to 4 bytes of $t1 into memory, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param label+100000($t2: Parameter 1


.. mips:instructions:: swr $t1, ($t2)

   Store Word Right : Store low-order 1 to 4 bytes of $t1 into memory, starting with high-order byte of word containing effective memory byte address and continuing through that byte address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: swr $t1, -100

   Store Word Right : Store low-order 1 to 4 bytes of $t1 into memory, starting with high-order byte of word containing effective memory byte address and continuing through that byte address

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: swr $t1, 100

   Store Word Right : Store low-order 1 to 4 bytes of $t1 into memory, starting with high-order byte of word containing effective memory byte address and continuing through that byte address

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: swr $t1, 100($t2)

   Store Word Right : Store low-order 1 to 4 bytes of $t1 into memory, starting with high-order byte of word containing effective memory byte address and continuing through that byte address

   :param $t1: Parameter 0
   :param 100($t2): Parameter 1


.. mips:instructions:: swr $t1, 100000

   Store Word Right : Store low-order 1 to 4 bytes of $t1 into memory, starting with high-order byte of word containing effective memory byte address and continuing through that byte address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: swr $t1, 100000($t2)

   Store Word Right : Store low-order 1 to 4 bytes of $t1 into memory, starting with high-order byte of word containing effective memory byte address and continuing through that byte address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: swr $t1, label

   Store Word Right : Store low-order 1 to 4 bytes of $t1 into memory, starting with high-order byte of word containing effective memory byte address and continuing through that byte address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: swr $t1, label($t2)

   Store Word Right : Store low-order 1 to 4 bytes of $t1 into memory, starting with high-order byte of word containing effective memory byte address and continuing through that byte address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: swr $t1, label+100000

   Store Word Right : Store low-order 1 to 4 bytes of $t1 into memory, starting with high-order byte of word containing effective memory byte address and continuing through that byte address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: swr $t1, label+100000($t2

   )Store Word Right : Store low-order 1 to 4 bytes of $t1 into memory, starting with high-order byte of word containing effective memory byte address and continuing through that byte address

   :param $t1: Parameter 0
   :param label+100000($t2: Parameter 1


.. mips:instructions:: ulh $t1, ($t2)

   Unaligned Load Halfword : Set $t1 to the 16 bits, sign-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: ulh $t1, -100($t2)

   Unaligned Load Halfword : Set $t1 to the 16 bits, sign-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: ulh $t1, 100000

   Unaligned Load Halfword : Set $t1 to the 16 bits, sign-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: ulh $t1, 100000($t2)

   Unaligned Load Halfword : Set $t1 to the 16 bits, sign-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: ulh $t1, label

   Unaligned Load Halfword : Set $t1 to the 16 bits, sign-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: ulh $t1, label($t2)

   Unaligned Load Halfword : Set $t1 to the 16 bits, sign-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: ulh $t1, label+100000

   Unaligned Load Halfword : Set $t1 to the 16 bits, sign-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: ulh $t1, label+100000($t2

   )Unaligned Load Halfword : Set $t1 to the 16 bits, sign-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param label+100000($t2: Parameter 1


.. mips:instructions:: ulhu $t1, ($t2)

   Unaligned Load Halfword : Set $t1 to the 16 bits, zero-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: ulhu $t1, -100($t2)

   Unaligned Load Halfword : Set $t1 to the 16 bits, zero-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: ulhu $t1, 100000

   Unaligned Load Halfword : Set $t1 to the 16 bits, zero-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: ulhu $t1, 100000($t2)

   Unaligned Load Halfword : Set $t1 to the 16 bits, zero-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: ulhu $t1, label

   Unaligned Load Halfword : Set $t1 to the 16 bits, zero-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: ulhu $t1, label($t2)

   Unaligned Load Halfword : Set $t1 to the 16 bits, zero-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: ulhu $t1, label+100000

   Unaligned Load Halfword : Set $t1 to the 16 bits, zero-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: ulhu $t1, label+100000($t

   2)Unaligned Load Halfword : Set $t1 to the 16 bits, zero-extended, starting at effective memory byte address

   :param $t1: Parameter 0
   :param label+100000($t: Parameter 1


.. mips:instructions:: ulw $t1, ($t2)

   Unaligned Load Word : Set $t1 to the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: ulw $t1, -100($t2)

   Unaligned Load Word : Set $t1 to the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: ulw $t1, 100000

   Unaligned Load Word : Set $t1 to the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: ulw $t1, 100000($t2)

   Unaligned Load Word : Set $t1 to the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: ulw $t1, label

   Unaligned Load Word : Set $t1 to the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: ulw $t1, label($t2)

   Unaligned Load Word : Set $t1 to the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: ulw $t1, label+100000

   Unaligned Load Word : Set $t1 to the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: ulw $t1, label+100000($t2

   )Unaligned Load Word : Set $t1 to the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param label+100000($t2: Parameter 1


.. mips:instructions:: ush $t1, ($t2)

   Unaligned Store Halfword: Store low-order halfword $t1 contents into the 16 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: ush $t1, -100($t2)

   Unaligned Store Halfword: Store low-order halfword $t1 contents into the 16 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: ush $t1, 100000

   Unaligned Store Halfword: Store low-order halfword $t1 contents into the 16 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: ush $t1, 100000($t2)

   Unaligned Store Halfword: Store low-order halfword $t1 contents into the 16 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: ush $t1, label

   Unaligned Store Halfword: Store low-order halfword $t1 contents into the 16 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: ush $t1, label($t2)

   Unaligned Store Halfword: Store low-order halfword $t1 contents into the 16 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: ush $t1, label+100000

   Unaligned Store Halfword: Store low-order halfword $t1 contents into the 16 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: ush $t1, label+100000($t2

   )Unaligned Store Halfword: Store low-order halfword $t1 contents into the 16 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param label+100000($t2: Parameter 1


.. mips:instructions:: usw $t1, ($t2)

   Unaligned Store Word : Store $t1 contents into the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param ($t2): Parameter 1


.. mips:instructions:: usw $t1, -100($t2)

   Unaligned Store Word : Store $t1 contents into the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: usw $t1, 100000

   Unaligned Store Word : Store $t1 contents into the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param 100000: Parameter 1


.. mips:instructions:: usw $t1, 100000($t2)

   Unaligned Store Word : Store $t1 contents into the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param 100000($t2): Parameter 1


.. mips:instructions:: usw $t1, label

   Unaligned Store Word : Store $t1 contents into the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: usw $t1, label($t2)

   Unaligned Store Word : Store $t1 contents into the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param label($t2): Parameter 1


.. mips:instructions:: usw $t1, label+100000

   Unaligned Store Word : Store $t1 contents into the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param label+100000: Parameter 1


.. mips:instructions:: usw $t1, label+100000($t2

   )Unaligned Store Word : Store $t1 contents into the 32 bits starting at effective memory byte address

   :param $t1: Parameter 0
   :param label+100000($t2: Parameter 1


.. mips:instructions:: xor $t1, $t2, 100

   XOR : set $t1 to ($t2 bitwise-exclusive-OR 16-bit unsigned immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100: Parameter 2


.. mips:instructions:: xor $t1, 100

   XOR : set $t1 to ($t1 bitwise-exclusive-OR 16-bit unsigned immediate)

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: xori $t1, $t2, 100000

   XOR Immediate : set $t1 to ($t2 bitwise-exclusive-OR 32-bit immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100000: Parameter 2


.. mips:instructions:: xori $t1, 100

   XOR Immediate : set $t1 to ($t1 bitwise-exclusive-OR 16-bit unsigned immediate)

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: xori $t1, 100000

   XOR Immediate : set $t1 to ($t1 bitwise-exclusive-OR 32-bit immediate)

   :param $t1: Parameter 0
   :param 100000: Parameter 1
