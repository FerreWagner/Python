#错误和异常

# 以下例子中，让用户输入一个合法的整数，但是允许用户中断这个程序（使用 Control-C 或者操作系统提供的方法）。用户中断的信息会引发一个 KeyboardInterrupt 异常
while True:
   try:
       x = int(input("Please enter a number: "))
       break
   except ValueError:
       print("Oops!  That was no valid number.  Try again   ")


# 如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
# 如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。

