# by Kami Bigdely
# Docstrings and blank lines

######################
# INSTRUCTIONS: 
# - Add Docstrings
# - Fix any other issues discussed in this document (if you find any)
#
# GUIDELINES:
# - Triple Double Quotes
# - Start with a verb
# - End with a period
######################

class OnBoardTemperatureSensor:
    """Converts voltage to temperature"""

    VOLTAGE_TO_TEMP_FACTOR = 5.6

    def __init__(self):
        pass

    def read_voltage(self):
        """Return voltage number"""
        return 2.7
    
    def get_temperature(self):
        """Return voltage to temperature in celcius"""
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]

  
class CarbonMonoxideSensor:
    """Calculates monoxide levels using temperature and voltage"""

    VOLTAGE_TO_CO_FACTOR = 0.048

    def __init__(self, temperature_sensor):
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide_level(self):
        """Returns carbon monoxide level"""
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = (
            CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(
                sensor_voltage, self.on_board_temp_sensor.get_temperature()
            )
        )
        return self.carbon_monoxide
    
    def read_sensor_voltage(self):
        """Returns sensor voltage number"""
        # In real life, it should read from hardware.        
        return 2.3
    
    def convert_voltage_to_carbon_monoxide_level(voltage, temperature):
        """Calculates carbon monoxide level"""
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature

    
class DisplayUnit:
    """Display message"""

    def __init__(self):
        self.string = ''

    def display(self, msg):
        """Prints given message"""
        print(msg)


class CarbonMonoxideDevice():
    """Applies display to carbon monoxide sensor"""

    def __init__(self, co_sensor, display_unit):
        self.carbon_monoxide_sensor = co_sensor 
        self.display_unit = display_unit

    def display(self):
        """Display carbon monoxide levels"""
        msg = 'Carbon Monoxide Level is : ' +  str(self.carbon_monoxide_sensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)


if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.display()