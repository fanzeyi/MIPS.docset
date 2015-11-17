Basic Instructions
==================


.. mips:instructions:: abs.d $f2, $f4

   Floating point absolute value double precision : Set $f2 to absolute value of $f4, double precision

   :param $f2: Parameter 0
   :param $f4: Parameter 1


.. mips:instructions:: abs.s $f0, $f1

   Floating point absolute value single precision : Set $f0 to absolute value of $f1, single precision

   :param $f0: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: add $t1, $t2, $t3

   Addition with overflow : set $t1 to ($t2 plus $t3)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: add.d $f2, $f4, $f6

   Floating point addition double precision : Set $f2 to double-precision floating point value of $f4 plus $f6

   :param $f2: Parameter 0
   :param $f4: Parameter 1
   :param $f6: Parameter 2


.. mips:instructions:: add.s $f0, $f1, $f3

   Floating point addition single precision : Set $f0 to single-precision floating point value of $f1 plus $f3

   :param $f0: Parameter 0
   :param $f1: Parameter 1
   :param $f3: Parameter 2


.. mips:instructions:: addi $t1, $t2, -100

   Addition immediate with overflow : set $t1 to ($t2 plus signed 16-bit immediate)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: addiu $t1, $t2, -100

   Addition immediate unsigned without overflow : set $t1 to ($t2 plus signed 16-bit immediate), no overflow

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: addu $t1, $t2, $t3

   Addition unsigned without overflow : set $t1 to ($t2 plus $t3), no overflow

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: and $t1, $t2, $t3

   Bitwise AND : Set $t1 to bitwise AND of $t2 and $t3

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: andi $t1, $t2, 100

   Bitwise AND immediate : Set $t1 to bitwise AND of $t2 and zero-extended 16-bit immediate

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100: Parameter 2


.. mips:instructions:: bc1f 1, label

   Branch if specified FP condition flag false (BC1F, not BCLF) : If Coprocessor 1 condition flag specified by immediate is false (zero) then branch to statement at label's address

   :param 1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: bc1f label

   Branch if FP condition flag 0 false (BC1F, not BCLF) : If Coprocessor 1 condition flag 0 is false (zero) then branch to statement at label's address

   :param label: Parameter 0


.. mips:instructions:: bc1t 1, label

   Branch if specified FP condition flag true (BC1T, not BCLT) : If Coprocessor 1 condition flag specified by immediate is true (one) then branch to statement at label's address

   :param 1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: bc1t label

   Branch if FP condition flag 0 true (BC1T, not BCLT) : If Coprocessor 1 condition flag 0 is true (one) then branch to statement at label's address

   :param label: Parameter 0


.. mips:instructions:: beq $t1, $t2, label

   Branch if equal : Branch to statement at label's address if $t1 and $t2 are equal

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: bgez $t1, label

   Branch if greater than or equal to zero : Branch to statement at label's address if $t1 is greater than or equal to zero

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: bgezal $t1, label

   Branch if greater then or equal to zero and link : If $t1 is greater than or equal to zero, then set $ra to the Program Counter and branch to statement at label's address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: bgtz $t1, label

   Branch if greater than zero : Branch to statement at label's address if $t1 is greater than zero

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: blez $t1, label

   Branch if less than or equal to zero : Branch to statement at label's address if $t1 is less than or equal to zero

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: bltz $t1, label

   Branch if less than zero : Branch to statement at label's address if $t1 is less than zero

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: bltzal $t1, label

   Branch if less than zero and link : If $t1 is less than or equal to zero, then set $ra to the Program Counter and branch to statement at label's address

   :param $t1: Parameter 0
   :param label: Parameter 1


.. mips:instructions:: bne $t1, $t2, label

   Branch if not equal : Branch to statement at label's address if $t1 and $t2 are not equal

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param label: Parameter 2


.. mips:instructions:: break 

   Break execution : Terminate program execution with exception

   :param : Parameter 0


.. mips:instructions:: break 100

   Break execution with code : Terminate program execution with specified exception code

   :param 100: Parameter 0


.. mips:instructions:: c.eq.d $f2, $f4

   Compare equal double precision : If $f2 is equal to $f4 (double-precision), set Coprocessor 1 condition flag 0 true else set it false

   :param $f2: Parameter 0
   :param $f4: Parameter 1


.. mips:instructions:: c.eq.d 1, $f2, $f4

   Compare equal double precision : If $f2 is equal to $f4 (double-precision), set Coprocessor 1 condition flag specified by immediate to true else set it to false

   :param 1: Parameter 0
   :param $f2: Parameter 1
   :param $f4: Parameter 2


.. mips:instructions:: c.eq.s $f0, $f1

   Compare equal single precision : If $f0 is equal to $f1, set Coprocessor 1 condition flag 0 true else set it false

   :param $f0: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: c.eq.s 1, $f0, $f1

   Compare equal single precision : If $f0 is equal to $f1, set Coprocessor 1 condition flag specied by immediate to true else set it to false

   :param 1: Parameter 0
   :param $f0: Parameter 1
   :param $f1: Parameter 2


.. mips:instructions:: c.le.d $f2, $f4

   Compare less or equal double precision : If $f2 is less than or equal to $f4 (double-precision), set Coprocessor 1 condition flag 0 true else set it false

   :param $f2: Parameter 0
   :param $f4: Parameter 1


.. mips:instructions:: c.le.d 1, $f2, $f4

   Compare less or equal double precision : If $f2 is less than or equal to $f4 (double-precision), set Coprocessor 1 condition flag specfied by immediate true else set it false

   :param 1: Parameter 0
   :param $f2: Parameter 1
   :param $f4: Parameter 2


.. mips:instructions:: c.le.s $f0, $f1

   Compare less or equal single precision : If $f0 is less than or equal to $f1, set Coprocessor 1 condition flag 0 true else set it false

   :param $f0: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: c.le.s 1, $f0, $f1

   Compare less or equal single precision : If $f0 is less than or equal to $f1, set Coprocessor 1 condition flag specified by immediate to true else set it to false

   :param 1: Parameter 0
   :param $f0: Parameter 1
   :param $f1: Parameter 2


.. mips:instructions:: c.lt.d $f2, $f4

   Compare less than double precision : If $f2 is less than $f4 (double-precision), set Coprocessor 1 condition flag 0 true else set it false

   :param $f2: Parameter 0
   :param $f4: Parameter 1


.. mips:instructions:: c.lt.d 1, $f2, $f4

   Compare less than double precision : If $f2 is less than $f4 (double-precision), set Coprocessor 1 condition flag specified by immediate to true else set it to false

   :param 1: Parameter 0
   :param $f2: Parameter 1
   :param $f4: Parameter 2


.. mips:instructions:: c.lt.s $f0, $f1

   Compare less than single precision : If $f0 is less than $f1, set Coprocessor 1 condition flag 0 true else set it false

   :param $f0: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: c.lt.s 1, $f0, $f1

   Compare less than single precision : If $f0 is less than $f1, set Coprocessor 1 condition flag specified by immediate to true else set it to false

   :param 1: Parameter 0
   :param $f0: Parameter 1
   :param $f1: Parameter 2


.. mips:instructions:: ceil.w.d $f1, $f2

   Ceiling double precision to word : Set $f1 to 32-bit integer ceiling of double-precision float in $f2

   :param $f1: Parameter 0
   :param $f2: Parameter 1


.. mips:instructions:: ceil.w.s $f0, $f1

   Ceiling single precision to word : Set $f0 to 32-bit integer ceiling of single-precision float in $f1

   :param $f0: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: clo $t1, $t2

   Count number of leading ones : Set $t1 to the count of leading one bits in $t2 starting at most significant bit position

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: clz $t1, $t2

   Count number of leading zeroes : Set $t1 to the count of leading zero bits in $t2 starting at most significant bit positio

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: cvt.d.s $f2, $f1

   Convert from single precision to double precision : Set $f2 to double precision equivalent of single precision value in $f1

   :param $f2: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: cvt.d.w $f2, $f1

   Convert from word to double precision : Set $f2 to double precision equivalent of 32-bit integer value in $f1

   :param $f2: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: cvt.s.d $f1, $f2

   Convert from double precision to single precision : Set $f1 to single precision equivalent of double precision value in $f2

   :param $f1: Parameter 0
   :param $f2: Parameter 1


.. mips:instructions:: cvt.s.w $f0, $f1

   Convert from word to single precision : Set $f0 to single precision equivalent of 32-bit integer value in $f2

   :param $f0: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: cvt.w.d $f1, $f2

   Convert from double precision to word : Set $f1 to 32-bit integer equivalent of double precision value in $f2

   :param $f1: Parameter 0
   :param $f2: Parameter 1


.. mips:instructions:: cvt.w.s $f0, $f1

   Convert from single precision to word : Set $f0 to 32-bit integer equivalent of single precision value in $f1

   :param $f0: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: div $t1, $t2

   Division with overflow : Divide $t1 by $t2 then set LO to quotient and HI to remainder (use mfhi to access HI, mflo to access LO)

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: div.d $f2, $f4, $f6

   Floating point division double precision : Set $f2 to double-precision floating point value of $f4 divided by $f6

   :param $f2: Parameter 0
   :param $f4: Parameter 1
   :param $f6: Parameter 2


.. mips:instructions:: div.s $f0, $f1, $f3

   Floating point division single precision : Set $f0 to single-precision floating point value of $f1 divided by $f3

   :param $f0: Parameter 0
   :param $f1: Parameter 1
   :param $f3: Parameter 2


.. mips:instructions:: divu $t1, $t2

   Division unsigned without overflow : Divide unsigned $t1 by $t2 then set LO to quotient and HI to remainder (use mfhi to access HI, mflo to access LO)

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: eret 

   Exception return : Set Program Counter to Coprocessor 0 EPC register value, set Coprocessor Status register bit 1 (exception level) to zero

   :param : Parameter 0


.. mips:instructions:: floor.w.d $f1, $f2

   Floor double precision to word : Set $f1 to 32-bit integer floor of double-precision float in $f2

   :param $f1: Parameter 0
   :param $f2: Parameter 1


.. mips:instructions:: floor.w.s $f0, $f1

   Floor single precision to word : Set $f0 to 32-bit integer floor of single-precision float in $f1

   :param $f0: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: j target

   Jump unconditionally : Jump to statement at target address

   :param target: Parameter 0


.. mips:instructions:: jal target

   Jump and link : Set $ra to Program Counter (return address) then jump to statement at target address

   :param target: Parameter 0


.. mips:instructions:: jalr $t1

   Jump and link register : Set $ra to Program Counter (return address) then jump to statement whose address is in $t1

   :param $t1: Parameter 0


.. mips:instructions:: jalr $t1, $t2

   Jump and link register : Set $t1 to Program Counter (return address) then jump to statement whose address is in $t2

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: jr $t1

   Jump register unconditionally : Jump to statement whose address is in $t1

   :param $t1: Parameter 0


.. mips:instructions:: lb $t1, -100($t2)

   Load byte : Set $t1 to sign-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: lbu $t1, -100($t2)

   Load byte unsigned : Set $t1 to zero-extended 8-bit value from effective memory byte address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: ldc1 $f2, -100($t2)

   Load double word Coprocessor 1 (FPU)) : Set $f2 to 64-bit value from effective memory doubleword address

   :param $f2: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: lh $t1, -100($t2)

   Load halfword : Set $t1 to sign-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: lhu $t1, -100($t2)

   Load halfword unsigned : Set $t1 to zero-extended 16-bit value from effective memory halfword address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: ll $t1, -100($t2)

   Load linked : Paired with Store Conditional (sc) to perform atomic read-modify-write.  Treated as equivalent to Load Word (lw) because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: lui $t1, 100

   Load upper immediate : Set high-order 16 bits of $t1 to 16-bit immediate and low-order 16 bits to 0

   :param $t1: Parameter 0
   :param 100: Parameter 1


.. mips:instructions:: lw $t1, -100($t2)

   Load word : Set $t1 to contents of effective memory word address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: lwc1 $f1, -100($t2)

   Load word into Coprocessor 1 (FPU) : Set $f1 to 32-bit value from effective memory word address

   :param $f1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: lwl $t1, -100($t2)

   Load word left : Load from 1 to 4 bytes left-justified into $t1, starting with effective memory byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: lwr $t1, -100($t2)

   Load word right : Load from 1 to 4 bytes right-justified into $t1, starting with effective memory byte address and continuing through the high-order byte of its word

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: madd $t1, $t2

   Multiply add : Multiply $t1 by $t2 then increment HI by high-order 32 bits of product, increment LO by low-order 32 bits of product (use mfhi to access HI, mflo to access LO)

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: maddu $t1, $t2

   Multiply add unsigned : Multiply $t1 by $t2 then increment HI by high-order 32 bits of product, increment LO by low-order 32 bits of product, unsigned (use mfhi to access HI, mflo to access LO)

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: mfc0 $t1, $8

   Move from Coprocessor 0 : Set $t1 to the value stored in Coprocessor 0 register $8

   :param $t1: Parameter 0
   :param $8: Parameter 1


.. mips:instructions:: mfc1 $t1, $f1

   Move from Coprocessor 1 (FPU) : Set $t1 to value in Coprocessor 1 register $f1

   :param $t1: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: mfhi $t1

   Move from HI register : Set $t1 to contents of HI (see multiply and divide operations)

   :param $t1: Parameter 0


.. mips:instructions:: mflo $t1

   Move from LO register : Set $t1 to contents of LO (see multiply and divide operations)

   :param $t1: Parameter 0


.. mips:instructions:: mov.d $f2, $f4

   Move floating point double precision : Set double precision $f2 to double precision value in $f4

   :param $f2: Parameter 0
   :param $f4: Parameter 1


.. mips:instructions:: mov.s $f0, $f1

   Move floating point single precision : Set single precision $f0 to single precision value in $f1

   :param $f0: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: movf $t1, $t2

   Move if FP condition flag 0 false : Set $t1 to $t2 if FPU (Coprocessor 1) condition flag 0 is false (zero)

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: movf $t1, $t2, 1

   Move if specified FP condition flag false : Set $t1 to $t2 if FPU (Coprocessor 1) condition flag specified by the immediate is false (zero)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 1: Parameter 2


.. mips:instructions:: movf.d $f2, $f4

   Move floating point double precision : If condition flag 0 false, set double precision $f2 to double precision value in $f4

   :param $f2: Parameter 0
   :param $f4: Parameter 1


.. mips:instructions:: movf.d $f2, $f4, 1

   Move floating point double precision : If condition flag specified by immediate is false, set double precision $f2 to double precision value in $f4

   :param $f2: Parameter 0
   :param $f4: Parameter 1
   :param 1: Parameter 2


.. mips:instructions:: movf.s $f0, $f1

   Move floating point single precision : If condition flag 0 is false, set single precision $f0 to single precision value in $f1

   :param $f0: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: movf.s $f0, $f1, 1

   Move floating point single precision : If condition flag specified by immediate is false, set single precision $f0 to single precision value in $f1e

   :param $f0: Parameter 0
   :param $f1: Parameter 1
   :param 1: Parameter 2


.. mips:instructions:: movn $t1, $t2, $t3

   Move conditional not zero : Set $t1 to $t2 if $t3 is not zero

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: movn.d $f2, $f4, $t3

   Move floating point double precision : If $t3 is not zero, set double precision $f2 to double precision value in $f4

   :param $f2: Parameter 0
   :param $f4: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: movn.s $f0, $f1, $t3

   Move floating point single precision : If $t3 is not zero, set single precision $f0 to single precision value in $f1

   :param $f0: Parameter 0
   :param $f1: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: movt $t1, $t2

   Move if FP condition flag 0 true : Set $t1 to $t2 if FPU (Coprocessor 1) condition flag 0 is true (one)

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: movt $t1, $t2, 1

   Move if specfied FP condition flag true : Set $t1 to $t2 if FPU (Coprocessor 1) condition flag specified by the immediate is true (one)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 1: Parameter 2


.. mips:instructions:: movt.d $f2, $f4

   Move floating point double precision : If condition flag 0 true, set double precision $f2 to double precision value in $f4

   :param $f2: Parameter 0
   :param $f4: Parameter 1


.. mips:instructions:: movt.d $f2, $f4, 1

   Move floating point double precision : If condition flag specified by immediate is true, set double precision $f2 to double precision value in $f4e

   :param $f2: Parameter 0
   :param $f4: Parameter 1
   :param 1: Parameter 2


.. mips:instructions:: movt.s $f0, $f1

   Move floating point single precision : If condition flag 0 is true, set single precision $f0 to single precision value in $f1e

   :param $f0: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: movt.s $f0, $f1, 1

   Move floating point single precision : If condition flag specified by immediate is true, set single precision $f0 to single precision value in $f1e

   :param $f0: Parameter 0
   :param $f1: Parameter 1
   :param 1: Parameter 2


.. mips:instructions:: movz $t1, $t2, $t3

   Move conditional zero : Set $t1 to $t2 if $t3 is zero

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: movz.d $f2, $f4, $t3

   Move floating point double precision : If $t3 is zero, set double precision $f2 to double precision value in $f4

   :param $f2: Parameter 0
   :param $f4: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: movz.s $f0, $f1, $t3

   Move floating point single precision : If $t3 is zero, set single precision $f0 to single precision value in $f1

   :param $f0: Parameter 0
   :param $f1: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: msub $t1, $t2

   Multiply subtract : Multiply $t1 by $t2 then decrement HI by high-order 32 bits of product, decrement LO by low-order 32 bits of product (use mfhi to access HI, mflo to access LO)

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: msubu $t1, $t2

   Multiply subtract unsigned : Multiply $t1 by $t2 then decrement HI by high-order 32 bits of product, decement LO by low-order 32 bits of product, unsigned (use mfhi to access HI, mflo to access LO)

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: mtc0 $t1, $8

   Move to Coprocessor 0 : Set Coprocessor 0 register $8 to value stored in $t1

   :param $t1: Parameter 0
   :param $8: Parameter 1


.. mips:instructions:: mtc1 $t1, $f1

   Move to Coprocessor 1 (FPU) : Set Coprocessor 1 register $f1 to value in $t1

   :param $t1: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: mthi $t1

   Move to HI registerr : Set HI to contents of $t1 (see multiply and divide operations)

   :param $t1: Parameter 0


.. mips:instructions:: mtlo $t1

   Move to LO register : Set LO to contents of $t1 (see multiply and divide operations)

   :param $t1: Parameter 0


.. mips:instructions:: mul $t1, $t2, $t3

   Multiplication without overflow  : Set HI to high-order 32 bits, LO and $t1 to low-order 32 bits of the product of $t2 and $t3 (use mfhi to access HI, mflo to access LO)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: mul.d $f2, $f4, $f6

   Floating point multiplication double precision : Set $f2 to double-precision floating point value of $f4 times $f6

   :param $f2: Parameter 0
   :param $f4: Parameter 1
   :param $f6: Parameter 2


.. mips:instructions:: mul.s $f0, $f1, $f3

   Floating point multiplication single precision : Set $f0 to single-precision floating point value of $f1 times $f3

   :param $f0: Parameter 0
   :param $f1: Parameter 1
   :param $f3: Parameter 2


.. mips:instructions:: mult $t1, $t2

   Multiplication : Set hi to high-order 32 bits, lo to low-order 32 bits of the product of $t1 and $t2 (use mfhi to access hi, mflo to access lo)

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: multu $t1, $t2

   Multiplication unsigned : Set HI to high-order 32 bits, LO to low-order 32 bits of the product of unsigned $t1 and $t2 (use mfhi to access HI, mflo to access LO)

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: neg.d $f2, $f4

   Floating point negate double precision : Set double precision $f2 to negation of double precision value in $f4

   :param $f2: Parameter 0
   :param $f4: Parameter 1


.. mips:instructions:: neg.s $f0, $f1

   Floating point negate single precision : Set single precision $f0 to negation of single precision value in $f1

   :param $f0: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: nop 

   Null operation : machine code is all zeroes

   :param : Parameter 0


.. mips:instructions:: nor $t1, $t2, $t3

   Bitwise NOR : Set $t1 to bitwise NOR of $t2 and $t3

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: or $t1, $t2, $t3

   Bitwise OR : Set $t1 to bitwise OR of $t2 and $t3

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: ori $t1, $t2, 100

   Bitwise OR immediate : Set $t1 to bitwise OR of $t2 and zero-extended 16-bit immediate

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100: Parameter 2


.. mips:instructions:: round.w.d $f1, $f2

   Round double precision to word : Set $f1 to 32-bit integer round of double-precision float in $f2

   :param $f1: Parameter 0
   :param $f2: Parameter 1


.. mips:instructions:: round.w.s $f0, $f1

   Round single precision to word : Set $f0 to 32-bit integer round of single-precision float in $f1

   :param $f0: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: sb $t1, -100($t2)

   Store byte : Store the low-order 8 bits of $t1 into the effective memory byte address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: sc $t1, -100($t2)

   Store conditional : Paired with Load Linked (ll) to perform atomic read-modify-write.  Stores $t1 value into effective address, then sets $t1 to 1 for success.  Always succeeds because MARS does not simulate multiple processors.

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: sdc1 $f2, -100($t2)

   Store double word from Coprocessor 1 (FPU)) : Store 64 bit value in $f2 to effective memory doubleword address

   :param $f2: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: sh $t1, -100($t2)

   Store halfword : Store the low-order 16 bits of $t1 into the effective memory halfword address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: sll $t1, $t2, 10

   Shift left logical : Set $t1 to result of shifting $t2 left by number of bits specified by immediate

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 10: Parameter 2


.. mips:instructions:: sllv $t1, $t2, $t3

   Shift left logical variable : Set $t1 to result of shifting $t2 left by number of bits specified by value in low-order 5 bits of $t3

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: slt $t1, $t2, $t3

   Set less than : If $t2 is less than $t3, then set $t1 to 1 else set $t1 to 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: slti $t1, $t2, -100

   Set less than immediate : If $t2 is less than sign-extended 16-bit immediate, then set $t1 to 1 else set $t1 to 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: sltiu $t1, $t2, -100

   Set less than immediate unsigned : If $t2 is less than  sign-extended 16-bit immediate using unsigned comparison, then set $t1 to 1 else set $t1 to 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param -100: Parameter 2


.. mips:instructions:: sltu $t1, $t2, $t3

   Set less than unsigned : If $t2 is less than $t3 using unsigned comparision, then set $t1 to 1 else set $t1 to 0

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: sqrt.d $f2, $f4

   Square root double precision : Set $f2 to double-precision floating point square root of $f4

   :param $f2: Parameter 0
   :param $f4: Parameter 1


.. mips:instructions:: sqrt.s $f0, $f1

   Square root single precision : Set $f0 to single-precision floating point square root of $f1

   :param $f0: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: sra $t1, $t2, 10

   Shift right arithmetic : Set $t1 to result of sign-extended shifting $t2 right by number of bits specified by immediate

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 10: Parameter 2


.. mips:instructions:: srav $t1, $t2, $t3

   Shift right arithmetic variable : Set $t1 to result of sign-extended shifting $t2 right by number of bits specified by value in low-order 5 bits of $t3

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: srl $t1, $t2, 10

   Shift right logical : Set $t1 to result of shifting $t2 right by number of bits specified by immediate

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 10: Parameter 2


.. mips:instructions:: srlv $t1, $t2, $t3

   Shift right logical variable : Set $t1 to result of shifting $t2 right by number of bits specified by value in low-order 5 bits of $t3

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: sub $t1, $t2, $t3

   Subtraction with overflow : set $t1 to ($t2 minus $t3)

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: sub.d $f2, $f4, $f6

   Floating point subtraction double precision : Set $f2 to double-precision floating point value of $f4 minus $f6

   :param $f2: Parameter 0
   :param $f4: Parameter 1
   :param $f6: Parameter 2


.. mips:instructions:: sub.s $f0, $f1, $f3

   Floating point subtraction single precision : Set $f0 to single-precision floating point value of $f1  minus $f3

   :param $f0: Parameter 0
   :param $f1: Parameter 1
   :param $f3: Parameter 2


.. mips:instructions:: subu $t1, $t2, $t3

   Subtraction unsigned without overflow : set $t1 to ($t2 minus $t3), no overflow

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: sw $t1, -100($t2)

   Store word : Store contents of $t1 into effective memory word address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: swc1 $f1, -100($t2)

   Store word from Coprocesor 1 (FPU) : Store 32 bit value in $f1 to effective memory word address

   :param $f1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: swl $t1, -100($t2)

   Store word left : Store high-order 1 to 4 bytes of $t1 into memory, starting with effective byte address and continuing through the low-order byte of its word

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: swr $t1, -100($t2)

   Store word right : Store low-order 1 to 4 bytes of $t1 into memory, starting with high-order byte of word containing effective byte address and continuing through that byte address

   :param $t1: Parameter 0
   :param -100($t2): Parameter 1


.. mips:instructions:: syscall 

   Issue a system call : Execute the system call specified by value in $v0

   :param : Parameter 0


.. mips:instructions:: teq $t1, $t2

   Trap if equal : Trap if $t1 is equal to $t2

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: teqi $t1, -100

   Trap if equal to immediate : Trap if $t1 is equal to sign-extended 16 bit immediate

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: tge $t1, $t2

   Trap if greater or equal : Trap if $t1 is greater than or equal to $t2

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: tgei $t1, -100

   Trap if greater than or equal to immediate : Trap if $t1 greater than or equal to sign-extended 16 bit immediate

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: tgeiu $t1, -100

   Trap if greater or equal to immediate unsigned : Trap if $t1 greater than or equal to sign-extended 16 bit immediate, unsigned comparison

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: tgeu $t1, $t2

   Trap if greater or equal unsigned : Trap if $t1 is greater than or equal to $t2 using unsigned comparision

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: tlt $t1, $t2

   Trap if less than: Trap if $t1 less than $t2

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: tlti $t1, -100

   Trap if less than immediate : Trap if $t1 less than sign-extended 16-bit immediate

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: tltiu $t1, -100

   Trap if less than immediate unsigned : Trap if $t1 less than sign-extended 16-bit immediate, unsigned comparison

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: tltu $t1, $t2

   Trap if less than unsigned : Trap if $t1 less than $t2, unsigned comparison

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: tne $t1, $t2

   Trap if not equal : Trap if $t1 is not equal to $t2

   :param $t1: Parameter 0
   :param $t2: Parameter 1


.. mips:instructions:: tnei $t1, -100

   Trap if not equal to immediate : Trap if $t1 is not equal to sign-extended 16 bit immediate

   :param $t1: Parameter 0
   :param -100: Parameter 1


.. mips:instructions:: trunc.w.d $f1, $f2

   Truncate double precision to word : Set $f1 to 32-bit integer truncation of double-precision float in $f2

   :param $f1: Parameter 0
   :param $f2: Parameter 1


.. mips:instructions:: trunc.w.s $f0, $f1

   Truncate single precision to word : Set $f0 to 32-bit integer truncation of single-precision float in $f1

   :param $f0: Parameter 0
   :param $f1: Parameter 1


.. mips:instructions:: xor $t1, $t2, $t3

   Bitwise XOR (exclusive OR) : Set $t1 to bitwise XOR of $t2 and $t3

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param $t3: Parameter 2


.. mips:instructions:: xori $t1, $t2, 100

   Bitwise XOR immediate : Set $t1 to bitwise XOR of $t2 and zero-extended 16-bit immediate

   :param $t1: Parameter 0
   :param $t2: Parameter 1
   :param 100: Parameter 2
