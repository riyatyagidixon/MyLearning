CC=gcc


%.o: %.c 
	$(CC) -c -o $@ $< 

calculator_if: calculator_if.o sum.o mul.o div.o sub.o 
	$(CC) -o calculator_if calculator_if.o sum.o mul.o div.o sub.o

calculator_switch: calculator_switch.o sum.o mul.o div.o sub.o 
	$(CC) -o calculator_switch calculator_switch.o sum.o mul.o div.o sub.o

clean:
	rm -rf *.o calculator_if calculator_switch

all: calculator_if calculator_switch
