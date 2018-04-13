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

# 抛出异常
# Python 使用 raise 语句抛出一个指定的异常。例如:
# raise NameError('asd')

# 如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后再次被抛出。


# 在 python3 中，处理带有参数的异常的方法如下：
# 定义函数
# 定义函数

def temp_convert(var):
    try:
        return int(var)
    except (ValueError) as Argument:
        print ("参数没有包含数字\n", Argument)

# 调用函数
temp_convert("xasdyz");
