import serial
import adafruit_thermal_printer
uart = serial.Serial("/dev/ttyS1", baudrate=9600, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)
printer = ThermalPrinter(uart)

printer.test_page() 
printer.feed(2)
printer = ThermalPrinter(uart)
printer.test_page()
printer.feed(2)
printer.print('Hello from CircuitPython!') 
printer.feed(2)
printer.bold = True
printer.print('This is bold text!')
printer.bold = False
printer.feed(2)
printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER 
printer.size = adafruit_thermal_printer.SIZE_MEDIUM  
printer.print('Medium Center')
printer.feed(2)
printer.print_barcode('123456789012', printer.UPC_A) 
printer.feed(2)
printer.has_paper()
